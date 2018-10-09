from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)

	model_directory = trainer.persist(model_dir, fixed_model_name='weathernlu')


def run_nlu():
	interpreter = Interpreter.load('./models/current/nlu', RasaNLUConfig('config_spacy.json'))
	print(interpreter.parse("Hello"))


if __name__ == '__main__':
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
