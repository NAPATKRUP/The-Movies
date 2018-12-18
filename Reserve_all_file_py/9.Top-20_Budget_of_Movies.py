"""
The-Movies : Top-20_Budget_of_Movies
"""
import pandas as pd
import pygal
import time
start_time = time.time()

# banner
print("|>>> Top-20 Budget of Movies in 2000 - 2016 Dataset <<<|")

def budget_movies():
    """ Create Top-20 Budget of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % (year))
        title = dataset["title"].tolist() #Title Movies
        budget = dataset["budget"].tolist() #Budget
        data = []
        for j in range(len(title)):
            data.append([title[j], budget[j]])
        data.sort(key=lambda x: x[1], reverse=True)
        graph = pygal.HorizontalBar(x_title="Budget")
        graph.value_formatter = lambda x: '{:.10g}‎M'.format(x)
        graph.title = "Top-20 Budget of Movies in %i Dataset" % year
        for i in range(20):
            graph.add(data[i][0], data[i][1] / 1000000)
        graph.render_to_file("Graph_Export/Top-20_Budget/Top-20_Budget_%i.svg" % year)

        # End display
        print(">> [status] Created Graph Successful!")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

budget_movies()
