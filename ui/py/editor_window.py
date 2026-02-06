
################################################################################
## Form generated from reading UI file 'editor_window_dark.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (
    QFormLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 760)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainVBoxLayout = QVBoxLayout()
        self.mainVBoxLayout.setObjectName("mainVBoxLayout")
        self.canvasFrame = QFrame(self.centralwidget)
        self.canvasFrame.setObjectName("canvasFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.canvasFrame.sizePolicy().hasHeightForWidth())
        self.canvasFrame.setSizePolicy(sizePolicy)
        self.canvasLayout = QVBoxLayout(self.canvasFrame)
        self.canvasLayout.setObjectName("canvasLayout")
        self.spacerCanvasCenter = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.canvasLayout.addItem(self.spacerCanvasCenter)


        self.mainVBoxLayout.addWidget(self.canvasFrame)

        self.settingsPanel = QFrame(self.centralwidget)
        self.settingsPanel.setObjectName("settingsPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.settingsPanel.sizePolicy().hasHeightForWidth())
        self.settingsPanel.setSizePolicy(sizePolicy1)
        self.settingsVBox = QVBoxLayout(self.settingsPanel)
        self.settingsVBox.setObjectName("settingsVBox")
        self.labelSettingsTitle = QLabel(self.settingsPanel)
        self.labelSettingsTitle.setObjectName("labelSettingsTitle")
        self.labelSettingsTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelSettingsTitle.setMargin(6)

        self.settingsVBox.addWidget(self.labelSettingsTitle)

        self.settingsFormFrame = QFrame(self.settingsPanel)
        self.settingsFormFrame.setObjectName("settingsFormFrame")
        self.settingsFormFrame.setFrameShape(QFrame.NoFrame)
        self.formLayoutSettings = QFormLayout(self.settingsFormFrame)
        self.formLayoutSettings.setObjectName("formLayoutSettings")
        self.labelBackground = QLabel(self.settingsFormFrame)
        self.labelBackground.setObjectName("labelBackground")

        self.formLayoutSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelBackground)

        self.lineBackground = QLineEdit(self.settingsFormFrame)
        self.lineBackground.setObjectName("lineBackground")

        self.formLayoutSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineBackground)

        self.labelMusic = QLabel(self.settingsFormFrame)
        self.labelMusic.setObjectName("labelMusic")

        self.formLayoutSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelMusic)

        self.lineMusic = QLineEdit(self.settingsFormFrame)
        self.lineMusic.setObjectName("lineMusic")

        self.formLayoutSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineMusic)

        self.spacerRow2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayoutSettings.setItem(2, QFormLayout.ItemRole.FieldRole, self.spacerRow2)

        self.btnObjectEditor = QPushButton(self.settingsFormFrame)
        self.btnObjectEditor.setObjectName("btnObjectEditor")

        self.formLayoutSettings.setWidget(3, QFormLayout.ItemRole.LabelRole, self.btnObjectEditor)

        self.btnPreview = QPushButton(self.settingsFormFrame)
        self.btnPreview.setObjectName("btnPreview")
        font = QFont()
        font.setFamilies(["Segoe UI,Arial"])
        self.btnPreview.setFont(font)

        self.formLayoutSettings.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnPreview)

        self.spacerPreview1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayoutSettings.setItem(4, QFormLayout.ItemRole.FieldRole, self.spacerPreview1)


        self.settingsVBox.addWidget(self.settingsFormFrame)

        self.spacerSettingsBottom = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.settingsVBox.addItem(self.spacerSettingsBottom)


        self.mainVBoxLayout.addWidget(self.settingsPanel)


        self.verticalLayout.addLayout(self.mainVBoxLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1057, 21))
        self.menuFile_2 = QMenu(self.menuBar)
        self.menuFile_2.setObjectName("menuFile_2")
        self.menuEdit_2 = QMenu(self.menuBar)
        self.menuEdit_2.setObjectName("menuEdit_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar.addAction(self.menuFile_2.menuAction())
        self.menuBar.addAction(self.menuEdit_2.menuAction())
        self.menuFile_2.addSeparator()
        self.menuFile_2.addAction(self.action_2)
        self.menuFile_2.addAction(self.action_3)
        self.menuFile_2.addAction(self.action_4)
        self.menuFile_2.addAction(self.action_5)
        self.menuFile_2.addAction(self.action_6)
        self.menuEdit_2.addAction(self.action_7)
        self.menuEdit_2.addAction(self.action_8)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0437\u0430\u0441\u0442\u0430\u0432\u043e\u043a", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", "\n"
"    QWidget { background-color: #222222; color: #CCCCCC; font-family: Segoe UI, Arial; font-size: 12px; }\n"
"    QFrame { background-color: #2B2B2B; border: 1px solid #444444; }\n"
"    QPushButton { background-color: #3C3C3C; border: 1px solid #555555; padding: 6px; }\n"
"    QPushButton:hover { background-color: #505050; }\n"
"    QLineEdit, QComboBox, QListWidget, QSpinBox, QDoubleSpinBox { background-color: #333333; border: 1px solid #555555; color: #FFFFFF; }\n"
"    QLabel { color: #FFFFFF; }\n"
"    QMenuBar { background-color: #2B2B2B; color: #FFFFFF; }\n"
"   ", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", "\u041d\u043e\u0432\u044b\u0439", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "\u0412\u044b\u0445\u043e\u0434", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", "\u041d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", "\u041d\u0430\u0437\u0430\u0434", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", "\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.canvasFrame.setStyleSheet(QCoreApplication.translate("MainWindow", "background-color: #555555;", None))
        self.labelSettingsTitle.setText(QCoreApplication.translate("MainWindow", "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0446\u0435\u043d\u044b", None))
        self.labelBackground.setText(QCoreApplication.translate("MainWindow", "\u0424\u043e\u043d:", None))
        self.lineBackground.setPlaceholderText(QCoreApplication.translate("MainWindow", "\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.labelMusic.setText(QCoreApplication.translate("MainWindow", "\u041c\u0443\u0437\u044b\u043a\u0430:", None))
        self.lineMusic.setPlaceholderText(QCoreApplication.translate("MainWindow", "\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.btnObjectEditor.setText(QCoreApplication.translate("MainWindow", "\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.btnPreview.setText(QCoreApplication.translate("MainWindow", "\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.menuFile_2.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit_2.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
    # retranslateUi

