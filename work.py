words = ["apple", "banana", "orange", "grape", "umbrella"]
vowels=["a","e","i","o","u"]
new=list(filter(lambda word:word[0] in vowels,words))
print(new)