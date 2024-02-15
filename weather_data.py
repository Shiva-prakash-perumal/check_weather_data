import os
import schedule
import smtplib
import requests
import json
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("API_KEY")
app_password = os.getenv("APP_PASSWORD")
user_email = os.getenv("SMTP_USERNAME")

def umbrellaReminder():
    zipcode = '07029'
    country = 'US'
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={zipcode}%20{country}&apikey={apikey}"
    x = requests.get(url).content
    if x:
        x = x.decode('utf8')
        x = json.loads(x)
        if x['data']['values']['weatherCode'] < 2100:
            print('yes')
            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            smtp_object.starttls()
            app_password = 'rnrx gxhf spdn bvgh'
            # Authentication
            smtp_object.login(user_email, app_password)
            subject = "Umbrella Reminder"
            body = f"Take an umbrella before leaving the house."
            msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode(
                'utf-8')

            smtp_object.sendmail("shivavihs98@gmail.com",
                                 "shiva.prakash.perumal@gmail.com", msg)

            smtp_object.quit()
            print("Email Sent!")
        else:
            print(f"No need for an umbrella today.")
    else:
        print("Unable to retrieve weather information.")
# Every day at 06:00AM time umbrellaReminder() is called.
schedule.every().day.at("06:00").do(umbrellaReminder)

while True:
    schedule.run_pending()
