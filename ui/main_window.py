# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(400, 300)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.project_list = QListWidget(self.centralwidget)
        self.project_list.setObjectName(u"project_list")

        self.verticalLayout.addWidget(self.project_list)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName(u"new_btn")

        self.button_layout.addWidget(self.new_btn)

        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName(u"open_btn")

        self.button_layout.addWidget(self.open_btn)


        self.verticalLayout.addLayout(self.button_layout)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout.addWidget(self.exit_btn)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Box of Balls - \u0412\u0445\u043e\u0434", None))
        self.centralwidget.setStyleSheet(QCoreApplication.translate(
            "LoginWindow",
            u"""
            /* Фон ТОЛЬКО для центрального виджета */
            QWidget#centralwidget {
                background-image: url(C:/Users/polina/PycharmProjects/box_of_balls/resources/backgrounds/balls.png);
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }

            /* Полупрозрачная тёмная вуаль поверх фона */
            QWidget#centralwidget::before {
                content: "";
            }

            /* Все элементы интерфейса */
            QLabel, QListWidget, QPushButton {
                background-color: rgba(25, 25, 25, 180);
                color: white;
                font-family: "Montserrat", "Inter", "Segoe UI", sans-serif;
                font-size: 14px;
            }

            QLabel#title_label {
                background-color: transparent;
                font-size: 26px;
                font-weight: 600;
            }

            QListWidget {
                border: 1px solid rgba(255, 255, 255, 40);
                border-radius: 6px;
            }

            QPushButton {
                border: 1px solid rgba(255, 255, 255, 60);
                padding: 6px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: rgba(60, 60, 60, 200);
            }
            """,
            None
        ))
        self.title_label.setText(QCoreApplication.translate("LoginWindow", u"Box of Balls", None))
        self.new_btn.setText(QCoreApplication.translate("LoginWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.open_btn.setText(QCoreApplication.translate("LoginWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.exit_btn.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

