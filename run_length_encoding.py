import random


def run_length_encoding():
    last = alphabets[0]
    count = 1
    result = ''
    for i in range(1, len(alphabets)):
        if alphabets[i] == last:
            count += 1
        else:
            result += f'{count}{last}'
            count = 1
            last = alphabets[i]
    if result[-1] != alphabets[len(alphabets) - 1]:
        result += f'{count}{last}'
        return result


alphabets = [chr(random.randint(65, 69)) for x in range(1, 10)]
print(alphabets)
print(run_length_encoding())
