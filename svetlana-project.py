#выводятся автоматически подсказки если импортируем весь модуль
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget

from PySide2.QtWidgets import QAction

from PySide2.QtWidgets import QDockWidget, QListWidget, QTabWidget, QLabel

from PySide2.QtWidgets import QListView


from PySide2.QtGui import QStandardItemModel, QStandardItem

from PySide2.QtWidgets import QGridLayout

from PySide2.QtGui import QImageReader, QIcon


from PySide2.QtCore import Qt


# <div>Icons made by <a href="https://www.flaticon.com/authors/dave-gandy" title="Dave Gandy">Dave Gandy</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/gregor-cresnar" title="Gregor Cresnar">Gregor Cresnar</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
# <div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/egor-rumyantsev" title="Egor Rumyantsev">Egor Rumyantsev</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>



# from PySide2.QtCore import QObject, SIGNAL




#from PySide2.QtWidgets import (QAction, QApplication, QHBoxLayout, QVBoxLayout,
                            #QHeaderView,QHBoxLayout, QLabel,
                            #QMainWindow, QSizePolicy, QTableView, QWidget, QSplitter,QScrollArea)#чтобы класс можно было писать без "QtWidgets." перед ним надо записать его тут
#from PySide2 import QtCore # qtCore надо 2 раза импортировать тк Qt почему то не импортируется если не перечислять его отдельно
#from PySide2.QtCore import (QAbstractTableModel, QDateTime, QModelIndex, Qt, QTimeZone, Slot)
#from PySide2 import QtGui
#from PySide2.QtGui import QColor, QPainter
#from PySide2.QtCharts import QtCharts

import sys
import argparse
import pandas as pd
import copy


