from radloader import EdIELoader
from argparse import ArgumentParser


if __name__ == "__main__":

    parser = ArgumentParser(description='Load radiology dataset.')

    parser.add_argument('-f', '--folder', required=True, type=str,
                        help='Path to folder with radiology reports')
    parser.add_argument('--proc_all', action='store_true',
                        help='Whether to also load sentences marked proc=no')

    args = parser.parse_args()

    # NOTE: By default we only load all sentences with a proc=yes attribute
    # This discards sentences that weren't processed by EdIE-R
    # pass --proc_all to also load these additional sentences.
    loader = EdIELoader.load(args.folder, proc_all=args.proc_all)

    sentences = [s for doc in loader.docs
                 for s in doc.sentences]

    # NOTE:
    # The below entities differ from the result extracted from sentences below
    # in the case that the same word span has been annotated both as a modifier
    # and an entity (Rare case - occurs in Tayside data)
    #
    # entities = [e for doc in loader.docs
    #             for e in doc.entities]

    entities = [e
                for doc in loader.docs
                for s in doc.sentences
                for e in s.ner_and_mod_tags
                if e.startswith('B-')
                ]

    # These counts will be a bit different from those reported in Table 1 of
    # https://arxiv.org/pdf/1903.03985.pdf. This is due to the proc=yes filtering.
    # Pass --proc_all to crossvalidate with the counts of sentences in the paper.
    print('Loaded %d documents with %d sentences containing %d entities' %
          (len(loader.docs), len(sentences), len(entities)))
    print()

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
        print(sent.tokens)
        # Or as characters
        # print(sent.chars)
        # Named entities
        print(sent.ner_tags)
        # Negation per word
        print(sent.negation)
        print()
