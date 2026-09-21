from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

n = 2
# Hay n qubits de entrada y un qubit auxiliar para el oráculo.
q = QuantumRegister(n, "q")

# Este registro almacena el resultado de la medición final de las entradas.
c = ClassicalRegister(n, "c")
circuit = QuantumCircuit(q, c)

for i in range(n):
    circuit.h(q[i])

circuit.cz(0,1) # marca el elemento que buscamos, el 11
                # multiplica por -1 si ambos son 1
for i in range(n):
    circuit.h(q[i]) #Volvemos a aplicar hadamard a la entrada
for i in range(n):
    circuit.x(i)
circuit.cz(0,1) # marca el elemento que buscamos, el 00
for i in range(n):
    circuit.x(i)    
for i in range(n):
    circuit.h(q[i]) #Volvemos a aplicar hadamard a la entrada
for i in range(n):
    circuit.measure(i, i)
