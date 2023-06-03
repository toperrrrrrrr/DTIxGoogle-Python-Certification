import os
import pandas as pd

# Example usage
folder_path = r'C:\Users\lacsi\Documents\pythonconverter'



def csv_to_xls(csv_file, xls_file):
    df = pd.read_csv(csv_file)
    df.to_excel(xls_file, index=False)

def convert_folder_csv_to_xls(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            csv_file = os.path.join(folder_path, file_name)
            xls_file = os.path.join(folder_path, file_name[:-4] + '.xls')
            csv_to_xls(csv_file, xls_file)

convert_folder_csv_to_xls(folder_path)