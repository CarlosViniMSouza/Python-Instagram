import numpy as np

# Create 2 Matrix's:

m1 = np.array([[2, 5], [-4, 3]])
m2 = np.array([[1, -3], [2, -6]])

#1 - Method add() for add matrices:
print("Matrix Final: \n", np.array.add(m1, m2))

#2 - Method subtract() for subtract matrices:
print("Matrix Final: \n", np.array.subtract(m1, m2))

# 3 - Method multiply() for multiply matrices:
print("Matrix Final: \n", np.array.multiply(m1, m2))

# 4 - Method divide() for divide matrices:
print("Matrix Final: \n", np.array.divide(m1, m2))
