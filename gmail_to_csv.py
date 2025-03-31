"""
Sample code to extract emails from gmail and save them to a csv file.
resource: https://sidratulmuntahaghouri.medium.com/get-your-emails-in-excel-b33f4e8b28cc
"""
import imaplib
import email
import pandas as pd

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email_address', 'your_email_password')

mail.select('inbox')

result, data = mail.search(None, 'SINCE "01-JAN-2025"')

email_list = []
for i in data[0].split():
    result, data = mail.fetch(i, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    email_subject = email_message['Subject']
    email_sender = email_message['From']
    email_date = email_message['Date']
    email_list.append([email_subject, email_sender, email_date])

df = pd.DataFrame(email_list, columns=['Subject', 'Sender', 'Date'])
df.to_excel('email_data.xlsx', index=False)

mail.close()
mail.logout()