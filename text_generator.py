import random
from collections import defaultdict, Counter
from nltk.util import ngrams

s = input()
f = open(s, "r", encoding="utf-8")
words = []
for line in f:
    for word in line.split():
        words.append(word)

grams = ngrams(words, 3)
trigrams = [(' '.join(gram[:2]), gram[2]) for gram in grams]

model = defaultdict(Counter)
for h, t in trigrams:
    model[h][t] += 1

for _ in range(10):
    sentence = []

    while len(sentence) < 1:
        head = random.choice(trigrams)[0]
        first = head.split()[0]
        if first.isupper() and not first.endswith(".") and not first.endswith("!") and not first.endswith("?"):
            sentence.append(head)
    sentence.append(model[sentence[-1]].most_common(1)[0][0])
    for _ in range(2):
        whole = " ".join(sentence)
        text = whole.split()[-2] + " " + whole.split()[-1]
        sentence.append(model[text].most_common(1)[0][0])

    while not sentence[-1].endswith('.') and not sentence[-1].endswith('?') and not sentence[-1].endswith('!'):
        whole = " ".join(sentence)
        text = whole.split()[-2] + " " + whole.split()[-1]
        sentence.append(model[text].most_common(1)[0][0])

    print(" ".join(sentence))
