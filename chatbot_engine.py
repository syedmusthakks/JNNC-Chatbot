# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:45:05 2021

@author: Musthak
"""

from chatbot_data import chatbot_data

chatbot_data_obj = chatbot_data()

class chatbot_engine:
    
    def __init__(self):
        self.trained_data_dict = chatbot_data_obj.read_excel()
    
    def get_response(self, query):
        query = query.lower()
        
        if query in self.trained_data_dict:
            return self.trained_data_dict [query]["answer"]
        
        for questions, data_dict in self.trained_data_dict.items():
            if query in questions:
                return data_dict["answer"]
            elif questions in query:
                return data_dict["answer"]
            
        return self.trained_data_dict["default_1"]["answer"]
        
    
if __name__ == "__main__":
    obj = chatbot_engine()
    obj.get_response("hi")
    
    