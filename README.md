# df_to_excel
A utility for appending DataFrames to Single Excel file in different sheets.

## Installation

Install the package using pip:


pip install df-to-excel-appender


from df_to_excel_appender.df_to_excel import append_df_to_excel

Import the append_df_to_excel function:


from df_to_excel_appender.df_to_excel import append_df_to_excel
# Use the function to append a DataFrame to an Excel file:
# Example usage
output_file = 'output.xlsx'
your_dataframe = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
append_df_to_excel(output_file, your_dataframe, sheet_name='Sheet1', index=False)

Run the script from the command line:

df_to_excel_appender input.csv -o output.xlsx
Command Line Options
-i, --input: Input CSV file.
-o, --output: Output Excel file.

Dependencies
pandas
openpyxl

Contributing

If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet

Make sure to replace placeholders such as `yourusername` with your actual GitHub username and customize the content based on your project's features and functionalities.

Include sections that are relevant to your project, such as installation instructions, usage examples, command-line options, dependencies, contributing guidelines, and licensing information. A well-documented README helps users and potential contributors understand and use your project effectively.
