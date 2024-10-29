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

