from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister


def inicializar():
	"""Crea el circuito inicial de dos qubits y aplica H al primer qubit."""
	q = QuantumRegister(2)
	c = ClassicalRegister(2)
	circuit = QuantumCircuit(q, c)


	return q, c, circuit
