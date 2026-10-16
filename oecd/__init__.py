import csv
import json
import math
import os
import re

import check50

DATA = ["oecd.csv", "worldpop.txt", "worldarea.txt"]
NUMBER = re.compile(r"-?\d*\.?\d+")


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
    """plots health expenditures against life expectancy, without the United States"""
    find_plot(*health_data(), "health expenditures and life expectancy", us=united_states("Health expenditures"))


@check50.check(health_points)
def health_line():
    """health expenditures plot includes the regression line"""
    check_line(*health_data())


@check50.check(health_points)
def health_correlation():
    """health expenditures plot shows the correlation"""
    check_correlation(*health_data())


@check50.check(runs)
def income_points():
    """plots per capita income against life expectancy, without the United States"""
    find_plot(*income_data(), "per capita income and life expectancy", us=united_states("Per capita income"))


@check50.check(income_points)
def income_line():
    """income plot includes the regression line"""
    check_line(*income_data())


@check50.check(income_points)
def income_correlation():
    """income plot shows the correlation"""
    check_correlation(*income_data())


@check50.check(runs)
def area_points():
    """plots country area against population"""
    find_plot(*area_data(), "country area and population")


@check50.check(area_points)
def area_line():
    """area plot includes the regression line"""
    check_line(*area_data())


@check50.check(area_points)
def area_correlation():
    """area plot shows the correlation"""
    check_correlation(*area_data())


def health_data():
    """Return health expenditures and life expectancies, excluding the United States."""
    rows = oecd_rows(exclude="United States")
    return column(rows, "Health expenditures"), column(rows, "Life expectancy")


def income_data():
    """Return per capita incomes and life expectancies, excluding the United States."""
    rows = oecd_rows(exclude="United States")
    return column(rows, "Per capita income"), column(rows, "Life expectancy")


def area_data():
    """Return each country's area and population, in the same order."""
    return world_values("worldarea.txt"), world_values("worldpop.txt")


def united_states(name):
    """Return the United States' (name, life expectancy), if present."""
    for row in oecd_rows():
        if row["Country"] == "United States":
            return float(row[name]), float(row["Life expectancy"])
    return None


def oecd_rows(exclude=None):
    with open("oecd.csv") as f:
        return [row for row in csv.DictReader(f) if row["Country"] != exclude]


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


def load_plots():
    with open("plots.json") as f:
        return json.load(f)


def same_points(actual, expected):
    """Return True if actual and expected contain the same points, in any order."""
    if len(actual) != len(expected):
        return False
    return all(
        math.isclose(a, e, rel_tol=1e-9, abs_tol=1e-9)
        for p, q in zip(sorted(actual), sorted(expected))
        for a, e in zip(p, q)
    )


def contains_points(actual, expected):
    """Return True if every point in expected appears in actual."""
    remaining = [tuple(point) for point in actual]
    for point in expected:
        match = next((p for p in remaining if all(math.isclose(a, e, rel_tol=1e-9, abs_tol=1e-9) for a, e in zip(p, point))), None)
        if match is None:
            return False
        remaining.remove(match)
    return True


def matches(plot, x, y):
    """Return (x, y) as plot draws them, swapping axes if needed, or None if plot draws other points."""
    points = [tuple(point) for point in plot["points"]]
    for a, b in ((x, y), (y, x)):
        if same_points(points, list(zip(a, b))):
            return a, b
    return None


def find_plot(x, y, description, us=None):
    """Return the first plot of (x, y) and its axes, or fail with a hint about what went wrong."""
    plots = load_plots()
    for plot in plots:
        oriented = matches(plot, x, y)
        if oriented:
            return plot, oriented
    if not plots:
        raise check50.Failure("oecd.py did not save or show any plots")
    if us and any(matches(plot, x + [us[0]], y + [us[1]]) for plot in plots):
        raise check50.Failure(f"the plot of {description} still includes the United States")
    if any(contains_points(plot["points"], zip(a, b)) for plot in plots for a, b in ((x, y), (y, x))):
        raise check50.Failure(
            f"the plot of {description} also contains points from another plot",
            help="did you clear the figure (e.g., with matplotlib.pyplot.clf) before starting this plot?",
        )
    raise check50.Failure(f"could not find a plot of the {len(x)} points of {description}")


def check_line(x, y):
    plot, (x, y) = find_plot(x, y, "")
    slope, intercept, _ = regress(x, y)
    tolerance = 1e-6 * (max(y) - min(y))
    on_line = [
        line for line in plot["lines"]
        if len({px for px, _ in line}) >= 2 and all(abs(py - (intercept + slope * px)) <= tolerance for px, py in line)
    ]
    if not on_line:
        raise check50.Failure("could not find the regression line on this plot")
    if len(on_line) != len(plot["lines"]):
        raise check50.Failure(
            "this plot contains lines other than its regression line",
            help="did you clear the figure (e.g., with matplotlib.pyplot.clf) before starting this plot?",
        )


def check_correlation(x, y):
    plot, (x, y) = find_plot(x, y, "")
    _, _, correlation = regress(x, y)
    numbers = [float(n) for text in plot["texts"] for n in NUMBER.findall(text)]
    if not any(abs(n - correlation) <= 0.006 for n in numbers):
        raise check50.Failure(
            f"could not find the correlation, {correlation:.2f}, on this plot",
            help="try including it in the plot's title",
        )
