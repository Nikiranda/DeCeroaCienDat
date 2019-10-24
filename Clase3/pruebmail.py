from gmailsendemail import SendEmailUtility
import os

remitente="d0a100prueba@gmail.com"
destinario="hayde.mtzl@gmail.com"
subject="Holi"
text="Holi mandé un mail, bye"

mailito = SendEmailUtility()
mailito.send_mail_no_attachment(remitente, "pepitopito", destinario,subject, text)
