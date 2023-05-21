from aws_practitioner.aws_practitioner_data import aws_cloud_practitioner_data
import genanki

# Config variables
DECK_NAME = 'Cloud Practitioner'
APKG_NAME = 'AWS.apkg'
DATA_SOURCE = aws_cloud_practitioner_data()

# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Básico',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',  # Include the tags in the question
            'afmt': '{{Description}}'  # Include the tags in the answer
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',  # Include the tags in the question
            'afmt': '{{Directory}}'  # Include the tags in the answer
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, DECK_NAME)
for tag, note in DATA_SOURCE.items():
    for dir_name, description in note:
        note = genanki.Note(model=model, fields=[dir_name, description])
        note.tags.append(tag)
        deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file(f"./anki_apkg/{APKG_NAME}")
