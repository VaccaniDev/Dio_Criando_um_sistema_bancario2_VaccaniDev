from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def saldo(self):
        return self._cliente

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("A operação falhou: você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        else:
            print("A operação falhou! O valor inválido.")

        return False

    def depositar(saldo, valor):
        if valor > 0:
            saldo._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("A operação falhou: valor inválido.")
            return False

        return True


class ContaCorrente(Conta):
    def _init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque"
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou: o valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou: número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    # def menu():
    #     menu = """\n
    #     ================= MENU =================
    #     [d]\tDepositar
    #     [s]\tSacar
    #     [e]\tExtrato
    #     [nc]\tNova conta
    #     [lc]\tListar contas
    #     [nu]\tNovo usuário
    #     [q]\t Sair
    #     => """
    #     return input(textwrap.dedent(menu))

    # def depositar(saldo, valor):
    #     if valor > 0:
    #         saldo._saldo += valor
    #         print("Depósito realizado com sucesso!")
    #     else:
    #         print("A operação falhou: valor inválido.")
    #         return False

    #     return True

    # def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("A operação falhou: você não tem saldo suficiente.")

    elif valor > 0:
        self._saldo -= valor
        print("Saque realizado com sucesso!")
        return True

    else:
        print("A operação falhou! O valor inválido.")

    return False


# def exibir_extrato(saldo, /, *, extrato):
#     print("\n=============== EXTRATO ===============")
#     print("Não foram realizadas movimentações." if not extrato else extrato)
#     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
#     print("\n=======================================")


# def criar_usuario(usuarios):
#     cpf = input("Informe o CPF (somente número): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("Aviso: esse CPF já foi registrado.")
#         return

#     nome = input("Informe o seu nome completo:")
#     data_nascimento = input("Inform sua data de nascimento:")
#     endereco = input("Informe seu endereço:")

#     usuarios.append(
#         {
#             "nome": nome,
#             "data_nascimento": data_nascimento,
#             "cpf": cpf,
#             "endereco": endereco,
#         }
#     )

#     print("Usuário criado com sucesso! ")


# def filtrar_usuario(cpf, usuarios):
#     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#     return usuarios_filtrados[0] if usuarios_filtrados else None


# def listar_contas(contas):
#     for conta in contas:
#         linha = f"""\
#             Agência:\t{conta['agencia']}
#             C/C:\t\t{conta['numero_conta']}
#             Titular:\t{conta['usuario']['nome']}
#         """
#         print("=" * 100)
#         print(textwrap.dedent(linha))


# def criar_conta(agencia, numero_conta, usuarios):
#     cpf = input("Informe o CPF do usuário:")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("Conta criada com sucesso!")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

#     print("Usuário não encontrado, fluxo de criação de conta encerrado!")


# def main():
#     LIMITE_SAQUES = 3
#     AGENCIA = "0001"

#     saldo = 0
#     limite = 500
#     extrato = ""
#     numero_saques = 0
#     usuarios = []
#     contas = []

#     while True:
#         opcao = menu()

#         if opcao == "d":
#             valor = float(input("Informe o valor de deposito: "))

#             saldo, extrato = depositar(saldo, valor, extrato)

#         elif opcao == "s":
#             valor = float(input("Informe o valor do saque: "))

#             saldo, extrato = sacar(
#                 saldo=saldo,
#                 valor=valor,
#                 extrato=extrato,
#                 limite=limite,
#                 numero_saques=numero_saques,
#                 limite_saques=LIMITE_SAQUES,
#             )

#         elif opcao == "e":
#             exibir_extrato(saldo, extrato=extrato)

#         elif opcao == "nu":
#             criar_usuario(usuarios)

#         elif opcao == "nc":
#             numero_conta = len(contas) + 1
#             conta = criar_conta(AGENCIA, numero_conta, usuarios)

#             if conta:
#                 contas.append(conta)

#         elif opcao == "lc":
#             listar_contas(contas)

#         elif opcao == "q":
#             break

#         else:
#             print(
#                 "Operação inválida, por favor selecione novamente a operação desejada."
#             )


# main()
