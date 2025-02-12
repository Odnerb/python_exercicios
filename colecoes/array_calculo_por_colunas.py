# Algoritmo que soma vetores por coluna e armazena em um arrau unidimensional

from typing import List

matriz: List[List[int]] = [[5, -8, 10], [1, 2, 15], [25, 10, 7]]  # matriz 3x3
array: List[int] = []
s: int = 0
cont: int = 0

if __name__ == "__main__":
    while cont < 3:
        for num in matriz:
            for c in range(3):
                if num[c] == num[0] and cont == 0:
                    s += num[c]
                elif num[c] == num[1] and cont == 1:
                    s += num[c]
                elif num[c] == num[2] and cont == 2:
                    s += num[c]

        array.append(s)
        s = 0
        cont += 1
    print(array)
