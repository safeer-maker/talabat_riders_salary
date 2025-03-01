import pandas as pd
import os
from datetime import datetime

class SalikFinesFullProcessing:
    def __init__(self, sheet_path_name):
        self.data_path = sheet_path_name
        self.excel_file = ""
        self.loaded_data = pd.DataFrame()
        self.output_path = 'data/salik_fines_processed'
        self.output_file = 'salik_fines_full_processed.csv'
        self.output_columns = ['plate', 'fine_date', 'fine_amount', 'fine_location', 'fine_status', 'fine_description']
        self.sheet_name = ''
        self.__sheet = 'salik'

        if not os.path.exists(self.data_path):
            assert False, f'Path: {self.data_path} does not exist'
        else:
            self.excel_file = pd.ExcelFile(self.data_path)
            print("Excel file exist,\nExcel sheets name: ",self.excel_file.sheet_names)
        
        self.__get_sheet_name(self.excel_file)

        self.loaded_data = self.excel_file.parse(self.sheet_name)

        print("Loaded data: ", self.loaded_data.head())


    def __get_sheet_name (self,  excel_file):
        salik_sheets = [sheet for sheet in excel_file.sheet_names if self.__sheet in sheet.lower()]
        print(salik_sheets)
        self.sheet_name = salik_sheets[0]

if __name__ == '__main__':
    sheet_path_name = 'data/Dec Data.xlsx'
    salik_fines = SalikFinesFullProcessing(
             sheet_path_name=sheet_path_name
             )
    

