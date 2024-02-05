def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    for word in reversed_words:
        print(word, end=' ')
user = input()
reverse_words(user)
