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
    parser = argparse.ArgumentParser(
        description="Generate check50 scripts for movies-like problems."
    )
    parser.add_argument("db", type=str, help="database to run queries on")
    parser.add_argument(
        "solutions",
        type=str,
        help="path to directory containing solutions, numbered 1.sql, 2.sql...",
    )
    parser.add_argument(
        "helpers_template",
        type=str,
        help="file containing helpers",
    )
    args = parser.parse_args()

    # open command line arguments
    relative_db_path = args.db
    relative_solution_path = args.solutions
    helpers_template = args.helpers_template
    files = os.listdir(relative_solution_path)

    # write .cs50.yml config
    write_check_config(files)
    write_check_file(files, relative_db_path, relative_solution_path, helpers_template)


def write_check_config(required_files: list[str]) -> None:
    """
    Create a .cs50.yml file that requires the given list of files

    Args:
        files (list[str]): a list of files to require as part of the check

    Returns:
        None
    """
    HEADER = """\
    check50:
      files: &check50_files
      - !exclude "*"
      - !include "*.sql"
    """
    FOOTER = """\
    
    submit50:
      files: *check50_files
      style: false
    """

    with open(".cs50.yml", "w") as f:
        f.write(dedent(HEADER))
        for i, file in enumerate(required_files):
            f.write(f'    - !require "{i + 1}".sql\n')
        f.write(dedent(FOOTER))


def write_check_file(
    solution_files: list[str],
    db_path: str,
    solution_directory: str,
    path_to_helpers_template: str,
) -> None:
    DEPENDENCIES = """\
        from cs50 import SQL
                        
        import check50
        import sqlparse

        
        """

    db_filename = db_path.split("/")[-1]
    exists_check = construct_exists_check(solution_files, db_filename)

    with open("__init__.py", "w") as check_file:
        check_file.write(dedent(DEPENDENCIES))
        check_file.write(dedent(exists_check))

        db = SQL(f"sqlite:///{db_path}")
        for i, file in enumerate(natsorted(solution_files)):
            check_file.write(
                dedent(construct_check(i + 1, file, db, solution_directory))
            )

        with open(path_to_helpers_template, "r") as helpers_file:
            helpers = helpers_file.read()
        helpers = helpers.replace("DATABASE", db_filename)
        check_file.write(dedent(helpers))


def construct_exists_check(
    files_to_check_if_exists: list[str], db_filename: str
) -> str:
    last_filename = natsorted(files_to_check_if_exists)[-1]
    last_file_number = last_filename[0:-4]
    exists_check = f'''\
        @check50.check()
        def exists():
            """SQL files exist"""
            for i in range({last_file_number}):
                check50.exists(f"{{i + 1}}.sql")
            check50.include("{db_filename}")
        '''
    return exists_check + "\n\n"


def construct_check(
    check_number: int, check_file: str, db, solution_directory: str
) -> str:
    INDENT_AMOUNT = 4

    def run_query(filename):
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
            ordered = "ORDER BY" in query.upper()
        result = db.execute(query)
        return result, ordered

    actual, ordered = run_query(os.path.join(solution_directory, check_file))
    if actual is None or actual == []:
        raise Exception("Query did not return result")

    check = dedent(
        f'''\
        @check50.check(exists)
        def test{check_number}():
            """{check_file} produces correct result"""
        '''
    )

    # if single cell, single string
    if len(actual) == 1 and len(list(actual[0].values())) == 1:
        result = str(list(actual[0].values())[0])
        function_call = dedent(
            f"""\
            check_single_cell(run_query("{check_file}"), '{result}')
            """
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    # if single column, list of strings
    elif max([len(list(row_dict.values())) for row_dict in actual]) == 1:
        result = [str(list(row_dict.values())[0]) for row_dict in actual]
        function_call = dedent(
            f"""\
            check_single_col(
                run_query("{check_file}"),
                {indent(pformat(result), '    ' * 4, lambda line: line[0] != '[')},
                ordered={ordered},
            )
            """
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    # if multi column, list of sets of strings
    else:
        result = [{str(elt) for elt in list(row_dict.values())} for row_dict in actual]
        function_call = dedent(
            f"""\
            check_multi_col(
                run_query("{check_file}"),
                {indent(pformat(result), '    ' * 4, lambda line: line[0] != '[')},
                ordered={ordered},
            )
            """
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    return check + "\n\n"


if __name__ == "__main__":
    main()
