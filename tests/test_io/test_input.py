import unittest
import os
from app.io.input import read_from_file_builtin, read_from_file_pandas
import pandas as pd


class TestReadFromFileBuiltin(unittest.TestCase):
    def test_file_existence(self):
        filename = 'temp_test_file.txt'
        with open(filename, 'w') as f:
            f.write('Test data')
        content = read_from_file_builtin(filename)
        self.assertIsNotNone(content)
        os.remove(filename)

    def test_file_content(self):
        filename = 'temp_test_file.txt'
        expected_content = "This is a test file.\nIt contains some text."
        with open(filename, 'w') as f:
            f.write(expected_content)
        content = read_from_file_builtin(filename)
        self.assertEqual(content, expected_content)
        os.remove(filename)

    def test_empty_file(self):
        filename = 'temp_test_file.txt'
        expected_content = ""
        with open(filename, 'w') as f:
            f.write(expected_content)
        content = read_from_file_builtin(filename)
        self.assertEqual(content, expected_content)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
