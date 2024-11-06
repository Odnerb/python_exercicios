from collections import OrderedDict

seq1 = OrderedDict({'a': 1, 'b': 2})
seq2 = OrderedDict({'b': 2, 'a': 1})

print(seq1 == seq2)
print(type(seq1))
