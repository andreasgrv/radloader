from radloader import EdIELoader
from argparse import ArgumentParser

parser = ArgumentParser(description='Load radiology dataset.')

parser.add_argument('-f', '--folder', required=True, type=str,
                    help='Path to folder with radiology reports.')

args = parser.parse_args()

loader = EdIELoader.load(args.folder)

# Print 5 document representations
for doc in loader.docs[:5]:
    print(doc)
    # Document relations
    # print(doc.relations)
    # Document labels
    # print(doc.labels)
print()

# Print 5 sentence representations
first_doc = loader.docs[0]
for sent in first_doc.sentences[:5]:
    # The sentence as words
    print(sent.words)
    # Or as characters
    # print(sent.chars)
    # Named entities
    print(sent.ner_tags)
    # Negation per word
    print(sent.negation)
    print()
