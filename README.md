# Weather Umbrella Reminder

This Python script sends an email reminder to take an umbrella based on the weather forecast for a specific location. It utilizes the [Tomorrow.io](https://app.tomorrow.io/home) weather API to retrieve real-time weather data and the smtplib library to send emails via Gmail.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Python packages:
  - schedule
  - smtplib
  - requests
  - json
  - dotenv

## Setup

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
2. Navigate to the project directory in loacal:
   ```bash
   cd weather-umbrella-reminder
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
4. Activate the virtual environment:

   On Windows:
   ```bash
   venv\Scripts\activate

   On macOS/Linux:
   ```bash
  source venv/bin/activate

5. Install the required Python packages:
   ```bash
    pip install -r requirements.txt

6. Create a .env file in the project directory and add the following variables:
   ```bash
   touch .env
   ```bash .env
    API_KEY=your_tomorrow_io_api_key
    APP_PASSWORD=your_gmail_app_password
    SMTP_USERNAME=your_gmail_username
   
## Usage
To run the script:
   ```bash
   python weather_umbrella_reminder.py
