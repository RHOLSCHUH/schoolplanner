import smtplib
from main import address_entry
from main import email_body_entry
from main import address
from main import email_body

def send_message():
    address_info = address.get()
    email_body_info = email_body.get()
    print(address_info,email_body_info)
    sender_email = "####ENTERYOUREMAILHERE######"
    sender_password = "###ENTERYOURPASSWORDHERE#####"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)
    print("Login successful")
    server.sendmail(sender_email,address_info,email_body_info)
    print("Message sent")
    address_entry.delete(0, END)
    email_body_entry.delete(0, END)
