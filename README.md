# Desafio Hard Python Infinity School
1° lugar no desafio da trilha hard

TRILHA HARD

O professor de uma turma de programação passou um projeto para seus alunos realizarem em grupo. Cada grupo pode ter, no máximo, 3 integrantes.
Os alunos foram informados que poderiam ficar à vontade para montar suas equipes, mas teriam que informar ao professor, na aula seguinte, os integrantes de cada grupo.
Como os alunos estão estudando estrutura de dados, eles decidiram informar a definição das equipes de uma forma diferente. Combinaram de passar uma lista ao professor, em que cada linha contém um par de nomes, X e Y, representando que o estudante X está no mesmo grupo do estudante Y.
Os alunos afirmaram que, com base nessa lista, é possível saber quais são os grupos, quantas pessoas estão em cada grupo, e quantos grupos foram formados. Como o professor estava com muitas outras atividades, ele acabou passando essa missão para você. Você vai precisar criar um código que receba essa lista com os pares de alunos e, com base nela, deverá informar apenas o número de grupos formados e quantos grupos são inválidos, ou seja, quais têm mais do que 3 integrantes.

Entrada

A entrada será formada por uma matriz, em que cada linha será um array com dois elementos, X e Y, que são os nomes dos estudantes que estão no mesmo grupo.

Saída

A saída deverá ser um array com dois valores, A e B, sendo A o total de grupos formados, e B o número de grupos inválidos.

Exemplos:

Exemplo 01

Se a entrada for composta pela matriz abaixo, a saída deve ser [2, 0].

[
  ["jose", "maria"],
  ["luiza", "andre"],
]

Exemplo 02

Se a entrada for composta pela matriz abaixo, a saída deve ser [3, 1].

[
 ['jose', 'maria'],
  ['jose', 'andre'],
  ['jose', 'barbara'],
  ['maria', 'andre'],
  ['andre', 'barbara'],
  ['andressa', 'luiza'],
  ['luiza', 'gabriel'],
  ['leandro', 'victor'],
  ['victor', 'john'],
  ['john', 'leandro'], 
]
