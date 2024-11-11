#!/usr/bin/env python3
"""
This module demonstrates how to
test python code with dependencies
using parameterized and Mocks
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient  # Assuming this is the path

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ('google', {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ('abc', {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')  # Patch `get_json` in the `client` module
    def test_org(self, org, result, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Set the return value for `get_json` mock
        mock_get_json.return_value = result

        # Create an instance of GithubOrgClient
        instance = GithubOrgClient(org)

        # Call the `org` method (this will call `get_json` internally)
        org_data = instance.org

        # Check if `get_json` was called with the correct URL
        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)

        # Check that the result from `org` matches the mock return value
        self.assertEqual(org_data, result)


if __name__ == '__main__':
    unittest.main()

