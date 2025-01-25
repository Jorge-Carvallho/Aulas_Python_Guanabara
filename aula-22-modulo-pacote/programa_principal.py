# ####### ex 01
# # import calculo 
# # então adiciono a nome do modulo a frente das funções
# # ex: calculo.fatorial   ----  calculo.triplo etc...



# ###### ex 02   Não é recomendado pois posso ter outra função com mesmo nome e confundir
# # porem a que vale é a última função importada

# # ou posso colocar from calculo import nome_das_funcoes
# from calculo import fatorial, dobro, triplo
# # desta forma não é necess[ario colocar (calculo) a frente de cada função com no exemplo acima 

# # Programa principal

####### ex 03 usando pocotes

from pacote_geral import pacote_numeros

num = int(input('Digite um número: '))
fat = pacote_numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
dob= pacote_numeros.dobro(num)
tri= pacote_numeros.triplo(num)
print(f'O dobro de {num} e {dob}')
print(f'O triplo de {num} é {tri}')

























    #-------------- pertence au arquivo do calculo.py (ou seja é um modulo)---------
# def fatorial(n):
#     f=1
#     for c in range(1,n+1):
#         f*=c 
#     return f

# def dobro(n):
#     return n*2

# def triplo(n):
#     return n*3