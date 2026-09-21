from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

q = QuantumRegister(2)  # qubits, |0> |0> o |00>
c = ClassicalRegister(2)  # bits normales

circuit = QuantumCircuit(q, c)  # circuito

circuit.h(q[0])  # aprimer quibit a |+>
circuit .x(q[1])  # segundo qubit a |1>
circuit.h(q[1])  # segundo qubit a |-> ahora |+->

# Ahora kickback
# Con CNOT la fase negatica de q1 pasa a q0
circuit.cx(q[0], q[1]) 

circuit.h(q[0])  # aplicamos hadamard al primer qubit de control