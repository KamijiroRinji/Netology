import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailProcessor:

    def __init__(self, mail_smtp, mail_smtp_port, mail_imap, mail_imap_port,
                 login, password):
        self.mail_smtp = mail_smtp
        self.mail_smtp_port = mail_smtp_port
        self.mail_imap = mail_imap
        self.mail_imap_port = mail_imap_port
        self.login = login
        self.password = password

    def send_email(self, subject, message):
        recipients = \
            input('Введите адресатов (через запятую без пробелов): ') \
            .lower().split(',')
        send_email = MIMEMultipart()
        send_email['From'] = self.login
        send_email['To'] = ', '.join(recipients)
        send_email['Subject'] = subject
        send_email.attach(MIMEText(message))

        mail_client = smtplib.SMTP(self.mail_smtp, self.mail_smtp_port)
        # identify ourselves to smtp gmail client
        mail_client.ehlo()
        # secure our email with tls encryption
        mail_client.starttls()
        # re-identify ourselves as an encrypted connection
        mail_client.ehlo()

        mail_client.login(self.login, self.password)
        mail_client.sendmail(self.login, send_email['To'].split(', '),
                             send_email.as_string())

        mail_client.quit()

    def receive_email(self, header):
        mail_client = imaplib.IMAP4_SSL(self.mail_imap, self.mail_imap_port)
        mail_client.login(self.login, self.password)
        mail_client.list()
        mail_client.select('inbox')

        header_criterion = f'(HEADER Subject {header if header else "ALL"})'
        result, data = mail_client.uid('search', None, header_criterion)

        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail_client.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(str(raw_email))
        print(email_message)
        mail_client.logout()


if __name__ == '__main__':
    gmail = MailProcessor(mail_smtp, mail_smtp_port, mail_imap, mail_imap_port,
                          login, password)
    gmail.send_email()

