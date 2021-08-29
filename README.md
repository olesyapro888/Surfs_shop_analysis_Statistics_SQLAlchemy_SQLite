# Surfs shop analysis. Project 9 of the UofT.
## `-Contents-`	
	
- [Overview of the Project](#overview-of-the-Surf-shop-Analysis)	
- [Resources](#resources)	
- [Surfs up Analysis Result](#surf-shop-Analysis-Result)	
  - [1 difference](# )	
  - [2 difference ](#)
  - [3 difference ](#)		 
- [ Analysis Summary](#surf-shop-Analysis-Summary)	
## `Overview of the Surf shop Analysis`	
	
The purpose for the Surfs shop analysis is to determine if the surf and ice cream shop business sustainable year-round. 
The tasks of the Challenge are:
1. Retrieve all the temperatures for the 2 months of June and December. Convert the temperatures to a list, create a DataFrame from the list, and generate the summary statistics.
2. Write a report that describes the key differences in weather between June and December and two recommendations for further analysis.
## `Resources`	
The analysis was created using next resources:	
  - Data Source: [Resources](./Resources/).	
  - Software: Python 3.8.8, Pandas 1.2.4, Jupyter-notebook 6.3.0, SQLAlchemy, PostgreSQL 11.12 and pgAdmin 5.5.	
## `Surf shop Analysis Result`	
There is a bulleted list that addresses the three key differences in weather between June and December

Full results can be found in the [SurfsUp_Challenge](./SurfsUp_Challenge.ipynb) file.	
### ` - The difference (min, max, mean) in the summary statistics for the June and December temperatures`	

Based on the summary statistics for the June and December temperatures, the good temperatures are sustainable year-round the surf and ice cream shop business.
 
The not significant (less 5%) differences of the summary statistics display following:
  - mean is greater in June by almost 4&deg;F;
  - min is greater in June by almost 8&deg;F;
  - max is greater in June by almost 4&deg;F.

![image](https://user-images.githubusercontent.com/68247343/131223675-5d82fffc-83c1-412e-9f86-0b343f3a3fd4.png)

### ` - The difference (std) in the summary statistics for the June and December temperatures`

The standard deviation in the summary statistics for the June and December temperatures is higher in December than June. That means the temperatures are volatile and often changeable between min and max.
  
screen boxplot and plot
### ` - The third difference between the June and the December temperatures`	

Additionally, there is a difference between the June and the December temperatures as most of June's temperatures are between 71&deg;F - 81&deg;F comparing with December's temperatures: 65J&deg;F - 75&deg;F.

screen histogram
## `Surf shop Analysis Summary`	

The analysis provides a lot of summarizing and displays the main 3 differences between the June and the December temperatures:
- There are not significant (less 5%) differences of the summary statistics;
- The December's temperatures are volatile and often changeable between min and max;
- The  December's temperatures are colder comparing with June's temperatures approximately by 10&deg;F0.

But the analyse of temperatures is not enough for the opening the surf shop purpose. A fact -is a surfing after rainfall may seriously affect health. So, that is important to add precipitation analysis for the months of June and December to our temperature analysis.

The 2 can be chosen as main and essential business recommendations to pay attention.
Firstly, the rainfall is often in June than December but it's stronger in December. 

screen plot

Secondly, standard deviation is bigger by 34% in December than in June. So, storm rain is often in December.

Screen boxplot
