import schedule
import smtplib
import requests
from bs4 import BeautifulSoup


def umbrellaReminder():
    city = "harrison"
    state = "nj"

    url = "https://www.google.com/search?q=" + "weather" + city + state
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    # temperature = soup.find('div',
    #                         attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # time_sky = soup.find('div',
    #                      attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    temperature_elem = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
    time_sky_elem = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})

    if temperature_elem and time_sky_elem:
        temperature = temperature_elem.text
        time_sky = time_sky_elem.text


        sky = time_sky.split('\n')[1]

        if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy":
            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            smtp_object.starttls()

            # Authentication
            smtp_object.login("shivavihs98@gmail.com", "avihs98..")
            subject = "GeeksforGeeks Umbrella Reminder"
            body = f"Take an umbrella before leaving the house.\
            Weather condition for today is {sky} and temperature is \
                    {temperature} in {city}."
            msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode(
                'utf-8')

            # sending the mail
            smtp_object.sendmail("shivavihs98@gmail.com",
                                 "shiva.prakash.perumal@gmail.com", msg)

            # terminating the session
            smtp_object.quit()
            print("Email Sent!")
        else:
            print(f"No need for an umbrella today. Weather condition for today is {sky} and temperature is {temperature} in {city}.")
    else:
        print("Unable to retrieve weather information.")
    # Every day at 06:00AM time umbrellaReminder() is called.
schedule.every().day.at("13:41").do(umbrellaReminder)

while True:
    schedule.run_pending()
