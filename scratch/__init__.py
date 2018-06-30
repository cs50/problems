import json
import os
import shlex
import itertools

import check50


@check50.check()
def valid():
    """project exists and is valid Scratch program"""

    # Make sure there is only one .sb2 file.
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb2")]

    if len(filenames) > 1:
        raise check50.Failure("more than one .sb2 file found. Make sure there's only one!")
    elif not filenames:
        raise check50.Failure("no .sb2 file found.")

    filename = filenames[0]

    # Ensure that unzipped .sb2 file contains .json file.
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("invalid .sb2 file.")
    check50.exists("project.json")

@check50.check(valid)
def two_sprites():
    """project contains at least two sprites"""

    with open("project.json") as f:
        project = json.load(f)

    # Loop over children: includes sprites and stages.
    num_sprites = sum("costumes" in child for child in project["children"])

    if num_sprites < 2:
        raise check50.Failure(f"only {num_sprites} sprite{'' if num_sprites == 1 else 's'} found, 2 required.")

@check50.check(valid)
def non_cat():
    """project contains a non-cat sprite"""

    with open("project.json") as f:
        project = json.load(f)

    for child in project["children"]:

        # Skip over any non-sprites (e.g. backdrops).
        if "costumes" not in child:
            continue

        # Check if the sprite has the default costume.
        is_cat = any(costume["baseLayerMD5"] == "09dc888b0b7df19f70d81588ae73420e.svg"
                       for costume in child.get("costumes", []))

        # If it doesn't meow, we've found a non-cat sprite.
        if not is_cat:
            return

    # If we haven't returned, then no non-cat sprite found.
    raise check50.Failure("requires a non-cat sprite.")

@check50.check(valid)
def three_scripts():
    """project contains at least three scripts"""

    with open("project.json") as f:
        project = json.load(f)

    # Add up scripts from each sprite or backdrop.
    num_scripts = sum(len(child.get("scripts", [])) for child in project["children"])
    num_scripts += len(project.get("scripts", []))

    if num_scripts < 3:
        raise check50.Failure(f"only {num_scripts} script{'' if num_scripts == 1 else 's'} found, 3 required.")

@check50.check(valid)
def uses_condition():
    """project uses at least one condition"""
    with open("project.json") as f:
        project = json.load(f)

    # Search project scripts for an if or if/else block.
    if not project_contains_keywords(project, ["doIf", "doIfElse", "doUntil"]):
        raise check50.Failure("no conditions found, 1 required.")

@check50.check(valid)
def uses_loop():
    """project uses at least one loop"""
    with open("project.json") as f:
        project = json.load(f)

    # Search project scripts for a repeat, repeat until, or forever block.
    if not project_contains_keywords(project, ["doRepeat", "doUntil", "doForever"]):
        raise check50.Failure("no loops found, 1 required.")

@check50.check(valid)
def uses_variable():
    """project uses at least one variable"""
    with open("project.json") as f:
        project = json.load(f)

    # Look for global variables.
    if project.get("variables"):
        return

    # Look for local-to-sprite variables.
    if any(child.get("variables") for child in project["children"]):
        return

    # If we've reached this point, no variable found.
    raise check50.Failure("no variables found, 1 required.")

@check50.check(valid)
def uses_sound():
    """project uses at least one sound"""
    with open("project.json") as f:
        project = json.load(f)

    # Search scripts for a sound block.
    keywords = ["playSound:", "doPlaySoundAndWait", "playDrum", "noteOn:duration:elapsed:from:"]
    if not project_contains_keywords(project, keywords):
        raise check50.Failure("no sounds found, 1 required.")


def project_contains_keywords(project, keywords):
    """Returns True if project contains at least one of the keywords."""
    return any(any(contains(script, keywords)
                   for script in child.get("scripts", []))
               for child in itertools.chain(project["children"], [project]))


def contains(script, keywords):
    """Performs DFS on the script to determine if keyword exists."""

    # The keyword must be the first item in a list.
    if type(script) != list or not script:
        return False

    if script[0] in keywords:
        return True

    # Iterate over all children.
    return any(contains(child, keywords) for child in script)
