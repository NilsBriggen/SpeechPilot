import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x)
def f(x):
    return 3 * np.sin(x * np.pi / 2)

# Generate x values
x_values = np.linspace(0, 8, 500)

# Generate y values based on f(x)
y_values = f(x_values)

# Plot the function f(x)
plt.plot(x_values, y_values, label='Analoges Signal', color='red')

# Create bar graph
bar_x1 = np.arange(0, 4, 0.1)  # Step length 0.5 for 0 <= x < 3
plt.bar(bar_x1, f(bar_x1), width=0.08, alpha=1, label='Hohe Abtastrate', color='blue')
bar_x2 = np.arange(4, 8, 0.2)  # Step length 1 for 3 <= x <= 6
plt.bar(bar_x2, f(bar_x2), width=0.17, alpha=1, label='Niedrige Abtastrate', color='orange')

# Add labels and title
plt.xlabel('[t] Zeit')
plt.ylabel('[A] Amplitude]')
plt.title('Graph einer analogen Sinusfunktion (3*sin(x*pi/2)))')
plt.legend()
plt.grid()

# Show the plot
plt.show()
