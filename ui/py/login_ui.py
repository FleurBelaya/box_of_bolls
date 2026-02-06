
################################################################################
## Form generated from reading UI file 'login_window_dark.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Ui_LoginWindow:
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.project_list = QListWidget(self.centralwidget)
        self.project_list.setObjectName("project_list")

        self.verticalLayout.addWidget(self.project_list)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName("new_btn")

        self.button_layout.addWidget(self.new_btn)

        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")

        self.button_layout.addWidget(self.open_btn)


        self.verticalLayout.addLayout(self.button_layout)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName("exit_btn")

        self.verticalLayout.addWidget(self.exit_btn)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", "Box of Balls - \u0412\u0445\u043e\u0434", None))
        self.centralwidget.setStyleSheet(QCoreApplication.translate("LoginWindow", "\n"
"     QWidget {\n"
"         background-color: #2e2e2e;\n"
"         color: #ffffff;\n"
"         font-family: 'Segoe UI', sans-serif;\n"
"         font-size: 14px;\n"
"     }\n"
"     QListWidget {\n"
"         background-color: #3c3c3c;\n"
"         border: 1px solid #555555;\n"
"     }\n"
"     QPushButton {\n"
"         background-color: #4a4a4a;\n"
"         border: 1px solid #666666;\n"
"         padding: 5px;\n"
"         border-radius: 4px;\n"
"     }\n"
"     QPushButton:hover {\n"
"         background-color: #5a5a5a;\n"
"     }\n"
"     QLabel#title_label {\n"
"         font-size: 24px;\n"
"         font-weight: bold;\n"
"     }\n"
"    ", None))
        self.title_label.setText(QCoreApplication.translate("LoginWindow", "Box of Balls", None))
        self.new_btn.setText(QCoreApplication.translate("LoginWindow", "\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.open_btn.setText(QCoreApplication.translate("LoginWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.exit_btn.setText(QCoreApplication.translate("LoginWindow", "\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

