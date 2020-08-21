import json
import unittest
from unittest.mock import Mock, patch
from src.clients.quickfs import QuickFS


class TestQuickFS(unittest.TestCase):

    def setUp(self):
        pass

    @patch('src.clients.quickfs.requests.get')
    def test_get_fundamentals(self, mock_get):
        mock_response = {"data": [29321000000, 37905000000, 46039000000, 55519000000, 66001000000, 74989000000, 90272000000, 110855000000, 136819000000, 161857000000]}
        mock_get.return_value.ok = True
        mock_get.return_value.content = json.dumps(mock_response)

        collected_data = QuickFS().get("WHATEVER")
        print(collected_data.fundamentals)


if __name__=="__main__":
    unittest.main()
