#!/usr/bin/env python3

"""
This module demonstrates how to test
python code with parameterized unit
tests.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, error):
        self.assertRaises(
            error,
            access_nested_map,
            nested_map=nested_map,
            path=path)


class TestGetJson(unittest.TestCase):
    """Test the get_json function in utils"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, ret_dict, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = ret_dict
        mock_request.return_value = mock_response
        response = get_json(url)
        mock_request.assert_called_once_with(url)
        self.assertEqual(get_json(url), ret_dict)


if __name__ == '__main__':
    unittest.main()
