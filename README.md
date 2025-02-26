# Milton Keynes Bin Collection Helper

A Streamlit web application designed to help Milton Keynes residents quickly identify their bin collection color and understand waste management guidelines. The app provides an intuitive, user-friendly interface for checking weekly bin collection information.

## Features

- 📅 Weekly bin color indicator (Red/Blue)
- ⚠️ Special collection day notifications
- 📱 Responsive design
- 📝 Detailed bin type guide
- 🗓️ Calendar integration (.ics file export)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/urbanevac/BinSchedule.git
cd BinSchedule
```

2. Install the required packages:
```bash
pip install streamlit ics
```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

## Project Structure

```
project_directory/
│
├── .streamlit/
│   └── config.toml  (Streamlit server configuration)
│
├── main.py          (Main Streamlit application)
├── bin_schedule.py  (Bin schedule logic)
└── README.md        (This file)
```

## Usage

The application will:
- Show the current week's bin color (Red or Blue)
- Highlight special collection days
- Allow you to export collection schedule to your calendar
- Provide a detailed guide for what goes in each bin type

## Bin Types Guide

- 🔴 **Red Bin**: Recycling (plastics, metals, cans)
- 🔵 **Blue Bin**: Paper and cardboard recycling
- ⚫ **Black Bin**: General waste (collected weekly)
- 🟢 **Green Bin**: Garden waste (collected weekly)

## Contributing

Feel free to submit issues and enhancement requests!

## Data Source

Based on Milton Keynes Council 2025 collection calendar.
