# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editor_window_dark.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1057, 760)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainVBoxLayout = QVBoxLayout()
        self.mainVBoxLayout.setObjectName(u"mainVBoxLayout")
        self.canvasFrame = QFrame(self.centralwidget)
        self.canvasFrame.setObjectName(u"canvasFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.canvasFrame.sizePolicy().hasHeightForWidth())
        self.canvasFrame.setSizePolicy(sizePolicy)
        self.canvasLayout = QVBoxLayout(self.canvasFrame)
        self.canvasLayout.setObjectName(u"canvasLayout")
        self.topBar = QFrame(self.canvasFrame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBarLayout = QHBoxLayout(self.topBar)
        self.topBarLayout.setObjectName(u"topBarLayout")
        self.windowButtonsLayout = QHBoxLayout()
        self.windowButtonsLayout.setObjectName(u"windowButtonsLayout")
        self.spacerTopLeft = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.windowButtonsLayout.addItem(self.spacerTopLeft)

        self.btnMaximize = QPushButton(self.topBar)
        self.btnMaximize.setObjectName(u"btnMaximize")

        self.windowButtonsLayout.addWidget(self.btnMaximize)

        self.btnMinimize = QPushButton(self.topBar)
        self.btnMinimize.setObjectName(u"btnMinimize")

        self.windowButtonsLayout.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.topBar)
        self.btnClose.setObjectName(u"btnClose")

        self.windowButtonsLayout.addWidget(self.btnClose)


        self.topBarLayout.addLayout(self.windowButtonsLayout)


        self.canvasLayout.addWidget(self.topBar)

        self.spacerCanvasCenter = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.canvasLayout.addItem(self.spacerCanvasCenter)


        self.mainVBoxLayout.addWidget(self.canvasFrame)

        self.settingsPanel = QFrame(self.centralwidget)
        self.settingsPanel.setObjectName(u"settingsPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.settingsPanel.sizePolicy().hasHeightForWidth())
        self.settingsPanel.setSizePolicy(sizePolicy1)
        self.settingsVBox = QVBoxLayout(self.settingsPanel)
        self.settingsVBox.setObjectName(u"settingsVBox")
        self.labelSettingsTitle = QLabel(self.settingsPanel)
        self.labelSettingsTitle.setObjectName(u"labelSettingsTitle")
        self.labelSettingsTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelSettingsTitle.setMargin(6)

        self.settingsVBox.addWidget(self.labelSettingsTitle)

        self.settingsFormFrame = QFrame(self.settingsPanel)
        self.settingsFormFrame.setObjectName(u"settingsFormFrame")
        self.settingsFormFrame.setFrameShape(QFrame.NoFrame)
        self.formLayoutSettings = QFormLayout(self.settingsFormFrame)
        self.formLayoutSettings.setObjectName(u"formLayoutSettings")
        self.labelBackground = QLabel(self.settingsFormFrame)
        self.labelBackground.setObjectName(u"labelBackground")

        self.formLayoutSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelBackground)

        self.lineBackground = QLineEdit(self.settingsFormFrame)
        self.lineBackground.setObjectName(u"lineBackground")

        self.formLayoutSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineBackground)

        self.labelMusic = QLabel(self.settingsFormFrame)
        self.labelMusic.setObjectName(u"labelMusic")

        self.formLayoutSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelMusic)

        self.lineMusic = QLineEdit(self.settingsFormFrame)
        self.lineMusic.setObjectName(u"lineMusic")

        self.formLayoutSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineMusic)

        self.spacerRow2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayoutSettings.setItem(2, QFormLayout.ItemRole.FieldRole, self.spacerRow2)

        self.btnObjectEditor = QPushButton(self.settingsFormFrame)
        self.btnObjectEditor.setObjectName(u"btnObjectEditor")

        self.formLayoutSettings.setWidget(3, QFormLayout.ItemRole.LabelRole, self.btnObjectEditor)

        self.btnPreview = QPushButton(self.settingsFormFrame)
        self.btnPreview.setObjectName(u"btnPreview")
        font = QFont()
        font.setFamilies([u"Segoe UI,Arial"])
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
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1057, 21))
        self.menuFile_2 = QMenu(self.menuBar)
        self.menuFile_2.setObjectName(u"menuFile_2")
        self.menuEdit_2 = QMenu(self.menuBar)
        self.menuEdit_2.setObjectName(u"menuEdit_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0437\u0430\u0441\u0442\u0430\u0432\u043e\u043a", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"    QWidget { background-color: #222222; color: #CCCCCC; font-family: Segoe UI, Arial; font-size: 12px; }\n"
"    QFrame { background-color: #2B2B2B; border: 1px solid #444444; }\n"
"    QPushButton { background-color: #3C3C3C; border: 1px solid #555555; padding: 6px; }\n"
"    QPushButton:hover { background-color: #505050; }\n"
"    QLineEdit, QComboBox, QListWidget, QSpinBox, QDoubleSpinBox { background-color: #333333; border: 1px solid #555555; color: #FFFFFF; }\n"
"    QLabel { color: #FFFFFF; }\n"
"    QMenuBar { background-color: #2B2B2B; color: #FFFFFF; }\n"
"   ", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.canvasFrame.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #555555;", None))
#if QT_CONFIG(tooltip)
        self.btnMaximize.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btnMaximize.setText(QCoreApplication.translate("MainWindow", u"\u25a2", None))
#if QT_CONFIG(tooltip)
        self.btnMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btnMinimize.setText(QCoreApplication.translate("MainWindow", u"\u2013", None))
#if QT_CONFIG(tooltip)
        self.btnClose.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
        self.labelSettingsTitle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0446\u0435\u043d\u044b", None))
        self.labelBackground.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u043d:", None))
        self.lineBackground.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.labelMusic.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0437\u044b\u043a\u0430:", None))
        self.lineMusic.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.btnObjectEditor.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.btnPreview.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.menuFile_2.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit_2.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

