import random
import time
print(random.randint(1,9))
def getRandomDate(startDate, endDate):
    print("printing random date between ", startDate , " and ", endDate)
    rg = random.random()
    print(rg)
    dateformat = '%m%d%y'
print(getRandomDate("11/1/2024", "12/2/2025"))