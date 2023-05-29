from transformers import pipeline
classifier = pipeline('sentiment-analysis')


def data(text):
 result = classifier(text)
 result1 = result[0]
 return result1


