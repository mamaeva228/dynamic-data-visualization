import sys
""" особый модуль sys(обеспечивает доступ к некоторым переменным, используемым  интерпретатором, и к функциям, которые  взаимодействуют с ним)"""
import argparse
""" модуль определяет какие аргументы требуются и генерирует справки и сообщ об ошибке,
с помощью него могу управлять компом так как через командную строку"""
import pandas as pd
""" импотируем pandas(это высокоуровневая Python библиотека для анализа и визуализации, в виде всевозможных графиков, данных)
под псевдонимом pd"""
from PySide2.QtCore import (QAbstractTableModel, QDateTime, QModelIndex,
                            Qt, QTimeZone, Slot)# Slot
""" 

QAbstractTableModel-предоставляет абстрактную модель, его наследники-таблицы.
Объект QDateTime содержит дату календаря и время часов («время-дата»). Это комбинация классов QDate и QTime.
Он может читать текущую дату и время из системных часов. Он предоставляет функции для сравнения даты и времени и манипуляции с датой, добавляя количество секунд,
дни, месяцы или годы.
QModelIndex-размещение данных в моделе данных(сопоставление данных модели данных созданному по особому алгоритму индексному ряду)
Qt-ПРОСТРАНСТВО ИМЕН, Содержит различные идентификаторы, используемые по всей библиотеке Qt
QTimeZone-Класс конвертирует между UTC и местным временем в конкретной временной зоне.
Этот класс предоставляет калькулятор без сохранения состояния для преобразования часового пояса между UTC и местным временем в определенном часовом поясе.
"""
from PySide2.QtGui import QColor, QPainter
""" QColor- Цвета, основанные на значениях цветовых моделей RGB, HSV или CMYK
QPainter-Выполняет низкоуровневое рисование на виджетах и других устройствах рисования

"""
from PySide2.QtWidgets import (QAction, QApplication, QHBoxLayout, QVBoxLayout,
                               QHeaderView,
                               QMainWindow, QSizePolicy, QTableView, QWidget, QSplitter)
