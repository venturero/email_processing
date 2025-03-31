def generate_availability_narrative(availability_df):
    narratives = []
    for _, row in availability_df.iterrows():
        ordered_quantity = row['ordered_quantity']
        warehouse_quantity = row['warehouse_quantity']

        if warehouse_quantity >= ordered_quantity:
            narratives.append(
                f"Order {row['orderid']}: {ordered_quantity} piece of {row['product']} is fully available in warehouse. "
                f"Warehouse locking task is created for warehouse manager Deniz Alp. "
                f"Shipment task is assigned to logistic coordinator Ahmet Mehmet. "
                f"Factory work is completed. "
                f"Sales development representative Aksel has been informed about the order completion."
            )
        elif warehouse_quantity > 0 and warehouse_quantity < ordered_quantity:
            production_quantity = ordered_quantity - warehouse_quantity
            narratives.append(
                f"Order {row['orderid']}: {warehouse_quantity} piece of {row['product']} is available in the warehouse. "
                f"Warehouse locking task is created for warehouse manager Deniz Alp for {warehouse_quantity} available items. "
                f"Production task is created for production engineer Semi Venturero for {production_quantity} additional pieces. "
                f"Deadline for production is 15/4/2025. "
                f"Next task is warehouse locking for the newly produced items."
            )
        else:
            narratives.append(
                f"Order {row['orderid']}: {row['product']} is not available in warehouse. "
                f"Production task is created for production engineer Semi Venturero for {ordered_quantity} pieces. "
                f"Deadline is 15/4/2025. "
                f"Next task is warehouse locking after production."
            )

    return narratives
