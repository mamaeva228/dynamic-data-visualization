import sys
import argparse
from PySide2.QtCore import (Qt, QPointF)
from PySide2.QtGui import (QColor, QPainter, QPainterPath, QImage,
                           QPen)
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts
import math

import ddv.csv


if __name__ == "__main__":

    app = QApplication(sys.argv)

    data = ddv.csv.getPieChartData("refugees-by-asylum.csv")
    
    series = QtCharts.QPieSeries()

    sliceList = list(map(lambda nv: QtCharts.QPieSlice(nv[0], nv[1]),
                         zip(data[0], data[1])))

    #s1 = QtCharts.QPieSlice("Jane", 1)
    # s2 = QtCharts.QPieSlice("Doe", 2)

    series.append(sliceList)
    #series.append("Jane", 1)
    #series.append("Joe", 2)
    #series.append("Andy", 3)
    #series.append("Barbara", 4)
    #series.append("Axel", 5)

    #slc = series.slices()[1]
    #slc.setExploded()
    #slc.setLabelVisible()
    #slc.setPen(QPen(Qt.darkGreen, 2))
    #slc.setBrush(Qt.green)

    for s in series.slices():
        s.setLabelVisible()

    chart = QtCharts.QChart();
    chart.addSeries(series);
    chart.setTitle("Simple piechart example");
    # chart.legend()->hide();

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing);
    
    

    window = QMainWindow() 
    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())

    

