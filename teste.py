def criar_carro(marca, modelo, ano, cor):
    carro = {
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Cor":cor
    }
    return carro

def adicionar_carros(lista_carros, dicionario_carros):
    lista_carros.append(dicionario_carros)
    return lista_carros
    
carros = []
carro1 = criar_carro("Fiat", "Uno", "2010", "Preto")
carro2 = criar_carro("Fiat", "Toro", "2017", "Amarelo")
carro3 = criar_carro("Fiat", "Strada", "2005", "Verde")


adicionar_carros(carros,carro1)
adicionar_carros(carros,carro2)
adicionar_carros(carros,carro3)

def remover_carro_modelo(lista_carros, modelo):
    for carro in lista_carros:
        if carro["Modelo"] == modelo:
            lista_carros.remove(carro)
    return lista_carros

def remover_carro (modelo):    
    for i, carro in enumerate(carros):
        if (carro["Modelo"] == modelo ):
            del carros[i]
            return "Carro excluido!"
    return "Carro nao esta na lista"

#print(remover_carro_modelo(carros,"Uno"))

#modelo_remover = input("Digite o modelo que deseja remover: ")
#print(remover_carro (modelo_remover))
#print(carros)

def ordenar_carros_por_ano(lista):
    lista_ordenada = sorted(lista, key=lambda x:x["Ano"])
    return lista_ordenada

#print(ordenar_carros_por_ano(carros))


def ordenar_carros_por_ano(lista):
    lista_ordenada = sorted(lista, key=lambda x:x["Ano"],reverse=True)
    return lista_ordenada

#print(ordenar_carros_por_ano(carros))

def atualizar_cor_carro (carros, modelo, cor):
    for carro in carros:
        if carro["Modelo"] == modelo:
            carro["Cor"] = cor
    return carros

#modelo_carro = input("Digite o modelo do carro: ")
#trocar_cor = input("Digite a cor que quer mudar: ")

#print(atualizar_cor_carro(carros,modelo_carro,trocar_cor))
def ordenar_carros_por_ano_bubble(lista):
    quant_trocas = 0 
    quant_compa = 0 
    
    for index in range(len(lista)):
        for x in range(0, len(lista) - index - 1):
            quant_compa += 1
            if(lista[x]["Ano"] > lista[x + 1]["Ano"]):            
                lista[x],lista[x + 1] = lista[x + 1], lista[x]
                quant_trocas += 1
    
    print(f"Houve {quant_trocas} trocas")
    print(f"Houve {quant_compa} comparações")
    print()
    return lista
                
print(ordenar_carros_por_ano_bubble(carros))

