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


class TestReadFromFilePandas(unittest.TestCase):
    def test_file_existence(self):
        filename = "test_file.csv"
        data = {"Name": [], "Age": [], "City": []}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

        df = read_from_file_pandas(filename)
        self.assertIsInstance(df, pd.DataFrame)
        os.remove(filename)

    def test_correct_columns(self):
        filename = "test_file.csv"
        data = {"Name": [], "Age": [], "City": []}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

        df = read_from_file_pandas(filename)
        expected_columns = ["Name", "Age", "City"]
        self.assertListEqual(list(df.columns), expected_columns)
        os.remove(filename)

    def test_empty_file(self):
        filename = "test_file.csv"
        data = {"Name": [], "Age": [], "City": []}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

        df = read_from_file_pandas(filename)
        self.assertTrue(df.empty)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
