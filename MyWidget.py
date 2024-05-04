from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from main import Audio_Item

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400)


        mainLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()

        mainLayout.addLayout(verticalLayout)

        self.setLayout(mainLayout)

        self.myLabel=QLabel("Кол-во нажатий на кнопку")
        myLable2=QLabel("BBB")

        select_file_button = QPushButton('Выбрать файл')
        spectre_button = QPushButton('Показать спектр')
        osc_button = QPushButton('Показать осциллограмму')

        verticalLayout.addWidget(self.myLabel)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)

        mainLayout.addWidget(myLable2)

        select_file_button.clicked.connect(self.select_file)

        self.clicks_counter= 0

        

    def select_file(self):
        filename, filter = QFileDialog.getOpenFileName()
        self.audio_item = Audio_Item(filename)
        self.myLabel.setText(f'Выбранный файл : {filename}')
        print(self.audio_item)

app=QApplication([])
mainWidget = MyWidget()
mainWidget.show()
app.exec()