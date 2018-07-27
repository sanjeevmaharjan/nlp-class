file = open("testfile.txt", "rt")

words = []

for line in file:
    for word in line.split():
        # add = True
        # for w in words:
        #     if w == word:
        #         add = False
        #         break
        # if add == False:
        #     continue
        words.append(word)

words.sort()

outfile = open("listOfWords.txt", "w+")
for word in words:
    outfile.writelines(word + "\n")
outfile.close

wordCount = ["word\tcount"]

for word in words:
    wordCount.append(word + "\t" + str(words.count(word)))

outfile = open("listOfWordsAndCounts.csv", "w+")
for wc in wordCount:
    outfile.writelines(wc + "\n")
outfile.close