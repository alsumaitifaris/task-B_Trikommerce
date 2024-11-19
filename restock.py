def restock_inventory(available_items, inventory_records, current_day):
    """
    Updates the stock/restock for a given day.
    
    Args:
        available_items (int): Available T-shirts from the previous day
        inventory_records (list): List of inventory records until previous day
        current_day (int): Current day number
        
    Returns:
        int: Updated number of available items
    """
    restocked_units = 0
    
    # Check if it's a restocking day (day 0 or every 7 days)
    if current_day % 7 == 0:
        # For day 0, set initial stock to 2000
        if current_day == 0:
            restocked_units = 2000
            available_items = 2000
        else:
            # Calculate how many units needed to reach 2000
            units_needed = 2000 - available_items
            if units_needed > 0:
                restocked_units = units_needed
                available_items = 2000
        
        # Add record for restocking day
        inventory_records.append((current_day, 0, restocked_units, available_items))
    else:
        # Add record for non-restocking day
        inventory_records.append((current_day, 0, 0, available_items))
    
    return available_items