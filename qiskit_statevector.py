# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 06:00:42 2020

@author: asgun
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:12:36 2020

@author: asgun
"""

from qiskit import *


circuit = QuantumCircuit(1,1)

circuit.h(0)

#Se Utilizar o state vector e o simulador unitário, comentar a linha da medida
#circuit.measure(0,0)

print(circuit)


#simulator1 = Aer.get_backend('qasm_simulator')
#simulator2 = Aer.get_backend('statevector_simulator')
simulator3 = Aer.get_backend('unitary_simulator')

#result1  = execute(circuit, backend=simulator1, shots=512).result()
#result2  = execute(circuit, backend=simulator2).result()
result3  = execute(circuit, backend=simulator3).result()

#print(result1.get_counts(circuit))
#print(result2.get_statevector())
print(result3.get_unitary())
