#Write a function that takes a list of YOB and the CY as parameters, 
#then calculate and return a list containing the age of each YOB prodided in the parameter.

YOB = ["1915","1952","1965","1982","2012"]
print(YOB)

def calculateage(currentyear, YOB):
    Age = []
    for year in YOB:
        age = currentyear - year
        Age.append(age)

    return Age

print(calculateage(2021, [1915, 1952, 1965, 1982, 2012]))