import random
import time

class MemoryGame:
    def __init__(self):
        self.colors = {
            "🔴": "red",
            "🔵": "blue",
            "🟢": "green",
            "🟡": "yellow",
            "🟣": "purple",
            "🟤": "brown",
            "⚫": "black"
        }

    def start_game(self):
        print("Welcome to the Memory Game!")
        print("Watch the random colors appear. Try to remember the sequence!")
        sequence = self.generate_sequence()
        self.get_user_input(sequence)

    def generate_sequence(self):
        sequence = []
        try:
            for i in range(5):  # Display 5 colors in sequence
                emoji = random.choice(list(self.colors.keys()))
                sequence.append(emoji)
                print(emoji, flush=True)
                time.sleep(1)  # Show each color for 1 second
                print("\n" * 10)  # Clear the screen
            print("Now, enter the colors in the correct sequence!")
        except KeyboardInterrupt:
            print("\nGame Over. Thanks for playing!")
        return sequence

    def get_user_input(self, sequence):
        try:
            user_input = input("Enter the colors separated by commas (e.g., red, blue, green): ").split(",")
            user_input = [color.strip().lower() for color in user_input]
            expected_sequence = [self.colors[emoji] for emoji in sequence]
            if user_input == expected_sequence:
                print("Congratulations! You remembered the sequence correctly!")
            else:
                print("Oops! The correct sequence was:", ", ".join(expected_sequence))
        except KeyboardInterrupt:
            print("\nGame Over. Thanks for playing!")

if __name__ == "__main__":
    game = MemoryGame()
    game.start_game()