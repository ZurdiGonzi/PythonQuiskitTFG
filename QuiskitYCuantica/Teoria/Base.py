
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

q = QuantumRegister(2)  # qubits, |0> |0> o |00>
c = ClassicalRegister(2)  # bits normales

circuit = QuantumCircuit(q, c)  # circuito

# inicio |00> o {1000} 100% 00
circuit.h(q[0])  # aplica hadamard al qubit 0
# ahora |+0> 50% |00> 50% |10>

# estado |00> + |10> /sqrt(2)

circuit.cx(q[0], q[1])  # aplica cnot al qubit 0 y 1
# cx|00> + cx|10>/sqrt(2) = |00> + |11> /sqrt(2)

# estado |00> + |11> /sqrt(2)

circuit.measure(q, c)  # medimos los qubits y los guardamos en los bits
# P(00) = 50% P(11) = 50%
# P(11) = 50% P(00) = 50%
print (circuit.draw())  # dibuja el circuito
print (circuit)  # dibuja el circuito
print (circuit.decompose())  # descompone el circuito
print (circuit.decompose().draw())  # dibuja el circuito descompuesto
print(c)
