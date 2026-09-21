from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.quantum_info import Statevector


q = QuantumRegister(2)  # qubits, |0> |0> o |00>
c = ClassicalRegister(2)  # bits normales

circuit = QuantumCircuit(q, c)  # circuito

circuit.h(q[0]) 
circuit.cx(q[0], q[1])
circuit.x(q[1])

print (circuit.draw())  # dibuja el circuito
print (circuit)  # dibuja el circuito
print (circuit.decompose())  # descompone el circuito
print(Statevector.from_instruction(circuit))