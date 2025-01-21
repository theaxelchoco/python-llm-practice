from transformers import pipeline

classifier = pipeline("sentiment-analysis")
results = classifier([
    "We are happy to show the transfomers library.",
    "I hate you",
    "I love you"
])

for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")