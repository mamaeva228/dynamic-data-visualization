import pandas as pd

from PySide2.QtCore import (QDateTime)# Slot


# считывает данные для splineChart из searchEngineShares.csv
def getSplineChartData(fname):
    df = pd.read_csv(fname)

    # получает 0-й столбец df (временные метки)
    timeStamps = df.iloc[:, 0]
    timeStamps = [QDateTime.fromString(x, "yyyy-MM")
                  for x in timeStamps]


    values = []
    names = []

    for x in df.iloc[:, 1:]:
        values.append(list(df[x]))
        names.append(x)
  
    return timeStamps, values, names
