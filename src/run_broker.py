from WifiBroker import WifiBroker

wifiBroker = WifiBroker()
wifiBroker.connect_to_broker()
msg = 'Stuxnet > world'
wifiBroker.pub_message(msg)
wifiBroker.disconnect()

