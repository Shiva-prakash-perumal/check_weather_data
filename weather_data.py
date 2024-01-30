import schedule
import smtplib
import requests
import json
from datetime import date, datetime

# t_date = date.today()
# print(t_date)

def umbrellaReminder():
    zipcode = '07029'
    country = 'US'
    apikey = apikey
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
            app_password = app_password
            # Authentication
            smtp_object.login("shivavihs98@gmail.com", app_password)
            subject = "Umbrella Reminder"
            body = f"Take an umbrella before leaving the house.\
            Weather condition for today is rainy in HARRISON."
            msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode(
                'utf-8')

            # sending the mail
            smtp_object.sendmail("shivavihs98@gmail.com",
                                 "shiva.prakash.perumal@gmail.com", msg)

            # terminating the session
            smtp_object.quit()
            print("Email Sent!")
        else:
            print(f"No need for an umbrella today.")
    else:
        print("Unable to retrieve weather information.")
    # Every day at 06:00AM time umbrellaReminder() is called.
# schedule.every().day.at("14:48").do(umbrellaReminder)
#
# while True:
#     schedule.run_pending()

umbrellaReminder()