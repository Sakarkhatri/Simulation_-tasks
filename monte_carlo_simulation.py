import random
import matplotlib.pyplot as plt

def draw_balls(num_red, num_blue, num_draws):
    urn = ['red'] * num_red + ['blue'] * num_blue
    return [random.choice(urn) for _ in range(num_draws)]

def monte_carlo_simulation(num_red, num_blue, num_draws, num_simulations):
    same_color_count = 0
    
    for _ in range(num_simulations):
        drawn_balls = draw_balls(num_red, num_blue, num_draws)
        if all(ball == drawn_balls[0] for ball in drawn_balls):
            same_color_count += 1
    
    return same_color_count / num_simulations

# Set up the simulation parameters
num_red = 3
num_blue = 3
num_draws = 2
num_simulations = 100000

# Run the simulation
probability = monte_carlo_simulation(num_red, num_blue, num_draws, num_simulations)

print(f"Estimated probability of drawing {num_draws} balls of the same color: {probability:.4f}")

# Plot the convergence of the probability estimate
probabilities = []
sim_numbers = []

for i in range(1, num_simulations + 1):
    prob = monte_carlo_simulation(num_red, num_blue, num_draws, i)
    probabilities.append(prob)
    sim_numbers.append(i)

plt.figure(figsize=(10, 6))
plt.plot(sim_numbers, probabilities)
plt.title('Convergence of Probability Estimate')
plt.xlabel('Number of Simulations')
plt.ylabel('Estimated Probability')
plt.xscale('log')
plt.grid(True)
plt.show()