""" 
Класс QAction предоставляет абстрактное действие пользовательского интерфейса, которое может быть вставлено в виджеты.
Класс QApplication руководит управляющей логикой ГПИ(граф. пользоват. интерфейс) и основными настройками
Класс QHBoxLayout выстраивает виджеты в горизонтальную линию,
Класс QHeaderView предоставляет строку заголовка или столбец заголовка для представлений элементов.
QMainWindow-Главное окно предоставляет структуру для создания пользовательского интерфейса приложения. Qt имеет
класс QMainWindow и связанные с ним классы для управления главным окном
Класс QSizePolicy описываtn политику горизонтального и вертикального изменения размера виджета
QTableView используется для предоставления данных в виде визуальных таблиц, который ранее были предоставлен классом QTable, но с использованием более гибкого подхода,
Класс QWidget является базовым для всех объектов пользовательского интерфейса

"""
from PySide2.QtCharts import QtCharts
"""QtCore, QtGui-основные модули PyQt, содержащие различные классы 

QtCore-основные не графические классы: система сигналов и слотов
QtGui — компоненты графического интерфейса
Основные виджеты расположены в PyQt5.QtWidgets
Основные графики в QtCharts

"""
class CustomTableModel(QAbstractTableModel):#CustomTableModel
    def __init__(self, data=None):#Обычно функция определяется с помощью инструкции def
        """в конструкторе класса CustomTableModel я запускаю конструктор класса QAbstractTableModel, кот за нас написали
        """
        QAbstractTableModel.__init__(self)
        self.color = None
        self.load_data(data)
        """в моем конструкторе опеределяется сво-во color и вызывается метод load_data """

    def load_data(self, data):
        """ функция load_data структуру из 3 столбцов преобразует в 3 структуры по одному столбцу  """
        self.input_dates = data[0].values
        self.input_magnitudes = data[1].values
        self.input_depth= data[2].values

        self.column_count = 3#Возвращает количество столбцов для дочерних элементов данного родителя 
        self.row_count = len(self.input_dates)
        """Задаются 2 св-ва класса:column_count=3,row_count=длина столбца input_magnitudes, тк у них одинак колво строк """

    def rowCount(self, parent=QModelIndex()):
        """ Возвращает количество строк под указанным родителем"""
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        """ Возвращает количество столбцов под указанным родителем ."""
        return self.column_count

    def headerData(self, section, orientation, role):
        """ Возвращает данные для данной роли и раздела в заголовке с указанной ориентацией.
        Для горизонтальных заголовков номер раздела соответствует номеру столбца. Аналогично, 
        для вертикальных заголовков номер раздела соответствует номеру строки."""
        if role != Qt.DisplayRole:
            """Ключевые данные, которые будут отрисованы в виде текста"""
            return None
        if orientation == Qt.Horizontal:
            """Horizontal значение 1, Vertical-2 """
            return ("Date", "Magnitude","Depth")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        """Возвращает данные, хранящиеся под данной ролью для элемента, на который ссылается индекс. """
        column = index.column()
        row = index.row()#index

        if role == Qt.DisplayRole:
            """Qt.DisplayRole-Ключевые данные, которые будут отрисованы в виде текста, еще могут быть: 
           
            DecorationRole Данные, которые будут отрисованы как украшение в виде пиктограммы. (QColor, QIcon или QPixmap)
            Qt::EditRole Данные в форме, подходящей для редактирования с помощью редактора. (QString)
            Qt::ToolTipRole Данные отображаемые в подсказке к элементу. (QString)
            Qt::StatusTipRole Данные отображаемые в строке статуса. (QString)
            Qt::WhatsThisRole Данные отображаемые для элемента в режиме "Что это?". (QString)
            Qt::SizeHintRole Предпочитаемый размер для элемента, который будет применен в представлении. (QSize)
            """
            if column == 0:
                raw_date = self.input_dates[row]#input_dates[row]
                date = "{}".format(raw_date.toPython())
                """Подстановку данных можно сделать с помощью форматирования строк. Форматирование можно сделать с помощью оператора %, либо с помощью метода format"""
                return date[:-3]
            elif column == 1:
                return "{:.2f}".format(self.input_magnitudes[row])
            elif column==2:
                return "{:.2f}".format(self.input_depth[row])

        elif role == Qt.BackgroundRole:
            """Кисть фона используемая для отрисовки элементов с делегатом по умолчанию """
            return (QColor(Qt.white), QColor(self.color), QColor(self.color))[column]
            """QColor предоставляет цвета"""
        elif role == Qt.TextAlignmentRole:
            """Выравнивание текста для отрисовки элементов с делегатом по умолчанию """
            return Qt.AlignRight
            """Выравнивание по правому краю"""
        return None


