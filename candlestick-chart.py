import sys
import argparse
from PySide2.QtCore import (Qt, QPointF, QDateTime)
from PySide2.QtGui import (QColor, QPainter, QPainterPath, QImage,
                           QPen)
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts

import math
import statistics

import ddv.csv


def readBoxWhiskersFile(fname):    
    res = []
    
    with open(fname) as fp:  
       line = fp.readline()
       line = fp.readline()
       
       line = fp.readline()
       while line:
           line = line.strip().split(" ")
           d = []
           d.append(int(line[0]))
           d.extend([float(x) for x in line[1:]])
           res.append(d)
           
           line = fp.readline()           

    return res


    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    data = readBoxWhiskersFile("acme_data.txt")
    
    chart = QtCharts.QChart();
    chart.setTitle("Simple Candlestick Series example");
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        
    series1 = QtCharts.QCandlestickSeries()        
    series1.setName("Acme")
    series1.setIncreasingColor(Qt.green)
    series1.setDecreasingColor(Qt.red)

    for x in data:            
    
        category = x[0]
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
    
        
    window = QMainWindow() 
    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())
    

    

