from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QGroupBox, QPushButton, QTableWidget, QTableWidgetItem,
                               QWidget)


class Ui_MainWindow(object):
    def __init__(self):
        self.btn_info = None
        self.tableWidget_matrixB = None
        self.groupBox_5 = None
        self.tableWidget_new_matrixB = None
        self.groupBox_6 = None
        self.tableWidget_new_matrixA = None
        self.groupBox_4 = None
        self.tableWidget_matrixA = None
        self.groupBox_3 = None
        self.btn_modificate_matrixB = None
        self.btn_generate_matrixB = None
        self.groupBox_2 = None
        self.btn_modificate_matrixA = None
        self.btn_generate_matrixA = None
        self.groupBox = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 949)
        MainWindow.setMinimumSize(QSize(932, 949))
        MainWindow.setMaximumSize(QSize(932, 949))
        icon = QIcon()
        icon.addFile(u"img/favicon.gif", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba("
                                 u"81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, "
                                 u"255));")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(660, 170, 251, 231))
        self.groupBox.setStyleSheet(u"color: white;\n"
                                    "font-weight: bold;\n"
                                    "font-size:15;\n"
                                    "")
        self.btn_generate_matrixA = QPushButton(self.groupBox)
        self.btn_generate_matrixA.setObjectName(u"btn_generate_matrixA")
        self.btn_generate_matrixA.setGeometry(QRect(50, 40, 161, 31))
        self.btn_generate_matrixA.setStyleSheet(u"QPushButton{\n"
                                                "border: 2px solid rgba(255, 255, 255, 200);\n"
                                                "border-radius: 4px;\n"
                                                "}\n"
                                                "QPushButton:pressed\n"
                                                "{\n"
                                                "background-color: rgba(22, 184, 98,1)\n"
                                                "}")
        self.btn_modificate_matrixA = QPushButton(self.groupBox)
        self.btn_modificate_matrixA.setObjectName(u"btn_modificate_matrixA")
        self.btn_modificate_matrixA.setGeometry(QRect(50, 140, 161, 31))
        self.btn_modificate_matrixA.setStyleSheet(u"QPushButton{\n"
                                                  "border: 2px solid rgba(255, 255, 255, 200);\n"
                                                  "border-radius: 4px;\n"
                                                  "}\n"
                                                  "QPushButton:pressed\n"
                                                  "{\n"
                                                  "background-color: rgba(22, 184, 98,1)\n"
                                                  "}")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(660, 520, 251, 231))
        self.groupBox_2.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size:15;\n"
                                      "")
        self.btn_generate_matrixB = QPushButton(self.groupBox_2)
        self.btn_generate_matrixB.setObjectName(u"btn_generate_matrixB")
        self.btn_generate_matrixB.setGeometry(QRect(50, 50, 161, 31))
        self.btn_generate_matrixB.setStyleSheet(u"QPushButton{\n"
                                                "border: 2px solid rgba(255, 255, 255, 200);\n"
                                                "border-radius: 4px;\n"
                                                "}\n"
                                                "QPushButton:pressed\n"
                                                "{\n"
                                                "background-color: rgba(22, 184, 98,1)\n"
                                                "}")
        self.btn_modificate_matrixB = QPushButton(self.groupBox_2)
        self.btn_modificate_matrixB.setObjectName(u"btn_modificate_matrixB")
        self.btn_modificate_matrixB.setGeometry(QRect(50, 150, 161, 31))
        self.btn_modificate_matrixB.setStyleSheet(u"QPushButton{\n"
                                                  "border: 2px solid rgba(255, 255, 255, 200);\n"
                                                  "border-radius: 4px;\n"
                                                  "}\n"
                                                  "QPushButton:pressed\n"
                                                  "{\n"
                                                  "background-color: rgba(22, 184, 98,1)\n"
                                                  "}")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 481, 221))
        self.groupBox_3.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size:15;\n"
                                      "")
        self.tableWidget_matrixA = QTableWidget(self.groupBox_3)
        if self.tableWidget_matrixA.columnCount() < 7:
            self.tableWidget_matrixA.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_matrixA.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if self.tableWidget_matrixA.rowCount() < 5:
            self.tableWidget_matrixA.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_matrixA.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(0, 6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(1, 6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(3, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_matrixA.setItem(4, 1, __qtablewidgetitem21)
        self.tableWidget_matrixA.setObjectName(u"tableWidget_matrixA")
        self.tableWidget_matrixA.setGeometry(QRect(40, 40, 361, 161))
        self.tableWidget_matrixA.setStyleSheet(u"color: white;\n"
                                               "")
        self.tableWidget_matrixA.setShowGrid(True)
        self.tableWidget_matrixA.setRowCount(5)
        self.tableWidget_matrixA.setColumnCount(7)
        self.tableWidget_matrixA.horizontalHeader().setVisible(False)
        self.tableWidget_matrixA.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_matrixA.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_matrixA.verticalHeader().setVisible(False)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 230, 481, 221))
        self.groupBox_4.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size:15;\n"
                                      "")
        self.tableWidget_new_matrixA = QTableWidget(self.groupBox_4)
        if self.tableWidget_new_matrixA.columnCount() < 7:
            self.tableWidget_new_matrixA.setColumnCount(7)
        if self.tableWidget_new_matrixA.rowCount() < 5:
            self.tableWidget_new_matrixA.setRowCount(5)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(0, 6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(2, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(3, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_new_matrixA.setItem(4, 0, __qtablewidgetitem32)
        self.tableWidget_new_matrixA.setObjectName(u"tableWidget_new_matrixA")
        self.tableWidget_new_matrixA.setGeometry(QRect(40, 40, 361, 161))
        self.tableWidget_new_matrixA.setStyleSheet(u"color: white;\n"
                                                   "")
        self.tableWidget_new_matrixA.setRowCount(5)
        self.tableWidget_new_matrixA.setColumnCount(7)
        self.tableWidget_new_matrixA.horizontalHeader().setVisible(False)
        self.tableWidget_new_matrixA.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_new_matrixA.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_new_matrixA.verticalHeader().setVisible(False)
        self.tableWidget_new_matrixA.verticalHeader().setHighlightSections(True)
        self.tableWidget_new_matrixA.verticalHeader().setStretchLastSection(False)
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 700, 481, 221))
        self.groupBox_6.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size:15;\n"
                                      "")
        self.tableWidget_new_matrixB = QTableWidget(self.groupBox_6)
        if self.tableWidget_new_matrixB.columnCount() < 5:
            self.tableWidget_new_matrixB.setColumnCount(5)
        if self.tableWidget_new_matrixB.rowCount() < 4:
            self.tableWidget_new_matrixB.setRowCount(4)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(0, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(0, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(0, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(0, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(0, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(2, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_new_matrixB.setItem(3, 0, __qtablewidgetitem40)
        self.tableWidget_new_matrixB.setObjectName(u"tableWidget_new_matrixB")
        self.tableWidget_new_matrixB.setGeometry(QRect(40, 40, 361, 131))
        self.tableWidget_new_matrixB.setStyleSheet(u"color: white;\n"
                                                   "")
        self.tableWidget_new_matrixB.setRowCount(4)
        self.tableWidget_new_matrixB.setColumnCount(5)
        self.tableWidget_new_matrixB.horizontalHeader().setVisible(False)
        self.tableWidget_new_matrixB.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_new_matrixB.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget_new_matrixB.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_new_matrixB.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_new_matrixB.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_new_matrixB.verticalHeader().setVisible(False)
        self.tableWidget_new_matrixB.verticalHeader().setStretchLastSection(False)
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 470, 481, 221))
        self.groupBox_5.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size:15;\n"
                                      "")
        self.tableWidget_matrixB = QTableWidget(self.groupBox_5)
        if self.tableWidget_matrixB.columnCount() < 5:
            self.tableWidget_matrixB.setColumnCount(5)
        if self.tableWidget_matrixB.rowCount() < 4:
            self.tableWidget_matrixB.setRowCount(4)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(0, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(0, 3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(0, 4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(1, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(2, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_matrixB.setItem(3, 0, __qtablewidgetitem48)
        self.tableWidget_matrixB.setObjectName(u"tableWidget_matrixB")
        self.tableWidget_matrixB.setGeometry(QRect(40, 40, 361, 131))
        self.tableWidget_matrixB.setStyleSheet(u"color: white;\n"
                                               "")
        self.tableWidget_matrixB.setRowCount(4)
        self.tableWidget_matrixB.setColumnCount(5)
        self.tableWidget_matrixB.horizontalHeader().setVisible(False)
        self.tableWidget_matrixB.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_matrixB.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_matrixB.verticalHeader().setVisible(False)
        self.tableWidget_matrixB.verticalHeader().setStretchLastSection(False)
        self.btn_info = QPushButton(self.centralwidget)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setEnabled(True)
        self.btn_info.setGeometry(QRect(880, 0, 51, 41))
        icon1 = QIcon()
        icon1.addFile(u"img/matrinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info.setIcon(icon1)
        self.btn_info.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Curse project: Generate and modificate matrix", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow",
                                                          u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f "
                                                          u"\u0438 "
                                                          u"\u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446"
                                                          u"\u0438\u044f \u041c\u0430\u0442\u0440\u0438\u0446\u044b "
                                                          u"\u0410",
                                                          None))
        self.btn_generate_matrixA.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446"
                                                                     u"\u0438\u044f "
                                                                     u"\u043c\u0430\u0442\u0440\u0438\u0446\u044b "
                                                                     u"\u0410",
                                                                     None))
        self.btn_modificate_matrixA.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u041c\u043e\u0434\u0438\u0444\u0438\u043a"
                                                                       u"\u0430\u0446\u0438\u044f "
                                                                       u"\u043c\u0430\u0442\u0440\u0438\u0446\u044b "
                                                                       u"\u0410",
                                                                       None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f "
                                                            u"\u0438 "
                                                            u"\u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446"
                                                            u"\u0438\u044f \u041c\u0430\u0442\u0440\u0438\u0446\u044b "
                                                            u"B",
                                                            None))
        self.btn_generate_matrixB.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446"
                                                                     u"\u0438\u044f "
                                                                     u"\u043c\u0430\u0442\u0440\u0438\u0446\u044b B",
                                                                     None))
        self.btn_modificate_matrixB.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u041c\u043e\u0434\u0438\u0444\u0438\u043a"
                                                                       u"\u0430\u0446\u0438\u044f "
                                                                       u"\u043c\u0430\u0442\u0440\u0438\u0446\u044b B",
                                                                       None))
        self.groupBox_3.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0410 (5x7)", None))

        __sortingEnabled = self.tableWidget_matrixA.isSortingEnabled()
        self.tableWidget_matrixA.setSortingEnabled(False)
        self.tableWidget_matrixA.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0410 (5x7) "
                                                            u"\u043f\u043e\u0441\u043b\u0435 "
                                                            u"\u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446"
                                                            u"\u0438\u0438",
                                                            None))

        __sortingEnabled1 = self.tableWidget_new_matrixA.isSortingEnabled()
        self.tableWidget_new_matrixA.setSortingEnabled(False)
        self.tableWidget_new_matrixA.setSortingEnabled(__sortingEnabled1)

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0412 (4x5) "
                                                            u"\u043f\u043e\u0441\u043b\u0435 "
                                                            u"\u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446"
                                                            u"\u0438\u0438",
                                                            None))

        __sortingEnabled2 = self.tableWidget_new_matrixB.isSortingEnabled()
        self.tableWidget_new_matrixB.setSortingEnabled(False)
        self.tableWidget_new_matrixB.setSortingEnabled(__sortingEnabled2)

        self.groupBox_5.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0412 (4x5)", None))

        __sortingEnabled3 = self.tableWidget_matrixB.isSortingEnabled()
        self.tableWidget_matrixB.setSortingEnabled(False)
        self.tableWidget_matrixB.setSortingEnabled(__sortingEnabled3)

        self.btn_info.setText("")
    # retranslateUi
