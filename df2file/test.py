import unittest
import pandas as pd
import os

from your_module_name import append_df_to_excel, append_df_to_csv

class TestAppendToExcelAndCsv(unittest.TestCase):
    """
    Test cases for append_df_to_excel and append_df_to_csv functions.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        # Create a sample DataFrame
        self.data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        self.df = pd.DataFrame(self.data)

    def test_append_to_excel_existing_file(self):
        """
        Test appending DataFrame to an existing Excel file.
        """
        # Define the existing Excel file
        excel_file = 'test_excel_file.xlsx'

        # Append DataFrame to Excel
        append_df_to_excel(excel_file, self.df, sheet_name='Sheet1')

        
        self.assertTrue(os.path.isfile(excel_file))

        # Check if the sheet 'Sheet1' exists in the Excel file
        with pd.ExcelFile(excel_file) as xls:
            self.assertIn('Sheet1', xls.sheet_names)

    def test_append_to_csv_existing_file(self):
        """
        Test appending DataFrame to an existing CSV file.
        """
        # Define the existing CSV file.
        csv_file = 'test_csv_file.csv'

        # Append DataFrame to CSV.
        append_df_to_csv(csv_file, self.df, header=False)

        # Check if the CSV file exists.
        self.assertTrue(os.path.isfile(csv_file))

        # Check if the CSV file contains the expected data
        df_read = pd.read_csv(csv_file, header=None)
        expected_data = [[1, 2, 3], [4, 5, 6]]
        self.assertTrue(df_read.equals(pd.DataFrame(expected_data)))

    def tearDown(self):
        """
        Clean up test environment.
        """
        # Delete test files after each test
        if os.path.isfile('test_excel_file.xlsx'):
            os.remove('test_excel_file.xlsx')
        if os.path.isfile('test_csv_file.csv'):
            os.remove('test_csv_file.csv')

if __name__ == '__main__':
    unittest.main()
