#!/usr/bin/env python3
"""
This module demonstrates how to
test python code with dependencies
using parameterized and Mocks
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize
GitClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ('google', {"git": "myorg"}),
        ('abc', {"git": "myorg"})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, result, mock_request):
        """Test the org method"""

        ORG_URL = "https://api.github.com/orgs/{}"
        mock_request.return_value = result
        instance = GitClient(org)
        self.assertEqual(instance.org, result)
        mock_request.assert_called_once_with(ORG_URL.format(org))


if __name__ == '__main__':
    unittest.main()
