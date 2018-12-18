"""
The-Movies : Top-20_Rated_of_Movies
"""
import pandas as pd
import pygal
import time
start_time = time.time()

# banner
print("|>>> Top-20 Rated of Movies in 2000 - 2016 Dataset <<<|")

def rate_movies():
    """ Create Top-20 Rated of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % (year))
        title = dataset["title"].tolist() #Title Movies
        rate = dataset["rate"].tolist() #Rate
        graph = pygal.Bar(x_title="Movie Name & Rated")
        graph.title = "Top-20 Rated of Movies in %i Dataset" % year
        for i in range(20):
            graph.add(title[i], rate[i])
        graph.render_to_file("Graph_Export/Top-20_Rated_Movies/Top-20_Rated_of_Movies_%i.svg" % year)

        # End display
        print(">> [status] Created Graph Successful!")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

rate_movies()