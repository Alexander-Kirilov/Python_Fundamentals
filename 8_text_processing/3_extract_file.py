file_path = list(input().split("\\"))

file_name = file_path[-1].split(".")[0]
file_ext = file_path[-1].split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")
