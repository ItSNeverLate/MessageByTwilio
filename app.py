from twilio.rest import Client
import config

twilio_client = Client(config.twilio_account_sid, config.twilio_auth_token)
call = twilio_client.messages.create(
    to="+989120148067",
    from_="+16267747535",
    body="Test SMS from twilio!"
)
print(call)
