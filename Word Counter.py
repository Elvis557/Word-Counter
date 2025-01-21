def word_count(text):
    return len(text.split())

text = input("Enter a sentence: ")
print(f"Word count: {word_count(text)}")
