# 🐒 Random Sentence Generator — Inspired by the Infinite Monkey Theorem

A Python experiment that simulates the **Infinite Monkey Theorem** — the idea that, given enough time, a monkey hitting random keys could eventually type any text, like “hello world.”

This program randomly types characters (`a–z`, space, `.`), ending each sentence when a period appears, until one of those sentences matches your chosen message. It then prints how many characters and sentences it took, and how long the process lasted.

---

## ✨ Example

```text
What is your message? hi
q
sja
hi
Message received after 1128 characters (53 sentences)
Took 0 minute(s) 1.23 second(s)
🧠 How it Works
The program picks from 28 characters:
a–z, space, and .

Every time it picks ., it ends a sentence and checks if the sentence equals your target.

If it matches — success!

Otherwise, it resets and keeps typing.

This is a finite, practical version of the Infinite Monkey Theorem — except here, the “monkey” is a short Python script.

📊 Probability Background
For a target of length L, the chance of success for one sentence is:

ini
Copy code
p = (1/28)^(L+1)
Expected number of sentences before success ≈ 28^(L+1)
That means longer words grow exponentially harder:

Target	Expected Sentences	Average Time*
a	784	< 1 sec
hi	21,952	~seconds
cat	614,656	minutes
hello	13,492,928	hours

Assuming 1M characters/sec and no print delay.

🚀 How to Run
Make sure you have Python 3.8+ installed.

Clone or download this repo:

bash
Copy code
git clone https://github.com/thatguysudsy/random-sentence-generator.git
cd random-sentence-generator
Run the script:

bash
Copy code
python main.py
Enter your target message (letters, space, or period).

🧩 Features
Simple command-line interface

Tracks total characters, sentences, and elapsed time

Based on the Infinite Monkey Theorem

Works on Windows, macOS, and Linux

⚖️ License
Licensed under the MIT License
Copyright (c) 2025 thatguysudsy

🐍 Author
thatguysudsy
Student • Coder • Gamer
🧩 Loves experiments like this one — turning math and probability into code.

📚 References
Infinite Monkey Theorem — Wikipedia

Geometric Distribution — Wikipedia

yaml
Copy code
