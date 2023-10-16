from twilio.rest import Client

def send_sms(number, text):
  account_sid = 'Your_account_sid'
  auth_token = 'Your_auth_token'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                     body=text,
                     from_="generated_number",
                     to=number
                 )
  return message.sid