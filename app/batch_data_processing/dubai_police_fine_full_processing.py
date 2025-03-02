import pandas as pd
import os

class DubaiFineFullProcessing:
    def __init__(self, sheet_path_name):
        # Initialize the class with the path to the Excel sheet
        self.data_path      = sheet_path_name
        self.excel_file     = pd.ExcelFile()
        self.loaded_data    = pd.DataFrame()
        self.sheet_name     = str
        self.df_error       = pd.DataFrame()
        self.__sheet        = 'fine'

        # Check if the provided path exists
        if not os.path.exists(self.data_path):
            assert False, f'Path: {self.data_path} does not exist'
        else:
            # Load the Excel file
            self.excel_file = pd.ExcelFile(self.data_path)
            print("Excel file exists,\nExcel sheets name: ", self.excel_file.sheet_names)

        # Get the sheet name that contains 'salik'
        self.__get_sheet_name(self.excel_file)

    def __get_sheet_name(self, excel_file):
        # Identify the sheet name that contains 'salik'
        salik_sheets = [sheet for sheet in excel_file.sheet_names if self.__sheet in sheet.lower()]
        print("Sheets name:",salik_sheets[0])
        self.sheet_name = salik_sheets[0]

    def check_na(self):
        # Check for missing values in the loaded data
        self.df_error = self.loaded_data[self.loaded_data.isna().any(axis=1)]
        print("Number of entries with missing values: ", self.df_error.shape[0])
        return self.df_error.index.values + 3

    def return_error_rows(self):
        # Return rows with errors if any
        if len(self.df_error) > 0:
            return self.df_error
        
if __name__ == "__main__":
    # Path to the Excel sheet
    sheet_path_name = 'data/Dec Data.xlsx'
    
    # Create an instance of the SalikFinesFullProcessing class
    salik_fines = DubaiFineFullProcessing (sheet_path_name=sheet_path_name)
    
    # Check for missing values
    salik_fines.check_na()
    
    # Print rows with errors
    print(salik_fines.return_error_rows())
