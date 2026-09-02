import json
import os
import shlex

import check50


@check50.check()
def exists_six_squares():
    """sixSquares.sb3 exists"""
    check50.exists("sixSquares.sb3")


@check50.check()
def exists_six_triangles():
    """sixTriangles.sb3 exists"""
    check50.exists("sixTriangles.sb3")


@check50.check()
def exists_six_other_shapes():
    """sixOtherShapes.sb3 exists"""
    check50.exists("sixOtherShapes.sb3")


@check50.check(exists_six_squares)
def valid_six_squares():
    """sixSquares.sb3 is a valid Scratch program"""
    load_project("sixSquares.sb3")


@check50.check(exists_six_triangles)
def valid_six_triangles():
    """sixTriangles.sb3 is a valid Scratch program"""
    load_project("sixTriangles.sb3")


@check50.check(exists_six_other_shapes)
def valid_six_other_shapes():
    """sixOtherShapes.sb3 is a valid Scratch program"""
    load_project("sixOtherShapes.sb3")


def load_project(filename):
    """Unzip the given .sb3 file and return its list of targets."""
    directory = os.path.splitext(filename)[0]
    if check50.run(f"unzip -o -d {shlex.quote(directory)} {shlex.quote(filename)}").exit():
        raise check50.Failure(f"{filename} is not a valid .sb3 file")

    project_path = os.path.join(directory, "project.json")
    check50.exists(project_path)
    with open(project_path) as project_file:
        try:
            return json.load(project_file)["targets"]
        except (KeyError, json.JSONDecodeError):
            raise check50.Failure(f"{filename} does not contain a valid Scratch project.json")
