### Project : df2file:
A Python utility designed for efficiently appending Pandas DataFrames to a single Excel file, each in a separate sheet.

#### Features:

- **Convenient Dataframe Appending:** Easily append Pandas DataFrames to an existing Excel file, with each DataFrame creating a new sheet within the workbook.

- **Sheet Customization:** Specify sheet names, starting row positions, and other options to customize the placement of each DataFrame within the Excel file.

- **Excel File Management:** If the specified Excel file does not exist, the utility will create it. If it does exist, the utility will append DataFrames to existing sheets or create new sheets as needed.


### Installation:
url = https://pypi.org/project/df-to-excel-appender/

#### Install the package using pip:

1.pip install df2file

2.from df2file.df_to_file import append_df_to_excel

3.from df2file.df_to_file import append_df_to_csv

#### Use the function to append a DataFrame to an Excel file:
#### Example usage:
output_file = 'output.xlsx'
your_dataframe = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
append_df_to_excel(output_file, your_dataframe, sheet_name='Sheet1', index=False)

#### Run the script from the command line:

df_to_excel_appender input.csv -o output.xlsx
 

#### Options:

-i, --input: Input CSV file.

-o, --output: Output Excel file.

#### Dependencies:
pandas

openpyxl

#### Contributing:

If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

#### License:
This project is licensed under the MIT License - see the LICENSE file for details.