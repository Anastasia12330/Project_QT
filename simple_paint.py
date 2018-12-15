# импортируем несколько модулей
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QPixmap, QColor
from PyQt5.QtCore import Qt, QPoint, QRect

# создаю константы
TOP = 400
LEFT = 400
WIDTH = 800
HEIGHT = 600


# создаю класс Window, который наследуется от класса QMainWindow
class Window(QMainWindow):
    def __init__(self):
        # строка вызывает конструктор родительского класса
        super().__init__()

        # создаю название окна
        self.setWindowTitle("Simple Paint")
        # задаю его размеры
        self.setGeometry(TOP, LEFT, WIDTH, HEIGHT)
        # добавляю иконку
        self.setWindowIcon(QIcon("icons/paint.png"))
        # создаю место, где буду рисовать
        self.image = QImage(self.size(), QImage.Format_RGB32)
        # заполняю его белым цветом
        self.image.fill(Qt.white)

        # делаю так, чтобы при открытии мы могли рисовать черной кисточкой с толщиной 2
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        # создаем меню
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")
        eraser = mainMenu.addMenu('Eraser')

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        onepxAction = QAction(QIcon("icons/onepx.png"), "1px", self)
        onepxAction.setShortcut("Ctrl+O")
        brushMenu.addAction(onepxAction)
        onepxAction.triggered.connect(self.onePx)

        threepxAction = QAction(QIcon("icons/threepx.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+Q")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        elevenpxAction = QAction(QIcon("icons/elevenpx.png"), "11px", self)
        elevenpxAction.setShortcut("Ctrl+W")
        brushMenu.addAction(elevenpxAction)
        elevenpxAction.triggered.connect(self.elevenPx)

        thirteenpxAction = QAction(QIcon("icons/thirteenpx.png"), "13px", self)
        thirteenpxAction.setShortcut("Alt+R")
        brushMenu.addAction(thirteenpxAction)
        thirteenpxAction.triggered.connect(self.thirteenPx)

        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        blueAction = QAction(QIcon("icons/blue.png"), "Blue", self)
        blueAction.setShortcut("Ctrl+L")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blueColor)

        cyanAction = QAction(QIcon("icons/cyan.png"), "Cyan", self)
        cyanAction.setShortcut("Ctrl+H")
        brushColor.addAction(cyanAction)
        cyanAction.triggered.connect(self.cyanColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        grayAction = QAction(QIcon("icons/gray.png"), "Gray", self)
        grayAction.setShortcut("Ctrl+A")
        brushColor.addAction(grayAction)
        grayAction.triggered.connect(self.grayColor)

        amberAction = QAction(QIcon("icons/amber.png"), "Amber", self)
        amberAction.setShortcut("Ctrl+D")
        brushColor.addAction(amberAction)
        amberAction.triggered.connect(self.amberColor)

        brownAction = QAction(QIcon("icons/brown.png"), "Brown", self)
        brownAction.setShortcut("Ctrl+M")
        brushColor.addAction(brownAction)
        brownAction.triggered.connect(self.brownColor)

        eggplantAction = QAction(QIcon("icons/eggplant.png"), "Eggplant", self)
        eggplantAction.setShortcut("Ctrl+Z")
        brushColor.addAction(eggplantAction)
        eggplantAction.triggered.connect(self.eggplantColor)

        fuchsiaAction = QAction(QIcon("icons/fuchsia.png"), "Fuchsia", self)
        fuchsiaAction.setShortcut("Ctrl+J")
        brushColor.addAction(fuchsiaAction)
        fuchsiaAction.triggered.connect(self.fuchsiaColor)

        oliveAction = QAction(QIcon("icons/olive.png"), "Olive", self)
        oliveAction.setShortcut("Ctrl+P")
        brushColor.addAction(oliveAction)
        oliveAction.triggered.connect(self.oliveColor)

        purpleAction = QAction(QIcon("icons/purple.png"), "Purple", self)
        purpleAction.setShortcut("Ctrl+I")
        brushColor.addAction(purpleAction)
        purpleAction.triggered.connect(self.purpleColor)

        sapphireAction = QAction(QIcon("icons/sapphire.png"), "Sapphire", self)
        sapphireAction.setShortcut("Ctrl+V")
        brushColor.addAction(sapphireAction)
        sapphireAction.triggered.connect(self.sapphireColor)

        limeAction = QAction(QIcon("icons/lime.png"), "Lime", self)
        limeAction.setShortcut("Ctrl+U")
        brushColor.addAction(limeAction)
        limeAction.triggered.connect(self.limeColor)

        palebrownAction = QAction(QIcon("icons/palebrown.png"), "Pale Brown", self)
        palebrownAction.setShortcut("Ctrl+K")
        brushColor.addAction(palebrownAction)
        palebrownAction.triggered.connect(self.palebrownColor)

        pinkAction = QAction(QIcon("icons/pink.png"), "Pink", self)
        pinkAction.setShortcut("Ctrl+X")
        brushColor.addAction(pinkAction)
        pinkAction.triggered.connect(self.pinkColor)

        orangeAction = QAction(QIcon("icons/orange.png"), "Orange", self)
        orangeAction.setShortcut("Alt+Q")
        brushColor.addAction(orangeAction)
        orangeAction.triggered.connect(self.orangeColor)

        khakiAction = QAction(QIcon("icons/khaki.png"), "Khaki", self)
        khakiAction.setShortcut("Alt+W")
        brushColor.addAction(khakiAction)
        khakiAction.triggered.connect(self.khakiColor)

        goldAction = QAction(QIcon("icons/gold.png"), "Gold", self)
        goldAction.setShortcut("Alt+G")
        brushColor.addAction(goldAction)
        goldAction.triggered.connect(self.goldColor)

        eraserAction = QAction(QIcon("icons/eraser.png"), "Eraser", self)
        eraserAction.setShortcut("Ctrl+E")
        eraser.addAction(eraserAction)
        eraserAction.triggered.connect(self.eraser)

    #   согласовываем действия с мышкой
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            # позиция мышки
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    # сохранение файла
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL FILES(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    # отчистка
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    #  задаем размер кисти
    def onePx(self):
        self.brushSize = 1

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def elevenPx(self):
        self.brushSize = 11

    def thirteenPx(self):
        self.brushSize = 13

    # задаем цвет
    def blackColor(self):
        self.brushColor = QColor('#000000')

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def blueColor(self):
        self.brushColor = Qt.blue

    def cyanColor(self):
        self.brushColor = Qt.cyan

    def eraser(self):
        self.brushColor = Qt.white

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def grayColor(self):
        self.brushColor = Qt.gray

    def amberColor(self):
        self.brushColor = QColor('#ffbf00')

    def brownColor(self):
        self.brushColor = QColor('#964b00')

    def eggplantColor(self):
        self.brushColor = QColor('#990066')

    def fuchsiaColor(self):
        self.brushColor = QColor('#ff00ff')

    def oliveColor(self):
        self.brushColor = QColor('#808000')

    def purpleColor(self):
        self.brushColor = QColor('#800080')

    def sapphireColor(self):
        self.brushColor = QColor('#082567')

    def limeColor(self):
        self.brushColor = QColor('#ccff00')

    def palebrownColor(self):
        self.brushColor = QColor('#987654')

    def pinkColor(self):
        self.brushColor = QColor('#ffc0cb')

    def orangeColor(self):
        self.brushColor = QColor('#ffa500')

    def khakiColor(self):
        self.brushColor = QColor('#bdb76b')

    def goldColor(self):
        self.brushColor = QColor('#ffd700')


# запускаем программу для появления приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()