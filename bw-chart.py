import sys
import argparse
from PySide2.QtCore import (Qt, QPointF)
from PySide2.QtGui import (QColor, QPainter, QPainterPath, QImage,
                           QPen)
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts

import math
import statistics

import ddv.csv

    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    # data = ddv.csv.getPieChartData("refugees-by-asylum.csv")
    acmeData = ddv.csv.getBoxWhiskersData("acme_data_bw.txt")
    bwData = ddv.csv.getBoxWhiskersData("boxwhisk_data.txt")

    chart = QtCharts.QChart();
    chart.setTitle("Simple boxwhiskerschart example");

    data = [("acme", acmeData),
            ("box whiskers", bwData)]

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
    
    
    
    window = QMainWindow() 
    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())
    

    

