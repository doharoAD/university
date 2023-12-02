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
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTableWidgetItem
from grafical_user_interface import Ui_MainWindow
from class_matrix import ModifiedMatrix, AnotherModifiedMatrix


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
        self.matrA.replace_zeros_in_third_column()
        self.gui.tableWidget_new_matrixA.setRowCount(self.matrA.rows)
        self.gui.tableWidget_new_matrixA.setColumnCount(self.matrA.cols)
        for i in range(self.matrA.rows):
            for j in range(self.matrA.cols):
                item = QTableWidgetItem(str(self.matrA.data[i][j]))
                self.gui.tableWidget_new_matrixA.setItem(i, j, item)

    # функция заполнения таблицы tableWidget_matrixB сгенерированной матрицей В(4х5)
    def input_martixA_in_tableB(self):
        self.matrB = AnotherModifiedMatrix(4, 5)
        self.gui.tableWidget_matrixB.setRowCount(self.matrB.rows)
        self.gui.tableWidget_matrixB.setColumnCount(self.matrB.cols)
        for i in range(self.matrB.rows):
            for j in range(self.matrB.cols):
                item = QTableWidgetItem(str(self.matrB.data[i][j]))
                self.gui.tableWidget_matrixB.setItem(i, j, item)

    # функция для замены всех единиц в пятом столбце на нули
    def input_matrixB_in_modificate_tableB(self):
        self.matrB.replace_ones_in_fifth_column()
        self.gui.tableWidget_new_matrixB.setRowCount(self.matrB.rows)
        self.gui.tableWidget_new_matrixB.setColumnCount(self.matrB.cols)
        for i in range(self.matrB.rows):
            for j in range(self.matrB.cols):
                item = QTableWidgetItem(str(self.matrB.data[i][j]))
                self.gui.tableWidget_new_matrixB.setItem(i, j, item)

    # функция для изменения интерфейса
    def init_GUI(self):
        # добавление иконки окна
        self.setWindowIcon(QIcon('путь к файлу'))

        # кнопка заполнения матрицы А
        self.gui.btn_generate_matrixA.clicked.connect(self.input_martixA_in_tableA)

        # кнопка заполнения модифицированной матрицы А
        self.gui.btn_modificate_matrixA.clicked.connect(self.input_matrixA_in_modificate_tableA)

        # кнопка заполнения матрицы В
        self.gui.btn_generate_matrixB.clicked.connect(self.input_martixA_in_tableB)

        # кнопка заполнения модифицированной матрицы В
        self.gui.btn_modificate_matrixB.clicked.connect(self.input_matrixB_in_modificate_tableB)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CurseProjectWinApp()
    application.show()
    sys.exit(app.exec())
