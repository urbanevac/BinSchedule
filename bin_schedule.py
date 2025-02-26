from datetime import datetime, timedelta
import ics
from ics import Calendar, Event

# Calendar data for 2025 based on the image
# True = Red week, False = Blue week
# Special days are marked with *
COLLECTION_SCHEDULE_2025 = {
    1: [True, True, True, True, True],  # January weeks
    2: [True, True, False, False, True],  # February weeks (added last week)
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

# Special collection days (marked with * in the calendar)
SPECIAL_COLLECTION_DAYS_2025 = {
    1: [2, 3, 4, 7, 8, 9, 10, 11],  # January special days
    12: [26, 27, 28, 29, 30, 31]     # December special days
}

def get_week_number(date):
    """Get the week number within the month (0-based)"""
    return (date.day - 1) // 7

def is_special_collection_day(date):
    """Check if the given date is a special collection day"""
    month = date.month
    day = date.day
    return month in SPECIAL_COLLECTION_DAYS_2025 and day in SPECIAL_COLLECTION_DAYS_2025[month]

def is_red_bin_week(date):
    """Determine if it's a red bin week for the given date"""
    month = date.month
    week = get_week_number(date)

    try:
        return COLLECTION_SCHEDULE_2025[month][week]
    except (KeyError, IndexError):
        # If we're beyond the last defined week of the month,
        # use the first week of the next month
        if week >= len(COLLECTION_SCHEDULE_2025[month]):
            next_month = month + 1 if month < 12 else 1
            return COLLECTION_SCHEDULE_2025[next_month][0]
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

def generate_calendar_file(start_date):
    """Generate an ICS calendar file for the next month of collections"""
    cal = Calendar()

    current_date = start_date
    end_date = start_date + timedelta(days=30)  # Next 30 days

    while current_date <= end_date:
        if is_red_bin_week(current_date) is not None:
            event = Event()
            bin_color = get_bin_color(current_date)
            is_special = is_special_collection_day(current_date)

            event.name = f"{bin_color} Bin Collection"
            if is_special:
                event.name += " (Special Collection Day)"

            event.begin = current_date.strftime("%Y-%m-%d 07:00:00")
            event.duration = timedelta(hours=1)
            event.description = (
                f"Put out your {bin_color.lower()} bin for collection.\n"
                f"{'⚠️ Special collection day - check council website for details.' if is_special else ''}"
            )
            cal.events.add(event)

        current_date += timedelta(days=1)

    return cal.serialize()