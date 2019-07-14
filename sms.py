from twilio.rest import Client
 
 
#----------------------------------------------------------------------
def send_sms(msg, to):
    """"""
    sid = "AC994925d1dc5a7XXXXXXXXXXXXXXX"
    auth_token = "669a9cXXXXXXXXXXXXXXXXXXxx"
    twilio_number = "+1XXXXXXXXXXXxx"
 
    client = Client(sid, auth_token)
 
    message = client.messages.create(body=msg,
                                     from_=twilio_number,
                                     to=to,
                                     )
 
if __name__ == "__main__":
    msg = "Hello from Bukan Coder!"
    to = "+62XXXXXXXXXXX"
    send_sms(msg, to)




