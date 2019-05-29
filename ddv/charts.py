from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (Qt, QPointF, QDateTime)
from PySide2.QtGui import (QPainter, QPen, QLinearGradient,
    QGradient)

import statistics

def createCandlestickChart(data):

    chart = QtCharts.QChart();
    chart.setTitle("Simple Candlestick Series example");
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        
    series1 = QtCharts.QCandlestickSeries()        
    series1.setName("Acme")
    series1.setIncreasingColor(Qt.green)
    series1.setDecreasingColor(Qt.red)

    for x in data:            
    
        category = float(x[0])
        csSet = QtCharts.QCandlestickSet(category)
        csSet.setOpen(x[1])
        csSet.setHigh(x[2])
        csSet.setLow(x[3])
        csSet.setClose(x[4])      
        

        series1.append(csSet)

    chart.addSeries(series1);

    chart.createDefaultAxes()


    axisX = QtCharts.QBarCategoryAxis()
    axisX.setCategories([QDateTime.fromMSecsSinceEpoch(d[0]).toString("d")
                         for d in data])
    axisX.setTitleText("day")

    axisY = QtCharts.QValueAxis()
    axisY.setMax(chart.axisY().max() * 1.01)
    axisY.setMin(chart.axisY().min() * 0.99)

    chart.setAxisX(axisX, series1)
    chart.setAxisY(axisY, series1)




    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing);
  

    return chartView



