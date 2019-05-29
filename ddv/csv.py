import pandas as pd

from PySide2.QtCore import (QDateTime)# Slot


def readCandleStickFile(fname):    
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




def readBoxWhiskersFile(fname):
    # df = pd.read_csv(fname)

    res = []
    
    with open(fname) as fp:  
       line = fp.readline()
       line = fp.readline()
       # cnt = 0
       while line:
           line = line.strip().split(" ")
           res.append((line[0],
                       [float(x) for x in line[1:]]))
           # res[line[0]] = [float(x) for x in line[1:]]
           
           line = fp.readline()
           # cnt += 1

    #values = []
    #names = []

    #for x in df.iloc[:, 1:]:
    #    values.append(list(df[x]))
    #    names.append(x)
  
    #return timeStamps, values, names

    return res




def getBoxWhiskersData():
    acmeData = readBoxWhiskersFile("acme_data_bw.txt")
    bwData = readBoxWhiskersFile("boxwhisk_data.txt")

    data = [("acme", acmeData),
            ("box whiskers", bwData)]

    return data

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



def getAreaChartData(fname):    
    df = pd.read_csv(fname)

    # получает 0-й столбец df (временные метки)
    timeStamps = df.iloc[:, 0]
    timeStamps = [QDateTime.fromString(str(x), "yyyy")
                  for x in timeStamps]


    values = []
    names = []

    for x in df.iloc[:, 1:]:
        values.append(list(df[x]))
        names.append(x)
  
    return timeStamps, values, names


# считывает данные для scatterChart из nba_player_data.csv
def getScatterChartData(fname):
    df = pd.read_csv(fname)

    # df = df[:10]

    df = df.loc[df['year_end'] == 2018]

    # print(df)


    # получает 0-й столбец df (временные метки)
    # timeStamps = df.iloc[:, 0]
    # timeStamps = [QDateTime.fromString(x, "yyyy-MM")
    #              for x in timeStamps]

    heights = list(df['height'])
    weights = list(df['weight'])

    lbsToKg = 0.453592

    weights = map(lambda w : w * lbsToKg, weights)

    
    

    return list(map(feetInchToCm, heights)), list(weights)

def feetInchToCm(s):
    ft, inch = s.split("-")
    return int(ft) * 30 + int(inch) * 2.5



# считывает данные для pieChart из refugees-by-asylum.csv
def getPieChartData(fname):
    df = pd.read_csv(fname)

    df = df[["Country Name", "2017"]]

    

    s = df["2017"].sum()
    threshold = s / 100
    threshold *= 2

    df = df.loc[df['2017'] > threshold]

    # print(s)
    # print(df)

    names = list(df["Country Name"])
    no = list(df["2017"])
    

    # print(df)


    # получает 0-й столбец df (временные метки)
    # timeStamps = df.iloc[:, 0]
    # timeStamps = [QDateTime.fromString(x, "yyyy-MM")
    #              for x in timeStamps]

    #heights = list(df['height'])
    #weights = list(df['weight'])

    #lbsToKg = 0.453592

    #weights = map(lambda w : w * lbsToKg, weights)

    #return list(map(feetInchToCm, heights)), list(weights)

    return names, no
