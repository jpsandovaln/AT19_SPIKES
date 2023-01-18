
from twilio.rest import Client

#credentials 
auth_token="8b294a87632bb949a47fc50fd32ffc41"
sid_id="AC16ed93da31a7d08a981dc1268a3c53c3"

client = Client(sid_id,auth_token)

#parameters
from_number    = 'whatsapp:+14155238886' 
to_number      = 'whatsapp:+59168050120' 
message_to_send= 'Mensaje directo desde twilio'


client.messages.create(
                        from_=from_number,
                        to=to_number,
                        body=message_to_send                        
                      )


