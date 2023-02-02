# data-dynamos-project-1

# Influencers of World Happiness Score and Suicide Rates

### Team Members: Leah Cho, Olga Dolzhko, Charlie Hinton, Oleksii Shumskyi

### Project Overview
•	Mental health issues are increasing in awareness and importance among the general public in recent years.
•	In this project, we set out to perform exploratory analysis to uncover the influencers of the World Happiness Score and Suicide Rates across the world.  We looked to quantify relationships between these two variables and other socio-economic indicators.
•	Mental Health for this project is quantified by the World Happiness Score and Suicide Rates by country:  the assumption being that the higher the happiness score the lower the country’s suicide rate.
•	Questions to answer with the data analysis:
–	Which countries have the highest and lowest 
happiness scores?
–	Which countries have the highest and lowest 
suicide rates per 100,000?
–	What are the linear relationships between socio-economic indicators and Happiness Score and Suicide Rates?


### Data
We used data from the 2022 World Happiness Report which contains the “happiness” scores from its annual Gallup Poll survey of 146 countries. We leveraged the following socio-economic data from the World Bank Group for years 2002-2019:  Adjusted Net National Income, Gross Domestic Product, Consumer Price Inflation, Life Expectancy, Unemployment Rate and Suicide Rates per 100,000 persons.  The Geoapify location platform API was used to plot maps of the datasets.

https://worldhappiness.report/ed/2022/

https://data.worldbank.org/

https://www.geoapify.com


### Approach
•	We performed ETL work on the datasets from worldbank.org
-	Ensured data were reported for the same set of countries across the 6 worldbank data sets
-	Transformed the numerical data from objects to float data types in Python
-	Condensed the datasets to the most relevant information
•	We calculated the mean values for the last 5 years reported for the worldbank data
•	Merged the data into a summary data containing 111 matched countries across all variables
•	Line graphs were created for each socio-economic variable showing the trend since 2002
•	Scatter plots and linear regressions were plotted between the following for all countries
•	The Geoapify API was used to determine the coordinates of each country and maps were generated with HVplot and Plotly Express Choropleth to showcase findings

### Findings
•	We uncovered moderate-to-strong, linear relationships between:
–	Happiness Score and Life Expectancy (R2 = 0.80) 
–	Happiness Score and Consumer Inflation (R2 = -0.43)
–	Suicide Rate and Unemployment Rate (R2 = 0.34) 

 

•	There doesn’t appear to be a linear relationship between Suicide Rate and Happiness Score

 

•	With more time, we would suggest:
–	Exploring more data sets from the World Bank to find other influencing variables
–	Conducting multivariate regression analysis with additional variables while controlling for multicollinearity

