"""
Project : The-Movies
"""
import csv
import pandas as pd
import pygal
import time
start_time = time.time()

def the_movies():
    """Please Select Number"""
    # banner of the-movies
    print("|>>>       The-Movies      <<<|")
    print("|>>> 1.Dataset_Export")
    print("|>>> 2.Number_of_Movies")
    print("|>>> 3.Top-100_Export")
    print("|>>> 4.Average_Rated_of_Movies")
    print("|>>> 5.Average_Budget_of_Movies")
    print("|>>> 6.Average_Revenue_of_Movies")
    print("|>>> 7.Average_Runtime_of_Movies")
    print("|>>> 8.Top-20_Rated_of_Movies")
    print("|>>> 9.Top-20_Budget_of_Movies")
    print("|>>> 10.Top-20_Revenue_of_Movies")
    print("|>>> 11.Top-20_Runtime_of_Movies")
    print("|>>> 12.All_Average_of_Movies")
    select_number = int(input("Select_number : "))

    # Select Number 1-12
    if select_number == 1:
        # Read Dataset and Create CSV File
        print("|>>> Dataset Export v2.0 <<<|")
        dataset_export()
    elif select_number == 2:
        # Number of Movies
        print("|>>> Number of Movies in 2000 - 2016 Dataset <<<|")
        number_of_movies()
    elif select_number == 3:
        # Read CSV and Create Top-100 Movies CSV Files
        print("|>>> Top-100 Movies per year Exported <<<|")
        top_100_export()
    elif select_number == 4:
        # Average_Rated_of_Movies
        print("|>>> Average Rated of Movies in year 2000-2016 Dataset <<<|")
        average_rates()
    elif select_number == 5:
        # Average_Budget_of_Movies
        print("|>>> Average Budget of Movies in year 2000-2016 Dataset <<<|")
        average_budget()
    elif select_number == 6:
        # Average_Revenue_of_Movies
        print("|>>> Average Revenue of Movies in year 2000-2016 Dataset <<<|")
        average_revenue()
    elif select_number == 7:
        # Average_Runtime_of_Movies
        print("|>>> Average Runtime of Movies in year 2000-2016 Dataset <<<|")
        average_runtime()
    elif select_number == 8:
        # Top-20_Rated_of_Movies
        print("|>>> Top-20 Rated of Movies in 2000 - 2016 Dataset <<<|")
        rate_movies()
    elif select_number == 9:
        # Top-20_Budget_of_Movies
        print("|>>> Top-20 Budget of Movies in 2000 - 2016 Dataset <<<|")
        budget_movies()
    elif select_number == 10:
        # Top-20_Revenue_of_Movies
        print("|>>> Top-20 Revenue of Movies in 2000 - 2016 Dataset <<<|")
        revenue_movies()
    elif select_number == 11:
        # Top-20_Runtime_of_Movies
        print("|>>> Top-20 Runtime of Movies in 2000 - 2016 Dataset <<<|")
        runtime_movies()
    elif select_number == 12:
        # All Average of Movies in year 2000 - 2016
        print("|>>> All Average of Movies in year 2000-2016 Dataset <<<|")
        all_average()


#--Select_number 1---------------------------------------------------------------------------------------------------|

def dataset_export():
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
        export_file_1(data[data_name], k)
    # end display
    print(">> [status] Exported Dataset Successful!")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def export_file_1(data, year):
    """ Export CSV File Sort By Year """
    file_name = "Data_Export/" + "Top-100_" + str(year) + ".csv"
    with open(file_name, "w", newline="") as export_file:
        file_ = csv.writer(export_file, delimiter=",")
        file_.writerows(data)

#--Select_number 2---------------------------------------------------------------------------------------------------|

def number_of_movies():
    """ Create graph of number of movies 2000 - 2016 """
    # start display
    print(">> [status] Creat Graph Starting!")
    graph = pygal.Bar(x_title="Year", y_title="Total", legend_at_bottom=True, print_values=True)
    graph.title = "Number of Movies per year"
    for i in range(2000, 2017):
        graph.add(str(i), dataload(i))
    graph.render_to_file("Graph_Export/Number_of_Movies.svg")
    # end display
    print(">> [status] Created Graph Successful!")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def dataload(year):
    """ Load Dataset """
    dataset = pd.read_csv("Data_Export/%i.csv" % (year))
    total = len(dataset["title"].tolist())
    return total

#--Select_number 3---------------------------------------------------------------------------------------------------|

def top_100_export():
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
        export_file_2(data, name)
        # end display
        print(">> [status] Exported Dataset Successful!")
        # Used time
        print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def export_file_2(data, name):
    """ Export CSV File Sort By Year """
    file_name = "Top-100_Export/" + name + ".csv"
    with open(file_name, "w", newline="") as export_file:
        file_ = csv.writer(export_file, delimiter=",")
        file_.writerows(data)

#--Select_number 4---------------------------------------------------------------------------------------------------|

