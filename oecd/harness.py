"""Runs oecd.py, recording what each saved figure contains in plots.json."""

import json
import os
import runpy
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.figure

plots = {}
savefig = matplotlib.figure.Figure.savefig


def record(figure, fname, *args, **kwargs):
    plots[os.path.basename(str(fname))] = describe(figure)
    return savefig(figure, fname, *args, **kwargs)


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


matplotlib.figure.Figure.savefig = record
sys.argv = ["oecd.py"]
try:
    runpy.run_path("oecd.py", run_name="__main__")
except BaseException as e:
    with open("error.txt", "w") as f:
        f.write(f"{type(e).__name__}: {e}")
    raise
finally:
    with open("plots.json", "w") as f:
        json.dump(plots, f)
