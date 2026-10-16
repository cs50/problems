import csv
import json
import math
import os
import re

import check50

DATA = ["oecd.csv", "worldpop.txt", "worldarea.txt"]
NUMBER = re.compile(r"-?\d*\.?\d+")
PNG = b"\x89PNG\r\n\x1a\n"


@check50.check()
def exists():
    """oecd.py exists"""
    check50.exists("oecd.py")
    check50.include(*DATA, "harness.py")


@check50.check(exists)
def runs():
    """oecd.py runs without errors"""
    if check50.run("python3 harness.py").exit(timeout=120) != 0:
        error = None
        if os.path.exists("error.txt"):
            with open("error.txt") as f:
                error = f.read()
        raise check50.Failure("oecd.py exited with an error", help=error)


@check50.check(runs)
def health_points():
    """health.png plots health expenditures against life expectancy, without the United States"""
    x, y = health_data()
    check_points("health.png", x, y, "health expenditures and life expectancy", extra=united_states())


@check50.check(health_points)
def health_line():
    """health.png includes the regression line"""
    check_line("health.png", *health_data())


@check50.check(health_points)
def health_correlation():
    """health.png shows the correlation"""
    check_correlation("health.png", *health_data())


@check50.check(runs)
def income_points():
    """income.png plots per capita income against life expectancy"""
    check_points("income.png", *income_data(), "per capita income and life expectancy")


@check50.check(income_points)
def income_line():
    """income.png includes the regression line"""
    check_line("income.png", *income_data())


@check50.check(income_points)
def income_correlation():
    """income.png shows the correlation"""
    check_correlation("income.png", *income_data())


@check50.check(runs)
def area_points():
    """area.png plots country area against population"""
    check_points("area.png", *area_data(), "country area and population")


@check50.check(area_points)
def area_line():
    """area.png includes the regression line"""
    check_line("area.png", *area_data())


@check50.check(area_points)
def area_correlation():
    """area.png shows the correlation"""
    check_correlation("area.png", *area_data())


def health_data():
    """Return health expenditures and life expectancies, excluding the United States."""
    rows = [row for row in oecd_rows() if row["Country"] != "United States"]
    return column(rows, "Health expenditures"), column(rows, "Life expectancy")


def income_data():
    """Return per capita incomes and life expectancies."""
    rows = oecd_rows()
    return column(rows, "Per capita income"), column(rows, "Life expectancy")


def area_data():
    """Return each country's area and population, in the same order."""
    return world_values("worldarea.txt"), world_values("worldpop.txt")


def united_states():
    """Return the United States' (health expenditures, life expectancy), if present."""
    for row in oecd_rows():
        if row["Country"] == "United States":
            return float(row["Health expenditures"]), float(row["Life expectancy"])
    return None


def oecd_rows():
    with open("oecd.csv") as f:
        return list(csv.DictReader(f))


def column(rows, name):
    return [float(row[name]) for row in rows]


def world_values(filename):
    """Return the number at the end of each nonblank line of filename."""
    with open(filename) as f:
        return [float(line.split()[-1]) for line in f if line.strip()]


def regress(x, y):
    """Return the slope, intercept, and correlation of the least-squares line through (x, y)."""
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    sxx = sum((xi - mean_x) ** 2 for xi in x)
    syy = sum((yi - mean_y) ** 2 for yi in y)
    sxy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    slope = sxy / sxx
    return slope, mean_y - slope * mean_x, sxy / math.sqrt(sxx * syy)


def load_plot(filename):
    """Return what oecd.py drew in the figure it saved as filename, or fail if it saved none."""
    if not os.path.exists(filename):
        raise check50.Failure(f"oecd.py did not create {filename}")
    with open(filename, "rb") as f:
        if f.read(len(PNG)) != PNG:
            raise check50.Failure(f"{filename} is not a PNG")
    with open("plots.json") as f:
        plots = json.load(f)
    if filename not in plots:
        raise check50.Failure(f"could not find a plot saved as {filename}")
    return plots[filename]


def same_points(actual, expected):
    """Return True if actual and expected contain the same points, in any order."""
    if len(actual) != len(expected):
        return False
    return all(
        math.isclose(a, e, rel_tol=1e-9, abs_tol=1e-9)
        for p, q in zip(sorted(actual), sorted(expected))
        for a, e in zip(p, q)
    )


def orientation(plot, x, y):
    """Return (x, y) as plotted, swapping axes if needed, or None if the points don't match."""
    points = [tuple(point) for point in plot["points"]]
    for a, b in ((x, y), (y, x)):
        if same_points(points, list(zip(a, b))):
            return a, b
    return None


def check_points(filename, x, y, description, extra=None):
    plot = load_plot(filename)
    if orientation(plot, x, y):
        return
    points = [tuple(point) for point in plot["points"]]
    if extra and any(same_points(points, list(zip(a, b)) + [e]) for a, b, e in ((x, y, extra), (y, x, extra[::-1]))):
        raise check50.Failure(f"{filename} still includes the United States")
    help = None
    if len(points) > len(x):
        help = "did you clear the figure (e.g., with matplotlib.pyplot.clf) before starting this plot?"
    raise check50.Failure(
        f"expected {filename} to plot {len(x)} points of {description}, but found {len(points)} points that didn't match",
        help=help,
    )


def check_line(filename, x, y):
    plot = load_plot(filename)
    x, y = orientation(plot, x, y)
    slope, intercept, _ = regress(x, y)
    tolerance = 1e-6 * (max(y) - min(y))
    on_line = [
        line for line in plot["lines"]
        if len({px for px, _ in line}) >= 2 and all(abs(py - (intercept + slope * px)) <= tolerance for px, py in line)
    ]
    if not on_line:
        raise check50.Failure(f"could not find the regression line in {filename}")
    if len(on_line) != len(plot["lines"]):
        raise check50.Failure(
            f"{filename} contains lines other than its regression line",
            help="did you clear the figure (e.g., with matplotlib.pyplot.clf) before starting this plot?",
        )


def check_correlation(filename, x, y):
    plot = load_plot(filename)
    _, _, correlation = regress(x, y)
    numbers = [float(n) for text in plot["texts"] for n in NUMBER.findall(text)]
    if not any(abs(n - correlation) <= 0.006 for n in numbers):
        raise check50.Failure(
            f"could not find the correlation, {correlation:.2f}, on {filename}",
            help="try including it in the plot's title",
        )
