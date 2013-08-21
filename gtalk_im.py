#!/usr/bin/python

import xmpp, time

# Set GTalk info
from_google_id = 'youraccount@gmail.com'
from_google_id_pw = 'acct password'
to_google_id = 'accountyouaresendingto@gmail.com'

jid  =  xmpp.protocol.JID( from_google_id )
cl  =  xmpp.Client('gmail.com')
cl.connect( ( 'talk.google.com', 5223 ) )
cl.auth( jid.getNode( ), from_google_id_pw )
IM = 'Test message sent from python script ... did it work??'
cl.send( xmpp.protocol.Message( to_google_id, IM,typ = "chat" ) )
time.sleep( 1 )
print str( IM ) + ' sent '