import pandas as pd
df = pd.read_csv("global_trust_survey.csv")

# get list of countries and indicators
countries = df.COUNTRY.unique() 
indicators = df.columns[2:]

# create empty dataframe to store countries' trust rate
df_rate = pd.DataFrame(columns=["Country", *indicators])
df_rate.Country = countries

# calculate rates for each countries
for i, country in enumerate(countries):
    temp = df[df.COUNTRY == country]
    rates = []
    # calculate rates for each indicators
    for indicator in indicators:
        num_of_trust = len(temp[temp[indicator].isin([1,2])]) # 1 and 2 answer
        num_of_data = len(temp[temp[indicator] != 99]) # remove null
        try:
            rate = round(num_of_trust/num_of_data*100, 2)
        except:
            rate = ""
        rates.append(rate)
    # add rates to dataframe
    df_rate.iloc[i,1:] = rates

# save as csv file
df_rate.to_csv("global_trust-rate.csv", index=None)