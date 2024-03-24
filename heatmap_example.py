
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generating a random dataset
data = np.random.rand(10, 12)  # Create a 10x12 array of random numbers

# Creating the heatmap
sns.heatmap(data, cmap='viridis', annot=True)

# Displaying the heatmap
plt.title('Heatmap Example')
plt.show()
