import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget, QMessageBox, QDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SorteadorDeTimes(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração principal da janela
        self.setWindowTitle("Sorteador de Times")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFD700;  /* Amarelo */
            }
            QLabel {
                color: #B22222;  /* Vermelho escuro */
                font-weight: bold;
                font-size: 14px;
            }
            QLineEdit {
                border: 2px solid #B22222;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #B22222;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #8B0000;
            }
            QTextEdit {
                background-color: #FFF8DC;  /* Bege claro */
                color: #B22222;
                font-size: 14px;
                border: 2px solid #B22222;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # Layout principal
        layout = QVBoxLayout()

        # Entrada para nomes
        self.label_nomes = QLabel("Digite os nomes separados por vírgulas:")
        layout.addWidget(self.label_nomes)

        self.input_nomes = QLineEdit()
        layout.addWidget(self.input_nomes)

        # Entrada para o número de grupos
        self.label_grupos = QLabel("Digite o número de grupos:")
        layout.addWidget(self.label_grupos)

        self.input_grupos = QLineEdit()
        layout.addWidget(self.input_grupos)

        # Botão para sortear
        self.btn_sortear = QPushButton("Sortear Times")
        self.btn_sortear.clicked.connect(self.sortear_times)
        layout.addWidget(self.btn_sortear)

        # Área de saída para os resultados
        self.resultados = QTextEdit()
        self.resultados.setReadOnly(True)
        layout.addWidget(self.resultados)

        # Créditos
        self.label_creditos = QLabel("Desenvolvido por Pretex (Caverna do Dragão)")
        self.label_creditos.setFont(QFont("Arial", 10, QFont.StyleItalic))
        self.label_creditos.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_creditos)

        # Configuração do widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def sortear_times(self):
        try:
            # Obter nomes e número de grupos
            nomes = self.input_nomes.text().split(',')
            num_grupos = int(self.input_grupos.text())

            if len(nomes) < num_grupos:
                raise ValueError("O número de grupos é maior que a quantidade de nomes disponíveis.")

            # Embaralhar e distribuir nomes
            random.shuffle(nomes)
            grupos = [[] for _ in range(num_grupos)]

            for i, nome in enumerate(nomes):
                grupos[i % num_grupos].append(nome.strip())

            # Exibir os resultados
            resultado_texto = ""
            for i, grupo in enumerate(grupos):
                resultado_texto += f"Grupo {i + 1}: {', '.join(grupo)}\n"
            
            self.resultados.setText(resultado_texto)

            # Sortear o mapa
            self.sortear_mapa()

        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Erro", "Ocorreu um erro inesperado.")

    def sortear_mapa(self):
        mapas = [
            "Ascent", "Abyss", "Bind", "Split", "Haven", 
            "Sunset", "Lotus", "Pearl", "Breeze", "Fracture", "Icebox"
        ]
        mapa_escolhido = random.choice(mapas)

        # Exibir o mapa em uma nova janela
        dialog = QDialog(self)
        dialog.setWindowTitle("Mapa Sorteado")
        dialog.setGeometry(200, 200, 300, 200)
        dialog.setStyleSheet("background-color: #FFD700; color: #B22222; font-size: 16px; font-weight: bold;")

        layout = QVBoxLayout()
        label = QLabel(f"O mapa sorteado é:\n\n{mapa_escolhido}")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(dialog.accept)
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec_()

# Função principal para rodar o aplicativo
def main():
    app = QApplication(sys.argv)
    janela = SorteadorDeTimes()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
