
from twilio.rest import Client

#credentials 
auth_token="8b294a87632bb949a47fc50fd32ffc41"
sid_id="AC16ed93da31a7d08a981dc1268a3c53c3"
sandbox_number='+14155238886'

client = Client(sid_id,auth_token)

dicdata ={'user1':['+59168050120','David'],'user2':['+59171963648','Ricardo']}

from_number    = 'whatsapp:' + sandbox_number
to_number      = 'whatsapp:' + dicdata['user1'][0]
message_to_hello= 'Hola '     + dicdata['user1'][1] +"! \n"
message_to_info ='Request finalizado, enlace de descarga: https://youtube.com'
message_to_send = message_to_hello+message_to_info

client.messages.create(
                        from_=from_number,
                        to=to_number,
                        body=message_to_send                        
                      )