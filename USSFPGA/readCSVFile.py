import csv

def readCSV(filepath):
       with open(filepath,"r") as fileHandle:
              csvData = csv.reader(fileHandle)
              ussData = []
              for row in csvData:
                     ussData.append(row)
              return ussData
if __name__ == "__main__":
       ussData = readCSV(r"D:\DEQTV\2021\07\IPU02\USS\test\USS.CSV")
