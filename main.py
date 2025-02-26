import streamlit as st
from datetime import datetime
from bin_schedule import get_bin_color, get_next_collection_date

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

# Display current week's bin
st.subheader("This Week's Collection")
color_class = bin_color.lower() + "-bin"
st.markdown(f"""
    <div class="bin-display {color_class}">
        <h2>{bin_color} Bin Week</h2>
    </div>
""", unsafe_allow_html=True)

# Next collection date
next_date = get_next_collection_date(current_date)
if next_date:
    next_bin_color = get_bin_color(next_date)
    st.subheader("Next Collection")
    st.write(f"Date: {next_date.strftime('%d %B %Y')}")
    st.write(f"Bin Color: {next_bin_color}")

# Instructions
st.markdown("""
---
### Instructions
1. Put your bin out the night before collection day
2. Ensure the bin is easily accessible
3. Check Milton Keynes Council website for holiday changes

For more information, visit [Milton Keynes Council Website](https://www.milton-keynes.gov.uk/collection-days)
""")

# Footer
st.markdown("---")
st.caption("Data based on Milton Keynes Council 2025 collection calendar")
