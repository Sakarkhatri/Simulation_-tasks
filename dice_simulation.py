import random
import matplotlib.pyplot as plt

def roll_dice(num_rolls):
    return [random.randint(1, 6) for _ in range(num_rolls)]

def plot_dice_rolls(rolls):
    plt.figure(figsize=(10, 6))
    plt.hist(rolls, bins=range(1, 8), align='left', rwidth=0.8)
    plt.title(f'Distribution of {len(rolls)} Dice Rolls')
    plt.xlabel('Dice Value')
    plt.ylabel('Frequency')
    plt.xticks(range(1, 7))
    plt.grid(axis='y')
    plt.show()

# Simulate dice rolls
num_rolls = 1000
rolls = roll_dice(num_rolls)

# Plot the results
plot_dice_rolls(rolls)

# Calculate and print probabilities
for i in range(1, 7):
    probability = rolls.count(i) / num_rolls
    print(f"Probability of rolling a {i}: {probability:.4f}")