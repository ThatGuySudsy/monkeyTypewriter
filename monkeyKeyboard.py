import random as r
import time as t

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "."]
sentence = ""
toPrint = ""
sentences = 0
cN = 0

if input("Turn quiet mode on? (Doesn't print into console) Answer y/n  ").lower() == "y":
    quiet = True
target = input("What is your message?  ").lower()

startTime = t.perf_counter()

while sentence != target:
    character = characters[r.randrange(len(characters))]
    cN += 1
    if character == ".":
        sentence = toPrint
        toPrint = ""
        if not quiet:
            print(sentence)
        sentences += 1
    else:
        toPrint += character

elapsed = t.perf_counter() - startTime
mins, secs = divmod(elapsed, 60)

print(f"Message recieved after {cN} characters ({sentences} sentences)")
print(f"Took {int(mins)} minute(s) {secs:.2f} second(s)")
