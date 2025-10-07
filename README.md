````markdown
# 🐒 Random Sentence Generator — Inspired by the Infinite Monkey Theorem

A Python experiment that simulates the **Infinite Monkey Theorem** — the idea that, given enough time, a monkey hitting random keys could eventually type any text, like “hello world.”

This program randomly types characters (`a–z`, space, `.`), ending each sentence when a period appears, until one of those sentences matches your chosen message. It then prints how many characters and sentences it took, how long the process lasted, and now features a **quiet mode** for faster performance.

---

## ✨ Example

```text
Turn quiet mode on? (Doesn't print into console) Answer y/n  y
What is your message? hi
Message received after 1128 characters (53 sentences)
Took 0 minute(s) 1.23 second(s)
````

---

## 🧠 How it Works

* The program picks from **28 characters**:
  `a–z`, space, and `.`
* Every time it picks `.`, it **ends a sentence** and checks if the sentence equals your target.
* If it matches — success!
* Otherwise, it resets and keeps typing.

This is a finite, practical version of the **Infinite Monkey Theorem** — except here, the “monkey” is a short Python script.

---

## 🧩 Quiet Mode

**Quiet mode** skips printing every random sentence to the console, which makes the program **much faster**. Printing is one of the slowest parts of the process, especially on Windows.

When you start the program, it asks:

```text
Turn quiet mode on? (Doesn't print into console) Answer y/n
```

* Type `y` for **quiet mode** (recommended for long targets).
* Type `n` to print every generated sentence (fun for small words like `hi` or `cat`).

Typical speed improvement: **50×–100× faster**.

---

## 📊 Probability Background

For a target of length **L**, the chance of success for one sentence is:

```
p = (1/28)^(L+1)
```

Expected number of sentences before success ≈ **28^(L+1)**
That means longer words grow *exponentially* harder:

| Target        |      Expected Sentences | Average Time (Quiet Mode, i5-12400F) |
| :------------ | ----------------------: | -----------------------------------: |
| `a`           |                     784 |                              < 1 sec |
| `hi`          |                  21,952 |                              < 1 sec |
| `cat`         |                 614,656 |                               ~8 sec |
| `game`        |              17,210,368 |                             ~3–4 min |
| `hello`       |             481,890,304 |                         ~1 hr 40 min |
| `hello world` | 232,218,265,089,212,416 |                     ~91,000 years 😅 |

> *Times assume quiet mode on an Intel i5-12400F desktop.*

---

## 🚀 How to Run

1. Make sure you have Python 3.8+ installed.
2. Clone or download this repo:

   ```bash
   git clone https://github.com/thatguysudsy/random-sentence-generator.git
   cd random-sentence-generator
   ```
3. Run the script:

   ```bash
   python main.py
   ```
4. When prompted, choose quiet mode (`y` or `n`), then enter your target message (letters, space, or period).

---

## 🧩 Features

* **Quiet Mode** for high-speed runs
* Simple command-line interface
* Tracks total characters, sentences, and elapsed time
* Based on the Infinite Monkey Theorem
* Works on Windows, macOS, and Linux

---

## ⚖️ License

Licensed under the **MIT License**
Copyright (c) 2025 **thatguysudsy**

---

## 🐍 Author

**thatguysudsy**
Coder • Gamer
🧩 Loves experiments like this one — turning math and probability into code.

---

## 📚 References

* [Infinite Monkey Theorem — Wikipedia](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)
* [Geometric Distribution — Wikipedia](https://en.wikipedia.org/wiki/Geometric_distribution)

```
```
