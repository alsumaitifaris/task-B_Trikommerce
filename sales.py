import random
def daily_sales(available_items, inventory_records, current_day):
    """
    Updates the sales for a given day.
    
    Args:
        available_items (int): Available T-shirts from the previous day
        inventory_records (list): List of inventory records until previous day
        current_day (int): Current day number
        
    Returns:
        int: Updated number of available items
    """
    # Get the current day's record (created by restock_inventory)
    current_record = inventory_records.pop()
    day, _, restocked_units, _ = current_record
    
    # No sales on restocking days
    if current_day % 7 == 0:
        sold_units = 0
    else:
	# Generate random sales for non-restocking days
	max_possible_sales = min(200, available_items)  # Ensure sales do not exceed 200 or available inventory
	sold_units = random.randint(0, max_possible_sales)  # Generate a valid random sales number
	available_items -= sold_units  # Update available items

    
    # Add updated record with sales information
    inventory_records.append((day, sold_units, restocked_units, available_items))
    
    return available_items