class Widget(QWidget):
    """ Класс QWidget является базовым для всех объектов пользовательского интерфейса
    Виджет - это элементарный объект пользовательского интерфейса:
    он получает события мыши, клавиатуры и другие события от оконной системы и рисует свое изображение на экране.
    """
    def __init__(self, data):
        QWidget.__init__(self)
        """ получение модели """
        self.model = CustomTableModel(data)
        """переходим в класс CustomTableModel и создаем объект-таблицу, model-часть класса с помощью которого работаем с данными,имя поля-model  """
        self.table_view = QTableView()
        """полностью устраивает класс  QTableView поэтому доп конструкторов и ф-ций не пишем, а просто создаем и он поле нашего класса, имя поля-table_view  """
        self.table_view.setModel(self.model)
        """может рисовать таблицу в соотвествие с полученными данными(3 столбца, нужные числа и тд) """
        resize = QHeaderView.ResizeToContents
        """ Класс QHeaderView предоставляет строку заголовка или столбец заголовка для представлений элементов, заголовок маштабируется """
        self.horizontal_header = self.table_view.horizontalHeader()

        self.vertical_header = self.table_view.verticalHeader()

        self.horizontal_header.setSectionResizeMode(resize)

        self.vertical_header.setSectionResizeMode(resize)

        self.horizontal_header.setStretchLastSection(True)
        """ Формируется данные для рисования заголовка  """

        """создание графика 
        модуль QtChart предоставляет множество типов графиков и опций для графического представления данных. 
        """

        self.chart1 = QtCharts.QChart()
        """нас устраивает класс QChart полностью, доп методы и консрукторы не нужны """
        self.chart1.setAnimationOptions(QtCharts.QChart.AllAnimations)
        """ установить параметры анимации, запускается рисование """
        self.add_series("Значение", [0,1] ,self.chart1)
        
        """подготовка вкладки на кот размещена диаграмма """
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size.setHorizontalStretch(4)
        #-----------------------------------------
        self.chart_view1 = QtCharts.QChartView(self.chart1)
        """подготовка визуализации продолжается """
        self.chart_view1.setRenderHint(QPainter.Antialiasing)
        
        #self.chart_view1.setSizePolicy(size)
        minWidth = 400
        self.chart_view1.setMinimumWidth(minWidth)
        
        
        #-----------------------------------------------------
        self.chart2 = QtCharts.QChart()
        self.chart2.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.add_series("Глубина", [0,2],self.chart2)#данные для каждого графика
        self.chart_view2 = QtCharts.QChartView(self.chart2)
        """подготовка визуализации продолжается """
        self.chart_view2.setRenderHint(QPainter.Antialiasing)
        """ QWidget расположение """
        """ правое расположение """
        #self.chart_view2.setSizePolicy(size)
        self.chart_view2.setMinimumWidth(minWidth)

        self.main_layout = QHBoxLayout()
        self.splitter = QSplitter()


        dateColumn = 0
        magColumn = 1
        depthsColumn = 2
        
        xDates = self.getDateAsCategoricalColumn(dateColumn)
        yMagnitudes = self.getFloatColumn(magColumn)
        yDepths = self.getFloatColumn(depthsColumn)

        
        bc1 = self.createBarCharts(xDates, yMagnitudes, yDepths)
        bar1ChartView = QtCharts.QChartView(bc1)
        bar1ChartView.setRenderHint(
            QPainter.Antialiasing)

                
        chartViewsHbox = QHBoxLayout()
        chartViewsHbox.addWidget(self.chart_view1)        
        chartViewsHbox.addWidget(self.chart_view2)

        vbox = QVBoxLayout()
        vbox.addLayout(chartViewsHbox)
        vbox.addWidget(bar1ChartView)

        #self.main_layout.addLayout(vbox)

        vboxWidget = QWidget()
        vboxWidget.setLayout(vbox)
        self.splitter.addWidget(vboxWidget)

        #self.main_layout.addWidget(self.table_view)
        #КУДА.addWidget(ЧТО)

        self.splitter.addWidget(self.table_view)

        self.main_layout.addWidget(self.splitter)
        
        self.setLayout(self.main_layout) # установить макет на QWidget """
        #-----------------------------------------------------
        """ левое расположение """
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
    def createBarCharts(self, x, y1, y2):
        barSet1 = QtCharts.QBarSet("Magnitude")
        barSet1.append(y1)

        barSet2 = QtCharts.QBarSet("Depths")
        barSet2.append(y2)
        
        barSeries1 = QtCharts.QBarSeries()
        barSeries1.append(barSet1)
        barSeries1.append(barSet2)
        
        barChart1 = QtCharts.QChart()
        barChart1.addSeries(barSeries1)
        barChart1.setTitle("my first bar chart")
        barChart1.setAnimationOptions(
            QtCharts.QChart.SeriesAnimations)

        categories = x
        barCategoryAxis = QtCharts.QBarCategoryAxis()
        barCategoryAxis.append(categories)
        barChart1.createDefaultAxes()
        barChart1.setAxisX(barCategoryAxis,
                           barSeries1)

        barChart1.legend().setVisible(True)
        barChart1.legend().setAlignment(Qt.AlignTop)

        return barChart1

    def getFloatColumn(self, column):

        res = []
        
        for i in range(self.model.rowCount()):
            # print("checking the data...", i, self.model.index(i, column).data())
            
            y = float(self.model.index(i, column).data())
            res.append(y)          
                
        return res

    def getDateAsCategoricalColumn(self, column):

        res = []
        
        for i in range(self.model.rowCount()):      
            t = self.model.index(i, column).data()
            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz" 
            #outDateFormat = "dd.MM.yyyy (h:mm)"
            outDateFormat = date_fmt
            
            # x = float(QDateTime().fromString(t, date_fmt).toMSecsSinceEpoch())
            x = QDateTime().fromString(t, date_fmt).toString(outDateFormat)
            res.append(x)          
            
            # y = float(self.model.index(i, columns[1]).data())

            # потому что сложно рисовать график с минусовой осью ???
            # if x > 0 and y > 0: 
                # self.series.append(x, y)
            
                
        return res
        
        
        
    def add_series(self, name, columns, chart):#выходит add.series так написан что по Ох автоматически будет дата?

        """ Формирует название оси """
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        """ формирует 1 массив series из 2 столбцов, добавляя в него данные из Х и У """
        for i in range(self.model.rowCount()):

            """ получение даты """
            t = self.model.index(i, 0).data()#типа нулевой столбец(дата) и в нем по строкам  будем переходить с помощью цикла этого
            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"#но вообще тут уже прописано как бы что в нулевом столбце будет дата

            #x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
            x = float(QDateTime().fromString(t, date_fmt).toMSecsSinceEpoch())
            #x = QDateTime().fromString("2019-01-01 12:00:00.100", date_fmt).toMSecsSinceEpoch() 

            # не работает:
            # QLineSeries.append(x, y) ждёт float-ов, а не QDateTime()
            # x = QDateTime().fromString(t, date_fmt)
            
            y = float(self.model.index(i, columns[1]).data())

            # print(x, y)

            # потому что сложно рисовать график с минусовой осью ???
            if x > 0 and y > 0: 
                self.series.append(x, y)




            
        chart.addSeries(self.series)

        """ задание оси X """
        #self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x = QtCharts.QValueAxis()
        """ Класс QDateTimeAxis добавляет даты и время к оси диаграммы. """
        self.axis_x.setTickCount(6)
        """setTickCounе( int count ) устанавливает количество отметок на оси для подсчета, на оси Х будет 10 штрихов """
        #self.axis_x.setFormat("dd.MM.yy hh:mm:ss")
        """ setFormat - задаёт формат вывод текстового представления значения. """
        self.axis_x.setTitleText("Дата")
        chart.addAxis(self.axis_x, Qt.AlignBottom)
        """ Добавляет ось оси к диаграмме, выровненной, как указано выравниванием. """
        self.series.attachAxis(self.axis_x)
        """ Возвращает, true если ось была успешно присоединена, false в противном случае. """

        """ задание оси Y """
        self.axis_y = QtCharts.QValueAxis() 
        """ Класс QValueAxis добавляет значения к осям диаграммы. """
        self.axis_y.setTickCount(6)
        """ Свойство setTickCount содержит количество отметок на оси. Это указывает, сколько линий сетки нарисовано на графике. """
        self.axis_y.setLabelFormat("%.2f")
        """ Свойство setLabelFormat содержит формат метки оси. """
        self.axis_y.setTitleText(name)#изменила название оси, что ифами написать, как обратиться к имени той колонки которую я в параметры передаю?
        chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        """ получение цвета из QC  hart для использования в QTableView, будет выделять столбец таблицы тем же цветом что и линия в диарамме!! """
        self.model.color = "{}".format(self.series.pen().color().name())


