import random
import time 
def getRandomdate(startDate, endDate ):
    print("Printing random date between",startDate,"and",endDate)
    randomGenerator = random.random()
    dateFormat= '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime =time.mktime(time.strftime(endDate,dateFormat))

    randomtime =startTime + randomGenerator *(endTime-startTime)
    Randomdate =time.strftime(dateFormat,time.localtime(randomtime))
print("Random Date =",getRandomdate('1/1/2016','12/12/2018'))