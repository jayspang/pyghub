"""
Unit tests for commands/pull.py
"""
import argparse
import mock
import json
import os
import pytest
import unittest

import pyghub.commands.pull

class TestGetRepoCommand(unittest.TestCase):
    """
    Tests for pyghub.commands.pull command
    """
    def setup(self):
        pass

    def test_register_subparser(self):
        subparser = mock.Mock()
        subparser.add_parser.return_value = subparser

        pyghub.commands.pull.register_subparser(subparser)

        subparser.add_parser.assert_called_once_with("pull", help=mock.ANY)
        subparser.add_argument.assert_any_call("-r", "--repo-path", help=mock.ANY)
        subparser.add_argument.assert_any_call("-m", "--remote", help=mock.ANY)
        subparser.add_argument.assert_any_call("-b", "--branch", help=mock.ANY)

        subparser.set_defaults.assert_called_once_with(func=pyghub.commands.pull.execute_command)

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_execute_command_with_valid_args_succeeds(self, mock_init, mock_path_exists):
        mock_init.Repo.init.return_value = 0
        mock_path_exists.return_value = True

        input_args = argparse.Namespace()
        input_args.repo_path = "c:\\Windows\\System32"
        input_args.remote = "some_remote"
        input_args.branch = "my_branch"

        result = pyghub.commands.pull.execute_command(input_args)
        self.assertEqual(result, 0)
        mock_init.assert_called_once_with(input_args.repo_path)
