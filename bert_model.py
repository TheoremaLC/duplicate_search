from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
inputs1 = tokenizer("i have a dog", return_tensors="pt")
outputs1 = model(**inputs1)
sentence_embedding1 = outputs1.last_hidden_state[0, 0, :]

inputs2 = tokenizer("he woke up at 5 a.m. today, I hope i'm welcome to the 5 a.m. club.", return_tensors="pt")
outputs2 = model(**inputs2)
sentence_embedding2 = outputs2.last_hidden_state[0, 0, :]

sentence_embedding1 = sentence_embedding1.detach().numpy().reshape(1, -1)
sentence_embedding2 = sentence_embedding2.detach().numpy().reshape(1, -1)

similarity = cosine_similarity(sentence_embedding1, sentence_embedding2)
print(f" The cosine similarity between the two sentences is {similarity[0][0]}")

