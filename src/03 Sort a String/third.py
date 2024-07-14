def sort_words(text):
  words = text.split()
  lowercase_words = [word.lower() for word in words]  # Create lowercase copy
  lowercase_words.sort()  # Sort the lowercase copy

  for _, original in zip(lowercase_words, words):
    index = lowercase_words.index(original.lower())  # Find original word's index
    lowercase_words[index] = original

  return lowercase_words

print(sort_words("tedt DICTATOR 1Distance gamer mode legacy annanus"))