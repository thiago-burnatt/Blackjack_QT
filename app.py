import sys
from funcoes import nova_carta, nova_banca
from PyQt5.QtWidgets import QApplication, QMainWindow
from layout import Ui_QmainWindow


class Jogo(QMainWindow, Ui_QmainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.cartas_jogador = []
        self.cartas_banca = []
        self.saldo = 0
        self.valor_aposta = 0

        self.btnCarta.clicked.connect(self.nova_carta)
        self.btnParar.clicked.connect(self.para)
        self.btnRecomecar.clicked.connect(self.recomecar)
        self.btnDepositar.clicked.connect(self.deposito)
        self.btnApostar.clicked.connect(self.aposta)
        self.btnNovaJogada.clicked.connect(self.nova_jogada)
        # self.btnParar.clicked.connect(self.exit)

    def deposito(self):
        try:
            self.saldo = (int(self.displayDefinirDeposito.text()))
            self.displaySaldo.setText(str(self.saldo))
            self.labelResultado.setText('')
        except:
            self.labelResultado.setText('Digite apenas valores numéricos')

    def aposta(self):
        try:
            self.valor_aposta = int(self.displayApostar.text())
            self.displaySaldo.setText(str(self.saldo))
            self.displayApostando.setText(str(self.valor_aposta))
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySoma.setText('0')
            self.displayCarta.setText('0')
            self.labelResultado.setText('')

            if self.valor_aposta > self.saldo:
                self.labelResultado.setText('Saldo insuficiente')
                return

            else:
                self.labelResultado.setText('')
        except:
            self.labelResultado.setText('Digite apenas valores numéricos')


    def nova_carta(self):
        if self.saldo == 0 and self.valor_aposta == 0:
            self.labelResultado.setText('Saldo insuficiente')
            return
        if self.valor_aposta > self.saldo:
            self.labelResultado.setText('Saldo insuficiente')
            return
        else:
            self.labelResultado.setText('')

        self.cartas_jogador.append(int(nova_carta()))   # ADICIONA UMA CARTA ALEATÓRIA NA LISTA
        self.displayCarta.setText(str(self.cartas_jogador[-1]))   # CONVERTE PARA STRING PARA MOSTRAR NA TELA
        soma_j = str(sum(self.cartas_jogador))
        self.displaySoma.setText(soma_j)
        self.cartas_banca.append(int(nova_banca()))
        self.displaySaldo.setText(str(self.saldo))

        if int(soma_j) == 21:
            self.saldo += self.valor_aposta * 2
            valor = self.valor_aposta * 2
            self.labelResultado.setText(f'Você ganhou R${valor} com {soma_j} pontos')
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySaldo.setText(str(self.saldo))


        if int(soma_j) > 21:
            self.saldo -= self.valor_aposta
            valor = self.valor_aposta
            self.labelResultado.setText(f'Você perdeu R${valor} com {soma_j} pontos')
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySaldo.setText(str(self.saldo))


    def para(self):
        if self.valor_aposta > self.saldo:
            self.labelResultado.setText('Saldo insuficiente')
            return
        else:
            self.labelResultado.setText('')

        soma_j = int(sum(self.cartas_jogador))
        soma_b = int(sum(self.cartas_banca))
        if soma_j == 21:
            self.saldo += self.valor_aposta * 2
            valor = self.valor_aposta * 2
            self.labelResultado.setText(f'Você ganhou R${valor} com {soma_j} pontos')
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySaldo.setText(str(self.saldo))

        if soma_j >= soma_b and soma_j != 0:
            self.saldo += self.valor_aposta * 2
            valor = self.valor_aposta * 2
            self.labelResultado.setText(f'Você ganhou R${valor} com {soma_j} pontos')
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySaldo.setText(str(self.saldo))

        if soma_b > soma_j:
            self.saldo -= self.valor_aposta
            valor = self.valor_aposta
            self.labelResultado.setText(f'Você perdeu R${valor}, Banca: {soma_b} pontos')
            self.cartas_jogador = []
            self.cartas_banca = []
            self.displaySaldo.setText(str(self.saldo))

    def nova_jogada(self):
        self.cartas_jogador = []
        self.cartas_banca = []
        self.displaySoma.setText('0')
        self.displayCarta.setText('0')
        self.displaySaldo.setText(str(self.saldo))
        self.labelResultado.setText('')
        if self.valor_aposta > self.saldo:
            self.labelResultado.setText('Saldo insuficiente')
            return
        else:
            self.labelResultado.setText('')

    def recomecar(self):
        self.cartas_jogador = []
        self.cartas_banca = []
        self.saldo = 0
        self.valor_aposta = 0
        self.displaySoma.setText('')
        self.displayCarta.setText('')
        self.displaySaldo.setText('')
        self.labelResultado.setText('')
        self.displayDefinirDeposito.setText('')
        self.displayApostar.setText('')
        self.displayApostando.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    black = Jogo()
    black.show()
    qt.exec_()

