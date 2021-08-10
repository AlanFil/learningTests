import json
import unittest


class TestIntegrationBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        with open('tests/integration/fixtures/test_basic.json', 'r') as f:
            self.data = json.load(f)

    def test_name(self):
        self.assertEqual(self.data['name'], 'Alan')

    def test_hobbies_count(self):
        self.assertEqual(len(self.data['hobbies']), 3)


if __name__ == '__main__':
    unittest.main()
