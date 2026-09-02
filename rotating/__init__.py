import json
import os
import shlex

import check50


@check50.check()
def valid():
    """project exists and is a valid Scratch program"""
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb3")]

    if len(filenames) > 1:
        raise check50.Failure("more than one .sb3 file found. Make sure there's only one!")
    if not filenames:
        raise check50.Failure("no .sb3 file found")

    filename = filenames[0]
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("invalid .sb3 file")

    check50.exists("project.json")
    with open("project.json") as project_file:
        try:
            return json.load(project_file)["targets"]
        except (KeyError, json.JSONDecodeError):
            raise check50.Failure("invalid Scratch project.json")
