import smtplib
from email.mime.text import MIMEText


def send_mail(customer, email, product, rating, comments):
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = 'a1db4e4575b217'
  password = '1f8a6162ab8745'
  message = f"""
              <h3>New Feedback Submission</h3><ul><li>
              Customer: {customer}</li><li>Email: {email}</li><li>
              Product: {product}</li><li>Rating: {rating}</li><li>
              Comments: {comments}</li></ul>
              """

  sender_email = email
  receiver_email = 'chokomateventures@yahoo.com'
  msg = MIMEText(message, 'html')
  msg['Subject'] = 'Chokomate Feedback'
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # send Email
  with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
