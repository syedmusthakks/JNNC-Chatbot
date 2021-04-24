# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:17:02 2021

@author: Musthak
"""
import os
import json
import xlrd

class chatbot_data:
    
    def __init__(self):
        self.script_path = os.path.abspath(os.path.dirname(__file__))
        self.cell_col_idx_dict = {"question": 0,
                             "unique_key": 1,
                             "answer": 3
                             }
        
        self.chatbot_excel_path = "%s/Database/chat_training_data.xlsx" %(self.script_path)
        self.chatbot_json_path = "%s/Database/chat_training_data.json" %(self.script_path)
        self.chatbot_trained_dict = {}
 
    def read_excel(self):
        # To open Workbook
        wb = xlrd.open_workbook(self.chatbot_excel_path)
        sheet = wb.sheet_by_index(0)
         
        for row_idx in range(1, sheet.nrows):
            if sheet.cell_value(row_idx, 0) == "":
                break
            question = sheet.cell_value(row_idx, 0).lower()
            self.chatbot_trained_dict[question] = {}
            self.chatbot_trained_dict[question]["unique_key"] = sheet.cell_value(row_idx, 1)
            self.chatbot_trained_dict[question]["answer"] = sheet.cell_value(row_idx, 3)
            
        self.json_dump()
        return self.chatbot_trained_dict
            
    def json_dump(self):
        with open(self.chatbot_json_path, "w") as fp:
            json.dump(self.chatbot_trained_dict, fp, indent=4, sort_keys=True)
        


if __name__ == "__main__":
    obj = chatbot_data()
    obj.read_excel()