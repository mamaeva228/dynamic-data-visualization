from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (Qt)# Slot
from PySide2.QtGui import QPainter



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

        print(values)

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
    
