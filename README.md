# anki_deck_creator

## Indications

This repo is for creating anki decks using genanki library, the main script is located in create_deck.py file.

The input data must be in the format of ordered list of tuples:

data = [
("question", "answer"), ("question", "answer")
]

Since this report is for personal usage, I have some folders with data of personal interest, this data is not sensitive, most of them can be found over the internet.

## How to run the script

1. Make sure to install the genanki library: pip install genanki.
2. The just run the scrip: python3 script_name.py
3. Note: make sure to change the data source, for the one of interest, and verify if it is in the currect format.


Note: An example of output data can be found on the anki_apkg folder.
