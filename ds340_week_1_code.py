# -*- coding: utf-8 -*-
"""DS340-Week 1: Code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a0gJW-4_khFO6WVwikrp28wUBE522efW
"""

import pandas as pd
from transformers import pipeline

# Load datasets
ai_essay = pd.read_csv("ChatGPT_essay.csv")
ai_poetry = pd.read_csv("ChatGPT_poetry.csv")
ai_story = pd.read_csv("ChatGPT_story.csv")

human_essay = pd.read_csv("human_essay_1.csv")
human_poetry = pd.read_csv("human_poetry.csv")
human_story = pd.read_csv("human_stories.csv")

# Cleaning + labeling data
ai_essay = ai_essay[['responses']].rename(columns={'responses': 'text'})
ai_poetry = ai_poetry[['responses']].rename(columns={'responses': 'text'})
ai_story = ai_story[['Chapter_text']].rename(columns={'Chapter_text': 'text'})

human_essay = human_essay[['essays']].rename(columns={'essays': 'text'})
human_poetry = human_poetry[['Poem']].rename(columns={'Poem': 'text'})
human_story = human_story[['Chapter_text']].rename(columns={'Chapter_text': 'text'})

ai_essay['label'] = 1
ai_poetry['label'] = 1
ai_story['label'] = 1

human_essay['label'] = 0
human_poetry['label'] = 0
human_story['label'] = 0

# Combine all datasets
df = pd.concat([ai_essay, ai_poetry, ai_story, human_essay, human_poetry, human_story], ignore_index=True)


test_texts = df['text'].astype(str).tolist()

# Load pre-trained model
classifier = pipeline("text-classification", model="distilbert-base-uncased", truncation=True, max_length=512)

predictions = classifier(test_texts[:10])

for i, pred in enumerate(predictions):
    print(f"Text: {test_texts[i]}")
    print(f"Prediction: {pred['label']}, Score: {pred['score']:.4f}\n")