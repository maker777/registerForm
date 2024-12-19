import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QPushButton, QLabel, QApplication

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
  
        self.setWindowTitle('Регистрация')
        self.setGeometry(300, 300, 300, 150)


        layout = QVBoxLayout()
        form_layout = QFormLayout()
        

        self.username = QLineEdit()
        label_username = QLabel("Имя пользователя:")
        form_layout.addRow(label_username, self.username)


        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        label_password = QLabel("Пароль:")
        form_layout.addRow(label_password, self.password)


        self.role = QComboBox()
        self.role.addItems(["Пользователь","Администратор"])
        label_role = QLabel("Роль:")
        form_layout.addRow(label_role, self.role)


        self.login_button = QPushButton("Войти")
        layout.addWidget(self.login_button)


        self.forgot_button = QPushButton("Забыли пароль?")
        layout.addWidget(self.forgot_button)


        layout.addLayout(form_layout)
        self.setLayout(layout)




app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())