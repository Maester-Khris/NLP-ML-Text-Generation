# ======================================
# Test code for Bert data augmentatio  
# with random insertion strategy
# ======================================

# Bert data augmentation with random insertion
# from transformers import pipeline
# import random

# unmasker = pipeline('fill-mask', model='bert-base-cased')
# input_text = "I went to see a movie in the theater"

# orig_text_list = input_text.split()
# len_input = len(orig_text_list)
# #Random index where we want to insert the word except at the start or end
# rand_idx = random.randint(1,len_input-2)

# new_text_list = orig_text_list[:rand_idx] + ['[MASK]'] + orig_text_list[rand_idx:]
# new_mask_sent = ' '.join(new_text_list)
# print("Masked sentence->",new_mask_sent)
# #I went to see a [Mask] movie in the theater

# augmented_text_list = unmasker(new_mask_sent)
# augmented_text = augmented_text_list[0]['sequence']
# print("Augmented text->",augmented_text)
# #I went to see a new movie in the theater