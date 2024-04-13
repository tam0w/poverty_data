# Estimation of National Poverty using Data Analysis

This project attempts to analyse and estimate poverty indicators at the Indian district level. We consider various parameters from the 2011 census data that may be relevant to the estimation of poverty in a district, and join them with their relevant poverty indicators. 

To estimate and mesaure poverty we use the multi-dimensional poverty index (MPI) based on the 2023 NITI Aayog report which has the headcount of persons under the MPI line for the years 2014 and 2019. We will be using the head-count of the 2014 MPI for each district. This data will be scraped out of the report PDF file (resources/NITI_2023.pdf), and be stored in resources/dataset.csv

This project is made in dash-plotly to create a responsive dashboard fully in a python environment.

## Dashboard

The plotly-based dashboard created looks like that. It provides 3 crucial graphs that give us crucial insights on to how the demographics of that state look, both aggregated and over the different districts.  

- A scatterplot indicating if there is a correlation b/w literate population of a district and the poverty level of the same.

- A grouped bar graph, that compares the population, literate population, and workign population for the state segregated by sex.

- A line plot that shows the MPI HCR level for all the districts in the state in decreasing order.

<img title="" src="https://github.com/tam0w/poverty_data/blob/master/assets/use2.png?raw=true" alt="" width="800">

You can choose any of the administrative states or union territories as of census data of 2011. At the time of the 2011 census, there were a recorded 640 districts. The HCR values will be considered for only these districts. There is no available data for a poverty indicator at the district level in the year 2011.

<img title="" style="text-align:center" src="https://github.com/tam0w/poverty_data/blob/master/assets/use1.png?raw=true" alt="" width="800">


