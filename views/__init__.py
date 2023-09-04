from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for i in range(10):
        check50.exists(f"{i + 1}.sql")
    check50.include("views.db")


@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    check_multi_col(
        run_query("1.sql"),
        [{'神奈川沖浪裏', 'The Great Wave off Kanagawa'},
         {'Fine Wind, Clear Morning', '凱風快晴'},
         {'Thunderstorm Beneath the Summit', '山下白雨'},
         {'深川万年橋下', 'Under Mannen Bridge at Fukagawa'},
         {'東都駿台', 'Sundai, Edo'},
         {'青山円座松', 'Cushion Pine at Aoyama'},
         {'武州千住', 'Senju, Musashi But'},
         {'Inume Pass, Kōshū', '甲州犬目峠'},
         {'Fuji View Field in Owari Province', '尾州不二見原'},
         {'Ejiri in Suruga Province', '駿州江尻'},
         {'A sketch of the Mitsui shop in Suruga in Edo', '江都駿河町三井見世略図'},
         {'Sunset across the Ryōgoku bridge from the bank of the Sumida River at '
          'Onmayagashi',
          '御厩川岸より両国橋夕陽見'},
         {'五百らかん寺さざゐどう', 'Sazai hall - Temple of Five Hundred Rakan'},
         {'礫川雪の旦', 'Tea house at Koishikawa. The morning after a snowfall'},
         {'下目黒', 'Shimomeguro'},
         {'隠田の水車', 'Watermill at Onden'},
         {'相州江の島', 'Enoshima in Sagami Province'},
         {'Shore of Tago Bay, Ejiri at Tōkaidō', '東海道江尻田子の浦略図'},
         {'東海道吉田', 'Yoshida at Tōkaidō'},
         {'上総の海路', 'The Kazusa Province sea route'},
         {'Nihonbashi bridge in Edo', '江戸日本橋'},
         {'隅田川関屋の里', 'Barrier Town on the Sumida River'},
         {'登戸浦', 'Bay of Noboto'},
         {'The lake of Hakone in Sagami Province', '相州箱根湖水'},
         {'Mount Fuji reflects in Lake Kawaguchi, seen from the Misaka Pass in Kai '
          'Province',
          '甲州三坂水面'},
         {'Hodogaya on the Tōkaidō', '東海道保土ケ谷'},
         {'武州玉川', 'Tama River in Musashi Province'},
         {'Asakusa Hongan-ji temple in the Eastern capital', '東都浅草本願寺'},
         {'Tsukuda Island in Musashi Province', '武陽佃島'},
         {'Shichiri beach in Sagami Province', '相州七里浜'},
         {'相州梅沢庄', 'Umezawa in Sagami Province'},
         {'甲州石班沢', 'Kajikazawa in Kai Province'},
         {'Mishima Pass in Kai Province', '甲州三嶌越'},
         {'遠江山中', 'Mount Fuji from the mountains of Tōtōmi'},
         {'A View of Mount Fuji Across Lake Suwa', '信州諏訪湖'},
         {'常州牛掘', 'Ushibori in Hitachi Province'},
         {'東都一石ばし', 'Ichikoku Bridge in the Eastern Capital'},
         {'東都駿河町', 'The Suruga District in the Eastern Capital'},
         {'Sukiyagashi in the Eastern Capital', '東都数奇屋河岸'},
         {'東都佃沖', 'Off Tsukuda Island in the Eastern Capital'},
         {'Ochanomizu in the Eastern Capital', '東都御茶の水'},
         {'Ryōgoku in the Eastern Capital', '東都両ごく'},
         {'The Sumida Embankment in the Eastern Capital', '東都墨田堤'},
         {'東都あすか山', 'Mt. Asuka in the Eastern Capital'},
         {'The Teahouse with the View of Mt. Fuji at Zōshigaya', '雑司かや不二見茶や'},
         {'東都目黒夕日か岡', 'Twilight Hill at Meguro in the Eastern Capital'},
         {'鴻之臺戸根川', 'Wild Goose Hill and the Tone River'},
         {'Koganei in Musashi Province', '武蔵小金井'},
         {'The Tama River in Musashi Province', '武蔵玉川'},
         {'武蔵越が谷在', 'Koshigaya in Musashi Province'},
         {'武蔵野毛横濱', 'Noge and Yokohama in Musashi Province'},
         {'Cherry Blossoms at Honmoku in Musashi Province', '武蔵本牧のはな'},
         {'相州三浦之海上', 'The Sea off the Miura Peninsula in Sagami Province'},
         {'The Sagami River', 'さがみ川'},
         {'The Seven Ri Beach in Sagami Province', '相摸七里か濱'},
         {'The Entrance gate at Enoshima in Sagami Province', '相摸江之島入口'},
         {'Lake at Hakone', 'はこ根の湖すい'},
         {'伊豆の山中', 'The Izu Mountains'},
         {'駿河薩タ之海上', 'The Sea off Satta in Suruga Province'},
         {'駿河三保之松原', 'The Pine Forest of Miho in Suruga Province'},
         {'Fuji on the left of the Tōkaidō Road', '東海堂左り不二'},
         {'駿遠大井川', 'The Ōi River between Suruga and Totomi Provinces'},
         {'伊勢二見か浦', 'Futami Bay in Ise Province'},
         {'信州諏訪之湖', 'Lake Suwa in Shinano Province'},
         {'Shiojiri Pass in Shinano Province', '信濃塩尻峠'},
         {'Misaka Pass in Kai Province', '甲斐御坂越'},
         {'甲斐大月の原', 'The Ōtsuki Plain in Kai Province'},
         {'Dog Eye Pass in Kai Province', '甲斐犬目峠'},
         {'下総小金原', 'Kogane Plain in Shimōsa Province'},
         {'上総黒戸の浦', 'Kuroto Bay in Kazusa Province'},
         {'Mt. Kanō in Kazusa Province', '上総鹿埜山'},
         {'The Hota Coast in Awa Province', '房州保田ノ海岸'}],
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    check_single_col(
        run_query("2.sql"),
        ['#8ba1a5', '#b3b399', '#a6a799'],
        ordered=False,
    )


@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_cell(run_query("3.sql"), '4')


@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_single_cell(run_query("4.sql"), '9')


@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_single_cell(run_query("5.sql"), '0.65')


@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_single_cell(run_query("6.sql"), '7.42')


@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_single_col(
        run_query("7.sql"),
        ['The Sea off the Miura Peninsula in Sagami Province',
         'Futami Bay in Ise Province',
         'The Sumida Embankment in the Eastern Capital',
         'Sukiyagashi in the Eastern Capital',
         'Cherry Blossoms at Honmoku in Musashi Province'],
        ordered=True,
    )


@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_single_col(
        run_query("8.sql"),
        ['Mount Fuji reflects in Lake Kawaguchi, seen from the Misaka Pass in Kai '
         'Province',
         'Kajikazawa in Kai Province',
         'Shimomeguro',
         'Bay of Noboto',
         'Ushibori in Hitachi Province'],
        ordered=True,
    )


@check50.check(exists)
def test9():
    """9.sql produces correct result"""
    check_multi_col(
        run_query("9.sql"),
        [{'Hokusai', 'A View of Mount Fuji Across Lake Suwa'}],
        ordered=True,
    )


@check50.check(exists)
def test10():
    """10.sql runs without error"""
    run_query("10.sql")


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
        db = SQL("sqlite:///views.db")
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