##class Graphic(QWidget):#сделать тут ф-цию добавить графики хотя вроде и правильно, надо както сделать чтобы можно было удалить график и длобавить
##    def __init__(self, sheet): 
##        QWidget.__init__(self)
##        self.sheet=sheet# sheet на кт он, график должен знать где он там и настройки и тд
##        self.cc=sheet.Data.columns.values #КАК БЫ МАССИВ ИЗ НАЗВАНИЙ СТОЛБЦОЫ
##        #gg=df[cc[1]].values #КАК БЫ МАССИВ ИЗ ЗНАЧЕНИЙ СТОЛБЦА КТ В МАССИВЕ НАЗВАНИЙ СТОЛБЦОВ ПОД ИНДЕКСОМ 1
##
##        self.graphic_Number=0
##
##        self.main_layout = QVBoxLayout()
##        self.setLayout(self.main_layout)
##    def add_Graphic(self):#ПРЕДПОЛАГАЕТСЯ ЧТО КОМБОБОКС С ВЫБОРОМ СТОЛБЦА УЖЕ ВЫБРАН И МЫ ЧИТАЕМ ЕГО ЗНАЧ ЧЕРЕЗ sheet И ОБРАЩАЕМСЯ К СТОЛБЦУ С ЭТИМ ИНДЕСОМ
##        self.graphic_Number=self.sheet.tip_graphic.currentIndex()+1 #ОЧЕНЬ ВАЖНОЕ ПОЛЕ, ТК ИЗЗА НЕГО ОБЪЕКТ Graphic ЗНАЕТ КАКОЙ ГРАФИК НА НЕМ И НУМЕРАЦИЯ ЭТА ОПРЕДЕЛЯЕТСЯ В self.tip_graphic(ТК ИНДЕКС ЭТОГО КОМБОБОКСА ПЕРЕДАЕМ В ПАРАМЕТР number)
##        if(self.graphic_Number==1):
##            self.add_Chart()
##        elif(self.graphic_Number==2):
##            self.add_BarChart()
##    def add_BarChart(self):#ЭТУ Ф-ЦИЮ МЫ ВЫЗЫВАЕМ ДЛЯ ДОБАВЛЕНИЯ BarChart, ПЕРЕДАЕМ ЕЙ ВСЕ НУЖНЫЕ ПАРАМЕТРЫ И ОНА ПЕРЕДАЕТ ИХ СВОИМ ПОДФУНКЦИЯМ
##        which_col=self.sheet.which_column.currentText()
##        Po_ox=self.sheet.Poka_Ox.currentText()
##        xDates =[]
##        for u in range(len(self.sheet.Data[Po_ox].values)):
##            xDates.append(self.sheet.Data[Po_ox].values[u])
##
##        yMagnitudes =[]
##        for u in range(len(self.sheet.Data[which_col].values)):
##            yMagnitudes.append(self.sheet.Data[which_col].values[u])
##        #yDepths =[]
##        #for u in range(len(self.sheet.Data[self.cc[3]].values)):
##        #    yDepths.append(self.sheet.Data[self.cc[3]].values[u])
##        #bc1 = self.createBarCharts(xDates, yMagnitudes, yDepths)
##
##        bc1 = self.createBarCharts(xDates, yMagnitudes)
##
##        self.bar1ChartView = QtCharts.QChartView(bc1)
##        self.bar1ChartView.setRenderHint(QPainter.Antialiasing)
##        self.main_layout.addWidget(self.bar1ChartView)
##    def createBarCharts(self, x, y1):
##        barSet1 = QtCharts.QBarSet("Magnitude")
##        barSet1.append(y1)
##        #barSet2 = QtCharts.QBarSet("depth")
##        #barSet2.append(y2)
##
##        barSeries1 = QtCharts.QBarSeries()
##        barSeries1.append(barSet1)
##        #barSeries1.append(barSet2)
##
##        barChart1 = QtCharts.QChart()
##        barChart1.addSeries(barSeries1)
##
##        barChart1.setTitle("my first bar chart")
##        barChart1.setAnimationOptions( QtCharts.QChart.SeriesAnimations)
##        categories = x
##        barCategoryAxis = QtCharts.QBarCategoryAxis()
##        barCategoryAxis.append(categories)
##        barChart1.createDefaultAxes()
##        barChart1.setAxisX(barCategoryAxis,
##                            barSeries1)
##        barChart1.legend().setVisible(True)
##        barChart1.legend().setAlignment(Qt.AlignTop)
##        return barChart1
##    def getFloatColumn(self, column):#мб тут возвращать рес как прост то что в дата под выбранным столбцом
##        table = CustomTableModel(self.sheet.Data)
##        res = []
##        for i in range(table.rowCount()):
##            # print("checking the data...", i, self.sheet.Data.index(i, column).data())
##            y = float(table.index(i, column).data())
##            res.append(y)          
##        return res
##    def getDateAsCategoricalColumn(self, column):
##        table = CustomTableModel(self.sheet.Data)
##        res = []
##        for i in range(table.rowCount()):      
##            t = table.index(i, column).data()
##            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz" 
##            outDateFormat = date_fmt
##            x = QDateTime().fromString(t, date_fmt).toString(outDateFormat)
##            res.append(x)          
##        return res
##    #----------------------------------------------
##    def add_Chart(self):#ЭТУ Ф-ЦИЮ МЫ ВЫЗЫВАЕМ ДЛЯ ДОБАВЛЕНИЯ Chart, ПЕРЕДАЕМ ЕЙ ВСЕ НУЖНЫЕ ПАРАМЕТРЫ И ОНА ПЕРЕДАЕТ ИХ СВОИМ ПОДФУНКЦИЯМ
##        chart1 = QtCharts.QChart()
##        chart1.setAnimationOptions(QtCharts.QChart.AllAnimations)
##        self.add_series("Значение", [0,1] ,chart1)
##        #-----------------------------------------
##        self.chart_view1 = QtCharts.QChartView(chart1)
##        self.chart_view1.setRenderHint(QPainter.Antialiasing)
##        #self.chart_view1.setSizePolicy(size)
##        minWidth = 400
##        self.chart_view1.setMinimumWidth(minWidth)
##        self.main_layout.addWidget(self.chart_view1)
##    def add_series(self, name, columns, chart):#выходит add.series так написан что по Ох автоматически будет дата?
##        table = CustomTableModel(self.sheet.Data)
##        """ Формирует название оси """
##        self.series = QtCharts.QLineSeries()
##        self.series.setName(name)
##        """ формирует 1 массив series из 2 столбцов, добавляя в него данные из Х и У """
##        for i in range(table.rowCount()):
##            """ получение даты """
##            t = table.index(i, 0).data()#типа нулевой столбец(дата) и в нем по строкам  будем переходить с помощью цикла этого
##            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"#но вообще тут уже прописано как бы что в нулевом столбце будет дата
##            x = float(QDateTime().fromString(t, date_fmt).toMSecsSinceEpoch())
##            y = float(table.index(i, columns[1]).data())
##            if x > 0 and y > 0: 
##                self.series.append(x, y)
##        chart.addSeries(self.series)
##        """ задание оси X """
##        self.axis_x = QtCharts.QValueAxis()
##        """ Класс QDateTimeAxis добавляет даты и время к оси диаграммы. """
##        self.axis_x.setTickCount(6)
##        """setTickCounе( int count ) устанавливает количество отметок на оси для подсчета, на оси Х будет 10 штрихов """
##        """ setFormat - задаёт формат вывод текстового представления значения. """
##        self.axis_x.setTitleText("Дата")
##        chart.addAxis(self.axis_x, Qt.AlignBottom)
##        """ Добавляет ось оси к диаграмме, выровненной, как указано выравниванием. """
##        self.series.attachAxis(self.axis_x)
##        """ Возвращает, true если ось была успешно присоединена, false в противном случае. """
##        """ задание оси Y """
##        self.axis_y = QtCharts.QValueAxis() 
##        """ Класс QValueAxis добавляет значения к осям диаграммы. """
##        self.axis_y.setTickCount(6)
##        """ Свойство setTickCount содержит количество отметок на оси. Это указывает, сколько линий сетки нарисовано на графике. """
##        self.axis_y.setLabelFormat("%.2f")
##        """ Свойство setLabelFormat содержит формат метки оси. """
##        self.axis_y.setTitleText(name)#изменила название оси, что ифами написать, как обратиться к имени той колонки которую я в параметры передаю?
##        chart.addAxis(self.axis_y, Qt.AlignLeft)
##        self.series.attachAxis(self.axis_y)
##        """ получение цвета из QC  hart для использования в QTableView, будет выделять столбец таблицы тем же цветом что и линия в диарамме!! """
##        table.color = "{}".format(self.series.pen().color().name())
##    #------------------------------------------
##    def DeletE(self):
##        if (self.graphic_Number==1):#приходиться делать так тк удаление не раьотает если добавлять просто на один виджет 
##            self.chart_view1.setParent(None)
##        elif(self.graphic_Number==2):
##            self.bar1ChartView.setParent(None)
##class Sheet(QWidget):
##    def __init__(self, data, num): 
##        QWidget.__init__(self)
##        #self.setSizePolicy(QSizePolicy([QtWidgets.Minimum, Minimum]))
##        print("gopnik2")
##        self.Data=pd.read_csv(data)
##
##        self.number= num # номер, чтобы объект знал свле место в массиве sheet
##        self.flag=False  # есть ли сейчас на sheet график(тк он должен быть ток один)
##
##        self.main_layout = QHBoxLayout()# главный контейнер
##        self.splitter = QSplitter() #сплитер(тк ток на него можно добвлять виджеты)
##        self.splitter.setChildrenCollapsible(False)
##        self.graphic_sheet=Graphic(self) #виджет на кт будет находиться неспредственно график
##        self.graphic_Dash=Graphic(self)
##        self.prevention=QLabel()
##
##        self.Settings_W = QWidget() #виджет на кт будут combobox действий с графиком и другие настройки sheet
##        self.which_column = QtWidgets.QComboBox()
##        self.Poka_Ox= QtWidgets.QComboBox()
##
##        self.tip_graphic = QtWidgets.QComboBox() #кб в кт выбираем тип графика кт будет на этой объекте sheet
##        self.button_remove= QtWidgets.QPushButton("Область для графика чиста") #кнопка по нажатию на кт мы удалим текущий график если есть(не в комбобокс тк там мы выбирает тип графика)
##        #--------------------------------
##        csv_column_names=[]
##        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
##        ddd=self.Data.select_dtypes(include=numerics) #ЭТО ОТБИРАЕМ СТОЛБЦЫ В КТ ТОЛЬКО ЧИСЛОВЫЕ ЗНАЧЕНИЯ
##        newdf=ddd.isnull().any() #ЭТО ВЕРНЕТ МАССИВ ИЗ ТРУ/ФОЛЗ: ТОТ СТОЛБЕЦ В КТ ЕСТЬ Nan БУДЕТ ТРУ
##        #ИТОГО ЭТО МАССИВ ПО КТ МЫ СМОЖЕМ ПОНЯТЬ В КАКИХ СТОЛБЦАХ ИЗ ТЕХ, КТ УЖЕ СОДЕРЖАТ ТОК ЧИСЛА ЕСТЬ ТЕ КТ СОДЕРЖАТ  Nan
##        for i in range(len(newdf.values)):
##            if(newdf.values[i]==False):
##                csv_column_names.append(ddd.columns.values[i])
##
##        CCN_model = QtCore.QStringListModel(csv_column_names) #одномерная модель содержащая списк строк
##        self.which_column.setModel(CCN_model) 
##        self.Poka_Ox.setModel(CCN_model) 
##        #-------------------УСТАНОВКА МОДЕЛИ НА КОМБОБОКС ВЫБОР ГРАФИКА-----------------------
##        lst2 = ['добавить график1 ', 'добавить barchart'] 
##        slm2 = QtCore.QStringListModel(lst2) #модель
##        self.tip_graphic.setModel(slm2) #связываем представление модели "действия с графиком"
##        #-----------------------------ПРИВЯЗЫВАЕМ К СОБЫТИЯМ------
##        self.tip_graphic.activated.connect(self.cbo_on_clicked)# к событию cbo_on_clicked привязали
##        self.button_remove.clicked.connect(self.but_on_clicked) # к событию but_on_clicked привязали
##        #-----------ДОБАВЛЯЕМ НА ВИДЖЕТ НАСТРОЙКА ГРАФИКА ВСЕ ЧТО НАДО--------------
##        VBlayout = QVBoxLayout()#
##
##        VBlayout.addWidget(QLabel("выберите что по Оу: "))
##        VBlayout.addWidget(self.which_column)
##
##        VBlayout.addWidget(QLabel("выберите что по ОX:"))#тут всегда будет время пока прост чтобы выбрать данные и попробовать на разных
##        VBlayout.addWidget(self.Poka_Ox)
##
##        VBlayout.addWidget(self.which_column)
##        VBlayout.addWidget(self.tip_graphic)
##        VBlayout.addWidget(self.button_remove)
##
##        self.Settings_W.setLayout(VBlayout)
##        #-------------------------------ДОБАВИМ ВИДЖЕТ НАСТРОЙКА ГРАФИКА И ГРАФИК НА СПЛИТТЕР-----
##        self.splitter.addWidget(self.Settings_W)
##        self.splitter.addWidget(self.graphic_sheet)
##        #---------------------------------
##        self.main_layout.addWidget(self.splitter)
##        self.setLayout(self.main_layout) ###self.arr_sheet=[]
##    def cbo_on_clicked(self):#если на Sheet в данный момент нет графика мы построим тот кт выбран, не помещаю в одну ф-цию тк у графиков могут оказаться разные параметры(тогда передавать буду )
##       if(self.flag==False):
##            self.graphic_Dash.add_Graphic()
##            self.graphic_sheet.add_Graphic()#график не может сущестовавть без шита(график всего лишь его поле)
##            self.prevention.setNum(self.number)
##            self.flag=True
##       else:
##            self.button_remove.setText("СНАЧАЛА УДАЛИТЕ ТОТ ГРАФИК, КТ ЕСТЬ СЕЙЧАС!")
##    def but_on_clicked(self):#если на sheet в данный момент есть любой график, удалим его
##        if(self.flag==True):
##            self.button_remove.setText("Область для графика чиста")
##            self.graphic_Dash.DeletE()
##            self.prevention.setText("удален")
##            self.graphic_sheet.DeletE()
##            self.flag=False
##class CustomTableModel(QAbstractTableModel):#CustomTableModel
##    def __init__(self, data=None): #Обычно функция определяется с помощью инструкции def
##        QAbstractTableModel.__init__(self)
##        self.color = None
##        self.load_data(data)
##        """в моем конструкторе опеределяется сво-во color и вызывается метод load_data """
##    def load_data(self, data):
##        """ функция load_data структуру из 3 столбцов преобразует в 3 структуры по одному столбцу  """
##        self.input_dates = data[0].values
##        self.input_magnitudes = data[1].values
##        self.input_depth= data[2].values
##
##        self.column_count = 3#Возвращает количество столбцов для дочерних элементов данного родителя 
##        self.row_count = len(self.input_dates)
##        """Задаются 2 св-ва класса:column_count=3,row_count=длина столбца input_magnitudes, тк у них одинак колво строк """
##    def rowCount(self, parent=QModelIndex()):
##        """ Возвращает количество строк под указанным родителем"""
##        return self.row_count
##    def columnCount(self, parent=QModelIndex()):
##        """ Возвращает количество столбцов под указанным родителем ."""
##        return self.column_count
##    def headerData(self, section, orientation, role):
##        """ Возвращает данные для данной роли и раздела в заголовке с указанной ориентацией.
##        Для горизонтальных заголовков номер раздела соответствует номеру столбца. Аналогично, 
##        для вертикальных заголовков номер раздела соответствует номеру строки."""
##        if role != Qt.DisplayRole:
##            """Ключевые данные, которые будут отрисованы в виде текста"""
##            return None
##        if orientation == Qt.Horizontal:
##            """Horizontal значение 1, Vertical-2 """
##            return ("Date", "Magnitude","Depth")[section]
##        else:
##            return "{}".format(section)
##    def data(self, index, role=Qt.DisplayRole):
##        """Возвращает данные, хранящиеся под данной ролью для элемента, на который ссылается индекс. """
##        column = index.column()
##        row = index.row()#index
##
##        if role == Qt.DisplayRole:
##            """Qt.DisplayRole-Ключевые данные, которые будут отрисованы в виде текста, еще могут быть: 
##           
##            DecorationRole Данные, которые будут отрисованы как украшение в виде пиктограммы. (QColor, QIcon или QPixmap)
##            Qt::EditRole Данные в форме, подходящей для редактирования с помощью редактора. (QString)
##            Qt::ToolTipRole Данные отображаемые в подсказке к элементу. (QString)
##            Qt::StatusTipRole Данные отображаемые в строке статуса. (QString)
##            Qt::WhatsThisRole Данные отображаемые для элемента в режиме "Что это?". (QString)
##            Qt::SizeHintRole Предпочитаемый размер для элемента, который будет применен в представлении. (QSize)
##            """
##            if column == 0:
##                raw_date = self.input_dates[row]#input_dates[row]
##                date = "{}".format(raw_date.toPython())
##                """Подстановку данных можно сделать с помощью форматирования строк. Форматирование можно сделать с помощью оператора %, либо с помощью метода format"""
##                return date[:-3]
##            elif column == 1:
##                return "{:.2f}".format(self.input_magnitudes[row])
##            elif column==2:
##                return "{:.2f}".format(self.input_depth[row])
##
##        elif role == Qt.BackgroundRole:
##            """Кисть фона используемая для отрисовки элементов с делегатом по умолчанию """
##            return (QColor(Qt.white), QColor(self.color), QColor(self.color))[column]
##            """QColor предоставляет цвета"""
##        elif role == Qt.TextAlignmentRole:
##            """Выравнивание текста для отрисовки элементов с делегатом по умолчанию """
##            return Qt.AlignRight
##            """Выравнивание по правому краю"""
##        return None
##class Dashboard(QWidget):
##    def __init__(self,num, MyWind): 
##        QWidget.__init__(self)
##        self.splitter = QSplitter()  
##        self.number=num #номер
##        self.Arr_S=MyWind.arr_sheet
##
##        self.Settings_D = QWidget()#виджет на кт будет список sheet и другие настройки дашборда
##        self.Sheet_n_predstavlenie = QtWidgets.QListView()
##        
##        self.D_Graphics= D_Graphic(self) #виджет на кт будут графики дашборда(взятые с выбранных sheet)
##        self.scrollArea=QScrollArea()#контейнер с ползунком для виджета с графиками
##        #----------------------НАСТРОЙКА СПЛИТТЕРА--------------------------
##        self.splitter.setChildrenCollapsible(False)
##        #----------------------
##        main_layout = QtWidgets.QHBoxLayout()
##        #----------------ДОБАВЛЯЕМ ВИДЖЕТ НА КТ БУДУТ ГРАФИКИ (D_Graphics) НА КОНТЕЙНЕР С ПОЛЗУНКОМ(scrollArea)-------------------------
##        self.scrollArea.setWidget(self.D_Graphics)
##        self.scrollArea.resize(200, 200)
##        self.scrollArea.setWidgetResizable(True)
##        #------------------------ЗАПОЛНЯЕМ СПИСОК С НАЗВАНИЯМИ ВКЛАДОК SHEET--------------
##        Sheet_names=[]
##        l=len(self.Arr_S)
##        for i in self.Arr_S:
##            Sheet_names.append("Sheet"+str(i.number))
##        Sheet_n_model = QtCore.QStringListModel(Sheet_names) #одномерная модель содержащая списoк строк
##        self.Sheet_n_predstavlenie.setModel(Sheet_n_model) 
##        #----------------------связываем представление модели "действия с графиком" с выбором
##        #когда изменился кокойто шиит
##        self.Sheet_n_predstavlenie.clicked.connect(self.cbo_on_clicked)
##        #---------------------ДОБАВЛЯЕМ НА ВИДЖЕТ НАСТРОЙКА ГРАФИКА ВСЕ ЧТО НАДО(пока ток список sheet)------------
##        vlayout = QtWidgets.QHBoxLayout()
##        vlayout.addWidget(self.Sheet_n_predstavlenie)
##        self.Settings_D.setLayout(vlayout)
##        #----ДОБАВИМ ВСЕ НА СПЛИТТЕР-------------------
##        self.splitter.addWidget(self.Settings_D)
##        self.splitter.addWidget(self.scrollArea)
##        #-----------------------------
##        main_layout.addWidget(self.splitter)
##        self.setLayout(main_layout) 
##    def cbo_on_clicked(self):
##        ff=self.Sheet_n_predstavlenie.currentIndex()#экземпляр класса QModelIndex для доступа к данным внутри модели
##        for i in range(len(self.Arr_S)):
##            if(i==ff.row()):
##                if(self.Arr_S[i].flag==True):
##                    self.D_Graphics.add_Graphic_on_DB(self.Arr_S[i])
##                break
##        #self.scrollArea.ensureWidgetVisible(self.D_Graphics.splitter.widget(1))#чтобы он прокручивался к только что добавленному виджету
##class D_Graphic(QWidget):# виджет на кт будут размещаться графики sheet-ов
##    def __init__(self, dashboard): 
##        QWidget.__init__(self)
##        self.D = dashboard
##        self.splitter = QSplitter()
##        self.main_layout = QHBoxLayout()
##        self.arr_sheet_g=[]
##
##        self.main_layout.addWidget(self.splitter)
##        self.setLayout(self.main_layout)
##    def add_Graphic_on_DB(self, sheet):#данные как параметр тк для разных графиков они могут быть разные
##        on_DB=False
##        i=0
##        for i in range(len(self.arr_sheet_g)):
##            if(self.arr_sheet_g[i].number==sheet.number):
##                on_DB=True
##                break
##        if(on_DB==True):
##            num_sh=i
##            self.D.scrollArea.ensureWidgetVisible(self.splitter.widget(num_sh))#чтобы он прокручивался к только что добавленному виджету
##            #self.D.scrollArea.ensureWidgetVisible(self.splitter.widget(self.splitter.indexOf(self.arr_sheet_g[num_sh])))#чтобы он прокручивался к только что добавленному виджету
##        else:
##            self.arr_sheet_g.append(sheet)
##            w = QWidget()
##            l= QVBoxLayout()
##            l.addWidget(sheet.graphic_Dash)
##            l.addWidget(sheet.prevention)
##            w.setLayout(l)
##            self.splitter.addWidget(w)
##            if(self.splitter.count()>1):
##                        yyy=self.splitter.count()-1
##                        self.D.scrollArea.ensureWidgetVisible(self.splitter.widget(yyy))#чтобы он прокручивался к только что добавленному виджету
#######################################################################################################################################
##########################################################################################################################
##def transform_date(utc, timezone=None):
##    """значение timezone по умолчаннию=None, timezone-не обязательный параметр """
##    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
##    new_date = QDateTime().fromString(utc, utc_fmt)
##    """ Класс QDateTime предоставляет функции даты и времени.
##    Функция fromString () возвращает QDateTime , учитывая строку и формат даты, используемый для интерпретации даты в строке,
##    ИЗ СТРОКИ ВОЗВРАЩАЕТ ДАТУ В ЧИСЛОВОМ ФОРМАТЕ
##    """ 
##    if timezone:
##        new_date.setTimeZone(timezone)
##        """ setTimeZone Возвращает часовой пояс даты и времени, произведет преобразования с числом, добавив или отнимит какое число
##        в зависимости от зоны
##        """
##    return new_date
##    """ возвращается модифицированная дата """
##def read_data(fname):#Как умнее всю таблицу прочитать то
##    # Считать содержимое CSV 
##    df = pd.read_csv(fname)
##    for i in df.columns.values:
##        arr.append(i)
##    magnitudes = df["mag"]
##    """в список magnitudes записываются из столбца mag"""
##    #  Мой местный часовой пояс 
##    timezone = QTimeZone(b"Europe/Berlin")
##    # Получить временную метку, преобразованную в наш часовой пояс
##    times = df["time"].apply(lambda x: transform_date(x, timezone))
##    """запускается функция transform_date """
##    depth=df["depth"]
##    """ в depth записываются значения из столбца"depth" """
##    return times, magnitudes, depth
##    """сформировалось 3 списка times, magnitudes, depth -остальные столбцы игнорируются"""
##class Table(QtWidgets.QWidget):
##    def __init__(self, parent=None):
##        QtWidgets.QWidget.__init__(self, parent)
##        self.main_layout = QHBoxLayout()# главный контейнер
##
##        print("gopnik1")
##        df = pd.read_csv('all_hour.csv')
##        cc=df.columns.values #КАК БЫ МАССИВ ИЗ НАЗВАНИЙ СТОЛБЦОЫ
##        gg=df[cc[1]].values #КАК БЫ МАССИВ ИЗ ЗНАЧЕНИЙ СТОЛБЦА КТ В МАССИВЕ НАЗВАНИЙ СТОЛБЦОВ ПОД ИНДЕКСОМ 1
##
##        tv2 = QtWidgets.QTableView() 
##        sti2 = QtGui.QStandardItemModel() 
##        mas_column=[]
##
##        for r in range(len(cc)):#СКОК СТОЛБЦОВ В МАССИВЕ
##            for y in range(len(df)):#СКОК СТРОК
##                mas_column.append(QtGui.QStandardItem(str(df[cc[r]].values[y]))) #НЕ ЗАБЫТЬ ПЕРЕВЕСТИ В str
##            sti2.appendColumn(mas_column)
##            mas_column.clear() #ОЧИЩАЕМ МАССИВ
##
##        sti2.setHorizontalHeaderLabels(df.columns) #ТУТ ОДИН АРГУМЕНТ, КТ ИЗ СЕБЯ ПРЕДСТАВЛЯЕТ МАССИВ С ЭЛЕМЕНТАМИ STR КТ СТАНУТ ЗАГОЛОВКАМИ СТОЛБЦОВ
##        tv2.setModel(sti2) 
##        tv2.setColumnWidth(0, 50) 
##        tv2.setColumnWidth(2, 180) 
##        #####################################
##        self.main_layout.addWidget(tv2)
##        self.setLayout(self.main_layout)
##class MyWindow(QtWidgets.QWidget):
##    def __init__(self, parent=None):
##        QtWidgets.QWidget.__init__(self, parent)
##        #----------------------------------------------
##        self.TabW = QtWidgets.QTabWidget()
##        self.arr_sheet=[]
##        self.arr_Dash=[] #ТАМ ГДЕ ДОЛЖНЫ МЕНЯТЬСЯ ГРАФИКИ НА ДАШБОРДЕ ЕСЛИ ИЗМЕНИОИСТЬ НА SHEET У МЕНЯ СТОИТ self.arr_Dash[0] ПЕРЕМЕНИТЬ НА ФОР ПО ВСЕМ ДАШБОРДАМ ТК ГРАФИКИ НА ВСЕХ(!) ДОЛЖНЫ ИЗМЕНИТЬСЯ
##        self.arr_Tab=[]
##        self.CB_Vkladka = QtWidgets.QComboBox() 
##        #---------------------НАСТРОЙКА ПАНЕЛИ С ВКЛАДКАМИ-----------------------------------------
##        self.TabW.setCurrentIndex(0)
##        self.TabW.setTabPosition(QtWidgets.QTabWidget.South)
##        self.TabW.setTabsClosable(True) # можно премещать вкладки
##        self.TabW.setMovable(True) #но пока по нажатию ничего не происходит
##        #----------МОДЕЛЬ КТ УСТАНОВИМ В КОМБОБОКС CB_Vkladka------------------------------------------
##        l = ['добавить вкладку для графика', 'добавить вкладку для совмещения графиков','добавить вкладку для таблицы','удалить текущую вкладку'] 
##        s = QtCore.QStringListModel(l) 
##        self.CB_Vkladka.setModel(s) 
##        #-------------------------КОНТЕЙНЕР НА КТ УСТАНОВИМ ПАНЕЛЬ С ВКЛАДКАМИ И КМБОБОКС--------------
##        vbox = QtWidgets.QVBoxLayout()
##        vbox.addWidget(self.TabW)
##        vbox.addWidget(self.CB_Vkladka)
##        self.setLayout(vbox)
##        #----------------------------------
##        self.CB_Vkladka.activated.connect(self.cbo_on_clicked)
##    def cbo_on_clicked(self):#СОЗДАЮ ОБЪЕКТЫ РАЗНЫХ КЛАССОВ
##        if(self.CB_Vkladka.currentIndex()==0):
##            self.Add_S()
##        elif(self.CB_Vkladka.currentIndex()==1):
##            self.Add_D()
##        elif(self.CB_Vkladka.currentIndex()==2):
##            self.Add_T()
##        elif(self.CB_Vkladka.currentIndex()==3):
##            self.TabW.removeTab(self.TabW.currentIndex())# пока удаляет все вкладки, и потом сделать по нажаlabelтию на крест
##    def Add_S(self):                                                         #номер графика
##        my_sheet=Sheet("all_hour.csv", len(self.arr_sheet)+1) #наверное тк нет метода show()+скрин что надо деалать чтобы окно рисовалось
##        self.TabW.addTab(my_sheet, "Sheet"+str(my_sheet.number))
##        self.arr_sheet.append(my_sheet)
##    def Add_D(self):
##        my_dashboard=Dashboard(len(self.arr_Dash)+1, self)
##        self.TabW.addTab(my_dashboard, "Dashboard" + str(my_dashboard.number))  
##        self.arr_Dash.append(my_dashboard)
##    def Add_T(self):
##        my_table=Table()
##        self.TabW.addTab(my_table, "Table")  
##        #self.arr_Tab.append(my_table)
##    def Remove(self):
##        self.TabW.removeTab(self.TabW.currentIndex())
##


