words = input().split(", ")
text = input()

equal_words = [word for word in words if word in text]

print(equal_words)
