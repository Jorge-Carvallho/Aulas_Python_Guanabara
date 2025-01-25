#Modularização --> dividir um programa grande / aumentar a legibilidade / facilitarta manutenção

def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3



num = int(input('Digite um número: '))   
fat=fatorial(num)
print(f'O fatorial de {num} é {fat}')

# Vantagem --> 
# -organização do código
# -Facilidade na manutenção
# -Ocutação de código detalhado
# -Reutilização em outros projetos

#Pacotes --> sao diretorios contendo um arquivo especial chamado __init__.py que pode conter outros modulos e subpacotes