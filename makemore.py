# reading the dataset and learning about it
words = open('names.txt', 'r').read().splitlines()
print("number of names:", len(words))
print("shortest name length: ", min(len(w) for w in words))
print("longest name length: ", max(len(w) for w in words))

# creating a bigram from the data set
for w in words[:1]:
    for ch1, ch2 in zip(w, w[1:]):
        print(ch1, ch2)