from string import digits as d, ascii_letters as a, punctuation as p

for i in d + a + p:
    for j in d + a + p:
        for k in d + a + p:
            for l in d + a + p:
                print(i,j,k,l)

# print("hello")

# python crack.py