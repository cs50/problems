from cs50 import SQL

import argparse
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
        help="path to directory containing solutions, named for the view they create",
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
    files = [file for file in os.listdir(relative_solution_path) if file.endswith(".sql")]

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
        for filename in natsorted(required_files):
            f.write(f'  - !require "{filename}"\n')
        f.write(dedent(FOOTER))


def write_check_file(
    solution_files: list[str],
    db_path: str,
    solution_directory: str,
    path_to_helpers_template: str,
) -> None:
    DEPENDENCIES = """\
        from cs50 import SQL
        from pathlib import Path

        import check50
        import re

        
        """

    db_filename = db_path.split("/")[-1]
    exists_check = construct_exists_check(solution_files, db_filename)

    with open("__init__.py", "w") as check_file:
        check_file.write(dedent(DEPENDENCIES))
        check_file.write(dedent(exists_check))

        for i, file in enumerate(natsorted(solution_files)):
            check_file.write(
                dedent(construct_check(i + 1, file, db_path))
            )

        with open(path_to_helpers_template, "r") as helpers_file:
            helpers = helpers_file.read()
        helpers = helpers.replace("DATABASE", db_filename)
        check_file.write(dedent(helpers))


def construct_exists_check(
    files_to_check_if_exists: list[str], db_filename: str
) -> str:
    exists_check = f'''\
        @check50.check()
        def exists():
            """SQL files exist"""
            for filename in {indent(pformat(files_to_check_if_exists), '    ' * 7, lambda line: line[0] != '[')}:
                check50.exists(filename)
            check50.include("{db_filename}")
        '''
    return exists_check + "\n\n"


def construct_check(
    check_number: int, view_file: str, db_path: str
) -> str:
    INDENT_AMOUNT = 4

    check = dedent(
        f'''\
        @check50.check(exists)
        def test{check_number}():
            """{view_file} produces correct view"""
        '''
    )

    query = dedent(
        f'''\
        SELECT *
        FROM "{view_file[0:-4]}";
        '''
    )

    db = SQL(f"sqlite:///{db_path}")
    db_filename = db_path.split("/")[-1]
    view_contents = db.execute(query)

    # if single cell, single string
    if len(view_contents) == 1 and len(list(view_contents[0].values())) == 1:
        view_contents = str(list(view_contents[0].values())[0])
        function_call = dedent(
            f'''\
            test_view(SQL("sqlite:///{db_filename}"), Path("{view_file}"), {view_contents})
            '''
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    # if single column, list of strings
    elif max([len(list(row_dict.values())) for row_dict in view_contents]) == 1:
        view_contents = [str(list(row_dict.values())[0]) for row_dict in view_contents]
        function_call = dedent(
            f"""\
            test_view(SQL("sqlite:///{db_filename}"), 
                      Path("{view_file}"), 
                      {indent(pformat(view_contents), '    ' * 4, lambda line: line[0] != '[')})
            """
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    # if multi column, list of sets of strings
    else:
        view_contents = [{str(elt) for elt in list(row_dict.values())} for row_dict in view_contents]
        function_call = dedent(
            f"""\
            test_view(SQL("sqlite:///{db_filename}"), 
                      Path("{view_file}"), 
                      {indent(pformat(view_contents), '    ' * 4, lambda line: line[0] != '[')})
            """
        )
        check += indent(function_call, INDENT_AMOUNT * " ")

    return check + "\n\n"


if __name__ == "__main__":
    main()
