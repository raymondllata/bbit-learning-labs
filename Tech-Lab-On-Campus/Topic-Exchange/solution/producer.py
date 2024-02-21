from producer_sol import mqProducer

import sys


args = sys.argv[1:]
ticker = args[0]
stock = args[1]
price = args[2]

producer = mqProducer(routing_key="Tech Lab Key",exchange_name="Tech Lab Exchange")