class TabItemModel(QStandardItem):
    def __init__(self):
        super(TabItemModel, self).__init__()

        self.widget = None
        self.tab = None

class ChartItemModel(TabItemModel):
    def __init__(self):
        super(ChartItemModel, self).__init__()

        self.setIcon(QIcon('icons/chart.svg'))
        self.setEditable(False)

        self.widget = None
        self.tab = None

class TableItemModel(TabItemModel):
    def __init__(self):
        super(TableItemModel, self).__init__()

        self.setIcon(QIcon('icons/table.svg'))
        self.setEditable(False)

        self.widget = None
        self.tab = None


class DashboardItemModel(TabItemModel):
    def __init__(self):
        super(DashboardItemModel, self).__init__()

        self.setIcon(QIcon('icons/dashboard.svg'))
        self.setEditable(False)

        self.widget = None
        self.tab = None

class MainWindowV2(QMainWindow):

    def newChart(self):
        item = ChartItemModel()
        item.setText('New Chart')
        self.model.appendRow(item)
        pass

    def newTable(self):
        item = ChartItemModel()
        item.setText('New Table')
        self.model.appendRow(item)
        pass

    def newDashboard(self):
        item = ChartItemModel()
        item.setText('New Dashboard')
        self.model.appendRow(item)
        pass

    def closeTab(self):
        pass
    
    def createActions(self):
        self.newChartAction = QAction("New Chart", self,
                                      icon = QIcon('icons/chart.svg'))        
        self.newChartAction.triggered.connect(self.newChart)

        self.newTableAction = QAction("New Table", self,
                                      icon = QIcon('icons/table.svg'))        
        self.newTableAction.triggered.connect(self.newTable)

        self.newDashboardAction = QAction("New Dashboard", self,
                                      icon = QIcon('icons/dashboard.svg'))        
        self.newDashboardAction.triggered.connect(self.newDashboard)

        self.closeTabAction = QAction("Close Tab", self,
                                      icon = QIcon('icons/close.svg'))        
        self.closeTabAction.triggered.connect(self.closeTab)
    
    def __init__(self):
        super(MainWindowV2, self).__init__()

        self.model = QStandardItemModel(self)

        
        

        

        

        


