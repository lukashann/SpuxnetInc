from WifiBroker import WifiBroker

def run_broker()
    wifiBroker = WifiBroker()
    wifiBroker.connect_to_broker()
    msg = 'Stuxnet > world'
    wifiBroker.publish_msg(msg)
    wifiBroker.disconnect()

run_broker()
