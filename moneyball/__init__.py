from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for i in range(12):
        check50.exists(f"{i + 1}.sql")
    check50.include("moneyball-check.db")


@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    check_multi_col(
        run_query("1.sql"),
        [{'2001', '6482665.29'},
        {'2000', '6366333.19'},
        {'4537389.21', '1999'},
        {'3922388.73', '1998'},
        {'1997', '3542527.69'},
        {'1996', '3083634.96'},
        {'1995', '2862284.95'},
        {'2161123.9', '1994'},
        {'1993', '1943314.78'},
        {'1647884.62', '1992'},
        {'1991', '837435.92'},
        {'444020.88', '1990'},
        {'1989', '449020.88'},
        {'523125.0', '1988'},
        {'504166.67', '1987'},
        {'1986', '605000.0'},
        {'800000.0', '1985'}],
        ordered=True,
    )


@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    check_multi_col(
        run_query("2.sql"),
        [{'6300000', '2001'},
        {'2000', '6300000'},
        {'6500000', '1999'},
        {'1998', '6400000'},
        {'1997', '6850000'},
        {'1996', '6650000'},
        {'1995', '6700000'},
        {'1994', '5500000'},
        {'1993', '5200000'},
        {'1992', '2100000'},
        {'2566667', '1991'},
        {'1316667', '1990'},
        {'2466667', '1989'},
        {'1988', '1700000'},
        {'1987', '1350000'},
        {'1986', '1150000'},
        {'800000', '1985'}],
        ordered=True,
    )


@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_multi_col(
        run_query("3.sql"),
        [{'2001', '22'},
        {'40', '2000'},
        {'1999', '48'},
        {'1998', '56'},
        {'1997', '56'},
        {'1996', '49'},
        {'1995', '17'},
        {'40', '1994'},
        {'45', '1993'},
        {'1992', '27'},
        {'22', '1991'},
        {'22', '1990'},
        {'1989', '16'}],
        ordered=True,
    )


@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_multi_col(
        run_query("4.sql"),
        [{'200000', 'Pujols', 'Albert'},
        {'David', 'Eckstein', '200000'},
        {'200000', 'Jimmy', 'Rollins'},
        {'Rivas', 'Luis', '200000'},
        {'215000', 'Doug', 'Mientkiewicz'},
        {'Juan', '215000', 'Pierre'},
        {'230000', 'Paul', 'Lo Duca'},
        {'Torii', 'Hunter', '230000'},
        {'Long', '240750', 'Terrence'},
        {'Ramirez', '285000', 'Aramis'},
        {'Corey', '300000', 'Koskie'},
        {'Lance', 'Berkman', '305000'},
        {'Bubba', '335000', 'Trammell'},
        {'Cabrera', 'Orlando', '340000'},
        {'1125000', 'Richie', 'Sexson'},
        {'Glaus', '1250000', 'Troy'},
        {'2183333', 'Stewart', 'Shannon'},
        {'3250000', 'Boone', 'Bret'},
        {'Rich', '3250000', 'Aurilia'},
        {'4500000', 'Anderson', 'Garret'},
        {'4833333', 'Luis', 'Gonzalez'},
        {'Todd', '4950000', 'Helton'},
        {'5666667', 'Suzuki', 'Ichiro'},
        {'Cal', '6300000', 'Ripken'},
        {'7875000', 'Thome', 'Jim'},
        {'Palmeiro', 'Rafael', '9000000'},
        {'10300000', 'Bonds', 'Barry'},
        {'Larry', 'Walker', '12166667'},
        {'Green', 'Shawn', '12166667'},
        {'Bernie', 'Williams', '12357143'},
        {'Greg', '12500000', 'Maddux'},
        {'Griffey', '12500000', 'Ken'},
        {'Sosa', 'Sammy', '12500000'},
        {'Jeter', '12600000', 'Derek'},
        {'13000000', 'Martinez', 'Pedro'},
        {'Ramirez', 'Manny', '13050000'},
        {'Vaughn', 'Mo', '13166667'},
        {'13350000', 'Randy', 'Johnson'},
        {'Mike', 'Piazza', '13571429'},
        {'Delgado', '13650000', 'Carlos'},
        {'Brown', 'Kevin', '15714286'},
        {'Alex', 'Rodriguez', '22000000'}],
        ordered=True,
    )


