from Model import Model

class Control:
    def __init__(self):
        self.Model = Model()
        self.opcao = -1
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

    def getNum1(self):
        return self.num1

    def setNum1(self, num1):
        self.num1 = num1

    def getNum2(self):
        return self.num2

    def setNum2(self, num2):
        self.num2 = num2

    def getNum3(self):
        return self.num3

    def setNum3(self, num3):
        self.num3 = num3

    def getNum4(self):
        return self.num4

    def setNum4(self, num4):
        self.num4 = num4

    def coletar2(self):
        print("Informe o primeiro número:")
        self.setNum1(float(input()))
        print("Informe o segundo número:")
        self.setNum2(float(input()))

    def coletar4(self):
        print("Informe o primeiro número:")
        self.setNum1(float(input()))
        print("Informe o segundo número:")
        self.setNum2(float(input()))
        print("Informe o terceiro número:")
        self.setNum3(float(input()))
        print("Informe o quarto número:")
        self.setNum4(float(input()))


    def menu(self):
        print("Escolha uma das opções abaixo: \n\n"
              "0.Sair\n" +
              "1.Exercício 1: 'Alo Mundo'\n" +
              "2.Exercício 2: Pedir e informar um número\n" +
              "3.Exercício 3: Soma\n" +
              "4.Exercício 4: Média 4 números\n" +
              "5.Exercício 5: Conversão de metros para CM\n" +
              "6.Exercício 6: Área de um círculo baseado no raio\n" +
              "7.Exercício 7: Área do quadrado, área do quadrado dobrada\n" +
              "8.Exercício 8: Total salário no mês baseado no ganho por hora e nas horas trabalhadas\n" +
              "9.Exercício 9: Conversão de Fahrenheit para Celsius\n" +
              "10.Exercício 10: Conversão de Celsius para Fahrenheit\n" +
              "11.Exercício 11: Troca de números entre variáveis\n" +
              "12.Exercício 12: Informar o antecessor do número informado\n" +
              "13.Exercício 13: Calcular a área de um retãngulo\n" +
              "14.Exercício 14: Calcular idade de uma pessoa em dias\n" +
              "15.Exercício 15: Porcentagem votos\n" +
              "17.Exercício 17: Custo de um carro somando impostos" +
              "18.Exercício 18: Média final com 3 notas\n" +
              "18.Exercício 18: Média final com 3 notas\n" +
              "19.Exercício 19: Compra de maçãs\n" +
              "20.Exercício 20: Números em ordem crescente\n" +
              "21.Exercício 21: Salário total de um vendedor\n" +
              "22.Exercício 22: Conta Banco\n" +
              "23.Exercício 23: Tabuada\n" +
              "24.Exercício 24: Imprimir valores inteiro entre números:\n" +
              "25.Exercício 25: Números negativos entre 10 números\n" +
              "26.Exercício 26: Soma de 10 valores inferiores a 40\n" +
              "27.Exercício 27: Média Aritmética entre 15 e 100\n" +
              "29.Exercício 29: Média turma de 20 alunos\n")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()
            if self.opcao == 0:
                print("Fim!")
            elif self.opcao == 1:
                print("\nAlo Mundo\n")
            elif self.opcao == 2:
                print("Informe o número:")
                self.setNum1(float(input()))
                print("O número escolhido foi {}:".format(self.Model.exercicio2(self.getNum1())))
            elif self.opcao == 3:
                self.coletar2()
                print("O resultado da soma é: {}".format(self.Model.exercicio3Soma(self.getNum1(), self.getNum2())))
            elif self.opcao == 4:
                self.coletar4()
                print("A média final é: {}".format(self.Model.exercicio4Media(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())))
            elif self.opcao == 5:
                print("Informe a quantidade de metros: ")
                self.setNum1(float(input()))
                print("A conversão de metros para CM do número informado é: {}".format(self.Model.exercicio5MetrosCm(self.getNum1())))
            elif self.opcao == 6:
                print("Informe o raio do círculo: ")
                self.setNum1(float(input()))
                print("A área do círculo baseado no raio é aproximadamente: {}".format(self.Model.exercicio6AreaCirculo(self.getNum1())))
            elif self.opcao == 7:
                self.coletar2()
                self.Model.exercicio7AreaQuadrado(self.getNum1(), self.getNum2())
            elif self.opcao == 8:
                print("Informe quanto você ganha por hora: ")
                self.setNum1(float(input()))
                print("Informe quantas horas você trabalhou no mês: ")
                self.setNum2(float(input()))
                print("Seu salário no mês foi de: {}".format(self.Model.exercicio8HoraMesSalario(self.getNum1(), self.getNum2())))
            elif self.opcao == 9:
                print("Informe a temperatura em Fahrenheit: ")
                self.setNum1(float(input()))
                print("A conversão de Fahrenheit informado para Celsius é: {}".format(self.Model.exercicio9FahrenheitCelsius(self.getNum1())))
            elif self.opcao == 10:
                print("Informe a temperatura em Celsius: ")
                self.setNum1(float(input()))
                print("A conversão de Celsius informado para Fahrenheit é: {}".format(self.Model.exercicio10CelsiusFahrenheit(self.getNum1())))
            elif self.opcao == 11:
                self.coletar2()
                self.Model.exercicio11ValorAB(self.getNum1(), self.getNum2())
            elif self.opcao == 12:
                print("Informe o número desejado: ")
                self.setNum1(float(input()))
                print("O antecessor do número informado é: {}".format(self.Model.exercicio12Antecessor(self.getNum1())))
            elif self.opcao == 13:
                print("Informe a base do retângulo: ")
                self.setNum1(float(input()))
                print("Informe a algura do retângulo: ")
                self.setNum2(float(input()))
                print("A área do retângulo é: {}".format(self.Model.exercicio13AreaRetangulo(self.getNum1(), self.getNum2())))
            elif self.opcao == 14:
                print("Informe o número de anos: ")
                self.setNum1(float(input()))
                print("Informe o número de meses: ")
                self.setNum2(float(input()))
                print("Informe o número de dias: ")
                self.setNum3(float(input()))
                print("Sua idade em dias é de: {}".format(self.Model.exercicio14Idade(self.getNum1(), self.getNum2(), self.getNum3())))
            elif self.opcao == 15:
                print("Informe o número de eleitores: ")
                self.setNum1(float(input()))
                print("Informe o número de votos em branco: ")
                self.setNum2(float(input()))
                print("Informe o número de votos nulos: ")
                self.setNum3(float(input()))
                print("Informe o número de votos válidos")
                self.setNum4(float(input()))
                print("As porcentagens são: {}".format(self.Model.exercicio15Votos(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())))
            elif self.opcao == 17:
                print("Informe o valor do carro: ")
                self.setNum1(float(input()))
                print("O valor final do carro é de: {}".format(self.Model.exercicio17Carro(self.getNum1())))
            elif self.opcao == 18:
                print("Informe a primeira nota: ")
                self.setNum1(float(input()))
                print("Informe a segunda nota: ")
                self.setNum2(float(input()))
                print("Informe a terceira nota: ")
                self.setNum3(float(input()))
                print("A média final é de: {}".format(self.Model.exercicio18Media3(self.getNum1(), self.getNum2(), self.getNum3())))
            elif self.opcao == 19:
                print("Informe o número de maçãs compradas: ")
                self.setNum1(float(input()))
                print("O valor final da compra das maçãs é de: {}".format(self.Model.exercicio19Maca(self.getNum1())))
            elif self.opcao == 20:
                self.Model.exercicio20Crescente()
            elif self.opcao == 21:
                print("Informe seu Salário Fixo: ")
                self.setNum1(float(input()))
                print("Informe o valor total das vendas: ")
                self.setNum2(float(input()))
                print("O salário total é de: {}".format(self.Model.exercicio21Vendas(self.getNum1(), self.getNum2())))
            elif self.opcao == 22:
                print("Informe o número da conta: ")
                self.setNum1(int(input()))
                print("Informe seu Saldo: ")
                self.setNum2(float(input()))
                print("Informe seu Débito: ")
                self.setNum3(float(input()))
                print("Informe seu Crédito: ")
                self.setNum4(float(input()))
                self.Model.exercicio22Conta(self.getNum1(), self.getNum2(),self.getNum3(),self.getNum4())
            elif self.opcao == 23:
                print("Informe um número de 1 a 10: ")
                print(self.Model.exercicio23Tabuada(float(input())))
            elif self.opcao == 24:
                print("Informe um número: ")
                print(self.Model.exercicio24ValoresInteiros(int(input())))
            elif self.opcao == 25:
                self.Model.exercicio25Negativos()
            elif self.opcao == 26:
                self.Model.exercicio26SomaMenos40()
            elif self.opcao == 27:
                self.Model.exercicio27MediaAritmetica()
            else:
                print("Opção inválida")