def createBwChart(data):

    chart = QtCharts.QChart();
    chart.setTitle("Simple boxwhiskerschart example");
 
    for d in data:

        series1 = QtCharts.QBoxPlotSeries()
        series1.setName(d[0])        

        for x in d[1]:            
        
            janName = x[0]
            jan = x[1]

            le = min(jan)
            ue = max(jan)
            med = statistics.median(jan)
            lq = statistics.median(jan[0: len(jan) // 2])
            uq = statistics.median(jan[len(jan) // 2 + (len(jan) % 2): ])

            bs = QtCharts.QBoxSet(le, lq, med, uq, ue, janName)

            series1.append(bs)   


        chart.addSeries(series1);
    
    chart.createDefaultAxes()
    chart.axes(Qt.Vertical)[0].setMin(15.0)
    chart.axes(Qt.Vertical)[0].setMax(34.0)

    #chart.axes(Qt.Vertical)[0].setMin(0.0)
    #chart.axes(Qt.Vertical)[0].setMax(1.0)

    
    # chart.legend()->hide();

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing);
  

    return chartView



# createPieChart(data) => QChartView
# на примере беженцев по странам на 2017 год
# data:
# [ country_names, values ]
def createPieChart(data):

    chart = QtCharts.QChart()
    # chart.legend().hide()        
    chart.setTitle("Pie chart (refugees as of 2017)")

    series = QtCharts.QPieSeries()

    sliceList = list(map(lambda nv: QtCharts.QPieSlice(nv[0], nv[1]),
                         zip(data[0], data[1])))
    

    series.append(sliceList)

                       
    for s in series.slices():
        s.setLabelVisible()

    chart = QtCharts.QChart();
    chart.addSeries(series);
    chart.setTitle("Simple piechart example");
    # chart.legend()->hide();

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing);
  

    return chartView


# createSplineChart(self, data) => QChartView
# демонстрирует создание splineCharts
# по горизонтальной оси принимаем QDateTime (xTimestamps)
# и два lists с точками и названиями каждой series
# data:
# [ xTimestamps,
#  [serie1Points, serie2Points, ..]
#  [serie1Name, serie2Name, ..] ]
def createSplineChart(data):

    chart = QtCharts.QChart()
    # chart.legend().hide()        
    chart.setTitle("Spline chart (market shares)")

    
    axisX = QtCharts.QDateTimeAxis();
    # axisX.setTickCount(10);
    
    axisX.setFormat("MM-yyyy");
    #axisX.setFormat("yyyy/MM/dd hh:mm:ss:zzz");
    #axisX.setFormat("hh:mm:ss:zzz");
    
    axisX.setTitleText("Time");
    chart.addAxis(axisX, Qt.AlignBottom);

    axisY = QtCharts.QValueAxis();
    # axisY.setLabelFormat("%.2f");
    axisY.setTitleText("%");
    chart.addAxis(axisY, Qt.AlignLeft);

    # chart.axes(Qt.Vertical)[0].setRange(0, 100)
    chart.axes(Qt.Vertical)[0].setRange(0, 3)

    
    

    

    # seriesFilter = [0, 3, 4, 6]
    # seriesFilter = [0]
    seriesFilter = [3, 4, 6, 7, 9, 10]

    valuesToDraw = [data[1][i] for i in seriesFilter]
    namesToDraw = [data[2][i] for i in seriesFilter]        


    for i in range(len(seriesFilter)):

        values = valuesToDraw[i]
        name = namesToDraw[i]
    
        series = QtCharts.QSplineSeries()
        series.setName(name)

        n = len(values)

        # print(values)

         # конвертируем столбец time в float, чтобы можно было использовать его как значения оси x
        for j in range(n):
            # print(x)
            time = data[0][j]                
            series.append(float(time.toMSecsSinceEpoch()), values[j])

        chart.addSeries(series)

        series.attachAxis(axisX);        
        series.attachAxis(axisY);
    
    
    # chart.createDefaultAxes()       


    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    return chartView


# createScatterChart(data) => QChartView
# демонстрирует создание scatter chart
# на примере рост/вес баскетболистов NBA 2018 года
# data:
# [ heights, weights ]
def createScatterChart(data):

    chart = QtCharts.QChart()
    # chart.legend().hide()        
    chart.setTitle("Spline chart (market shares)")

    
    series0 = QtCharts.QScatterSeries()
    series0.setName("height / weight")
    series0.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeCircle)
    series0.setMarkerSize(5.0)    

    #series0.append([0, 6, 6, 4])

    pointsList = list(map(lambda hw: QPointF(hw[0], hw[1]),
                     zip(data[0], data[1])))

    series0.append(pointsList)
                       
    chartView = QtCharts.QChartView(chart)    
    chartView.setRenderHint(QPainter.Antialiasing)
    
    chart.addSeries(series0)
    
    chart.setTitle("Nba Players active as of 2018 height/weight")
    
    chart.createDefaultAxes()
    
    chart.setDropShadowEnabled(False)

    chart.axes(Qt.Vertical)[0].setTitleText("Weight")
    chart.axes(Qt.Horizontal)[0].setTitleText("Height")   
  

    return chartView
    



# createAreaChart(self, data) => QChartView
# демонстрирует создание area charts
# по горизонтальной оси принимаем QDateTime (xTimestamps)
# и два lists с точками и названиями каждой series
# data:
# [ xTimestamps,
#  [serie1Points, serie2Points, ..]
#  [serie1Name, serie2Name, ..] ]
def createAreaChart(data):

    

    """
    axisX = QtCharts.QDateTimeAxis();
    # axisX.setTickCount(10);
    
    axisX.setFormat("yyyy");
    #axisX.setFormat("yyyy/MM/dd hh:mm:ss:zzz");
    #axisX.setFormat("hh:mm:ss:zzz");
    
    axisX.setTitleText("Time");
    chart.addAxis(axisX, Qt.AlignBottom);

    axisY = QtCharts.QValueAxis();
    # axisY.setLabelFormat("%.2f");
    axisY.setTitleText("%");
    chart.addAxis(axisY, Qt.AlignLeft);

    # chart.axes(Qt.Vertical)[0].setRange(0, 100)
    # chart.axes(Qt.Vertical)[0].setRange(0, 3)
    """

    
    series0 = QtCharts.QSplineSeries()

    series0.append(QPointF(1, 5) )
    series0.append(QPointF(3, 7) )
    series0.append(QPointF(7, 6) )
    series0.append(QPointF(9, 7) )
    series0.append(QPointF(12, 6))
    series0.append(QPointF(16, 7) )
    series0.append(QPointF(18, 5))

    series1 = QtCharts.QSplineSeries()
    
    series1.append(QPointF(1, 3) )
    series1.append(QPointF(3, 4) )
    series1.append(QPointF(7, 3) )
    series1.append(QPointF(8, 2) )
    series1.append(QPointF(12, 3))
    series1.append(QPointF(16, 4) )
    series1.append(QPointF(18, 3))


    """    

    # seriesFilter = [0, 3, 4, 6]
    # seriesFilter = [0]
    seriesFilter = [0]

    valuesToDraw = [data[1][i] for i in seriesFilter]
    namesToDraw = [data[2][i] for i in seriesFilter]
  

    i = 0

    values = valuesToDraw[i]
    name = namesToDraw[i]

    topLineSeries = QtCharts.QLineSeries()    

    n = len(values)

    print(values)

     # конвертируем столбец time в float, чтобы можно было использовать его как значения оси x
    for j in range(n):
        # print(x)
        time = data[0][j]                
        topLineSeries.append(float(time.toMSecsSinceEpoch()), values[j])

    """

    #areaSeries = QtCharts.QAreaSeries(topLineSeries);
    areaSeries = QtCharts.QAreaSeries(series0, series1);
    #areaSeries.setName(name);
    areaSeries.setName("name4535343534");
    
    pen = QPen(0x059605);
    pen.setWidth(3);
    areaSeries.setPen(pen);

    gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
    gradient.setColorAt(0.0, 0x3cc63c);
    gradient.setColorAt(1.0, 0x26f626);
    gradient.setCoordinateMode(QGradient.ObjectBoundingMode);
    areaSeries.setBrush(gradient);


    chart = QtCharts.QChart()
    chart.addSeries(areaSeries)
    # chart.legend().hide()        
    chart.setTitle("Area chart (population by continents)")
    chart.createDefaultAxes()
    chart.axes(Qt.Horizontal)[0].setRange(0, 20) 
    chart.axes(Qt.Vertical)[0].setRange(0, 10)
    
    
    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    

    # areaSeries.attachAxis(axisX);        
    # areaSeries.attachAxis(axisY);
    


    """
    for i in range(len(seriesFilter)):

        values = valuesToDraw[i]
        name = namesToDraw[i]
    
        series = QtCharts.QSplineSeries()
        series.setName(name)

        n = len(values)

        # print(values)

         # конвертируем столбец time в float, чтобы можно было использовать его как значения оси x
        for j in range(n):
            # print(x)
            time = data[0][j]                
            series.append(float(time.toMSecsSinceEpoch()), values[j])

        chart.addSeries(series)

        series.attachAxis(axisX);        
        series.attachAxis(axisY);
    
    
    
    """

    
    return chartView
    
 
