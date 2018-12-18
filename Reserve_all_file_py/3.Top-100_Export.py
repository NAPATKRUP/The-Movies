"""
The-Movies : Read CSV and Create Top-100 Movies CSV Files
"""
import csv
import pandas as pd
import time
start_time = time.time()

# banner
print("|>>> Top-100 Movies per year Exported <<<|")

def top100_export():
    """ Load Dataset """
    for i in range(2000, 2017):
        # start display
        print(">> Year : %i" % i)
        print(">> [status] Export Dataset Starting!")

        # load dataset
        dataset = pd.read_csv("Data_Export/%i.csv" % (i))

        # convert to list
        title = dataset["title"].tolist()
        rate = dataset["rate"].tolist()
        budget = dataset["budget"].tolist()
        revenue = dataset["revenue"].tolist()
        runtime = dataset["runtime"].tolist()
        year = dataset["year"].tolist()

        # temp
        temp1 = [["title", "rate", "budget", "revenue", "runtime", "year"]]
        temp2 = []
        for j in range(len(title)):
            temp2.append([title[j], rate[j], budget[j], revenue[j], runtime[j], year[j]])

        # sort data
        temp2.sort(key=lambda x: x[1], reverse=True)

        # merge data and temp
        temp1.extend(temp2)

        # data
        data = []
        for k in range(100):
            data.append(temp1[k])

        # export file
        name = "Top-100_" + str(i)
        export_file(data, name)

        # end display
        print(">> [status] Exported Dataset Successful!")

        # Used time
        print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def export_file(data, name):
    """ Export CSV File Sort By Year """
    file_name = "Top-100_Export/" + name + ".csv"
    with open(file_name, "w", newline="") as export_file:
        file_ = csv.writer(export_file, delimiter=",")
        file_.writerows(data)

top100_export()
