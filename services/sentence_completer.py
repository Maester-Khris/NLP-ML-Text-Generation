import spacy

# Load spaCy for stop word analysis
nlp = spacy.load("fr_core_news_sm") 


def completer(sentence):
    doc = nlp(sentence)
    for token in doc:
        # Check if the token is a noun and if it needs a determiner
        if token.pos_ == "NOUN" and not any(t.dep_ == "det" for t in token.children):
            # Determine the appropriate determiner
            if token.tag_ == "NN":  # Singular noun
                determiner = "de" 
            elif token.tag_ in ["NN", "NNS"]:  # Assuming plural nouns
                determiner = "des"  # Plural determiner
            elif token.tag_ in ["NNP", "NNPS"]:  # Proper nouns
                determiner = "le"  # Default to masculine singular
            elif token.tag_ == "FEM":  # Feminine nouns (custom tagging needed)
                determiner = "la"  # Feminine singular determiner
            else:  # Default case for masculine singular
                determiner = "le"  # Masculine singular determiner

            # Additional logic for location or specific cases
            if  token.ent_type_ in ["GPE","LOC"]:  # Example condition for using 'à' or 'au'
                if token.pos_ == "PROPN":
                determiner = "au" # Use 'au' for masculine locations
                else:
                    determiner = "à" 
            # Insert the determiner before the noun
            words = sentence.split()
            words.insert(token.i, determiner)
            sentence = " ".join(words)
            break  # Insert only one determiner

    return sentence