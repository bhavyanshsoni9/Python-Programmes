import random
import time

class Player:
    def __init__(self):
        answers = [
            "a keyboard",
            "a candle",
            "a secret"
        ]

        questions = [
            "which thing has keys but no locks, space but you can't fit and enter but you can't go in?",
            "I am young when i am tall but i am old when i am short. Who am i?",
            "Which thing brokes when you tell it?"
        ]

        options = [
            "a house", "a lock", "a keyboard",
            "a mountain", "a candle", "a building",
            "a secret", "a promise", "a glass"
        ]
        
        hp = 100
        food = 0
        weapon = 0
        attack_damage = 0
        monster_hp = 100
        monster_attack_damage = 30
        def Level_1():
            print(f"{questions[0]}\n")
            time.sleep(1)
            print(f"(a) {options[0]}\t(b) {options[1]}\t(c) {options[2]}")
            time.sleep(1)
            answer = input("Type the Answer: ")
            if answer.lower() == answers[0]:
                print("Wow! Correct Answer\n")
                time.sleep(1)
                print("Now You have 20 Bread which increase 5 health\n")
                food = 20
                time.sleep(1)
                print("A sword which deals 20 damage\n")
                weapon = 1
                attack_damage = 20

                print("Time for the First Monster ☠\n")
                time.sleep(2)
                print("Here It Comes ☠ !")

                while monster_hp == 100:
                    
            else:
                print("Wrong Answer...")
                time.sleep(1)

        