import csv
import math

a, b = list(map(int, input("> ").split(" ")))


def func(x):
    return (math.e**x)+(0.1*(x**2))


with open('func.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, dialect=csv.excel)
    while a < b:
        csvwriter.writerow([a, func(a)])
        a += 1
