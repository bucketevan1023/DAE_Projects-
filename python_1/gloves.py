import random

welcoming_msg = "Welcome to my program"
print(welcoming_msg)

# Correcting the guess_the_number assignment
guess_the_number = random.randint(61, 100000)  # Random number between 61 and 100,000
print(guess_the_number)  

Dogs_Vs_cats = 100 + 100 - 110 - 100
print(Dogs_Vs_cats)

random_float_value = 1.0 + 6.7 - 8.0
print(random_float_value)

B_value = True   
print(B_value)

colors = ['red', 'blue', 'green', 'indigo', 'purple']   
print(colors[3])  # Printing 'indigo'

for color in colors:
    print(color)

class Boxer:
    def __init__(self, name, speed, power, stamina, defense):
        self.name = name
        self.speed = speed
        self.power = power
        self.stamina = stamina
        self.defense = defense

    def evaluate_opponent(self, opponent):
        """Evaluate the opponent's strengths and weaknesses."""
        evaluation = {
            'speed': opponent.speed,
            'power': opponent.power,
            'stamina': opponent.stamina,
            'defense': opponent.defense
        }
        return evaluation

    def choose_strategy(self, opponent_evaluation):
        """Choose a strategy based on opponent's attributes."""
        if opponent_evaluation['power'] > self.power and opponent_evaluation['defense'] > self.defense:
            return "Defensive"
        elif opponent_evaluation['speed'] > self.speed:
            return "Counter-Attack"
        elif self.power > opponent_evaluation['defense']:
            return "Aggressive"
        else:
            return "Balanced"

    def make_decision(self, opponent):
        """Make a decision based on opponent evaluation."""
        opponent_eval = self.evaluate_opponent(opponent)
        strategy = self.choose_strategy(opponent_eval)
        return f"{self.name} should adopt a '{strategy}' strategy against {opponent.name}."


def boxing_match(boxer1, boxer2):
    """Simulate a boxing match decision-making process."""
    print(boxer1.make_decision(boxer2))
    print(boxer2.make_decision(boxer1))


# Example usage
if __name__ == "__main__":
    boxer1 = Boxer(name="Boxer A", speed=8, power=7, stamina=6, defense=5)
    boxer2 = Boxer(name="Boxer B", speed=6, power=9, stamina=7, defense=6)

    # Simulate a boxing match decision-making process
    boxing_match(boxer1, boxer2)

# A simple loop that prints numbers from 1 to 5
for number in range(1, 6):  # range(start, stop) goes from start to stop - 1
    print(number)

import random

class Boxer:
    def __init__(self, name):
        self.name = name
        self.strength = 5
        self.speed = 5
        self.stamina = 5
        self.level = 1

    def train(self):
        print("\nTraining options:\n1. Strength\n2. Speed\n3. Stamina")
        choice = input("Choose a stat to train (1/2/3): ")
        if choice == "1":
            self.strength += random.randint(1, 3)
            print(f"{self.name}'s strength increased to {self.strength}!")
        elif choice == "2":
            self.speed += random.randint(1, 3)
            print(f"{self.name}'s speed increased to {self.speed}!")
        elif choice == "3":
            self.stamina += random.randint(1, 3)
            print(f"{self.name}'s stamina increased to {self.stamina}!")
        else:
            print("Invalid choice. Training session wasted.")

    def stats(self):
        print(f"\n{self.name}'s Stats:\nStrength: {self.strength}\nSpeed: {self.speed}\nStamina: {self.stamina}\nLevel: {self.level}")

    def can_fight(self, opponent):
        return self.strength >= opponent['strength'] and self.speed >= opponent['speed'] and self.stamina >= opponent['stamina']

# Opponent requirements
opponent = {
    "name": "Iron Fist",
    "strength": 15,
    "speed": 12,
    "stamina": 14
}

def main():
    print("Welcome to the Boxing Simulator!")
    username = input("Enter your boxer's name: ")
    player = Boxer(username)

    while True:
        print("\nMenu:\n1. View Stats\n2. Train\n3. Fight Opponent\n4. Exit")
        choice = input("Choose an action (1/2/3/4): ")

        if choice == "1":
            player.stats()
        elif choice == "2":
            player.train()
        elif choice == "3":
            print(f"\nOpponent: {opponent['name']}\nStrength: {opponent['strength']}\nSpeed: {opponent['speed']}\nStamina: {opponent['stamina']}")
            if player.can_fight(opponent):
                print(f"\nCongratulations! {player.name} defeated {opponent['name']}!")
                break
            else:
                print(f"\n{player.name} is not ready to fight {opponent['name']} yet. Keep training!")
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main
