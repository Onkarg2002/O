# AND Gate perceptron
import numpy as np
import matplotlib.pyplot as plt

# Define the perceptron function
def perceptron(x, w, b):
    y = np.dot(x, w) + b
    if y > 0:
        return 1
    else:
        return 0

# Defining the input data
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Defining weights and bias
w = np.array([1, 1])
b = -1.5

# Computing the output for each input
y = np.array([perceptron(i, w, b) for i in x])

# Plotting the data
plt.scatter(x[:, 0], x[:, 1], c=y)

# Plotting the boundary line
x1 = np.linspace(-0.5, 1.5, 2)
x2 = -(w[0]/w[1])*x1 - b/w[1]
plt.plot(x1, x2, 'r')
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.title('AND Gate',fontweight='bold')
plt.show()
--------------------------------------------------------------------------------
# OR gate perceptron
import numpy as np
import matplotlib.pyplot as plt

# Defining the perceptron function
def perceptron(x, w, b):
    y = np.dot(x, w) + b
    if y > 0:
        return 1
    else:
        return 0

# Defining input data
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

w = np.array([1, 1])
b = -0.5

# Computing output for each input
y = np.array([perceptron(i, w, b) for i in x])

# Plotting the data
plt.scatter(x[:, 0], x[:, 1], c=y)

# Plotting the boundary line
x1 = np.linspace(-0.5, 1.5, 2)
x2 = -(w[0]/w[1])*x1 - b/w[1]
plt.plot(x1, x2, 'r')
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.title('OR Gate',fontweight='bold')
plt.show()
---------------------------------------------------
# XOR gate perceptron
import numpy as np
import matplotlib.pyplot as plt

# Defining the perceptron function
def perceptron(x, w, b):
    y = np.dot(x, w) + b
    if y > 0:
        return 1
    else:
        return 0

# Defining input data
x = np.array([[0,0], [0,1], [1,0], [1,1]])

w = np.array([1, 1])
b = -0.5

# Computing output for each input
y = np.array([0, 1, 1, 0])

# Plotting the data
plt.scatter(x[:, 0], x[:, 1], c=y)

# Plotting the boundary line
x1 = np.linspace(-0.5, 1.5, 2)
x2 = -(w[0]/w[1])*x1 - b/w[1]
plt.scatter(x[:,0], x[:,1], c=y)
plt.plot(x1, x2, 'r')
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.title('XOR Gate',fontweight='bold')
plt.show()
