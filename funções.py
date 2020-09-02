import datetime
from datetime import date

def volume_esfera(raio):
    pi=3.14
    vol=(4/3*pi*raio**3)
    print("\nO volume da esfera é:", "{:.2f}".format(vol),"cm³\n")

def n_primo(n):                 #para cada i no range a função vai verificar se o valor i é divisor(mut) de n(valor input) através da operação resto(%)
    mut=0                       #Um numero primo só é divisor dele próprio, ou seja, n(fora do range) e de 1(fora do range), se ele tiver 1 ou mais divisores não é primo
    for i in range(2, n):
        if (n % i == 0):
            mut += 1
    if(mut==0):
        return True
    else:
        return False

def tempo_vida(dia, mes, ano):
    data = datetime.date(ano, mes, dia)
    data2 = date.today()
    data3 = data2 - data
    print(f"\nSua idade equivale a {data3.days} dias\n")

def val_perfeito(m):            #para cada u no range a função vai verificar se o valor u é divisor de m(valor input) através da operação resto(%)
    s=0                         #um numero é perfeito qunado a soma de seus divisores é igual ao próprio numero, portanto encontrando os divisores com a função resto podemos soma-los e armazenar o valor na variavel s(soma), se for igual ao m(input), então o numero é perfeito
    for u in range(1, m):
        if (m % u == 0):
            s += u
    if s == m:
        return True
    else:
        return False

while True:

    x=int(input("\nBem vindo!!\nEscolha uma das opções:\n1.Volume da esfera\n2.Numero primo\n3.Tempo de vida\n4.Numero perfeito\n5.Sair do programa\n\n"))

    if x==1:
        print("\nVamos calcular o volume de uma esfera\n")
        raio = int(input("\nDigite o raio da esfera: \n\n"))
        volume_esfera(raio)
    elif x==2:
        print("\nVamos verificar se um numero é primo ou não\n")
        n = int(input("\nDigite o um numero inteiro e positivo: \n\n"))
        n_primo(n)
        o = n_primo(n)
        if o == True:
            print(f"\nO numero {n} é primo\n")
        else:
            print(f"\nO numero {n} não é primo\n")
    elif x==3:
        print("\nVamos calcular sua idade em dias\n")
        dia = int(input("\nDigite o dia do seu nascimento: \n\n"))
        mes = int(input("\nDigite o mês do seu nascimento: \n\n"))
        ano = int(input("\nDigite o ano do seu nascimento: \n\n"))
        tempo_vida(dia, mes, ano)
    elif x==4:
        print("\nVamos verificar se um numero é perfeito ou não\n")
        m = int(input("\nDigite um numero: \n\n"))
        val_perfeito(m)
        p=val_perfeito(m)
        if p == True:
            print(f"\nO numero {m} é perfeito\n")
        else:
            print(f"\nO numero {m} não é perfeito\n")
    elif x==5:
        print("\nObrigado!!\nAté a próxima!!\n\n")
        break
    else:
        print("\nOpção invalida!!\n\n")