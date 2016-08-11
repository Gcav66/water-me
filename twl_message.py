from credentials import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER

from twilio.rest import TwilioRestClient

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

"""
message = client.messages.create(
    body="I see you sitting there by the window",  # Message body, if any
    to="+17034896183",
    from_=TWILIO_NUMBER,
)
print message.sid
"""

messages = client.messages.list(To=TWILIO_NUMBER)
for message in messages:
	print message.body
	print message.from_