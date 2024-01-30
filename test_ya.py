from math import factorial as f


with open('input.txt', encoding='utf-8') as file:
    chars = file.read()

count = 0
while len(chars) > 1:
    count += f(len(chars))
    chars = chars[:-1]


with open('output.txt', 'w', encoding='utf-8') as output:
    print(count, file=output)
