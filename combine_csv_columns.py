import pandas as pd

#Make sure to have pandas installed before running this code. You can install it using pip install pandas.
#This function reads the two input CSV files, extracts the first column from A.csv, adds it as a new column to B.csv, and then saves the modified DataFrame as c.csv.

def combine_csv_columns(A_file, B_file, output_file='c.csv'):
    # Read the CSV files into pandas DataFrames
    df_a = pd.read_csv(A_file)
    df_b = pd.read_csv(B_file)

    # Extract the first column of A.csv
    column_a = df_a.iloc[:, 0]

    # Add the column from A.csv to B.csv
    df_b['New_Column'] = column_a

    # Save the result to c.csv
    df_b.to_csv(output_file, index=False)

# Example usage:
combine_csv_columns('A.csv', 'B.csv', 'c.csv')
