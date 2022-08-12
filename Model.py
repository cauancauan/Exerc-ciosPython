class Model:
    def __init__(self):
        self.resultado = 0
        self.soma = 0
        self.multiplicacao = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.contador = 0
        self.lista = []
        self.negativos = 0
        self.positivos = 0

    def exercicio2(self, num1):
        return num1

    def exercicio3Soma(self, num1, num2):
        return num1+num2

    def exercicio4Media(self, num1, num2, num3, num4):
        self.soma = num1+num2+num3+num4
        self.resultado = self.soma / 4
        return self.resultado

    def exercicio5MetrosCm(self, num1):
        return num1*100

    def exercicio6AreaCirculo(self, num1):
        self.multiplicacao = num1*num1
        self.resultado = self.multiplicacao*3.14
        return self.resultado

    def exercicio7AreaQuadrado(self, base, altura):
        self.multiplicacao = base*altura
        return print("Área:", self.multiplicacao, "| Área dobrada:", self.multiplicacao*2)

    def exercicio8HoraMesSalario(self, ganhoHora, horasTrabalhadas):
        self.multiplicacao = ganhoHora*horasTrabalhadas
        return self.multiplicacao

    def exercicio9FahrenheitCelsius(self, fahrenheit):
        return 5*((fahrenheit-32)/9)

    def exercicio10CelsiusFahrenheit(self, celsius):
        return (celsius*1.8) + 32

    def exercicio11ValorAB(self, num1, num2):
        self.A = num2
        self.B = num1
        return print("Número A:", self.A, "| Número B:", self.B)

    def exercicio12Antecessor(self, num1):
        return num1-1

    def exercicio13AreaRetangulo(self, base, altura):
        return base*altura

    def exercicio14Idade(self, anos, meses, dias):
        self.A = anos*365
        self.B = meses*30
        return self.A+self.B+dias

    def exercicio15Votos(self, eleitores, vBranco, vNulo, vValido):
        self.soma = vBranco+vNulo+vValido
        self.A = (vBranco*100)/eleitores
        self.B = (vNulo*100)/eleitores
        self.C = (vValido*100)/eleitores
        return print(round(self.A),"Foi a porcentagem dos que votaram em branco", round(self.B),"| Foi a porcentagem dos que votaram nulo", round(self. C),"| Foi a porcentagem dos que votaram de forma válida")

    def exercicio17Carro(self, custoCarro):
        self.A = (28/100)*custoCarro
        self.B = (45/100)*custoCarro
        return self.A+self.B+custoCarro

    def exercicio18Media3(self, num1, num2, num3):
        return (num1+num2+num3)/3

    def exercicio19Maca(self, maca):
        if maca >= 12:
            return maca*1.30
        else:
            return maca*1

    def exercicio20Crescente(self):
        while (self.contador < 10):
            self.contador = self.contador + 1
            self.lista.append(float(input("Digite um valor:")))
        self.lista.sort()
        return print(f'Os valores em ordem crescente são: {self.lista}')

    def exercicio21Vendas(self, salaFix, valorVendas):
        if valorVendas < 1500:
            return (3/100)*valorVendas + salaFix
        else:
            final = valorVendas - 1500
            return (3/100)*1500 + (5/100)*final + salaFix

    def exercicio22Conta(self, numConta, saldo, debito, credito):
        saldoAtual = saldo - debito + credito
        if saldoAtual >= 0:
            return print(f'Número da conta: {numConta}' f' | Seu saldo é de: R${saldoAtual}' ' | Saldo Positivo')
        else:
            return print(f'Número da conta: {numConta}' f' | Seu saldo é de: R${saldoAtual}' ' | Saldo Negativo')

    def exercicio23Tabuada(self, num):
        msg = ""
        for i in range (11):
            msg = msg + "\n{} * {} = {}".format(num, i, num*i)
        return msg

    def exercicio24ValoresInteiros(self, num):
        msg = ""
        for i in range (1, num+1):
            msg = msg + "\n {}".format(i, num)
        return msg

    def exercicio25Negativos(self):
        while (self.contador < 10):
            self.contador = self.contador + 1
            self.lista.append(float(input("Digite um valor:")))
        for num in self.lista:
            if num < 0:
                self.negativos += 1
        print("O total de números negativos é de: ", self.negativos)

    def exercicio26SomaMenos40(self):
        while (self.contador < 10):
            self.contador = self.contador + 1
            self.lista.append(float(input("Digite um valor:")))
        for num in self.lista:
            if num < 40:
                self.soma = self.soma+num
            return print("A soma dos números inferiores a 40 é: ", self.soma)

    def exercicio27MediaAritmetica(self):
        num_range = range(15, 101)
        num_list = list(num_range)
        self.soma = sum(num_list) / len(num_list)
        print(self.soma)









