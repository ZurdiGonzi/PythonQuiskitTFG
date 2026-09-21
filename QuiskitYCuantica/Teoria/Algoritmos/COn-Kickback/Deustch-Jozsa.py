from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

n = 3

circuit = QuantumCircuit(n + 1 , n)  # circuito
circuit.x(n)
