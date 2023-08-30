from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for i in range(13):
        check50.exists(f"{i + 1}.sql")
    check50.include("cyberchase.db")


@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    check_single_col(
        run_query("1.sql"),
        ['Lost My Marbles',
         'Castleblanca',
         'R-Fair City',
         'Snow Day to be Exact',
         'Sensible Flats',
         'Zeus on the Loose',
         'The Poddleville Case',
         'And They Counted Happily Ever After',
         'Clock Like An Egyptian',
         'Secrets of Symmetria',
         'A Day at the Spa',
         'Of All The Luck',
         'Eureeka',
         'Cool It',
         'Find Those Gleamers',
         'Codename: Icky',
         'Return to Sensible Flats',
         'Problem Solving in Shangri-La',
         'Send in the Clones',
         'Trading Places',
         'Less Than Zero',
         'Model Behavior',
         'Fortress of Attitude',
         'Size Me Up',
         'A Battle of Equals',
         'Out of Sync'],
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    check_multi_col(
        run_query("2.sql"),
        [{'Lost My Marbles', '1'},
         {'2', 'Hugs & Witches'},
         {'EcoHaven CSE', '3'},
         {'Balancing Act', '4'},
         {'5', 'The Halloween Howl'},
         {'6', "Digit's B-Day Surprise"},
         {'Weather Watchers Gone With The Fog', '7'},
         {"The Hacker's Challenge", '8'},
         {'9', 'An Urchin Matter'},
         {'Fit to be Heroes', '10'},
         {'11', 'Watts of Halloween Trouble'},
         {'Space Waste Odyssey', '12'},
         {'13', 'Duck Stop'},
         {'14', 'Clean-Up on Isle 8'}],
        ordered=False,
    )


@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_cell(run_query("3.sql"), 'CYB091')


@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_single_col(
        run_query("4.sql"),
        ['Space Waste Odyssey',
         'Space Waste Odyssey',
         'Giving Thanks Day',
         'A Garden Grows in Botlyn',
         'Missing Bats in Sensible Flats',
         'Water Woes',
         'Soil Turmoil',
         'Hacker Hugs a Tree',
         'Pursuit of the Prism of Power',
         'Composting in the Clutch',
         'A Camping Conundrum',
         'Journey of a Thousand Food Miles',
         'Duck Stop',
         'The Great Outdoors',
         'Coral Grief',
         'Sustainable by Design',
         "Hacker's Bright Idea",
         'Buzz and the Tree',
         'The Lilting Loons',
         'Living in Disharmony',
         'Traffic Trouble',
         'A Garden is Born',
         'Clean-Up on Isle 8',
         'Weather or Not',
         'Weather or Not',
         'Trees, Please'],
        ordered=False,
    )


@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_single_cell(run_query("5.sql"), 'Starlight Night')


@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_single_col(
        run_query("6.sql"),
        ["Digit's B-Day Surprise", 'When Penguins Fly'],
        ordered=False,
    )


@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_multi_col(
        run_query("7.sql"),
        [{'Zeus on the Loose', 'Fractions'},
         {'Harriet Hippo & the Mean Green', 'Equivalent Fractions'},
         {'Shari Spotter and the Cosmic Crumpets', 'Mixed-Number Fractions'},
         {'A Fraction of a Chance', 'Fractions 101'},
         {'Peace, Love, and Hackerness', 'Measuring with Mixed Number Fractions'},
         {'Trash Creep', 'Fractions, Effects of Trash, and Recycling'}],
        ordered=False,
    )


@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_single_cell(run_query("8.sql"), '31')


@check50.check(exists)
def test9():
    """9.sql produces correct result"""
    check_single_cell(run_query("9.sql"), '74')


@check50.check(exists)
def test10():
    """10.sql produces correct result"""
    check_multi_col(
        run_query("10.sql"),
        [{'Lost My Marbles', '1', 'CYB001'},
         {'6', 'Zeus on the Loose', 'CYB002'},
         {'And They Counted Happily Ever After', 'CYB003', '8'},
         {'CYB004', '3', 'R-Fair City'},
         {'CYB005', '5', 'Sensible Flats'},
         {'CYB006', '7', 'The Poddleville Case'},
         {'4', 'CYB007', 'Snow Day to be Exact'},
         {'10', 'CYB008', 'Secrets of Symmetria'},
         {'9', 'Clock Like An Egyptian', 'CYB009'},
         {'2', 'CYB010', 'Castleblanca'},
         {'11', 'CYB011', 'A Day at the Spa'},
         {'CYB012', 'Return to Sensible Flats', '17'},
         {'Less Than Zero', '21', 'CYB013'},
         {'CYB014', '14', 'Cool It'},
         {'CYB015', 'Eureeka', '13'},
         {'18', 'CYB016', 'Problem Solving in Shangri-La'},
         {'CYB017', '15', 'Find Those Gleamers'},
         {'Of All The Luck', 'CYB018', '12'},
         {'CYB019', 'Codename: Icky', '16'},
         {'19', 'CYB020', 'Send in the Clones'},
         {'20', 'Trading Places', 'CYB021'},
         {'Out of Sync', '26', 'CYB022'},
         {'22', 'CYB023', 'Model Behavior'},
         {'CYB024', '23', 'Fortress of Attitude'},
         {'CYB025', 'Size Me Up', '24'},
         {'CYB026', 'A Battle of Equals', '25'},
         {'Harriet Hippo & the Mean Green', 'CYB027', '29'},
         {'CYB028', '30', 'True Colors'},
         {'CYB029', 'Hugs & Witches', '27'},
         {'28', 'CYB030', 'Totally Rad'},
         {'CYB031', '31', 'All the Right Angles'},
         {'33', 'CYB032', 'The Eye of Rom'},
         {'32', "Mother's Day", 'CYB033'},
         {'40', 'CYB034', 'Trick or Treat'},
         {'34', 'A Whale of a Tale', 'CYB035'},
         {'35', 'Double Trouble', 'CYB036'},
         {'CYB037', 'Raising the Bar', '36'},
         {'CYB038', 'A Time to Cook', '39'},
         {'38', 'CYB039', 'The Guilty Party'},
         {'The Wedding Scammer', '37', 'CYB040'},
         {'CYB041', '42', 'The Borg of the Ring'},
         {'CYB042', 'A World Without Zero', '43'},
         {'CYB043', '41', 'EcoHaven CSE'},
         {'44', 'CYB044', 'A Piece of the Action'},
         {'CYB045', '46', 'The Grapes of Plath'},
         {'CYB046', 'The Creech Who Would be Crowned', '45'},
         {'48', 'CYB047', 'Be Reasonable'},
         {'Shari Spotter and the Cosmic Crumpets', 'CYB048', '51'},
         {'52', 'CYB049', 'Starlight Night'},
         {'A Perfect Fit', 'CYB050', '47'},
         {'The Snelfu Snafu', '49', 'CYB051'},
         {'CYB052', '50', 'The Snelfu Snafu'},
         {'A Crinkle In Time', '60', 'CYB053'},
         {'The Icky Factor', '54', 'CYB054'},
         {'The Case of the Missing Memory', 'CYB055', '59'},
         {'Balancing Act', 'CYB056', '53'},
         {'55', 'Penguin Tears', 'CYB057'},
         {'A Change of Art', '58', 'CYB058'},
         {'CYB059', '56', 'Past Perfect Prediction'},
         {'CYB060', "A Broom Of One's Own", '61'},
         {'Measure For Measure', '57', 'CYB061'},
         {'62', 'A Tikiville Turkey Day', 'CYB062'},
         {'A Clean Sweep', 'CYB063', '64'},
         {'Designing Mr. Perfect', 'CYB064', '65'},
         {'CYB065', 'The Flying Parallinis', '68'},
         {'66', 'EcoHaven Ooze', 'CYB066'},
         {'CYB067', '67', 'The Fairy Borg Father'},
         {'Inside Hacker', '70', 'CYB068'},
         {'On the Line', 'CYB069', '71'},
         {'72', 'A Fraction of a Chance', 'CYB070'},
         {'CYB071', 'The Halloween Howl', '63'},
         {'69', 'Crystal Clear', 'CYB072'},
         {'CYB073', "Digit's B-Day Surprise", '73'},
         {'74', 'CYB074', 'When Penguins Fly'},
         {'Unhappily Ever After', 'CYB075', '75'},
         {'CYB076', '76', "Escape From Merlin's Maze"},
         {'Step By Step', 'CYB077', '77'},
         {'CYB078', 'Chaos as Usual', '81'},
         {'Team Spirit', 'CYB079', '78'},
         {'Jimaya Jam', 'CYB080', '79'},
         {'A Perfect Score', 'CYB081', '80'},
         {'82', 'CYB082', 'Spheres of Fears'},
         {'Weather Watchers Gone With The Fog', '83', 'CYB083'},
         {'The Emperor Has Snow Clothes', 'CYB084', '84'},
         {'CYB085', 'The X-Factor', '85'},
         {'86', 'CYB086', "Blowin' in the Wind Blowin in the Wind"},
         {'CYB087', '87', "Father's Day"},
         {'The Deedle Beast', 'CYB088', '88'},
         {'Spellbound', 'CYB089', '89'},
         {"The Hacker's Challenge", 'CYB090', '90'},
         {'CYB091', 'Hackerized!', '93'},
         {'94', 'The Bluebird of Zappiness', 'CYB092'},
         {'Face-Off!', 'CYB093', '91'},
         {'Peace, Love, and Hackerness', 'CYB094', '92'},
         {'An Urchin Matter', 'CYB095', '95'},
         {'CYB096', 'Going Solar', '96'},
         {'Trash Creep', '97', 'CYB097'},
         {'CYB099', 'The Cyberchase Movie', '98'},
         {'The Cyberchase Movie', '99', 'CYB100'},
         {'Fit to be Heroes', '100', 'CYB101'},
         {'A Recipe for Chaos', '101', 'CYB102'},
         {'A Seedy Business', 'CYB103', '102'},
         {'103', 'CYB104', 'Parks and Recreation'},
         {'CYB105', 'Bottled Up', '104'},
         {'Watts of Halloween Trouble', '105', 'CYB106'},
         {"Creech's Creature Quandary", 'CYB107', '106'},
         {'107', 'A Murky Mystery in Mermaidos', 'CYB108'},
         {'Plantasaurus!', '108', 'CYB109'},
         {'A Reboot Eve to Remember', 'CYB110', '109'},
         {'110', 'Housewarming Party', 'CYB111'},
         {'111', 'Invasion of the Funky Flower', 'CYB112'},
         {'A Renewable Hope', '112', 'CYB113'},
         {'113', 'CYB114', 'The Migration Situation'},
         {'114', 'CYB115', "Back to Canalia's Future"},
         {'CYB116', '117', 'Giving Thanks Day'},
         {'CYB117', '116', 'Space Waste Odyssey'},
         {'115', 'CYB118', 'Space Waste Odyssey'},
         {'118', 'CYB119', 'A Garden Grows in Botlyn'},
         {'119', 'CYB120', 'Missing Bats in Sensible Flats'},
         {'Water Woes', '120', 'CYB121'},
         {'Soil Turmoil', 'CYB122', '121'},
         {'122', 'CYB123', 'Hacker Hugs a Tree'},
         {'CYB124', '123', 'Pursuit of the Prism of Power'},
         {'124', 'Composting in the Clutch', 'CYB125'},
         {'CYB126', 'A Camping Conundrum', '125'},
         {'CYB127', 'Journey of a Thousand Food Miles', '126'},
         {'CYB128', '127', 'Duck Stop'},
         {'CYB129', '128', 'The Great Outdoors'},
         {'Coral Grief', 'CYB130', '129'},
         {'CYB131', '130', 'Sustainable by Design'},
         {'131', "Hacker's Bright Idea", 'CYB132'},
         {'Buzz and the Tree', '132', 'CYB133'},
         {'CYB134', '133', 'The Lilting Loons'},
         {'Living in Disharmony', '134', 'CYB135'},
         {'Traffic Trouble', 'CYB136', '135'},
         {'A Garden is Born', '136', 'CYB137'},
         {'CYB138', '137', 'Clean-Up on Isle 8'},
         {'CYB139', '140', 'Trees, Please'},
         {'Weather or Not', 'CYB140', '138'},
         {'Weather or Not', 'CYB141', '139'}],
        ordered=True,
    )


@check50.check(exists)
def test11():
    """11.sql produces correct result"""
    check_single_col(
        run_query("11.sql"),
        ['The Halloween Howl',
         'The Flying Parallinis',
         'The Fairy Borg Father',
         'On the Line',
         'Inside Hacker',
         'EcoHaven Ooze',
         'Designing Mr. Perfect',
         'Crystal Clear',
         'A Fraction of a Chance',
         'A Clean Sweep'],
        ordered=True,
    )


@check50.check(exists)
def test12():
    """12.sql produces correct result"""
    check_single_cell(run_query("12.sql"), '136')


# no test 13, since query 13 is student's choice


def run_query(filename):
    """
    Runs the SQL query contained in 'filename' and returns its output.

    positional arguments:
        filename (str)      file containing SQL query

    returns:
        list[dict]
    """

    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///cyberchase.db")
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error when executing query: {str(e)}")


def check_single_col(actual, expected, ordered=False):
    """
    Checks that the single column in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (list)           expected result to match against

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert list to list of frozen sets or set of frozen sets
    try:
        if ordered:
            expected = [frozenset([elt]) for elt in expected]
        else:
            expected = {frozenset([elt]) for elt in expected}
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered)


def check_single_cell(actual, expected):
    """
    Checks that the single cell in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (single element) expected result to match against

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert element to list of frozen set; ordered doesn't matter
    try:
        expected = [frozenset([expected])]
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered=True)


def check_multi_col(actual, expected, ordered=False):
    """
    Checks that the columns in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (list[set])      expected result to match against

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert list of sets to list of frozen sets or set of frozen sets
    try:
        if ordered:
            expected = [frozenset(unfrozen_set) for unfrozen_set in expected]
        else:
            expected = {frozenset(unfrozen_set) for unfrozen_set in expected}
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered)


def _check(actual, expected, ordered=False):
    """
    Checks that the SQL output in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected                  expected result to match against
            if ordered, should be list[frozenset];
            otherwise, set[frozenset]  (frozenset is needed for nested sets)

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # convert list of dictionaries to list of frozen sets or set of frozen sets,
    # depending on whether 'ordered' is True
    try:
        result = []
        for row_dict in actual:
            values = [str(elt) for elt in list(row_dict.values())]
            result.append(frozenset(values))
        result = result if ordered else set(result)
    except Exception as e:
        raise check50.Failure(f"Error with format of query: {str(e)}")

    # check result of query against expected values
    if result != expected:
        raise check50.Mismatch(
            "\n".join(", ".join(list(sorted(entry))) for entry in list(expected)),
            "\n".join(", ".join(list(sorted(entry))) for entry in list(result)),
        )
    return None
