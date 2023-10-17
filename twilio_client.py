from twilio.rest import Client

def send_sms(number, text):
  account_sid = 'YOUR_ACCOUNT_SID'
  auth_token = 'YOUR_AUTH_TOKEN'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                     body=text,
                     from_="NUMBER_TWILIO",
                     to=number
                 )
  return message.sid