@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_single_col(
        run_query("5.sql"),
        ['Cleveland Indians', 'Kansas City Athletics', 'St. Louis Browns'],
        ordered=False,
    )


@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_multi_col(
        run_query("6.sql"),
        [{'Minnesota Twins', '618'},
        {'Colorado Rockies', '573'},
        {'Anaheim Angels', '507'},
        {'448', 'Seattle Mariners'},
        {'365', 'Texas Rangers'}],
        ordered=True,
    )


@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_multi_col(
        run_query("7.sql"),
        [{'Alex', 'Rodriguez'}],
        ordered=False,
    )


@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_single_cell(run_query("8.sql"), '10300000')


@check50.check(exists)
def test9():
    """9.sql produces correct result"""
    check_multi_col(
        run_query("9.sql"),
        [{'Philadelphia Phillies', '200000.0'},
        {'200000.0', 'St. Louis Cardinals'},
        {'Minnesota Twins', '236250.0'},
        {'Oakland Athletics', '240750.0'},
        {'Pittsburgh Pirates', '285000.0'}],
        ordered=True,
    )


@check50.check(exists)
def test10():
    """10.sql produces correct result"""
    check_multi_col(
        run_query("10.sql"),
        [{'2001', 'Garret', '4500000', '28', 'Anderson'},
        {'Garret', '3250000', '35', 'Anderson', '2000'},
        {'Garret', '2200000', '21', 'Anderson', '1999'},
        {'Garret', '1998', 'Anderson', '1500000', '15'},
        {'Garret', '600000', '8', 'Anderson', '1997'},
        {'250000', '1996', 'Garret', '12', 'Anderson'},
        {'Garret', '16', '1995', 'Anderson', '114000'},
        {'0', 'Garret', '109000', 'Anderson', '1994'},
        {'2001', '3250000', '37', 'Rich', 'Aurilia'},
        {'1550000', 'Rich', '20', 'Aurilia', '2000'},
        {'950000', 'Rich', '22', 'Aurilia', '1999'},
        {'Rich', '1998', '9', 'Aurilia', '265000'},
        {'Rich', '175000', '5', 'Aurilia', '1997'},
        {'1996', 'Rich', '3', 'Aurilia', '110500'},
        {'2', '109000', '1995', 'Rich', 'Aurilia'},
        {'2001', '305000', 'Lance', '34', 'Berkman'},
        {'Lance', '200000', '4', 'Berkman', '1999'},
        {'2001', 'Barry', 'Bonds', '10300000', '73'},
        {'49', 'Bonds', '10658826', '2000', 'Barry'},
        {'Barry', '9381057', '34', 'Bonds', '1999'},
        {'8916667', '37', '1998', 'Bonds', 'Barry'},
        {'40', '8666667', 'Bonds', '1997', 'Barry'},
        {'1996', '8416667', '42', 'Bonds', 'Barry'},
        {'1995', '8166666', 'Bonds', '33', 'Barry'},
        {'37', '5166666', 'Bonds', '1994', 'Barry'},
        {'4516666', '46', 'Bonds', '1993', 'Barry'},
        {'4800000', '34', 'Bonds', '1992', 'Barry'},
        {'Bonds', '1991', '25', 'Barry', '2300000'},
        {'1990', 'Bonds', '33', 'Barry', '850000'},
        {'1989', 'Bonds', '360000', '19', 'Barry'},
        {'1988', '24', '220000', 'Bonds', 'Barry'},
        {'100000', 'Bonds', '1987', '25', 'Barry'},
        {'1986', '60000', '16', 'Bonds', 'Barry'},
        {'2001', '3250000', '37', 'Bret', 'Boone'},
        {'Bret', '3750000', 'Boone', '2000', '19'},
        {'2900000', 'Bret', '20', 'Boone', '1999'},
        {'Bret', '1998', 'Boone', '2800000', '24'},
        {'Bret', 'Boone', '1700000', '7', '1997'},
        {'1996', 'Bret', '12', 'Boone', '725000'},
        {'Bret', '1995', '400000', 'Boone', '15'},
        {'Bret', '12', '175000', 'Boone', '1994'},
        {'120000', 'Bret', '12', '1993', 'Boone'},
        {'15714286', '2001', 'Brown', 'Kevin', '1'},
        {'15714286', '0', 'Brown', '2000', 'Kevin'},
        {'0', 'Brown', '10714286', 'Kevin', '1999'},
        {'0', 'Brown', '1998', '4935000', 'Kevin'},
        {'0', '4510000', 'Brown', '1997', 'Kevin'},
        {'1996', '0', 'Brown', '3350000', 'Kevin'},
        {'0', 'Brown', '4225000', '1995', 'Kevin'},
        {'0', 'Brown', '4225000', '1994', 'Kevin'},
        {'0', 'Brown', '1993', '2800000', 'Kevin'},
        {'0', 'Brown', '1200000', '1992', 'Kevin'},
        {'0', 'Brown', '1991', '355000', 'Kevin'},
        {'0', 'Brown', '218000', '1990', 'Kevin'},
        {'Kevin', '0', 'Brown', '1989', '72500'},
        {'2001', '14', 'Cabrera', '340000', 'Orlando'},
        {'13', 'Cabrera', '2000', 'Orlando', '265000'},
        {'225000', 'Cabrera', '8', 'Orlando', '1999'},
        {'1998', '170500', 'Cabrera', '3', 'Orlando'},
        {'Delgado', '2001', '13650000', '39', 'Carlos'},
        {'Delgado', 'Carlos', '41', '6600000', '2000'},
        {'Delgado', '44', '5075000', 'Carlos', '1999'},
        {'Delgado', 'Carlos', '2400000', '1998', '38'},
        {'Delgado', 'Carlos', '30', '500000', '1997'},
        {'Delgado', '1996', 'Carlos', '25', '165000'},
        {'Delgado', '109000', 'Carlos', '9', '1994'},
        {'Eckstein', '2001', 'David', '200000', '4'},
        {'Glaus', '2001', 'Troy', '41', '1250000'},
        {'Glaus', 'Troy', '275000', '47', '2000'},
        {'Glaus', 'Troy', '207500', '1999', '29'},
        {'Glaus', 'Troy', '1998', '170000', '1'},
        {'Luis', '2001', 'Gonzalez', '57', '4833333'},
        {'Luis', 'Gonzalez', '31', '3333333', '2000'},
        {'2050000', 'Luis', 'Gonzalez', '26', '1999'},
        {'Luis', 'Gonzalez', '23', '2000000', '1998'},
        {'Luis', 'Gonzalez', '10', '1400000', '1997'},
        {'1996', 'Luis', 'Gonzalez', '1400000', '15'},
        {'Luis', 'Gonzalez', '1995', '7', '1500000'},
        {'Luis', 'Gonzalez', '6', '1995', '1500000'},
        {'Luis', 'Gonzalez', '8', '1630000', '1994'},
        {'Luis', 'Gonzalez', '1993', '360000', '15'},
        {'Luis', 'Gonzalez', '10', '285000', '1992'},
        {'Luis', 'Gonzalez', '105000', '13', '1991'},
        {'2001', '49', 'Shawn', '12166667', 'Green'},
        {'Shawn', '2000', 'Green', '24', '9416667'},
        {'42', 'Shawn', 'Green', '1999', '3125000'},
        {'1998', '1475000', 'Shawn', '35', 'Green'},
        {'16', 'Shawn', '1997', '500000', 'Green'},
        {'1996', '287500', 'Shawn', '11', 'Green'},
        {'15', '1995', 'Shawn', '130000', 'Green'},
        {'0', '109000', 'Shawn', 'Green', '1994'},
        {'0', '109000', 'Shawn', '1993', 'Green'},
        {'2001', 'Ken', 'Griffey', '12500000', '22'},
        {'40', 'Ken', '9329700', '2000', 'Griffey'},
        {'Ken', 'Griffey', '8760532', '1999', '48'},
        {'8153667', '56', 'Ken', '1998', 'Griffey'},
        {'7885532', '56', 'Ken', '1997', 'Griffey'},
        {'1996', '7650000', 'Ken', '49', 'Griffey'},
        {'7600000', '1995', '17', 'Ken', 'Griffey'},
        {'40', '5100000', 'Ken', 'Griffey', '1994'},
        {'Ken', '4150000', '1993', '45', 'Griffey'},
        {'27', 'Ken', '2025000', 'Griffey', '1992'},
        {'Ken', '1991', '700000', 'Griffey', '22'},
        {'180000', 'Ken', '1990', 'Griffey', '22'},
        {'16', 'Ken', '68000', '1989', 'Griffey'},
        {'2001', '49', 'Todd', '4950000', 'Helton'},
        {'42', 'Todd', '1300000', '2000', 'Helton'},
        {'750000', 'Todd', '35', '1999', 'Helton'},
        {'190000', '1998', 'Todd', '25', 'Helton'},
        {'Todd', '5', '150000', '1997', 'Helton'},
        {'2001', '27', 'Torii', 'Hunter', '230000'},
        {'225000', '5', 'Torii', '2000', 'Hunter'},
        {'Torii', '9', '200000', 'Hunter', '1999'},
        {'Jeter', '2001', '12600000', '21', 'Derek'},
        {'Jeter', '10000000', '2000', '15', 'Derek'},
        {'Jeter', 'Derek', '5000000', '24', '1999'},
        {'Jeter', '750000', '1998', '19', 'Derek'},
        {'Jeter', '550000', '10', '1997', 'Derek'},
        {'Jeter', '1996', '10', '130000', 'Derek'},
        {'0', '2001', 'Johnson', '13350000', 'Randy'},
        {'0', 'Johnson', '13350000', '2000', 'Randy'},
        {'0', 'Johnson', '9700000', 'Randy', '1999'},
        {'0', 'Johnson', '1998', '6000000', 'Randy'},
        {'0', 'Johnson', '1998', '6000000', 'Randy'},
        {'0', 'Johnson', '6325000', '1997', 'Randy'},
        {'1996', '0', 'Johnson', '6025000', 'Randy'},
        {'0', 'Johnson', '4675000', '1995', 'Randy'},
        {'0', 'Johnson', '3325000', 'Randy', '1994'},
        {'0', 'Johnson', '2625000', '1993', 'Randy'},
        {'0', 'Johnson', '1392500', 'Randy', '1992'},
        {'0', 'Johnson', '350000', '1991', 'Randy'},
        {'0', 'Johnson', '1990', '150000', 'Randy'},
        {'0', 'Johnson', '1989', 'Randy', '70000'},
        {'0', 'Johnson', '1989', 'Randy', '70000'},
        {'2001', 'Corey', '26', 'Koskie', '300000'},
        {'245000', 'Corey', '9', '2000', 'Koskie'},
        {'Corey', '200000', '11', 'Koskie', '1999'},
        {'2001', '25', 'Paul', 'Lo Duca', '230000'},
        {'3', '200000', 'Paul', 'Lo Duca', '1999'},
        {'Long', '2001', 'Terrence', '12', '240750'},
        {'Greg', '0', '2001', '12500000', 'Maddux'},
        {'Greg', '0', '11100000', '2000', 'Maddux'},
        {'Greg', '2', '10600000', '1999', 'Maddux'},
        {'Greg', '0', '1998', 'Maddux', '9600000'},
        {'Greg', '0', '6775000', '1997', 'Maddux'},
        {'1996', 'Greg', '0', '6675000', 'Maddux'},
        {'Greg', '0', '1995', '6500000', 'Maddux'},
        {'Greg', '0', '4975000', '1994', 'Maddux'},
        {'Greg', '0', '5875000', '1993', 'Maddux'},
        {'Greg', '4200000', '1992', '1', 'Maddux'},
        {'Greg', '2400000', '1991', '1', 'Maddux'},
        {'Greg', '0', '437500', '1990', 'Maddux'},
        {'Greg', '0', '275000', '1989', 'Maddux'},
        {'82500', 'Greg', '0', '1988', 'Maddux'},
        {'0', '2001', '13000000', 'Martinez', 'Pedro'},
        {'0', 'Martinez', '11500000', '2000', 'Pedro'},
        {'0', 'Martinez', '11100000', '1999', 'Pedro'},
        {'0', '1998', 'Martinez', '7575000', 'Pedro'},
        {'0', '3615000', 'Martinez', '1997', 'Pedro'},
        {'1996', '0', '315000', 'Martinez', 'Pedro'},
        {'0', '1995', '270000', 'Martinez', 'Pedro'},
        {'0', 'Martinez', '200000', '1994', 'Pedro'},
        {'0', 'Martinez', '1993', '119000', 'Pedro'},
        {'2001', 'Doug', '215000', '15', 'Mientkiewicz'},
        {'Doug', '2', '200000', '1999', 'Mientkiewicz'},
        {'2001', 'Palmeiro', 'Rafael', '9000000', '47'},
        {'39', 'Palmeiro', 'Rafael', '8620921', '2000'},
        {'Palmeiro', 'Rafael', '47', '8849931', '1999'},
        {'43', 'Palmeiro', 'Rafael', '1998', '6515828'},
        {'Palmeiro', 'Rafael', '5337021', '1997', '38'},
        {'1996', '5406603', '39', 'Palmeiro', 'Rafael'},
        {'4906603', '39', 'Palmeiro', '1995', 'Rafael'},
        {'5406603', 'Palmeiro', '23', 'Rafael', '1994'},
        {'37', 'Palmeiro', 'Rafael', '1993', '4550000'},
        {'Palmeiro', 'Rafael', '3850000', '1992', '22'},
        {'Palmeiro', 'Rafael', '1475000', '26', '1991'},
        {'Palmeiro', 'Rafael', '14', '1990', '300000'},
        {'Palmeiro', 'Rafael', '1989', '8', '212000'},
        {'1988', 'Palmeiro', 'Rafael', '8', '90000'},
        {'Palmeiro', 'Rafael', '14', '62500', '1987'},
        {'36', '2001', '13571429', 'Mike', 'Piazza'},
        {'12071429', 'Mike', 'Piazza', '2000', '38'},
        {'40', '7171428', 'Mike', 'Piazza', '1999'},
        {'23', 'Mike', '1998', 'Piazza', '8000000'},
        {'Mike', '1998', 'Piazza', '8000000', '9'},
        {'0', 'Mike', '1998', 'Piazza', '8000000'},
        {'40', 'Mike', 'Piazza', '7000000', '1997'},
        {'1996', '36', 'Mike', '2700000', 'Piazza'},
        {'32', '1995', 'Mike', 'Piazza', '900000'},
        {'Mike', '600000', 'Piazza', '1994', '24'},
        {'126000', 'Mike', 'Piazza', '35', '1993'},
        {'2001', '2', 'Juan', '215000', 'Pierre'},
        {'2001', '37', 'Albert', '200000', 'Pujols'},
        {'2001', '285000', 'Aramis', '34', 'Ramirez'},
        {'6', 'Aramis', '2000', 'Ramirez', '230000'},
        {'6', '1998', 'Aramis', '170000', 'Ramirez'},
        {'2001', '41', '13050000', 'Ramirez', 'Manny'},
        {'4250000', '2000', 'Ramirez', 'Manny', '38'},
        {'4350000', '44', 'Ramirez', 'Manny', '1999'},
        {'1998', '2850000', '45', 'Ramirez', 'Manny'},
        {'26', '2100000', '1997', 'Ramirez', 'Manny'},
        {'1996', '1100000', '33', 'Ramirez', 'Manny'},
        {'31', '1995', '150000', 'Ramirez', 'Manny'},
        {'17', '111000', 'Ramirez', '1994', 'Manny'},
        {'2', '109000', '1993', 'Ramirez', 'Manny'},
        {'2001', '14', 'Cal', '6300000', 'Ripken'},
        {'Cal', '6300000', 'Ripken', '2000', '15'},
        {'Cal', '18', '6500000', 'Ripken', '1999'},
        {'1998', '6400000', '14', 'Cal', 'Ripken'},
        {'17', 'Cal', 'Ripken', '1997', '6850000'},
        {'1996', '6650000', 'Cal', '26', 'Ripken'},
        {'6700000', '1995', '17', 'Cal', 'Ripken'},
        {'5500000', '13', 'Cal', 'Ripken', '1994'},
        {'Cal', '1993', 'Ripken', '24', '5200000'},
        {'14', 'Cal', 'Ripken', '2100000', '1992'},
        {'Cal', '34', 'Ripken', '1991', '2566667'},
        {'1990', 'Cal', 'Ripken', '21', '1316667'},
        {'Cal', '1989', 'Ripken', '21', '2466667'},
        {'1988', '23', 'Cal', 'Ripken', '1700000'},
        {'27', '1350000', 'Cal', 'Ripken', '1987'},
        {'1986', '1150000', 'Cal', 'Ripken', '25'},
        {'800000', 'Cal', '26', 'Ripken', '1985'},
        {'Rivas', 'Luis', '2001', '200000', '7'},
        {'2001', '22000000', '52', 'Alex', 'Rodriguez'},
        {'4362500', '41', 'Alex', '2000', 'Rodriguez'},
        {'42', 'Alex', '3112500', 'Rodriguez', '1999'},
        {'2162500', '1998', '42', 'Alex', 'Rodriguez'},
        {'1062500', '23', 'Alex', '1997', 'Rodriguez'},
        {'1996', '36', '442334', 'Alex', 'Rodriguez'},
        {'1995', '5', '442333', 'Alex', 'Rodriguez'},
        {'0', '442333', 'Alex', 'Rodriguez', '1994'},
        {'2001', 'Jimmy', '14', 'Rollins', '200000'},
        {'2001', 'Sexson', '1125000', 'Richie', '45'},
        {'16', 'Sexson', '247000', 'Richie', '2000'},
        {'Sexson', '14', '247000', 'Richie', '2000'},
        {'31', 'Sexson', '219000', 'Richie', '1999'},
        {'Sexson', '1998', '175000', '11', 'Richie'},
        {'Sosa', '2001', '64', 'Sammy', '12500000'},
        {'Sosa', 'Sammy', '2000', '50', '11000000'},
        {'Sosa', '63', 'Sammy', '9000000', '1999'},
        {'Sosa', '8325000', '66', 'Sammy', '1998'},
        {'Sosa', '36', 'Sammy', '5500000', '1997'},
        {'Sosa', '40', '1996', 'Sammy', '4750000'},
        {'Sosa', '36', '1995', 'Sammy', '4300000'},
        {'Sosa', '2950000', 'Sammy', '25', '1994'},
        {'Sosa', 'Sammy', '745000', '1993', '33'},
        {'Sosa', 'Sammy', '180000', '8', '1992'},
        {'Sosa', '10', 'Sammy', '1991', '150000'},
        {'Sosa', 'Sammy', '1990', '100000', '15'},
        {'Sosa', 'Sammy', '68000', '3', '1989'},
        {'Sosa', 'Sammy', '68000', '1989', '1'},
        {'2001', '2183333', '12', 'Stewart', 'Shannon'},
        {'683333', 'Stewart', '21', '2000', 'Shannon'},
        {'433333', 'Stewart', '11', 'Shannon', '1999'},
        {'192500', '1998', '12', 'Stewart', 'Shannon'},
        {'0', '154000', 'Stewart', '1997', 'Shannon'},
        {'2001', '5666667', '8', 'Suzuki', 'Ichiro'},
        {'2001', '7875000', '49', 'Thome', 'Jim'},
        {'8175000', '37', 'Thome', 'Jim', '2000'},
        {'8225000', 'Thome', 'Jim', '33', '1999'},
        {'4800000', '1998', 'Thome', '30', 'Jim'},
        {'40', '2625000', 'Thome', 'Jim', '1997'},
        {'1996', 'Thome', '1600000', 'Jim', '38'},
        {'1995', 'Thome', '825000', '25', 'Jim'},
        {'325000', 'Thome', '20', 'Jim', '1994'},
        {'135000', 'Thome', '1993', 'Jim', '7'},
        {'2', 'Thome', '110000', 'Jim', '1992'},
        {'Thome', '100000', '1991', 'Jim', '1'},
        {'2001', 'Bubba', '335000', 'Trammell', '25'},
        {'Bubba', '253000', 'Trammell', '7', '2000'},
        {'Bubba', '253000', 'Trammell', '3', '2000'},
        {'Bubba', '14', 'Trammell', '230000', '1999'},
        {'Bubba', '180000', '1998', '12', 'Trammell'},
        {'Bubba', 'Trammell', '4', '150000', '1997'},
        {'Vaughn', '36', 'Mo', '11166667', '2000'},
        {'Vaughn', 'Mo', '7166666', '33', '1999'},
        {'40', 'Vaughn', '6650000', 'Mo', '1998'},
        {'Vaughn', '6350000', 'Mo', '35', '1997'},
        {'1996', 'Vaughn', '44', 'Mo', '5400000'},
        {'Vaughn', '39', '1995', 'Mo', '2775000'},
        {'Vaughn', 'Mo', '675000', '26', '1994'},
        {'Vaughn', 'Mo', '290000', '1993', '29'},
        {'Vaughn', 'Mo', '13', '165000', '1992'},
        {'Vaughn', 'Mo', '100000', '1991', '4'},
        {'Larry', '2001', '12166667', 'Walker', '38'},
        {'Larry', '12142857', '2000', '9', 'Walker'},
        {'Larry', '5417857', '37', 'Walker', '1999'},
        {'Larry', '23', '6050000', '1998', 'Walker'},
        {'Larry', '49', '6325000', 'Walker', '1997'},
        {'Larry', '1996', '4375000', '18', 'Walker'},
        {'Larry', '36', '5019382', '1995', 'Walker'},
        {'Larry', '4025000', 'Walker', '19', '1994'},
        {'Larry', '1993', 'Walker', '3000000', '22'},
        {'Larry', '23', '990000', 'Walker', '1992'},
        {'Larry', '16', '1991', 'Walker', '185000'},
        {'2001', '12357143', 'Bernie', 'Williams', '26'},
        {'12357143', 'Bernie', 'Williams', '30', '2000'},
        {'Bernie', '9857143', 'Williams', '25', '1999'},
        {'Bernie', '1998', 'Williams', '26', '8300000'},
        {'Bernie', 'Williams', '21', '5300000', '1997'},
        {'1996', 'Bernie', 'Williams', '3000000', '29'},
        {'Bernie', '400000', '1995', 'Williams', '18'},
        {'Bernie', '225000', '12', 'Williams', '1994'},
        {'Bernie', '12', 'Williams', '1993', '150000'},
        {'Bernie', '125000', '5', 'Williams', '1992'},
        {'Bernie', '100000', 'Williams', '3', '1991'}],
        ordered=True,
        show_expected=False,
    )


