from twilio.rest import Client

def send_sms(number, text):
  account_sid = 'AC62eedb9843eec8fb4a755d0ae6960ccf'
  auth_token = '5b53741c9391e0cdcfb000988e573554'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                     body=text,
                     from_="+17147868497",
                     to=number
                 )
  return message.sid