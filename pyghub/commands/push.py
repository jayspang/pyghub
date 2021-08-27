"""
CLI command for pushing to a remote repo.
"""
import argparse
from pyghub.providers.git import Git # pylint: disable=import-error


def execute_command(args: argparse.Namespace) -> int:
    """
    Executes the command described in this file.

    This particular command pushes to a remote repo

    Args:
        args (as in, the arguments from this command's subparser)

    Returns:
        return code (0 for success, 1 for failure)
    """
    g = Git()
    g.push(args.repo_path, args.remote, args.branch)
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
        "push", help="Pull from a remote repository"
    )

    parser.add_argument(
        "-r", "--repo-path", help="Path to local git repository."
    )

    parser.add_argument(
        "-m", "--remote", help="Remote name to push to."
    )

    parser.add_argument(
        "-b", "--branch", help="Branch name to push to."
    )

    parser.set_defaults(func=execute_command)
