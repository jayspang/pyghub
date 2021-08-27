"""
Exposes a command line interface for the Github module.
"""
import argparse
import sys
from typing import Callable, List
import pyghub.commands.get_repo
import pyghub.commands.commit
import pyghub.commands.clone_repo
import pyghub.commands.pull
import pyghub.commands.push



#  Collect our subparsers from each file in commands/
command_parser_map: List[Callable[[], None]] = [
    pyghub.commands.get_repo.register_subparser,
    pyghub.commands.clone_repo.register_subparser,
    pyghub.commands.commit.register_subparser,
    pyghub.commands.pull.register_subparser,
    pyghub.commands.push.register_subparser,
]

def main():
    #  First, collect global arguments (just the API token really)
    parser = argparse.ArgumentParser(description="Command Line Interface for working with Github's API.")
    parser.add_argument("--api-token", help="Github.com API token")

    #  Now, iterate our commands and add each one's subparser
    subparsers = parser.add_subparsers()
    for command_parser in command_parser_map:
        command_parser(subparsers)

    args = parser.parse_args()

    #  Execute the desired command and exit with its return code
    exit_code = args.func(args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
