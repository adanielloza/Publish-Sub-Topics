import config 
import smtplib
from email.message import EmailMessage
import ssl

def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = config.email_sender
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        
        loginstate = server.login(config.email_sender, config.password, initial_response_ok=True)
        print(loginstate)
        
        send_main_stte= server.sendmail(config.email_sender, to,msg.as_string())
        print(send_main_stte)
        return True
