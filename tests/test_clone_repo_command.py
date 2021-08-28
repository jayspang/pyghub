"""
Unit tests for commands/clone_repo.py
"""
import argparse
import mock
import json
import os
import pytest
import unittest

import pyghub.commands.clone_repo

class TestGetRepoCommand(unittest.TestCase):
    """
    Tests for pyghub.commands.clone_repo command
    """
    def setup(self):
        pass

    def test_register_subparser(self):
        subparser = mock.Mock()
        subparser.add_parser.return_value = subparser

        pyghub.commands.clone_repo.register_subparser(subparser)

        subparser.add_parser.assert_called_once_with("clone_repo", help=mock.ANY)
        subparser.add_argument.assert_any_call("-r", "--repo-url", help=mock.ANY)
        subparser.add_argument.assert_any_call("-p", "--path", help=mock.ANY)

        subparser.set_defaults.assert_called_once_with(func=pyghub.commands.clone_repo.execute_command)

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.clone_from")
    def test_execute_command_with_valid_args_succeeds(self, mock_clone, mock_path_exists):
        mock_clone.Repo.clone_from.return_value = 0
        mock_path_exists.return_value = False

        input_args = argparse.Namespace()
        input_args.repo_url = "https://fake_repo"
        input_args.path = "c:\\Windows\\System32"

        result = pyghub.commands.clone_repo.execute_command(input_args)
        self.assertEqual(result, 0)
