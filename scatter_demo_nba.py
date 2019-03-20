import sys
import argparse
from PySide2.QtCore import (Qt, QPointF)
from PySide2.QtGui import (QColor, QPainter, QPainterPath, QImage,
                           )
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts
import math

import ddv.csv


if __name__ == "__main__":    
    app = QApplication(sys.argv)

    data = ddv.csv.getScatterChartData("nba_player_data.csv")

    chart = QtCharts.QChart()
    
    
    series0 = QtCharts.QScatterSeries()
    series0.setName("scatter1")
    series0.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeCircle)
    series0.setMarkerSize(5.0)    

    #series0.append([0, 6, 6, 4])

    pointsList = list(map(lambda hw: QPointF(hw[0], hw[1]),
                     zip(data[0], data[1])))

    series0.append(pointsList)
    #series0.append(2, 4)
    #series0.append(3, 8)
    #series0.append(7, 4)    
    #series0.append(10, 5)
                       
    chartView = QtCharts.QChartView(chart)    
    chartView.setRenderHint(QPainter.Antialiasing)
    
    chart.addSeries(series0)
    
    chart.setTitle("Simple scatterchart example")
    
    chart.createDefaultAxes()
    
    chart.setDropShadowEnabled(False)
        
    window = QMainWindow() 
    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()
