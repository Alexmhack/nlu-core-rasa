from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

interpreter = RasaNLUInterpreter("./models/current/nlu")
agent = Agent.load("models/dialogue", interpreter=interpreter)

while True:
	user = input(">> ")
	msg = agent.handle_text(user)
	print(msg)
