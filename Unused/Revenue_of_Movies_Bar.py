"""
The-Movies : Revenue_of_Movies_Bar
"""
import pandas as pd
import pygal
import time
start_time = time.time()

#Banner
print("|>>> Revenue of Movies in year 2000-2016 Dataset <<<|")

def rate_movies():
    """ Create Rated of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and revenue"""
    for year in range(2000, 2017):
        print(">> Year : %i" % year)

        # Start display
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Data_Export/%i.csv" % (year))
        title = dataset["title"].tolist() #Title Movies
        revenue = dataset["revenue"].tolist() #Revenue
        graph = pygal.Bar(x_title="Movie Name & Revenue")
        graph.title = "Revenue of Movies in year %i Dataset" % year
        for i in range(len(title)):
            if revenue[i] != 0:
                graph.add(title[i], revenue[i])
        graph.render_to_file("Graph_Export/Revenue_Movies/Bar/Revenue_of_Movies_%i.svg" % year)

        # End display
        print(">> [status] Created Graph Successful!")
        print()

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

rate_movies()
