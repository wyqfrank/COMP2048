

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def oracle(circuit, function_type):
    if function_type == "constant":
        # For a constant function, do nothing or apply X gate both times (0 -> 0, 1 -> 1)
        pass  # This will implement f(x) = 0 regardless of input
        # circuit.x(1)  # Uncomment this to switch to f(x) = 1
    elif function_type == "balanced":
        # For a balanced function, flip the ancilla bit only when the input is 1
        # This creates a mapping f(0) = 0, f(1) = 1 or vice versa
        circuit.cx(0, 1)  # CNOT gate, flips the target if the control (qubit 0) is |1>

# Setup a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Prepare the ancilla qubit in the state |1>
qc.x(1)  # NOT gate to flip |0> to |1>

# Apply Hadamard gates
qc.h(0)  # Hadamard on the input qubit
qc.h(1)  # Hadamard on the ancilla qubit

# Apply the oracle
oracle(qc, "balanced")  # Change to "constant" to test constant functions

# Apply Hadamard to the input qubit
qc.h(0)

# Initialize the statevector simulation
state = Statevector.from_label('00')

# Evolve the statevector through the circuit
final_state = state.evolve(qc)

# Get the probabilities of the outcomes
probabilities = final_state.probabilities_dict()

# Print the final probabilities
print("Probabilities of outcomes:", probabilities)

# To infer the function type:
if probabilities.get('00', 0) > 0.5:
    print("The function is constant.")
else:
    print("The function is balanced.")
