import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email():
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        self.MAIL_SMTP = "smtp.mail.ru"
        self.MAIL_IMAP = "imap.mail.ru"
    
    def send_message(self, recipients, subject, message):
        #send message
        msg = MIMEMultipart()
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        msg_send = smtplib.SMTP_SSL(self.MAIL_SMTP, 465)
        msg_send.login(self.login, self.password)
        msg_send.sendmail(from_addr=self.login, to_addrs=recipients, msg=msg.as_string())
        msg_send.quit()
        #send end

    def recieve(self, header):
        #recieve
        mail = imaplib.IMAP4_SSL(self.MAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("Inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        print(f'From: {email.utils.parseaddr(email_message["From"])} To: {email.utils.parseaddr(email_message["To"])[1]}')
        mail.logout()
        #end recieve


if __name__ == '__main__':

    emails = Email(login='example@mail.ru', password='')
    emails.send_message(recipients=['example@mail.ru'], subject='Test', message='Test message')
    emails.recieve(header = None)
