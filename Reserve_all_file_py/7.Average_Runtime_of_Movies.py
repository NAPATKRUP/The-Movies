"""
The-Movies : Average_Runtime_of_Movies
"""
import pandas as pd
import pygal
import time
start_time = time.time()

#Banner
print("|>>> Average Runtime of Movies in year 2000-2016 Dataset <<<|")

def average_runtime():
    """ Create Runtime of Movies average_graph of movies in year 2000-2016 and Load Dataset rate"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    graph.value_formatter = lambda x: '{:.10g}‎Min'.format(x)
    graph.title = "Average Runtime of Movies per year"

    for year in range(2000, 2017):
        print(">> Year : %i" % year)

        # Start display
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % (year))
        runtime = dataset["runtime"].tolist() #Runtime
        temp = []
        for i in runtime:
            if i > 0:
                temp.append(i)
        average = ((sum(temp)/len(temp))//0.01)/100
        graph.add(str(year), [{'value': average, 'max_value': 200}])

        # End display
        print(">> [status] Created Graph Successful!")

    graph.render_to_file("Graph_Export/Average_Runtime_of_Movies.svg")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

average_runtime()
