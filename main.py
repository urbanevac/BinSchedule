import streamlit as st
from datetime import datetime
from bin_schedule import (
    get_bin_color, 
    get_next_collection_date, 
    is_special_collection_day,
    generate_calendar_file
)

# Page config
st.set_page_config(
    page_title="MK Bin Collection",
    page_icon="🗑️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .bin-display {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
    }
    .red-bin {
        background-color: rgba(255, 0, 0, 0.2);
        border: 2px solid red;
    }
    .blue-bin {
        background-color: rgba(0, 0, 255, 0.2);
        border: 2px solid blue;
    }
    .unknown-bin {
        background-color: rgba(128, 128, 128, 0.2);
        border: 2px solid gray;
    }
    .special-day {
        border: 3px solid gold !important;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    .warning-text {
        color: #ff9800;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("Milton Keynes Bin Collection Helper")

# Current date
current_date = datetime.now()
st.write(f"Today's date: {current_date.strftime('%d %B %Y')}")

# Check if we're in 2025
if current_date.year != 2025:
    st.warning("⚠️ This tool is designed for 2025 collections. Dates shown may not be accurate for the current year.")

# Get bin color for this week
bin_color = get_bin_color(current_date)
is_special = is_special_collection_day(current_date)

# Display current week's bin
st.subheader("This Week's Collection")
color_class = f"bin-display {bin_color.lower()}-bin{'special-day' if is_special else ''}"
special_notice = "⚠️ Special Collection Day" if is_special else ""

st.markdown(f"""
    <div class="{color_class}">
        <h2>{bin_color} Bin Week</h2>
        <p class="warning-text">{special_notice}</p>
    </div>
""", unsafe_allow_html=True)

if is_special:
    st.warning("⚠️ This is a special collection day. Please check the Milton Keynes Council website for specific instructions.")

# Next collection date
next_date = get_next_collection_date(current_date)
if next_date:
    next_bin_color = get_bin_color(next_date)
    next_is_special = is_special_collection_day(next_date)

    st.subheader("Next Collection")
    st.write(f"Date: {next_date.strftime('%d %B %Y')}")
    st.write(f"Bin Color: {next_bin_color}")
    if next_is_special:
        st.warning("⚠️ Next collection is a special collection day")

# Calendar Integration
st.subheader("Add to Calendar")
if st.button("Download Calendar (.ics)"):
    calendar_data = generate_calendar_file(current_date)
    st.download_button(
        label="Save to Calendar",
        data=calendar_data,
        file_name="mk_bin_collection.ics",
        mime="text/calendar"
    )
    st.info("💡 Tip: Open this file with your calendar app to import the next month's collection schedule")

# Instructions
st.markdown("""
---
### Instructions
1. Put your bin out the night before collection day
2. Ensure the bin is easily accessible
3. Check Milton Keynes Council website for holiday changes
4. Black and Green bins are collected every week

### Special Collection Days
- Days marked with a gold border are special collection days
- Always check the [Milton Keynes Council Website](https://www.milton-keynes.gov.uk/collection-days) for the latest information about special collection days

For more information, visit [Milton Keynes Council Website](https://www.milton-keynes.gov.uk/collection-days)
""")

# Footer
st.markdown("---")
st.caption("Data based on Milton Keynes Council 2025 collection calendar")