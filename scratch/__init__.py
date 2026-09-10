import json
import os
import shlex

import check50


# Opcodes that start a script; a top-level block with any other opcode is
# a fragment left disconnected in the editor.
HAT_OPCODES = {"event_whenflagclicked",
               "event_whenkeypressed",
               "event_whenbroadcastreceived",
               "event_whenbackdropswitchesto",
               "event_whenthisspriteclicked",
               "control_start_as_clone",
               "procedures_definition"}


@check50.check()
def valid():
    """project exists and is valid Scratch program"""

    # Make sure there is only one .sb3 file.
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

    cat_sprite_ids = {"bcf454acf82e4504149f7ffe07081dbc",
                      "0fb9be3e8397c983338cb71dc84d0b25"}

    # A subset, not an exact match: a cat whose costume2 has been deleted is
    # still a cat.
    if all(target["isStage"] or {costume["assetId"] for costume in target["costumes"]} <= cat_sprite_ids for target in project):
        raise check50.Failure("no non-cat sprite found")

@check50.check(valid)
def three_blocks(project):
    """project contains at least three scripts"""

    num_scripts = sum(len(scripts(target)) for target in project)
    if num_scripts < 3:
        raise check50.Failure(f"only {num_scripts} script{'' if num_scripts == 1 else 's'} found, 3 required")

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

    # Declaring isn't using: Scratch declares "my variable" in every project.
    declared = {variable_id for target in project for variable_id in target["variables"]}

    if not declared & used_variables(project):
        raise check50.Failure("no variables used, 1 required")

@check50.check(valid)
def uses_custom_block(project):
    """project uses at least one custom block that takes an input"""

    for target in project:
        for block in target["blocks"].values():
            if isinstance(block, dict) and block["opcode"] == "procedures_definition":
                # A definition points at a prototype block, whose mutation lists
                # the inputs the block takes as a JSON-encoded string.
                prototype = target["blocks"][block["inputs"]["custom_block"][1]]
                if len(json.loads(prototype["mutation"]["argumentids"])) >= 1:
                    return

    raise check50.Failure("no custom block taking at least one input found, 1 required")

def scripts(target):
    """Return the ids of the blocks that start a real script in target"""
    return [block_id for block_id, block in target["blocks"].items()
            if isinstance(block, dict) and block.get("topLevel") and block["opcode"] in HAT_OPCODES]

def reachable_blocks(target):
    """Yield the blocks reachable from a hat block, following next and inputs"""
    blocks = target["blocks"]
    visited = set()
    pending = scripts(target)

    while pending:
        block_id = pending.pop()
        if block_id in visited:
            continue
        visited.add(block_id)

        block = blocks.get(block_id)
        if not isinstance(block, dict):
            continue

        yield block

        if block.get("next") is not None:
            pending.append(block["next"])

        # Within an input, a string member is the id of a nested block.
        for value in block.get("inputs", {}).values():
            if isinstance(value, list):
                pending.extend(item for item in value if isinstance(item, str))

def used_variables(project):
    """Return the ids of the variables that project's scripts reference"""
    used = set()

    for target in project:
        for block in reachable_blocks(target):
            # Set, change, show and hide name their variable in a field.
            field = block.get("fields", {}).get("VARIABLE")
            if field:
                used.add(field[1])

            # A variable read inside an input is inlined as [12, name, id].
            for value in block.get("inputs", {}).values():
                if isinstance(value, list):
                    used.update(item[2] for item in value
                                if isinstance(item, list) and len(item) > 2 and item[0] == 12)

    return used

def contains_blocks(project, opcodes):
    """Return whether project's scripts contain any blocks with their names in opcodes"""
    return any(block["opcode"] in opcodes
               for target in project
               for block in reachable_blocks(target))
