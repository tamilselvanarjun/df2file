import os
import pandas as pd
from openpyxl import load_workbook

def append_df_to_excel(filename, df, sheet_name='Sheet1', startrow=None,
                       truncate_sheet=False, **to_excel_kwargs):
    """
    Append a DataFrame to an existing Excel file or create a new one if the file doesn't exist.

    Parameters:
    - filename (str): Path to the Excel file.
    - df (DataFrame): DataFrame to be appended.
    - sheet_name (str): Name of the Excel sheet.
    - startrow (int): Starting row for appending the DataFrame.
    - truncate_sheet (bool): If True, truncate the sheet before appending.
    - to_excel_kwargs (dict): Additional arguments for DataFrame to_excel method.

    Returns:
    - None
    """
    # Ensure filename ends with '.xlsx'
    if not filename.endswith('.xlsx'):
        filename = filename + '.xlsx'

    
    if not os.path.isfile(filename):
        df.to_excel(filename, sheet_name=sheet_name, startrow=startrow if startrow is not None else 0, **to_excel_kwargs)
        return

    # Open existing workbook
    writer = pd.ExcelWriter(filename, engine='openpyxl', mode='a')
    writer.book = load_workbook(filename)

    # Get the last row in the sheet or set startrow if not specified
    if startrow is None and sheet_name in writer.book.sheetnames:
        startrow = writer.book[sheet_name].max_row

    # Truncate sheet if specified
    if truncate_sheet and sheet_name in writer.book.sheetnames:
        idx = writer.book.sheetnames.index(sheet_name)
        writer.book.remove(writer.book.worksheets[idx])
        writer.book.create_sheet(sheet_name, idx)

    # Copy existing sheets
    writer.sheets = {ws.title: ws for ws in writer.book.worksheets}

    # Write DataFrame to Excel
    df.to_excel(writer, sheet_name, startrow=startrow, **to_excel_kwargs)

    # Save the workbook
    writer.save()


def append_df_to_csv(filename, df, header=True, index=False, **to_csv_kwargs):
    """
    Append a DataFrame to an existing CSV file or create a new one if the file doesn't exist.

    Parameters:
    - filename (str): Path to the CSV file.
    - df (DataFrame): DataFrame to be appended.
    - header (bool): Whether to write header row.
    - index (bool): Whether to write index.

    Returns:
    - None
    """
    # Ensure filename ends with '.csv'
    if not filename.endswith('.csv'):
        filename = filename + '.csv'

    # Append DataFrame to CSV file
    df.to_csv(filename, mode='a', header=header, index=index, **to_csv_kwargs)


# Example usage:
# output_csv = 'output.csv'
# df = pd.DataFrame({'Column1': [4, 5, 6], 'Column2': ['D', 'E', 'F']})
# append_df_to_csv(output_csv, df, header=False, index=False)
