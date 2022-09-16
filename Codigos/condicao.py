
nota_aluno = input("Informe a nota: ")
nota_aluno = float(nota_aluno)


if nota_aluno >= 9 and nota_aluno <= 10: 
    print("Parabéns Voce tem o conceito máximo... A+")
elif nota_aluno >= 7 and nota_aluno <= 8.9: 
    print("Parabéns. Conceito A")
elif nota_aluno >= 6 and nota_aluno <= 6.9: 
    print("Passaou, mas deve estudar mais. Conceito B")
elif nota_aluno >= 4 and nota_aluno <= 5.9: 
    print("Recuperacao. Conceito C")
elif nota_aluno >= 0 and nota_aluno <= 3.9: 
    print("Reprovado. Conceito D")
else:
    print("O número que você digitou não esta no intervalo de notas de 0 a 10... Por favor digite uma nota valida.")


