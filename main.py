"""One-Sentence Absurd Invention Pitch — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one sentence pitching a ridiculous invention that fixes a tiny everyday annoyance, at most 220 characters.
"""
import os

LINE = "Introducing the self-apologising alarm clock: it wakes you up, says sorry for doing it, then snoozes itself out of guilt."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
