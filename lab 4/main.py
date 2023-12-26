def levenshtein_distance(word1, word2):
    matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[len(word1)][len(word2)]

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

distance = levenshtein_distance(word1, word2)
print("Расстояние Левенштейна равно:", distance)