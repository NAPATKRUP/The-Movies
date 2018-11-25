""" Read Dataset and Create CSV File """
import csv
import pandas as pd
import time
start_time = time.time()

#banner
print("|>>> Dataset Export v2.0 <<<|")

def data_load():
    """ Load Dataset """
    # start display
    print(">> [status] Export Dataset Starting!")

    # load dataset
    dataset = pd.read_csv("Dataset/tmdb_5000_movies.csv")

    # convert to list
    title = dataset["title"].tolist()
    rate = dataset["vote_average"].tolist()
    budget = dataset["budget"].tolist()
    revenue = dataset["revenue"].tolist()
    runtime = dataset["runtime"].tolist()
    year = dataset["release_date"].tolist()

    # data to export
    data = {
        "data_" + str(i): [["title", "rate", "budget", "revenue", "runtime", "year"]] for i in range(2000, 2017)
        }

    # add value to data classified by year
    for i in range(len(title)):
        for j in range(2000, 2017):
            if str(year[i])[:4] == str(j):
                data["data_" + str(j)].append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])

    # export file
    for k in range(2000, 2017):
        data_name = "data_" + str(k)
        export_file(data[data_name], k)

    # end display
    print(">> [status] Exported Dataset Successful!")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def export_file(data, year):
    """ Export CSV File Sort By Year """
    file_name = "Data_Export/" + str(year) + ".csv"
    with open(file_name, "w", newline="") as export_file:
        file_ = csv.writer(export_file, delimiter=",")
        file_.writerows(data)

data_load()
