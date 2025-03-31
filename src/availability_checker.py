import pandas as pd

def check_product_availability(orders_df, warehouse_df):
    orders_df['product'] = orders_df['product'].str.lower()
    warehouse_df['Product Name'] = warehouse_df['Product Name'].str.lower()

    availability_df = orders_df.merge(
        warehouse_df[['Product Name', 'Amount']], 
        left_on='product', 
        right_on='Product Name', 
        how='left', 
        suffixes=('_ordered', '')
    )

    availability_df['availability_status'] = availability_df.apply(
        lambda row: 'Available' if float(row['Amount']) >= float(row['quantity']) else 'Insufficient Stock',
        axis=1
    )

    return availability_df.rename(columns={
        'Product Name': 'warehouse_product',
        'quantity': 'ordered_quantity',
        'Amount': 'warehouse_quantity'
    })

def get_priority(row):
    if row['warehouse_quantity'] >= row['ordered_quantity']:
        return 1  
    elif row['warehouse_quantity'] > 0:
        return 2  
    else:
        return 3
