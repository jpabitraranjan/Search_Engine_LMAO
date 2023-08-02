from itertools import permutations
from re import search

s = (input("Enter Your Search:")).lower()
L = s.split()
p = list(permutations(L, 2))
txt_l = ['how to use permutations in python', 'how to convert string into identifier in python', 'how to use itertools in python', 'what does itertools do in python', 'how to increase height']

for j in txt_l:
    n = list(permutations(j.split(), 2))
    for i in p:
        for k in n:
            m = k[0] + " " + k[1]
            if search(f"^{i[0]}.*{i[1]}$", m.lower()):
                print(j)
                break
