import pandas as pd
import csv

warehouse_df = None
emails_df = None

def read_csv_files():
    global warehouse_df, emails_df
    try:
        warehouse_df = pd.read_csv(r"C:\\Users\\rvent\\Desktop\\code\\works\\email_processing\\data\\warehouse.csv", encoding='utf-8')
        print("Successfully loaded warehouse data into DataFrame")
        
        emails_df = pd.read_csv(r"C:\\Users\\rvent\\Desktop\\code\\works\\email_processing\\data\\emails.csv")
        print("Successfully loaded email data into DataFrame")
        
        return warehouse_df, emails_df
    
    except FileNotFoundError as e:
        print(f"Error: Could not find CSV file - {e}")
        return None, None
    except Exception as e:
        print(f"Error occurred while reading CSV files: {e}")
        return None, None

warehouse_df, emails_df = read_csv_files()

def reload_dataframes():
    global warehouse_df, emails_df
    warehouse_df, emails_df = read_csv_files()