##        self.arr_sheet=[]
##        self.arr_Dash=[] #ТАМ ГДЕ ДОЛЖНЫ МЕНЯТЬСЯ ГРАФИКИ НА ДАШБОРДЕ ЕСЛИ ИЗМЕНИОИСТЬ НА SHEET У МЕНЯ СТОИТ self.arr_Dash[0] ПЕРЕМЕНИТЬ НА ФОР ПО ВСЕМ ДАШБОРДАМ ТК ГРАФИКИ НА ВСЕХ(!) ДОЛЖНЫ ИЗМЕНИТЬСЯ
##        self.arr_Tab=[]

        useTab = False

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        
        self.tabWidget = QTabWidget()
        # self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabsClosable(True) # можно премещать вкладки
        self.tabWidget.setMovable(True) # но пока по нажатию ничего не происходит

        if useTab:

            self.cwGrid = QGridLayout(self.centralWidget)
            self.cwGrid.addWidget(self.tabWidget, 0, 0)
            # cwGrid.addWidget(QLabel("mudak"), 0, 0)
            self.centralWidget.setLayout(cwGrid)
            # self.tabWidget.hide()
            

        # summerfield "Rapid GUI Programming" ch6
        logDockWidget = QDockWidget("Tabs", self)
        logDockWidget.setTitleBarWidget(QWidget())

        # logDockWidget = QDockWidget(self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea |
                                      Qt.RightDockWidgetArea)
        logDockWidget.setFeatures(QDockWidget.DockWidgetMovable)
        # logDockWidget.setMinimumSize(100, 0)
                
        self.navListView = QListView()
        self.navListView.setModel(self.model)

        logDockWidget.setWidget(self.navListView)
        self.addDockWidget(Qt.LeftDockWidgetArea, logDockWidget)

        self.createActions()

        tabsToolbar = self.addToolBar("Tabs")
        tabsToolbar.setObjectName("tabsToolBar")
        tabsToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        for action in [self.newChartAction, self.newTableAction,
                       self.newDashboardAction, self.closeTabAction]:
            tabsToolbar.addAction(action)


        
        
        

        
        
        
if  __name__== "__main__":
    import sys
    app = QApplication(sys.argv)
    # window = MyWindow() #Создаем экземпляр класса
    window = MainWindowV2()
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(900, 600)
    window.show()   
    
    
    sys.exit(app.exec_())






