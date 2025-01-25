wordgame.py (c) Kingsley Ezenwaka, k3z3nw4k4@gmail.com

2025.01.24

# "Guess The Word" Game - A Beginner-level Python Project

## Introduction

The project idea is borrowed directly from the [dataquest.io beginner Python projects page](https://www.dataquest.io/projects/guided-project-a-word-raider/). The page also provides guided instructions to aid completing the project. However, the actual code here is completely mine.

The project itself is quite simple and straightforward: **Build a simple 1-player word guessing game where the word to be guessed is a 5-letter word**.

## Game Play

The game proceeds in this fashion:

1. The program randomly picks a word (called the "target word") from a list of 5-letter words imported from a "words.txt" file. This file is saved in the same folder as the game source code.
2. The player is asked to guess this target word; the player gets 7 chances to guess the correct word.
3. After each guess (called a "turn"), the game checks each letter in the player's guessed word and the player is shown which letters they have guessed correctly (including whether they are in the right position or misplaced) and which letters are completely wrong (i.e. letters which are not in the target word at all). This is repeated at each guessing turn, and the info shown to the player is updated each time.
4. If the player succeeds in guessing the correct word on or before the 7th turn, they win the game; otherwise, they lose the game and are then shown the target word. Then the game ends.