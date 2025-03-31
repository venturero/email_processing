import pandas as pd
from src.order_extractor import extract_order_details
from src.availability_checker import check_product_availability, get_priority
from src.narrative_generator import generate_availability_narrative
from utils.config import EMAILS_PATH, WAREHOUSE_PATH
import read

def create_orders_dataframe(emails_path):
    orders = []
    
    for index, row in read.emails_df.iterrows():
        order_details = extract_order_details(row['Email'])
        
        order_entry = {
            'orderid': index + 1,
            'product': order_details['product'],
            'quantity': order_details['quantity']
        }
        
        orders.append(order_entry)
    
    return pd.DataFrame(orders)

def main():
    orders_df = create_orders_dataframe(EMAILS_PATH)
    availability_df = check_product_availability(orders_df, read.warehouse_df)
    
    availability_df['sort_priority'] = availability_df.apply(get_priority, axis=1)
    sorted_availability_df = availability_df.sort_values(
        by=['sort_priority', 'ordered_quantity'], 
        ascending=[True, True]
    )

    availability_narratives = generate_availability_narrative(sorted_availability_df)

    print("\nAvailability Narratives:")
    for narrative in availability_narratives:
        print(narrative)
        print()   

if __name__ == "__main__":
    main()
