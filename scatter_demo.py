import sys
import argparse
from PySide2.QtCore import (Qt)
from PySide2.QtGui import (QColor, QPainter, QPainterPath, QImage,
                           )
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts
import math


if __name__ == "__main__":    
    app = QApplication(sys.argv)

    chart = QtCharts.QChart()
    
    
    series0 = QtCharts.QScatterSeries()
    series0.setName("scatter1")
    series0.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeCircle)
    series0.setMarkerSize(15.0)

    series1 = QtCharts.QScatterSeries()
    series1.setName("scatter2")
    series1.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeRectangle)
    series1.setMarkerSize(20.0)

    series2 = QtCharts.QScatterSeries()
    series2.setName("scatter3")
    series2.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeRectangle)
    series2.setMarkerSize(30.0)

    series0.append(0, 6)
    series0.append(2, 4)
    series0.append(3, 8)
    series0.append(7, 4)
    series0.append(10, 5)
                       
    series1.append(1, 1)
    series1.append(3, 3)
    series1.append(7, 6)
    series1.append(8, 3)
    series1.append(10, 2)
    
    series2.append(1, 5)
    series2.append(4, 6)
    series2.append(6, 3)
    series2.append(9, 5)

    starPath = QPainterPath()

    starPath.moveTo(28, 15)
    
    for i in range(5):
        starPath.lineTo(14 + 14 * math.cos(0.8 * i * math.pi),
                        15 + 14 * math.sin(0.8 * i * math.pi))

    starPath.closeSubpath()

    star = QImage(30, 30, QImage.Format_ARGB32)
    star.fill(Qt.transparent)
    painter = QPainter(star)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(QColor.fromRgb(0xf6, 0xa6, 0x25))
    painter.setBrush(painter.pen().color())
    painter.drawPath(starPath)

    series2.setBrush(star)
    series2.setPen(QColor(Qt.transparent))

    chartView = QtCharts.QChartView(chart)
    
    chartView.setRenderHint(QPainter.Antialiasing)
    chart.addSeries(series0)
    chart.addSeries(series1)
    chart.addSeries(series2)

    chart.setTitle("Simple scatterchart example")
    chart.createDefaultAxes()
    chart.setDropShadowEnabled(False)
    chart.legend().setMarkerShape(QtCharts.QLegend.MarkerShapeFromSeries)

    window = QMainWindow() 
    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()
