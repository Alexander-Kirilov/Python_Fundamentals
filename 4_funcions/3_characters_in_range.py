def characters(start_char, end_char):
    for char in range(start_char+1, end_char):
        print(chr(char), end=" ")

starting = ord(input())
ending = ord(input())
characters(starting, ending)