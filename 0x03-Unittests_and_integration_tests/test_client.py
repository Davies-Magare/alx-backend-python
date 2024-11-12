#!/usr/bin/env python3
"""
This module demonstrates how to
test python code with dependencies
using parameterized and Mocks
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict
from client import GithubOrgClient as GitCli

GitClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ('google', {"git": "myorg"}),
        ('abc', {"git": "myorg"})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, result: Dict, mock_request: Mock) -> None:
        """Test the org method"""

        ORG_URL = "https://api.github.com/orgs/{}"
        mock_request.return_value = result
        instance = GitClient(org)
        self.assertEqual(instance.org, result)
        mock_request.assert_called_once_with(ORG_URL.format(org))

    def test_public_repos_url(self):
        """Test public_repos method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock)as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/repos"}
            instance = GitClient('google')
            self.assertEqual(
                instance._public_repos_url,
                "https://api.github.com/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_request):
        """Test public_repos method"""
        with patch('client.GithubOrgClient._public_repos_url')as mock_url:
            mock_request.return_value = [
                {"name": "dart"}, {"name": "cpp-netlib"}]
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            instance = GitClient("google")
            self.assertEqual(instance.public_repos(), ["dart", "cpp-netlib"])
            mock_request.assert_called_once()
            # mock_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
