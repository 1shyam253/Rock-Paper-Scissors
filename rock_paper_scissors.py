#!/usr/bin/env python3
"""Rock Paper Scissors - play against the computer."""
import argparse, random
CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def winner(player, computer):
    if player == computer: return "draw"
    return "win" if BEATS[player] == computer else "lose"

def main():
    p = argparse.ArgumentParser(description="Rock Paper Scissors")
    p.add_argument("--choice", choices=CHOICES, help="Your move (non-interactive mode)")
    p.add_argument("--rounds", type=int, default=1)
    args = p.parse_args()
    score = {"win": 0, "lose": 0, "draw": 0}
    for _ in range(args.rounds):
        player = args.choice or input("Rock, paper or scissors? ").strip().lower()
        if player not in CHOICES: print("Invalid choice, try rock, paper or scissors."); continue
        computer = random.choice(CHOICES)
        result = winner(player, computer)
        score[result] += 1
        print(f"You: {player} | Computer: {computer} -> {result}")
    print(f"Score: {score['win']} wins, {score['lose']} losses, {score['draw']} draws")

if __name__ == "__main__":
    main()
