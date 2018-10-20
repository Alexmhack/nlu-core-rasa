from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

def train_nlu(data, config, model_dir):
	training_data = load_data('./data/data.json')
	trainer = Trainer(config.load("config_spacy.json"))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name='nlu', project='current')


def run_nlu(model_dir):
	interpreter = Interpreter.load(model_dir)
	print(interpreter.parse("I am planning a trip to Indore. What's the weather out there."))


if __name__ == '__main__':
	# train_nlu('./data/data.json', 'config_spacy.json', './models')
	run_nlu('./models/current/nlu')
