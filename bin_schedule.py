from datetime import datetime, timedelta

# Calendar data for 2025 based on the image
# True = Red week, False = Blue week
COLLECTION_SCHEDULE_2025 = {
    1: [True, True, True, True, True],  # January weeks
    2: [True, True, False, False],      # February weeks
    3: [False, False, False, False],    # March weeks
    4: [True, True, True, True],        # April weeks
    5: [True, True, False, False, True], # May weeks
    6: [True, True, False, False],      # June weeks
    7: [False, False, False, False],    # July weeks
    8: [False, False, False, False, True], # August weeks
    9: [True, True, False, False],      # September weeks
    10: [False, False, False, False],   # October weeks
    11: [False, False, False, False],   # November weeks
    12: [True, True, True, True, True]  # December weeks
}

def get_week_number(date):
    """Get the week number within the month (0-based)"""
    return (date.day - 1) // 7

def is_red_bin_week(date):
    """Determine if it's a red bin week for the given date"""
    month = date.month
    week = get_week_number(date)
    
    try:
        return COLLECTION_SCHEDULE_2025[month][week]
    except (KeyError, IndexError):
        return None

def get_bin_color(date):
    """Returns the bin color for the given date"""
    is_red = is_red_bin_week(date)
    if is_red is None:
        return "Unknown"
    return "Red" if is_red else "Blue"

def get_next_collection_date(current_date):
    """Calculate the next collection date"""
    next_date = current_date + timedelta(days=7)
    while next_date.year == 2025:
        if is_red_bin_week(next_date) is not None:
            return next_date
        next_date += timedelta(days=7)
    return None
