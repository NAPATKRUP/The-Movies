"""
The-Movies : Top-20_Runtime_of_Movies
"""
import pandas as pd
import pygal
import time
start_time = time.time()

# banner
print("|>>> Top-20 Runtime of Movies in 2000 - 2016 Dataset <<<|")

def runtime_movies():
    """ Create Top-20 Runtime of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % (year))
        title = dataset["title"].tolist() #Title Movies
        runtime = dataset["runtime"].tolist() #Runtime
        data = []
        for j in range(len(title)):
            if runtime[j] > 0:
                data.append([title[j], runtime[j]])
        data.sort(key=lambda x: x[1], reverse=True)
        graph = pygal.Bar(x_title="Movie Name & Runtime")
        graph.value_formatter = lambda x: '{:.10g}‎Min'.format(x)
        graph.title = "Top-20 Runtime of Movies in %i Dataset" % year
        for i in range(20):
            graph.add(data[i][0], data[i][1])
        graph.render_to_file("Graph_Export/Top-20_Runtime/Top-20_Runtime_%i.svg" % year)

        # End display
        print(">> [status] Created Graph Successful!")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

runtime_movies()
