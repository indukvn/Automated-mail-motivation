import smtplib
import datetime as dt
import random

my_mail = "newmail002244@gmail.com"
my_pass = "xxx"

now = dt.datetime.now()
days_of_week = now.weekday()
if days_of_week == 2:

    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs="chu_4466@yahoo.com", msg=f"Subject: Motivation\n\n{quote}")
