input_text = input()

occurrences = {}

for ch in input_text:
    if ch == " ":
        continue

    if ch not in occurrences:
        occurrences[ch] = 0

    occurrences[ch] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")
