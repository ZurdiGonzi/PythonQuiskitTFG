from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

entradas = [
    "000",
    "001",
    "010",
    "011",
    "100",
    "101",
    "110",
    "111"
]

n = len(entradas[0]) 
# Hay n qubits de entrada y un qubit auxiliar para el oráculo.
q = QuantumRegister(n + 1, "q")

# Este registro almacena el resultado de la medición final de las entradas.
c = ClassicalRegister(n, "c")
circuit = QuantumCircuit(q, c)

circuit.x(q[n]) # Auxiliar en |1>

for i in range(n):
    circuit.h(q[i]) 

circuit.h(q[n])
#Oraculo
for i in range(n):
    circuit.cx(q[i], q[n]) #XOR xi con auxiliar
for i in range(n):
    circuit.h(q[i]) #Volvemos a aplicar hadamard a la entrada

# Medimos los qubits de entrada y guardamos el resultado en los bits clásicos.


# draw() devuelve el circuito dibujado como texto.
print(circuit.draw())
    