def average_rates():
    """ Create Rated of Movies average_graph of movies in year 2000-2016 and Load Dataset rate"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    graph.title = "Average Rated of Movies per year"
    for year in range(2000, 2017):
        print(">> Year : %i" % year)
        # Start display
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
        rate = dataset["rate"].tolist() #Rate
        average = ((sum(rate)/len(rate))//0.01)/100
        graph.add(str(year), [{'value': average, 'max_value': 10}])
        # End display
        print(">> [status] Created Graph Successful!")
    graph.render_to_file("Graph_Export/Average_Rated_of_Movies.svg")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

#--Select_number 5---------------------------------------------------------------------------------------------------|

def average_budget():
    """ Create Budget of Movies average_graph of movies in year 2000-2016 and Load Dataset revenue"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    usd_formatter = lambda x: '{:.10g}‎M$'.format(x)
    graph.value_formatter = usd_formatter
    graph.title = "Average Budget of Movies per year"
    for year in range(2000, 2017):
        print(">> Year : %i" % year)
        # Start display
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
        budget = dataset["budget"].tolist() #budget
        temp = []
        for i in budget:
            if i != 0:
                temp.append(i)
        average = ((((sum(temp)/len(temp)))/1000000//0.01)/100)
        graph.add(str(year), [{'value': average, 'max_value': 100}])
        # End display
        print(">> [status] Created Graph Successful!")
    graph.render_to_file("Graph_Export/Average_Budget_of_Movies.svg")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

#--Select_number 6---------------------------------------------------------------------------------------------------|

def average_revenue():
    """ Create Revenue of Movies average_graph of movies in year 2000-2016 and Load Dataset revenue"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    usd_formatter = lambda x: '{:.10g}‎M$'.format(x)
    graph.value_formatter = usd_formatter
    graph.title = "Average Revenue of Movies per year"
    for year in range(2000, 2017):
        print(">> Year : %i" % year)
        # Start display
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
        revenue = dataset["revenue"].tolist() #Revenue
        temp = []
        for i in revenue:
            if i != 0:
                temp.append(i)
        average = ((((sum(temp)/len(temp)))/1000000//0.01)/100)
        graph.add(str(year), [{'value': average, 'max_value': 250}])
        # End display
        print(">> [status] Created Graph Successful!")
    graph.render_to_file("Graph_Export/Average_Revenue_of_Movies.svg")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

#--Select_number 7---------------------------------------------------------------------------------------------------|

def average_runtime():
    """ Create Runtime of Movies average_graph of movies in year 2000-2016 and Load Dataset rate"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    graph.value_formatter = lambda x: '{:.10g}‎Min'.format(x)
    graph.title = "Average Runtime of Movies per year"
    for year in range(2000, 2017):
        print(">> Year : %i" % year)
        # Start display
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
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

#--Select_number 8---------------------------------------------------------------------------------------------------|

def rate_movies():
    """ Create Top-20 Rated of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
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

#--Select_number 9----------------------------------------------------------------------------------------------------|

def budget_movies():
    """ Create Top-20 Budget of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
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

#--Select_number 10---------------------------------------------------------------------------------------------------|

def revenue_movies():
    """ Create Top-20 Revenue of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
        title = dataset["title"].tolist() #Title Movies
        revenue = dataset["revenue"].tolist() #Revenue
        data = []
        for j in range(len(title)):
            data.append([title[j], revenue[j]])
        data.sort(key=lambda x: x[1], reverse=True)
        graph = pygal.HorizontalBar(x_title="Revenue")
        graph.value_formatter = lambda x: '{:.10g}‎M'.format(x)
        graph.title = "Top-20 Revenue of Movies in %i Dataset" % year
        for i in range(20):
            graph.add(data[i][0], data[i][1] / 1000000 // 0.01 / 100)
        graph.render_to_file("Graph_Export/Top-20_Revenue/Top-20_Revenue_%i.svg" % year)
        # End display
        print(">> [status] Created Graph Successful!")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

#--Select_number 11---------------------------------------------------------------------------------------------------|

def runtime_movies():
    """ Create Top-20 Runtime of Movies bar_graph of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        # Start display
        print(">> Year : %i" % year)
        print(">> [status] Create Graph Starting!")
        dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
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

#--Select_number 12---------------------------------------------------------------------------------------------------|

def all_average():
    """ Create All Average of Movies average_graph of movies in year 2000-2016 and Load Dataset rate"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    time_formatter = lambda x: '{:.10g}‎Min'.format(x)
    usd_formatter = lambda x: '{:.10g}‎M$'.format(x)
    graph.title = "Average in year 2000-2016"
    # Start display
    print(">> [status] Create Graph Starting!")
    select_mode = {'rate': 10, 'budget': 100, 'revenue': 200, 'runtime': 200}
    for mode in select_mode:
        all_rate = []
        for year in range(2000, 2017):
            print(mode, ">> Year : %i" % year)
            dataset = pd.read_csv("Top-100_Export/Top-100_%i.csv" % year)
            rate = dataset[mode].tolist() #Rate
            all_rate.extend(rate)
        if mode == 'rate':
            average = ((sum(all_rate)/len(all_rate))//0.01)/100
            graph.add(mode.title(), [{'value': average, 'max_value': select_mode[mode]}])
        elif mode == 'runtime':
            temp = []
            for i in all_rate:
                if i > 0:
                    temp.append(i)
            average = ((sum(temp)/len(temp))//0.01)/100
            graph.add(mode.title(), [{'value': average, 'max_value': select_mode[mode]}], formatter=time_formatter)
        else:
            temp = []
            for i in all_rate:
                if i != 0:
                    temp.append(i)
            average = ((((sum(temp)/len(temp)))/1000000//0.01)/100)
            graph.add(mode.title(), [{'value': average, 'max_value': select_mode[mode]}], formatter=usd_formatter)
    # End display
    print(">> [status] Created Graph Successful!")
    graph.render_to_file("Graph_Export/All_Average_of_Movies.svg")
    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

# ----------------------------------------------------------------------------------------------------------------------|

the_movies()
