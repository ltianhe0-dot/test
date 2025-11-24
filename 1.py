import numpy as np
import matplotlib.pyplot as plt

# Plot circles for sample values of a and b
fig = plt.figure(figsize=(6,6))

# Example values
a_values = [ -1, 0.5, 2 ]
b_values = [ 0.5, 2 ]

theta = np.linspace(0, 2*np.pi, 400)

for a in a_values:
    c = (a*a - 1)/(a*a + 1)
    r = 2*abs(a)/(a*a + 1)
    x = c + r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x, y, label=f"x={a}")

for b in b_values:
    c = (b-1)/(b+1)
    r = 2*np.sqrt(b)/(b+1)
    x = c + r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x, y, linestyle='--', label=f"y={b}")

plt.gca().set_aspect('equal')
plt.title("Images of x=a and y=b under w=(z-i)/(1-iz)")
plt.legend()
plt.grid(True)

plt.show()
