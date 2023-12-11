"""
Работу выполнил студент группы Иэозс-62-22 Муратов Артемий Денисович

ЗАДАЧА:
Разработать оконное приложение для консольной программы из пр56. 
Условие задачи из пр56:

Заменить в третьем столбце матрицы A (5×7) все нули на единицы,
а в пятом столбце матрицы  B (4×5) — все единицы на нули
"""
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem

from class_matrix import ModifiedMatrix, AnotherModifiedMatrix
from grafical_user_interface import Ui_MainWindow


class CurseProjectWinApp(QtWidgets.QMainWindow):
    def __init__(self):
        # super - возвращает объект родителя класса CurseProjectWinApp  и вызывает его конструктор
        super(CurseProjectWinApp, self).__init__()
        # экземпляры для отрисовки окна
        self.matrB = None
        self.matrA = None
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.init_GUI()

    # функция заполнения таблицы tableWidget_matrixA сгенерированной матрицей А(5х7)
    def input_martixA_in_tableA(self):
        self.matrA = ModifiedMatrix(5, 7)
        self.gui.tableWidget_matrixA.setRowCount(self.matrA.rows)
        self.gui.tableWidget_matrixA.setColumnCount(self.matrA.cols)
        for i in range(self.matrA.rows):
            for j in range(self.matrA.cols):
                item = QTableWidgetItem(str(self.matrA.data[i][j]))
                self.gui.tableWidget_matrixA.setItem(i, j, item)

    # функция замены всех нулей в третьем столбце на единицы
    def input_matrixA_in_modificate_tableA(self):
        # булевая переменная - флаг, с помощью которого будет проводится проверка условия
        zero_in_third_column = False
        # проверяем элементы 3го столбца,  есть ли 0, если есть то меняем флаг и выходим досрочно
        for i in range(self.matrA.rows):
            if self.matrA.data[i][2] == 0:
                zero_in_third_column = True
                break
        # если флаг True,  то меняем 0 на 1 и заполняем таблицу
        if zero_in_third_column:
            self.matrA.replace_zeros_in_third_column()
            self.gui.tableWidget_new_matrixA.setRowCount(self.matrA.rows)
            self.gui.tableWidget_new_matrixA.setColumnCount(self.matrA.cols)
            for i in range(self.matrA.rows):
                for j in range(self.matrA.cols):
                    item = QTableWidgetItem(str(self.matrA.data[i][j]))
                    self.gui.tableWidget_new_matrixA.setItem(i, j, item)

        # иначе выводим сообщение, что 0 в столбце нет
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Исключение")
            msg_box.setText("В сгенерированной матрице А в 3м столбце нет 0\nПожалуйста, создайте новую матрицу А!")
            close_button = QtWidgets.QPushButton("Закрыть")
            msg_box.addButton(close_button, QtWidgets.QMessageBox.AcceptRole)
            msg_box.exec_()

    # функция заполнения таблицы tableWidget_matrixB сгенерированной матрицей В(4х5)
    def input_martixB_in_tableB(self):
        self.matrB = AnotherModifiedMatrix(4, 5)
        self.gui.tableWidget_matrixB.setRowCount(self.matrB.rows)
        self.gui.tableWidget_matrixB.setColumnCount(self.matrB.cols)
        for i in range(self.matrB.rows):
            for j in range(self.matrB.cols):
                item = QTableWidgetItem(str(self.matrB.data[i][j]))
                self.gui.tableWidget_matrixB.setItem(i, j, item)

    # функция для замены всех единиц в пятом столбце на нули
    def input_matrixB_in_modificate_tableB(self):
        # булевая переменная - флаг, с помощью которого будет проводится проверка условия
        ed_in_five_columns = False
        # проверяем элементы 5го столбца,  есть ли 1, если есть то меняем флаг и выходим досрочно
        for i in range(self.matrB.rows):
            if self.matrB.data[i][4] == 1:
                ed_in_five_columns = True
                break
        # если флаг True,  то меняем 1 на 0 и заполняем таблицу
        if ed_in_five_columns:
            self.matrB.replace_ones_in_fifth_column()
            self.gui.tableWidget_new_matrixB.setRowCount(self.matrB.rows)
            self.gui.tableWidget_new_matrixB.setColumnCount(self.matrB.cols)
            for i in range(self.matrB.rows):
                for j in range(self.matrB.cols):
                    item = QTableWidgetItem(str(self.matrB.data[i][j]))
                    self.gui.tableWidget_new_matrixB.setItem(i, j, item)
        # иначе выводим сообщение, что 1 в столбце нет
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Исключение")
            msg_box.setText("В сгенерированной матрице B в 5м столбце нет 1\nПожалуйста, создайте новую матрицу В!")
            close_button = QtWidgets.QPushButton("Закрыть")
            msg_box.addButton(close_button, QtWidgets.QMessageBox.AcceptRole)
            msg_box.exec_()

    # функция для изменения интерфейса
    def init_GUI(self):

        # Всплывающая подсказка при наведении курсора на кнопку, в которой находится изображение
        self.gui.btn_info.setToolTip("Работу выполнил студент группы Иэозс-62-22 Муратов Артемий Денисович.\n"
                                     " ЗАДАЧА:\n"
                                     "Разработать оконное приложение для консольной программы из пр56. Условие задачи "
                                     "\n"
                                     "из пр56: Заменить в третьем столбце матрицы A (5×7) все нули на единицы,\n"
                                     "а в пятом столбце матрицы  B (4×5) — все единицы на нули \n")

        # кнопка заполнения матрицы А
        self.gui.btn_generate_matrixA.clicked.connect(self.input_martixA_in_tableA)

        # кнопка заполнения модифицированной матрицы А
        self.gui.btn_modificate_matrixA.clicked.connect(self.input_matrixA_in_modificate_tableA)

        # кнопка заполнения матрицы В
        self.gui.btn_generate_matrixB.clicked.connect(self.input_martixB_in_tableB)

        # кнопка заполнения модифицированной матрицы В
        self.gui.btn_modificate_matrixB.clicked.connect(self.input_matrixB_in_modificate_tableB)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CurseProjectWinApp()
    application.show()
    sys.exit(app.exec())
