# NOMES:  Ana Paula Duarte e Vitor Hanauer Fontena

import os

lista = []
id = 0


class Produto:

    def __init__(self, codigo, descricao, preco, custo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.custo = custo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setPreco(self, preco):
        if self.preco != 0:
            inferior = self.preco * 0.90
            superior = self.preco * 1.10
            if preco < inferior or preco > superior:
                print("Preço não deve aterar mais e menos que 10%")
                lista[trocar_id].setPreco(float(input("Digite outro valor para preço")))
                return
        self.preco = preco

    def setCusto(self, custo):
        self.custo = custo

    def getCodigo(self):
        return self.codigo

    def getDescricao(self):
        return self.descricao

    def getPreco(self):
        return self.preco

    def getCusto(self):
        return self.custo

    def calculaMargem(self):
        return ((self.preco - self.custo) / self.preco) * 100


def menu():
    os.system('clear')
    opcao = int(
        input(
            "1-Cadastrar produto\n2-Calcular margem\n3-Alterar dados do produto\n4-sair\n"
        )
    )
    os.system('clear')
    return opcao


p1 = Produto(0, 0, 0, 0)
while 1:
    opcao = menu()

    try:
        if opcao == 1:
            codigo = input("Digite o código: ")
            descricao = input("Digite a descrição: ")
            try:
                preco = float(input("Digite o preco: "))
            except:
                print("Apenas números")
                preco = float(input("Digite o preco: "))
            try:
                custo = float(input("Digite o custo: "))
            except:
                print("Apenas números")
                custo = float(input("Digite o custo: "))
            p1 = Produto(codigo, descricao, preco, custo)
            lista.append(p1)
            os.system('clear')

        elif opcao == 2:
            os.system('clear')
            for i in lista:
                print(
                    f'{"codigo":<10}|{"custo":<10}|{"preco":<10}|{"margem":<10}  \n|{i.getCodigo():<10}|{i.getCusto():<10}|{i.getPreco():<10}|{i.calculaMargem():<10}'
                )
            saida = input("Sair?")

        elif opcao == 3:
            os.system('clear')
            for i in lista:
                print(
                    f'{"ID":<10}|{"Descrição":<10}|{"custo":<10}|{"preco":<10} \n{id:<10}|{i.getDescricao():<10}|{i.getCusto():<10}|{i.getPreco():<10}'
                )
                id += 1
            try:
                trocar_id = int(input("Digite o id do produto que deseja trocar?"))
                lista[trocar_id].setDescricao(
                    input("Digite outro valor para descrição:")
                )
                lista[trocar_id].setCusto(float(input("Digite outro valor para custo")))
                lista[trocar_id].setPreco(float(input("Digite outro valor para preço")))
            except:
                valido = print("Digite um valor válido!")
                trocar_id = int(input("Digite o id do produto que deseja trocar?"))
                lista[trocar_id].setDescricao(
                    input("Digite outro valor para descrição:")
                )
                lista[trocar_id].setCusto(float(input("Digite outro valor para custo")))
                lista[trocar_id].setPreco(float(input("Digite outro valor para preço")))

        elif opcao == 4:
            os.system('clear')

    except:
        valido = print("Digite um valor válido!")
        input("entrou aqui")
