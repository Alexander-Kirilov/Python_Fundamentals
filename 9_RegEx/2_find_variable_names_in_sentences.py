import re

pattern = r"(^_{1}|(?<=\s_){1})[a-zA-Z0-9]+($|(?=[\s\.]))"
data = input()

result = [el.group() for el in re.finditer(pattern, data)]

print(','.join(result))
