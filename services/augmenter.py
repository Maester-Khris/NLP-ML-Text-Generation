from transformers import BertTokenizer, BertForMaskedLM
import torch
from .sentence_completer import completer

# Load the pre-trained BERT model and tokenizer
model_name = "bert-large-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForMaskedLM.from_pretrained(model_name)
model.eval()  # Set the model to evaluation mode

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def insert_context_keywords(sentence, keywords):
    """
    Inserts a list of keywords into a sentence using a pre-trained BERT model.
    Args:
        sentence (str): The original sentence.
        keywords (list): A list of keywords to insert.

    Returns:
        str: The sentence with the inserted keywords.
    """

    # 1. Tokenize the sentence
    input_ids = tokenizer.encode(sentence, add_special_tokens=True, return_tensors="pt")

    # 2. Create a list to store the inserted keywords
    inserted_keywords = []

    # 3. Iterate over the keywords
    for keyword in keywords:
        # 4. Find a suitable position for the keyword
        #   - We'll choose a random position for simplicity
        #   - You can implement more sophisticated strategies
        masked_index = torch.randint(1, input_ids.shape[1], (1,))

        # 5. Mask the sentence at the chosen position
        input_ids[0, masked_index] = tokenizer.mask_token_id

        # 6. Create input tensors for the model
        input_ids = input_ids.to(device)
        attention_mask = torch.ones_like(input_ids).to(device)

        # 7. Predict the most likely word to replace the mask
        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)

        predicted_token_id = torch.argmax(outputs.logits[0, masked_index]).item()

        # 8. Decode the predicted token and replace the mask
        predicted_word = tokenizer.decode([predicted_token_id])
        sentence = sentence.replace("[MASK]", predicted_word)

        # 9. Insert the keyword at the masked position
        #    - Assuming the sentence is a list of words
        words = sentence.split()
        words.insert(masked_index.item(), keyword)
        sentence = " ".join(words)

        # 10. Update the input_ids for the next iteration
        input_ids = tokenizer.encode(sentence, add_special_tokens=True, return_tensors="pt")
        inserted_keywords.append(keyword)

    # 11. Analyze the sentence to add some potential stop word around inserted keyword
    sentence = completer(sentence)
    return sentence, inserted_keywords


# =========== Test code =========
# if __name__ == "__main__":
#     sentence = "les etudiant ont fini"
#     keywords = ["cycle", "master", "tech"]
#     new_sentence, inserted_keywords = insert_keywords(sentence, keywords)
#     print(f"Original sentence: {sentence}")
#     print(f"New sentence: {new_sentence}")
#     print(f"Inserted keywords: {inserted_keywords}")
