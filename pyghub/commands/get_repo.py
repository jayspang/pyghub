"""
CLI command for getting repository information.
"""
import argparse
import json
from pyghub.github import Github # pylint: disable=import-error


def execute_command(args: argparse.Namespace) -> int:
    """
    Executes the command described in this file.

    This particular command hits Github's /repo URL to retrieve
    repo information. It's then pretty-printed to the terminal.

    Args:
        args (as in, the arguments from this command's subparser)

    Returns:
        return code (0 for success, 1 for failure)
    """
    gh = Github(args.api_token)
    parsed = json.loads(gh.get_repo(args.owner, args.repo))
    print(json.dumps(parsed, indent=4, sort_keys=True))
    return 0


def register_subparser(subparser) -> None:
    """
    Registers this command's parser with argparse

    Args:
        subparser object

    Returns:
        None
    """
    parser = subparser.add_parser(
        "get_repo", help="Get repository information"
    )

    parser.add_argument(
        "-o", "--owner", help="Ower of the repository."
    )

    parser.add_argument(
        "-r", "--repo", help="Repository name."
    )

    parser.set_defaults(func=execute_command)
