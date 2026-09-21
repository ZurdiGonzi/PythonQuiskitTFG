from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# qubit       registro clasico    circuito

key = 11
n = len(key)
# Hay n qubits de entrada y un qubit auxiliar para el oráculo.
q = QuantumRegister(n * 2, "q")

# Este registro almacena el resultado de la medición final de las entradas.
c = ClassicalRegister(n, "c")
circuit = QuantumCircuit(q, c)

for i in range(n):
    circuit.h(q[i]) 

reverse_key = key[::-1]

for i in range(n):
    circuit.cx(q[i], q[n + i]) #XOR xi con auxiliar
if '1' in reverse_key:
        m = reverse_key.find('1') # Encontramos el índice del primer '1'
        
        # Usamos el qubit de entrada 'm' para sobrescribir las salidas
        # de forma que f(x) colisione exactamente con f(x XOR s)
        for i in range(n):
            if reverse_key[i] == '1':
                circuit.cx(m, n + i)
for i in range(n):
    circuit.h(q[i]) #Volvemos a aplicar hadamard a la entrada
for i in range(n):
        circuit.measure(i, i)
