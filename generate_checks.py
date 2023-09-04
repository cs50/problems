from cs50 import SQL

import argparse
import sqlparse
import os
from natsort import natsorted
from textwrap import dedent, indent
from pprint import pformat


def main():
    """
    usage: generate_checks.py [-h] db solutions helpers_template

    Generate check50 scripts for movies-like problems.

    positional arguments:
    db                database to run queries on
    solutions         path to directory containing solutions, numbered 1.sql, 2.sql...
    helpers_template  path to directory containing template for helpers file

    options:
    -h, --help        show this help message and exit
    """

    # parse command line arguments
    parser = argparse.ArgumentParser(description='Generate check50 scripts for movies-like problems.')
    parser.add_argument('db', type=str,
                        help='database to run queries on')
    parser.add_argument('solutions', type=str,
                        help='path to directory containing solutions, numbered 1.sql, 2.sql...')
    parser.add_argument('helpers_template', type=str,
                        help='path to directory containing template for helpers file')
    args = parser.parse_args()

    # open command line arguments
    files = natsorted(os.listdir(args.solutions))
    file_num = len(files)
    db = SQL(f"sqlite:///{args.db}")

    # slightly specialized version of run_query for our uses
    def run_query(filename):
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
            ordered = "ORDER BY" in query.upper()
        result = db.execute(query)
        return result, ordered

    # write to __init__.py
    with open('__init__.py', 'w') as f:

        # top of file; exists check
        header = dedent(f'''\
        from cs50 import SQL

        import check50
        import sqlparse


        @check50.check()
        def exists():
            """SQL files exist"""
            for i in range({file_num}):
                check50.exists(f"{{i + 1}}.sql")
            check50.include("{args.db}")


        ''')

        f.write(header)

        # write test function for each .sql subproblem
        for i, file in enumerate(files):

            # run query; confirm result returned
            actual, ordered = run_query(os.path.join(args.solutions, file))
            if actual is None or actual == []:
                raise Exception("Query did not return result")

            test = f'''\
            @check50.check(exists)
            def test{i + 1}():
                """{i + 1}.sql produces correct result"""
            '''
            test = dedent(test)

            # if single cell, single string
            if len(actual) == 1 and len(list(actual[0].values())) == 1:
                result = str(list(actual[0].values())[0])
                test_string = f'''\
                check_single_cell(run_query("{i + 1}.sql"), '{result}')


                '''
                test += indent(dedent(test_string), '    ')

            # if single column, list of strings
            elif max([len(list(row_dict.values())) for row_dict in actual]) == 1:
                result = [str(list(row_dict.values())[0]) for row_dict in actual]
                test_string = f'''\
                check_single_col(
                    run_query("{i + 1}.sql"),
                    {indent(pformat(result), '    ' * 5, lambda line: line[0] != '[')},
                    ordered={ordered},
                )


                '''
                test += indent(dedent(test_string), '    ')

            # if multi column, list of sets of strings
            else:
                result = [{str(elt) for elt in list(row_dict.values())} for row_dict in actual]
                test_string = f'''\
                check_multi_col(
                    run_query("{i + 1}.sql"),
                    {indent(pformat(result), '    ' * 5, lambda line: line[0] != '[')},
                    ordered={ordered},
                )


                '''
                test += indent(dedent(test_string), '    ')

            f.write(test)

        # print helpers at end of check50 file;
        # replace DATABASE substring with provided database in command line args
        with open(args.helpers_template, 'r') as f2:
            helpers = f2.read()
        helpers = helpers.replace("DATABASE", args.db)
        f.write(dedent(helpers))

    # write .cs50.yml config
    with open('.cs50.yml', 'w') as f:
        header = '''\
        check50:
          files: &check50_files
            - !exclude "*"
            - !include "*.sql"
            '''
        f.write(dedent(header))
 
        for i, file in enumerate(files):
            f.write(f'    - !require "{i + 1}.sql"\n')

        footer = '''\

        submit50:
          files: *check50_files
          style: false
        '''
        f.write(dedent(footer))


if __name__ == '__main__':
    main()
