import os
from twilio.rest import Client


account_sid ="TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)

client.messages.create(from_="TWILIO_PHONE_NUMBER",
                       to="CELL_PHONE_NUMBER",
                       body="Hello! How are you? ")