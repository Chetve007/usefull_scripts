import csv


with open("expenses.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Description", "Amount"])
