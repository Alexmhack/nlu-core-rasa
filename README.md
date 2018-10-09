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

```
