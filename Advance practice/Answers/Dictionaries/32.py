sentence = input("Enter a sentence: ")
word_frequencies = {}

for word in sentence.lower().split():
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

print("Word frequencies:", word_frequencies)
