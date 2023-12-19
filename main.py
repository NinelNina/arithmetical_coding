from coding import coding
from decoding import decoding


def input_array():
    n = 4

    probabilities = []
    alphabet = "S = {"

    for i in range(n):
        probabilities.append(float(input(f"Введите вероятность символа s{i + 1}: ")))
        alphabet += "s" + str(i + 1)
        symb = ", " if i < n - 1 else "}"
        alphabet += symb

    sequence = input("Введите последовательность символов: ")

    return probabilities, sequence, alphabet


if __name__ == '__main__':
    probabilities, sequence, alphabet = input_array()

    result = alphabet + "\ns = (" + sequence + ")\n"

    sequence = [int(sequence[i + 1]) for i in range(0, len(sequence), 2)]

    str, x, q, F_S, G_S = coding(probabilities, sequence)
    result += str
    result += "-----------------------------------\n"
    result += decoding(probabilities, q, x, len(sequence), F_S, G_S)

    with open("result.txt", "w", encoding='utf-8') as file:
         file.write(result)

