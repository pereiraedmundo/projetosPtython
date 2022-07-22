print("-------------------------------------------------------------")
print("Jogo Pedra,Papel e Tesoura")
print("-------------------------------------------------------------")

print('Coleta do nome dos jogadores:\n')
nome1 = input('Digite seu nome jogador 1: ')
nome2 = input('Digite seu nome jogador 2: ')
print('-----------------------------------------------------------\n')

print(nome1,'e',nome2,',Prontos para o confronto?\n')
jogada1 = str(input(f'{nome1}, Digite PEDRA,PAPEL ou TESOURA: '))
jogada2 = str(input(f'{nome2}, Digite PEDRA,PAPEL ou TESOURA: '))

print('-----------------------------------------------------------\n')

if jogada1 == 'pedra' and jogada2 =='tesoura':
    print(nome1,'é o/a vencedor(a)')

elif jogada1 == 'tesoura' and jogada2 =='papel':
    print(nome1,'é o/a vencedor(a)')

elif jogada1 == 'papel' and jogada2 =='pedra':
    print(nome1,'é o/a vencedor(a)')

if jogada1 == 'tesoura' and jogada2 =='pedra':
    print(nome2,'é o/a vencedor(a)')

elif jogada1 == 'papel' and jogada2 =='tesoura':
    print(nome2,'é o/a vencedor(a)')

elif jogada1 == 'pedra' and jogada2 =='papel':
    print(nome2,'é o/a vencedor(a)')
else:
    print('Dado inválido ou empate \n')

print('***************FIM DE JOGO ***************')