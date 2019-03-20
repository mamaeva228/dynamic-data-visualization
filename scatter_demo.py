import sys
import argparse
from PySide2.QtCore import (Qt)
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts

if __name__ == "__main__":    
    app = QApplication(sys.argv)

series0 = QtCharts.QScatterSeries()
series0.setName("scatter1")
series0.setMarkerShape(MarkerShapeCircle)
series0.setMarkerSize(15.0)

series1 = QtCharts.QScatterSeries()
series1.setName("scatter2")
series1.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
series1.setMarkerSize(20.0)

series2 = QtCharts.QScatterSeries()
series2.setName("scatter3")
series2.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
series2.setMarkerSize(30.0)

series0.append(0, 6)
series0.append(2, 4)
series0.append(3, 8)
series0.append(7, 4)
series0.append(10, 5)
series0.append(1, 1)
series0.append(3, 3)
series0.append(7, 6)
series0.append(8, 3)
series0.append(10, 2)
series0.append(1, 5)
series0.append(4, 6)
series0.append(6, 3)
series0.append(9, 5)

starPath = QPainterPath()

starPath.moveTo(28, 15)
for i in range(5):

 starPath.lineTo(14 + 14 * qCos(0.8 * i * M_PI), 15 + 14 * qSin(0.8 * i * M_PI))

starPath.closeSubpath()

star = QImage(30, 30, QImage.Format_ARGB32)
#QImage star(30, 30, QImage.Format_ARGB32)
star.fill(Qt.transparent)
painter = QPainter(star)
#QPainter painter(&star)
painter.setRenderHint(QPainter.Antialiasing)
painter.setPen(QRgb(0xf6a625))
painter.setBrush(painter.pen().color())
painter.drawPath(starPath)

series2.setBrush(star)
series2.setPen(QColor(Qt.transparent))
setRenderHint(QPainter.Antialiasing)
chart().addSeries(series0)
chart().addSeries(series1)
chart().addSeries(series2)

chart().setTitle("Simple scatterchart example")
chart().createDefaultAxes()
chart().setDropShadowEnabled(false)
chart().legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
chartView = neChartView()
window = QMainWindow() 
window.setCentralWidget(chartView)
window.resize(400, 300)
window.show()