def transform_date(utc, timezone=None):
    """значение timezone по умолчаннию=None, timezone-не обязательный параметр """
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    """ Класс QDateTime предоставляет функции даты и времени.
    Функция fromString () возвращает QDateTime , учитывая строку и формат даты, используемый для интерпретации даты в строке,
    ИЗ СТРОКИ ВОЗВРАЩАЕТ ДАТУ В ЧИСЛОВОМ ФОРМАТЕ
    
    """ 
    if timezone:
        new_date.setTimeZone(timezone)
        """ setTimeZone Возвращает часовой пояс даты и времени, произведет преобразования с числом, добавив или отнимит какое число
        в зависимости от зоны
        """
    return new_date
    """ возвращается модифицированная дата """


def read_data(fname):
    # Считать содержимое CSV 
    df = pd.read_csv(fname)
    """df-переменная содержащая данные файла, в нее их закачивает метод read_csv(), если csv изменить Exel то csv не работает
    fname-параметр, у нас в программе это путь к файлу
    """

    # Удалить неправильные величины 
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]
    """в список magnitudes записываются из столбца mag"""

    #  Мой местный часовой пояс 
    timezone = QTimeZone(b"Europe/Berlin")

    # Получить временную метку, преобразованную в наш часовой пояс
    times = df["time"].apply(lambda x: transform_date(x, timezone))
    """запускается функция transform_date """

    depth=df["depth"]
    """ в depth записываются значения из столбца"depth" """

    return times, magnitudes, depth
