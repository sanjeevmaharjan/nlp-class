from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

import nltk.data

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

text = "Your twenties will be the great transitional period of your life. It is a time of crossroads. Of immense change of incredible uncertainty. Indeed my 20's were such a period for me. That was when I evolved from a no good troublemaker to the legendary sword you see before you today. Many men envy my hairstyle you see and they were inspired... and formed a fringe group, a sort of cult if you will - Dedicated to the adoration of my daring hairstyle. They met every week. Or was it everyday? As you may have noticed, humans are very young from the time they are born until some years later. I however was born old and wise and would often discuss abstract..."

print(sent_tokenize(text))
len(sent_tokenize(text))

print(tokenizer.tokenize(text))

print(word_tokenize(text))