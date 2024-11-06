from collections import deque

letras = deque('ABCDEFGHIJ')
print(letras)

letras.extend(['K', 'L', 'M', 'N', 'O', 'P'])
letras.pop()
letras.popleft()
print(letras)