"""сформировалось 3 списка times, magnitudes, depth -остальные столбцы игнорируются"""


class MainWindow(QMainWindow):
    def __init__(self, widget):
        """конструктор наешго класса, в нем мы запускаем конструктор прописанного класса QMainWindow """
        QMainWindow.__init__(self)
        self.setWindowTitle("Eartquakes information")
        """ Виджет без родительского виджета всегда является независимым окном 
        Для таких виджетов setWindowTitle() и setWindowIcon() устанавливают заголовок окна и иконку"""

        #  Меню
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        """ addMenu (), чтобы вставить меню в строку меню. """

        # Выход QAction(«Выход», чтобы закрыть окно)
        exit_action = QAction("Exit", self)#объект exit_action, создаю эл-т интерфейса
        exit_action.setShortcut("Ctrl+Q")
        """ setShortcut Устанавливает платформозависимый список горячих клавиш, основанный на клавише key.
        Если требуется только первичная комбинация горячих клавиш, то используйте вместо этого setShortcut. """
        exit_action.triggered.connect(self.exit_app)
        #""" закрепление за действием метода exit_app """
        self.file_menu.addAction(exit_action)

        # Строка состояния
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Размеры окна
        geometry = app.desktop().availableGeometry(self)
        # self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.9)
        self.setFixedSize(geometry.width(), geometry.height() * 0.9)
        self.setCentralWidget(widget)

    @Slot()#что это
    def exit_app(self, checked):
        sys.exit()


if __name__ == "__main__":
    """ выполнение прог-мы начинается отсюда"""
    # options = argparse.ArgumentParser()
    # options.add_argument("-f", "--file", type=str, required=True)
    # args = options.parse_args()
    # data = read_data(args.file)
    # data = read_data("C:/Users/79687/Downloads/all_hour.csv") #НАДО МЕНЯТЬ СЛЭШ С ТАКОГО "/" НА "\" В ЭТОМ ЯЗЫКЕ
    # data = read_data("C:/Users/79687/Downloads/all_hour.csv") #НАДО МЕНЯТЬ СЛЭШ С ТАКОГО "/" НА "\" В ЭТОМ ЯЗЫКЕ
    data = read_data("all_hour.csv") #НАДО МЕНЯТЬ СЛЭШ С ТАКОГО "/" НА "\" В ЭТОМ ЯЗЫКЕ
    

    # Qt Application
    app = QApplication(sys.argv)
    """запускает окно, его определит параметр sys.argv """
    # QWidget
    widget = Widget(data)# мб сюда как парметр передавать столбцы кот для граф нужны
    """data-данные ф-ции read_data, тоесть 3 столбца из файла """
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)

    window.show()
    """рисует все на экране """
    sys.exit(app.exec_())
    """осуществляет процесс корректного закрытия приложения """

