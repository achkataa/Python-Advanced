string = input()

vowels = ["a", "A", "o", "O", "u", "U", "e", "E", "i", "I"]

print(''.join([i for i in string if i not in vowels]))



