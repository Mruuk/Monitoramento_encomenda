from twilio.rest import Client

def send_sms(number, text):
  account_sid = 'YOUR_ACCOUNT_SID'
  auth_token = 'YOUR_AUTH_TOKEN'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                     body=text,
                     from_="GENERATED_NUMBER",
                     to=number
                 )
  return message.sid