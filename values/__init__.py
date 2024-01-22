import json
import os
import shlex
import itertools

import check50


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
def one_ask(project):
    """project contains ask and wait block"""

    num_asks = parse_blocks(project)["asks"]

    if num_asks < 1:
        raise check50.Failure("project should include an ask and wait block")


@check50.check(valid)
def one_answer(project):
    """project contains at least one answer block"""

    num_answers = parse_blocks(project)["answers"]

    if num_answers < 1:
        raise check50.Failure("project should include an answer block")


@check50.check(valid)
def one_join(project):
    """project contains at least one join block"""

    num_joins = parse_blocks(project)["joins"]

    if num_joins < 1:
        raise check50.Failure("project should include a join block")


################################################################################
# Helper functions
################################################################################
def parse_blocks(targets):
    stages = [target for target in targets if target["isStage"] == True]
    return {
        "sprites": len([target for target in targets if target["isStage"] == False]),
        "backdrops": count_costumes(stages),
        "looks": count_blocks(
            targets,
            [
                "looks_sayforsecs",
                "looks_say",
                "looks_thinkforsecs",
                "looks_think",
                "looks_switchcostumeto",
                "looks_costume",
                "looks_nextcostume",
                "looks_switchbackdropto",
                "looks_backdrops",
                "looks_nextbackdrop",
                "looks_changesizeby",
                "looks_setsizeto",
                "looks_changeeffectby",
                "looks_seteffectto",
                "looks_cleargraphiceffects",
                "looks_show",
                "looks_hide",
                "looks_gotofrontback",
                "looks_goforwardbackwardlayers",
            ],
        ),
        "motions": count_blocks(
            targets,
            [
                "motion_movesteps",
                "motion_turnright",
                "motion_turnleft",
                "motion_goto",
                "motion_goto_menu",
                "motion_gotoxy",
                "motion_glideto",
                "motion_glideto_menu",
                "motion_glidsecstoxy",
                "motion_pointindirection",
                "motion_pointtowards",
                "motion_pointtowardsmenu",
                "motion_changexby",
                "motion_setx",
                "motionchangeyby",
                "motion_sety",
                "motion_ifonedgebounce",
                "motion_setrotationstyle",
            ],
        ),
        "events": count_blocks(
            targets,
            [
                "event_whenflagclicked",
                "event_whenkeypressed",
                "event_whenthisspriteclicked",
                "event_whenbackdropswitchesto",
                "event_whengreaterthan",
                "event_broadcast",
                "event_broadcastandwait",
            ],
        ),
        "asks": count_blocks(targets, ["sensing_askandwait"]),
        "answers": count_blocks(targets, ["sensing_answer"]),
        "joins": count_blocks(targets, ["operator_join"]),
        "ifs": count_blocks(targets, ["control_if"]),
        "ifelses": count_blocks(targets, ["control_if_else"]),
        "fors": count_blocks(targets, ["control_forever"]),
        "repeats": count_blocks(targets, ["control_repeat_until", "control_repeat"]),
        "customs": count_blocks(
            targets,
            [
                "procedures_definition",
                "procedures_prototype",
                "procedures_call",
                "argument_reporter_string_number",
                "argument_reporter_boolean",
            ],
        ),
        "variables": count_blocks(
            targets,
            [
                "data_setvariableto",
                "data_changevariableby",
                "data_showvariable",
                "data_hidevariable",
            ],
        ),
        "sounds": count_blocks(
            targets,
            [
                "sound_play",
                "sound_playuntildone",
                "music_playDrumForBeats",
                "music_playNoteForBeats",
                "text2speech_speakAndWait",
            ],
        ),
        "broadcasts": count_blocks(
            targets, ["event_broadcast", "event_broadcastandwait"]
        ),
        "clones": count_blocks(
            targets,
            [
                "control_start_as_clone",
                "control_create_clone_of",
                "control_create_clone_of_menu",
                "control_delete_this_clone",
            ],
        ),
        "conditions": count_blocks(
            targets, ["control_repeat_until", "control_if_else", "control_if"]
        ),
        "loops": count_blocks(
            targets, ["control_forever", "control_repeat_until", "control_repeat"]
        ),
    }


def count_blocks(targets, blocks):
    count = 0
    for target in targets:
        for block in target["blocks"]:
            try:
                if target["blocks"][block]["opcode"] in blocks:
                    count += 1
            except:
                pass
    return count


def count_costumes(targets):
    count = 0
    for target in targets:
        if len(target["costumes"]) > 1:
            count += len(target["costumes"]) - 1
    return count
################################################################################