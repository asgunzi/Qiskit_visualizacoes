# Qiskit_visualizacoes
Alguns modos diferentes de visualização de estados no Qiskit

O Qiskit permite algumas visualizações diferentes do circuito quântico.

Vejamos três delas: o simulador, o vetor de estados, e o unitário.

Para tal, vou utilizar o mesmo circuito mais básico possível do tutorial anterior: apenas uma porta Hadamard.

`from qiskit import *`
`circuit = QuantumCircuit(1,1)`
`circuit.h(0)`
`circuit.measure(0,0)`


![](https://informacaoquantica.files.wordpress.com/2020/04/hadamard.png)


1) O primeiro modo de visualização é o simulador de circuito quântico. Defino o backend como ‘qasm_simulator’ (quantum assembly simulator). Mando rodar e capturar o resultado.

`simulator1 = Aer.get_backend('qasm_simulator')
result1  = execute(circuit, backend=simulator1, shots=512).result()
print(result1.get_counts(circuit))`

Resultado: o número de vezes que o circuito mediu ‘0’ e ‘1’. Deve somar 512, número de simulações definidas com o parâmetro ‘shots’. A probabilidade de cada um deve ser em torno de 50%, pela porta Hadamard ser um autêntico gerador de números aleatórios.

`{'0': 264, '1': 248}`

2 ) O segundo modo de visualização é o state vector simulator.

É o estado final do qubit, na forma vetorial.

É muito semelhante, bastando mudar o backend para ‘statevector_simulator’ e o resultado para ‘get_statevector()’.

Um detalhe importante. Comentar a linha do circuit.measure(). Porque, se o circuito estiver medindo, o statevector colapsa para |0> ou |1>, e queremos o valor antes disso.

`#Se Utilizar o state vector e o simulador unitário, comentar a linha da medida
#circuit.measure(0,0)`

`simulator2 = Aer.get_backend('statevector_simulator')
result2  = execute(circuit, backend=simulator2).result()
print(result2.get_statevector())`

Resultado:

`[0.70710678+0.j 0.70710678+0.j]`

Ou seja, [1 1]/sqrt(2).

\frac{\begin{pmatrix}1 & 1\end{pmatrix}}{\sqrt(2)}

É o resultado de passar [1 0] pela porta Hadamard [[1 1][1 -1]]/sqrt(2).

\frac{\begin{pmatrix}1 & 1 \\ 1 & -1 \end{pmatrix}}{\sqrt(2)}

Neste circuito simples, dá para deduzir facilmente, porém em casos mais complicados, ou para checar resultados teóricos, é bastante útil.

3 ) O terceiro modo é o do simulador unitário.

É o estado do circuito, na forma matricial. Aqui, refere-se ao circuito, e o item acima, ao qubit. Ou seja, se pegar o qubit inicial e multiplicar pela matriz descrita aqui, chega-se ao resultado do item 2.

Novamente, o circuit.measure() deve estar desativado – senão, colapsa a função de onda.

`#circuit.measure(0,0)
simulator3 = Aer.get_backend('unitary_simulator')
result3  = execute(circuit, backend=simulator3).result()
print(result3.get_unitary())`

Resultado:

`[[ 0.70710678+0.00000000e+00j  0.70710678-8.65956056e-17j]
 [ 0.70710678+0.00000000e+00j -0.70710678+8.65956056e-17j]]`

Ou seja, [[1 1][1 -1]]/sqrt(2), exatamente a porta Hadamard.

\frac{\begin{pmatrix}1 & 1 \\ 1 & -1 \end{pmatrix}}{\sqrt(2)}

