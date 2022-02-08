# Import pyQuil modules
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce

# Create a connection to tge Quantum Virtual Machine (QWM)
qwm = QVMConnection()

# Apply the Haramard gate to three qubits to generate 8 possible randomized result
dice = Program(H(0), H(1), H(2))

# 8 possible results: [[0,0,0], [0,0,1], [0,1,1], [1,1,1], [1,0,0], [0,1,0], [0,0,1]]
# Measure the qubits to get a result, i.e. roll the dice
roll_dice = dice.measure_all()

# Execute the program by runnin it with the QWM
result = qvm.run(roll_dice)

# Example results: [[1,0,1]]
# Format and print the result as a dice value between 1 and 8
dice_value = reduce(lambda x, y: 2*x + y, result [0], 0) +1
print ("Your quantum dice roll returned:", dice_value)
