#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    print("You will be playing as Player 1\n")

    def move(self):
        while True:
            human_move = input("rock, paper or scissors?\n").lower()
            if human_move not in moves:
                print("Please check your spelling and try again")
            else:
                break
        return human_move


class ReflectPlayer(Player):
    def __init__(self):
        self.reflect = random.choice(moves)
        self.score = 0

    def move(self):
        return self.reflect

    def learn(self, my_move, their_move):
        self.reflect = their_move
        return self.reflect


class CyclePlayer(Player):
    def __init__(self):
        self.cycle = random.choice(moves)
        self.score = 0

    def learn(self, my_move, their_move):
        self.cycle = my_move
        return self.cycle

    def move(self):
        if self.cycle == "rock":
            return "paper"
        elif self.cycle == "paper":
            return "scissors"
        elif self.cycle == "scissors":
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 wins the round")
        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 wins the round")
        else:
            print("The round is a tie\n")
        print(f"The score is,"
              f"Player 1: {self.p1.score} Player2: {self.p2.score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1.score > self.p2.score:
            print("Player 1 is the winner")
        elif self.p2.score > self.p1.score:
            print("Player 2 is the winner")
        else:
            print("We have a tie")


if __name__ == '__main__':
    players = random.choice([Player(),
                            RandomPlayer(),
                            HumanPlayer(),
                            ReflectPlayer(),
                            CyclePlayer()])
    game = Game(HumanPlayer(), players)
    game.play_game()
