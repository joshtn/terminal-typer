# web scrape stories from webbrowserrrr 
# filter away spaces
#     Make sure it starts with a capital letter and end at . instead of newline

import curses
from curses import wrapper
import time
import random

ESC_KEY = 27
BACKSPACE_1 = "KEY_BACKSPACE"
BACKSPACE_2 = "\b"
BACKSPACE_3 = "\x7f"
AVG_WORD_CHARS = 5
ONE_KEY = 49

def start_screen(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome to Terminal Typer!")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2, 0, f"WPM: {wpm}")
    stdscr.addstr(5, 0, "Press 1 to restart")
    stdscr.addstr(6, 0, "Press ESC  to quit")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
           color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text():
    with open("words.txt", "r") as f:
        words = f.readlines()
        word = random.choice(words).strip()
        sentence = []
        for i in range(5):
            sentence.append(random.choice(words).strip())
        return " ".join(sentence)

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / AVG_WORD_CHARS)

        stdscr.erase()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if current_text == []:
            start_time = time.time()

        if ord(key) == ESC_KEY:
            break

        if ord(key) == ONE_KEY:
            main(stdscr)

        if key in (BACKSPACE_1, BACKSPACE_2, BACKSPACE_3):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
                current_text.append(key)





def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "You reached the finish line! Press any key to play again...")
        key = stdscr.getkey()

        if ord(key) == ESC_KEY:
            break


wrapper(main)