@check50.check(exists)
def test11():
    """11.sql produces correct result"""
    check_multi_col(
        run_query("11.sql"),
        [{'Pujols', 'Albert', '1030'},
        {'Juan', 'Pierre', '1064'},
        {'1111', 'Jimmy', 'Rollins'},
        {'David', '1204', 'Eckstein'},
        {'1295', 'Doug', 'Mientkiewicz'},
        {'Rivas', 'Luis', '1333'},
        {'1352', 'Long', 'Terrence'},
        {'1564', 'Paul', 'Lo Duca'},
        {'Torii', '1564', 'Hunter'},
        {'Ramirez', 'Aramis', '1574'}],
        ordered=True,
    )


@check50.check(exists)
def test12():
    """12.sql produces correct result"""
    check_multi_col(
        run_query("12.sql"),
        [{'Torii', 'Hunter'},
        {'Paul', 'Lo Duca'},
        {'Long', 'Terrence'},
        {'Doug', 'Mientkiewicz'},
        {'Pujols', 'Albert'},
        {'Ramirez', 'Aramis'}],
        ordered=True,
    )


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
        db = SQL("sqlite:///moneyball-check.db")
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


def check_multi_col(actual, expected, ordered=False, show_expected=True):
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
    return _check(actual, expected, ordered, show_expected)


def _check(actual, expected, ordered=False, show_expected=True):
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
        if show_expected:
            raise check50.Mismatch(
                "\n".join(", ".join(list(sorted(entry))) for entry in list(expected)),
                "\n".join(", ".join(list(sorted(entry))) for entry in list(result)),
            )
        else:
            raise check50.Failure(f"Query returned incorrect results")
    return None
