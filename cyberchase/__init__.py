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
        [{'1', 'Lost My Marbles'},
         {'2', 'Hugs & Witches'},
         {'3', 'EcoHaven CSE'},
         {'Balancing Act', '4'},
         {'5', 'The Halloween Howl'},
         {"Digit's B-Day Surprise", '6'},
         {'7', 'Weather Watchers Gone With The Fog'},
         {"The Hacker's Challenge", '8'},
         {'9', 'An Urchin Matter'},
         {'10', 'Fit to be Heroes'},
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
        [{'Fractions', 'Zeus on the Loose'},
         {'Equivalent Fractions', 'Harriet Hippo & the Mean Green'},
         {'Shari Spotter and the Cosmic Crumpets', 'Mixed-Number Fractions'},
         {'A Fraction of a Chance', 'Fractions 101'},
         {'Measuring with Mixed Number Fractions', 'Peace, Love, and Hackerness'},
         {'Fractions, Effects of Trash, and Recycling', 'Trash Creep'}],
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
        [{'1', 'CYB001', 'Lost My Marbles'},
         {'CYB002', '6', 'Zeus on the Loose'},
         {'And They Counted Happily Ever After', '8', 'CYB003'},
         {'CYB004', 'R-Fair City', '3'},
         {'Sensible Flats', 'CYB005', '5'},
         {'The Poddleville Case', '7', 'CYB006'},
         {'CYB007', '4', 'Snow Day to be Exact'},
         {'10', 'CYB008', 'Secrets of Symmetria'},
         {'9', 'CYB009', 'Clock Like An Egyptian'},
         {'2', 'Castleblanca', 'CYB010'},
         {'11', 'CYB011', 'A Day at the Spa'},
         {'CYB012', '17', 'Return to Sensible Flats'},
         {'Less Than Zero', 'CYB013', '21'},
         {'Cool It', '14', 'CYB014'},
         {'13', 'Eureeka', 'CYB015'},
         {'Problem Solving in Shangri-La', 'CYB016', '18'},
         {'15', 'Find Those Gleamers', 'CYB017'},
         {'Of All The Luck', 'CYB018', '12'},
         {'Codename: Icky', '16', 'CYB019'},
         {'CYB020', '19', 'Send in the Clones'},
         {'CYB021', '20', 'Trading Places'},
         {'CYB022', 'Out of Sync', '26'},
         {'CYB023', '22', 'Model Behavior'},
         {'Fortress of Attitude', '23', 'CYB024'},
         {'Size Me Up', '24', 'CYB025'},
         {'CYB026', '25', 'A Battle of Equals'},
         {'29', 'CYB027', 'Harriet Hippo & the Mean Green'},
         {'True Colors', 'CYB028', '30'},
         {'Hugs & Witches', '27', 'CYB029'},
         {'28', 'Totally Rad', 'CYB030'},
         {'All the Right Angles', 'CYB031', '31'},
         {'CYB032', '33', 'The Eye of Rom'},
         {'CYB033', '32', "Mother's Day"},
         {'CYB034', '40', 'Trick or Treat'},
         {'34', 'CYB035', 'A Whale of a Tale'},
         {'35', 'Double Trouble', 'CYB036'},
         {'36', 'Raising the Bar', 'CYB037'},
         {'39', 'A Time to Cook', 'CYB038'},
         {'CYB039', 'The Guilty Party', '38'},
         {'37', 'CYB040', 'The Wedding Scammer'},
         {'CYB041', '42', 'The Borg of the Ring'},
         {'CYB042', 'A World Without Zero', '43'},
         {'CYB043', '41', 'EcoHaven CSE'},
         {'A Piece of the Action', 'CYB044', '44'},
         {'The Grapes of Plath', '46', 'CYB045'},
         {'The Creech Who Would be Crowned', 'CYB046', '45'},
         {'Be Reasonable', '48', 'CYB047'},
         {'Shari Spotter and the Cosmic Crumpets', '51', 'CYB048'},
         {'CYB049', 'Starlight Night', '52'},
         {'47', 'A Perfect Fit', 'CYB050'},
         {'CYB051', '49', 'The Snelfu Snafu'},
         {'50', 'The Snelfu Snafu', 'CYB052'},
         {'A Crinkle In Time', 'CYB053', '60'},
         {'54', 'The Icky Factor', 'CYB054'},
         {'59', 'CYB055', 'The Case of the Missing Memory'},
         {'53', 'Balancing Act', 'CYB056'},
         {'55', 'Penguin Tears', 'CYB057'},
         {'A Change of Art', 'CYB058', '58'},
         {'56', 'Past Perfect Prediction', 'CYB059'},
         {"A Broom Of One's Own", '61', 'CYB060'},
         {'CYB061', '57', 'Measure For Measure'},
         {'A Tikiville Turkey Day', 'CYB062', '62'},
         {'64', 'A Clean Sweep', 'CYB063'},
         {'Designing Mr. Perfect', '65', 'CYB064'},
         {'The Flying Parallinis', 'CYB065', '68'},
         {'EcoHaven Ooze', '66', 'CYB066'},
         {'The Fairy Borg Father', '67', 'CYB067'},
         {'70', 'Inside Hacker', 'CYB068'},
         {'On the Line', 'CYB069', '71'},
         {'CYB070', '72', 'A Fraction of a Chance'},
         {'CYB071', 'The Halloween Howl', '63'},
         {'Crystal Clear', 'CYB072', '69'},
         {'73', "Digit's B-Day Surprise", 'CYB073'},
         {'CYB074', '74', 'When Penguins Fly'},
         {'Unhappily Ever After', '75', 'CYB075'},
         {'CYB076', '76', "Escape From Merlin's Maze"},
         {'77', 'Step By Step', 'CYB077'},
         {'Chaos as Usual', 'CYB078', '81'},
         {'78', 'CYB079', 'Team Spirit'},
         {'CYB080', 'Jimaya Jam', '79'},
         {'80', 'CYB081', 'A Perfect Score'},
         {'Spheres of Fears', '82', 'CYB082'},
         {'Weather Watchers Gone With The Fog', 'CYB083', '83'},
         {'84', 'CYB084', 'The Emperor Has Snow Clothes'},
         {'The X-Factor', 'CYB085', '85'},
         {"Blowin' in the Wind Blowin in the Wind", 'CYB086', '86'},
         {'CYB087', '87', "Father's Day"},
         {'CYB088', 'The Deedle Beast', '88'},
         {'89', 'CYB089', 'Spellbound'},
         {"The Hacker's Challenge", '90', 'CYB090'},
         {'93', 'Hackerized!', 'CYB091'},
         {'The Bluebird of Zappiness', 'CYB092', '94'},
         {'91', 'CYB093', 'Face-Off!'},
         {'CYB094', '92', 'Peace, Love, and Hackerness'},
         {'CYB095', 'An Urchin Matter', '95'},
         {'96', 'Going Solar', 'CYB096'},
         {'97', 'Trash Creep', 'CYB097'},
         {'98', 'CYB099', 'The Cyberchase Movie'},
         {'CYB100', '99', 'The Cyberchase Movie'},
         {'CYB101', 'Fit to be Heroes', '100'},
         {'101', 'CYB102', 'A Recipe for Chaos'},
         {'A Seedy Business', 'CYB103', '102'},
         {'Parks and Recreation', 'CYB104', '103'},
         {'CYB105', '104', 'Bottled Up'},
         {'105', 'Watts of Halloween Trouble', 'CYB106'},
         {'CYB107', "Creech's Creature Quandary", '106'},
         {'107', 'A Murky Mystery in Mermaidos', 'CYB108'},
         {'108', 'CYB109', 'Plantasaurus!'},
         {'109', 'A Reboot Eve to Remember', 'CYB110'},
         {'CYB111', '110', 'Housewarming Party'},
         {'111', 'CYB112', 'Invasion of the Funky Flower'},
         {'CYB113', 'A Renewable Hope', '112'},
         {'The Migration Situation', '113', 'CYB114'},
         {"Back to Canalia's Future", 'CYB115', '114'},
         {'117', 'Giving Thanks Day', 'CYB116'},
         {'116', 'Space Waste Odyssey', 'CYB117'},
         {'Space Waste Odyssey', '115', 'CYB118'},
         {'118', 'A Garden Grows in Botlyn', 'CYB119'},
         {'CYB120', '119', 'Missing Bats in Sensible Flats'},
         {'Water Woes', 'CYB121', '120'},
         {'CYB122', '121', 'Soil Turmoil'},
         {'Hacker Hugs a Tree', 'CYB123', '122'},
         {'123', 'Pursuit of the Prism of Power', 'CYB124'},
         {'124', 'Composting in the Clutch', 'CYB125'},
         {'125', 'CYB126', 'A Camping Conundrum'},
         {'Journey of a Thousand Food Miles', 'CYB127', '126'},
         {'CYB128', 'Duck Stop', '127'},
         {'CYB129', '128', 'The Great Outdoors'},
         {'CYB130', 'Coral Grief', '129'},
         {'Sustainable by Design', 'CYB131', '130'},
         {"Hacker's Bright Idea", '131', 'CYB132'},
         {'CYB133', 'Buzz and the Tree', '132'},
         {'133', 'The Lilting Loons', 'CYB134'},
         {'CYB135', 'Living in Disharmony', '134'},
         {'CYB136', '135', 'Traffic Trouble'},
         {'A Garden is Born', 'CYB137', '136'},
         {'CYB138', '137', 'Clean-Up on Isle 8'},
         {'140', 'Trees, Please', 'CYB139'},
         {'CYB140', 'Weather or Not', '138'},
         {'CYB141', 'Weather or Not', '139'}],
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


@check50.check(exists)
def test13():
    """13.sql runs without error"""
    run_query("13.sql")


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


def check_query_existence(filename, keywords=[]):
    """
    Checks that filename exists and contains keywords in keywords.

    positional arguments:
        filename (str)       filename to check
        keywords (list[str]) keywords to ensure are in filename

    returns:
        None

    raises:
        check50.Failure
    """
    try:
        with open(filename, "r") as f:
            contents = f.read().upper()
            for keyword in keywords:
                if keyword.upper() not in contents:
                    raise check50.Failure(
                        f"Expected to find {keyword.upper()} in {filename}.",
                        help=f"Did you include {keyword.upper()} in {filename}?",
                    )
    except FileNotFoundError:
        raise check50.Failure(f"Could not find file {filename}")


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
