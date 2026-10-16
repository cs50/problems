"""Runs oecd.py, recording what each figure it saves or shows contains in plots.json."""

import builtins
import json
import os
import runpy
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.figure
import matplotlib.pyplot

DATA = {"oecd.csv", "worldpop.txt", "worldarea.txt"}

plots = []
savefig = matplotlib.figure.Figure.savefig
show = matplotlib.pyplot.show
open_ = builtins.open


def record_savefig(figure, *args, **kwargs):
    plots.append(describe(figure))
    return savefig(figure, *args, **kwargs)


def record_show(*args, **kwargs):
    record_open_figures()
    return show(*args, **kwargs)


def record_open_figures():
    for number in matplotlib.pyplot.get_fignums():
        plots.append(describe(matplotlib.pyplot.figure(number)))


def open_data(file, *args, **kwargs):
    """Open the check's copy of a data file, even if oecd.py names it with a path from elsewhere."""
    if isinstance(file, (str, os.PathLike)):
        name = os.path.basename(os.fspath(file))
        if name in DATA and not os.path.exists(file):
            file = name
    return open_(file, *args, **kwargs)


def describe(figure):
    """Return the points, lines, and text drawn on figure."""
    points, lines = [], []
    texts = [text.get_text() for text in figure.texts]
    texts += [text.get_text() for legend in figure.legends for text in legend.get_texts()]
    for ax in figure.axes:
        texts += [ax.get_title(loc) for loc in ("left", "center", "right")]
        texts += [ax.get_xlabel(), ax.get_ylabel()]
        texts += [text.get_text() for text in ax.texts]
        if ax.get_legend():
            texts += [text.get_text() for text in ax.get_legend().get_texts()]
        for collection in ax.collections:
            points += [[float(x), float(y)] for x, y in collection.get_offsets()]
        for line in ax.lines:
            xy = [[float(x), float(y)] for x, y in line.get_xydata()]
            if line.get_linestyle() in ("None", "", " "):
                points += xy
            else:
                lines.append(xy)
    return {"points": points, "lines": lines, "texts": texts}


matplotlib.figure.Figure.savefig = record_savefig
matplotlib.pyplot.show = record_show
builtins.open = open_data
sys.argv = ["oecd.py"]
try:
    namespace = runpy.run_path("oecd.py", run_name="__main__")

    # Call main ourselves if oecd.py defines it but never calls it
    if not plots and not matplotlib.pyplot.get_fignums() and callable(namespace.get("main")):
        namespace["main"]()
    record_open_figures()
except BaseException as e:
    with open_("error.txt", "w") as f:
        f.write(f"{type(e).__name__}: {e}")
    raise
finally:
    with open_("plots.json", "w") as f:
        json.dump(plots, f)
