import smtplib

my_email = "@gmail.com"
password = "1234567890"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Subject:Hello\n\nThis is the body of my email",
    )