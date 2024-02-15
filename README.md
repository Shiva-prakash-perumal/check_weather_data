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
   git clone https://github.com/Shiva-prakash-perumal/check_weather_data.git
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
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate

5. Install the required Python packages:
   ```bash
    pip install -r requirements.txt

6. Create a .env file in the project directory and add the following variables:
   ```bash
   touch .env
   ```
   ```bash .env
    API_KEY=your_tomorrow_io_api_key
    APP_PASSWORD=your_gmail_app_password
    SMTP_USERNAME=your_gmail_username
   ```
   You should create your unique API_KEY value from [Tomorrow.io](https://app.tomorrow.io/home)
   
## Usage
  To run the script:
  ```bash
  python weather_data.py
  ```
The script will run continuously and check the weather forecast every day at the specified time (configured in the schedule.every().day.at() function).

## Future Works
Here are some potential future enhancements for this project:

- Implement user input for location instead of hardcoding it.
- Add support for multiple email recipients.
- Enhance the email content with additional weather details.
- Implement logging to keep track of script execution and errors.
- Add implementation via `crontab` for scheduling instead of using the `schedule` library.

Feel free to contribute to this project or suggest new features!!

## Notes:-

Make sure to replace `your_tomorrow_io_api_key`, `your_gmail_app_password`, and `your_gmail_username` with your actual values.
You may need to allow less secure apps or generate an app password for your Gmail account to use SMTP authentication.
Adjust the time in the `schedule.every().day.at()` function to match your desired reminder time.


This README.md file provides detailed instructions on setting up the project, including cloning the repository, creating a virtual environment, installing dependencies from the `requirements.txt` file, setting up environment variables, and running the script. The hyperlink for Tomorrow.io has been added to the introduction section.


