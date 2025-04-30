# import numpy as np
# from qiskit import QuantumCircuit
# from qiskit.quantum_info import Statevector
# from qiskit.visualization import plot_histogram
# import matplotlib.pyplot as plt

# circ = QuantumCircuit(1)

# circ.h(0)

# circ.draw('mpl')

# state = Statevector.from_int(0, 2**3)

# state = state.evolve(circ)

# state.draw('latex')

# print(state)

# state.draw('qsphere')

# print(state.probabilities_dict())

# counts = state.sample_counts(shots=1000)
# print(counts)

# plot_histogram(counts)
# plt.show()

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

num_qubits = 3
qc = QuantumCircuit(num_qubits)

for qubit in range(num_qubits):
    qc.h(qubit)

state = Statevector.from_label('0' * num_qubits)  # Initial state |000>
state = state.evolve(qc)

probabilities = state.probabilities_dict()

decimal_counts = {}
for binary_string, probability in probabilities.items():
    decimal_number = int(binary_string, 2)
    decimal_counts[decimal_number] = round(probability * 1024)  # 1024 shots


print(decimal_counts)

plot_histogram(decimal_counts)
plt.show()

