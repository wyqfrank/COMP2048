from collections import Counter
sequence = [19, 17, 17, 19, 14, 20, 23, 18, 19, 8, 12, 16, 19, 8, 3, 21, 8, 25, 18, 14, 18, 6, 3, 18, 8, 15, 18, 22, 18, 11]

frequency = Counter(sequence)

# print(frequency)

for k, i in enumerate(sequence):
    print(k)
    if i == 19:
        sequence[k] = "a"
    elif i == 17:
         sequence[k] = "t"
    elif i == 14:
         sequence[k] = "c"
    elif i == 20:
         sequence[k] = "k" 
    elif i == 18:
         sequence[k] = "e" 
    elif i == 23:
         sequence[k] = "p"
    elif i == 8:
         sequence[k] = "r" 
    elif i == 12:
         sequence[k] = "l"
    elif i == 16:
         sequence[k] = "h"    
    elif i == 3:
         sequence[k] = "b"
    elif i == 21:
         sequence[k] = "o"
    elif i == 25:
         sequence[k] = "d"
    elif i == 6:
         sequence[k] = "m"
    elif i == 15:
         sequence[k] = "s"
    elif i == 22:
         sequence[k] = "v"
    elif i == 11:
         sequence[k] = "n"                     

print(" ".join(str(char) for char in sequence))