import json
import os
import shlex
import itertools

import check50


@check50.check()
def valid():
    """project exists and is valid Scratch program"""

    # Make sure there is only one .sb2 file.
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb3")]

    if len(filenames) > 1:
        raise check50.Failure("more than one .sb3 file found. Make sure there's only one!")
    elif not filenames:
        raise check50.Failure("no .sb3 file found")

    filename = filenames[0]

    # Ensure that unzipped .sb2 file contains .json file.
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("invalid .sb3 file")
    check50.exists("project.json")

    with open("project.json") as f:
        project = json.load(f)

    return project["targets"]

@check50.check(valid)
def two_sprites(project):
    """project contains at least two sprites"""

    num_sprites = sum(not target["isStage"] for target in project)

    if num_sprites < 2:
        raise check50.Failure(f"only {num_sprites} sprite{'' if num_sprites == 1 else 's'} found, 2 required")

@check50.check(valid)
def non_cat(project):
    """project contains a non-cat sprite"""

    cat_sprite_ids = {"fc0687f38ae230b8765eebf4100e2653",
                      "06c57b43f5a7d3500fd149de265c2289"}

    if all(target["isStage"] or {costume["assetId"] for costume in target["costumes"]} == cat_sprite_ids for target in project):
        raise check50.Failure("no non-cat sprite found")

@check50.check(valid)
def three_blocks(project):
    """project contains at least three blocks"""

    num_blocks = sum(len(target["blocks"]) for target in project)
    if num_blocks < 3:
        raise check50.Failure(f"only {num_blocks} script{'' if num_blocks == 1 else 's'} found, 3 required")

@check50.check(valid)
def uses_condition(project):
    """project uses at least one condition"""

    if not contains_blocks(project, ["control_repeat", "control_if_else", "control_if", "motion_ifonedgebounce"]):
        raise check50.Failure("no conditions found, 1 required")

@check50.check(valid)
def uses_loop(project):
    """project uses at least one loop"""

    # Search project scripts for a repeat, repeat until, or forever block.
    if not contains_blocks(project, ["control_forever", "control_repeat_until", "control_repeat"]):
        raise check50.Failure("no loops found, 1 required")

@check50.check(valid)
def uses_variable(project):
    """project uses at least one variable"""

    if not any(target["variables"] for target in project):
        raise check50.Failure("no variables found, 1 required")

@check50.check(valid)
def uses_sound(project):
    """project uses at least one sound"""
    if not contains_blocks(project, ["sound_play", "sound_playuntildone", "music_playNoteForBeats", "music_playDrumForBeats", "text2speech_speakAndWait"]):
        raise check50.Failure("no sounds used, 1 required")


def contains_blocks(project, opcodes):
    """Return whether project contains any blocks with their names in opcodes"""
    return any(any((isinstance(block, dict) and block["opcode"] in opcodes) for block in target["blocks"].values())
               for target in project)
