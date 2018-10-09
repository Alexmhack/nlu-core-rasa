# nlu-core-rasa
Working along with tutorial for building a chatbot using the open source machine learning libraries rasa core and rasa nlu

# Installation

```
pip install rasa_nlu
pip install rasa_core
python -m spacy download en
npm install -g rasa-nlu-trainer
```

# Train NLU
```
mkdir data
subl data/data.json
```

**data.json** file will contain

```
{
	"rasa_nlu_data": {
		"common_examples": [
		{
			"text": "Hello",
			"intent": "greet",
			"entities": []
		},
		{
			"text": "goodbye",
			"intent": "goodbye",
			"entities": []
		}
		]
	}
}
```

Entering data like this is very tedious so we will be using ```rasa-nlu-trainer```

```
cd data
rasa-nlu-trainer
```

A nice Web App will be launched where you can add new examples with entities and intents

For creating an entity highlight the words that are part of the entity and then click on 
add entity button.

Checkout ```data.json``` file for more info.

**Create ```config_spacy.json``` file which will contain the configuration for rasa nlu**

```
{
	"pipeline":"spacy_sklearn",
	"path":"./models/nlu",
	"data":"./data/data.json"
}
```

Now create another file with which we will handle the training using python

**nlu_model.py**

```
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
```

# Rasa Core
