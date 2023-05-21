from License_driver_CR.data_license_driver import generate_cap_2
import genanki

data_driver_license = generate_cap_2()
# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Capitulo 2')
import pdb; pdb.set_trace()
for note in data_driver_license.values():
    for dir_name, description in note:
        note = genanki.Note(model=model, fields=[dir_name, description])
        deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('cap2.apkg')
