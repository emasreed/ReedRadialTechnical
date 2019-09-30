import pandas as pd
import numpy as np

with open("Hospital General Information.csv") as csv_file:
    input_file = pd.read_csv(csv_file)

input_file['Hospital overall rating'] = pd.to_numeric(input_file['Hospital overall rating'],
                                                      errors='coerce')

acute_df = input_file.loc[input_file['Hospital Type'].str.contains('Acute Care Hospitals')]
acute_df = acute_df.groupby(['County Name', 'State']).agg(
    {'Provider ID': 'count', 'Hospital overall rating': [np.mean, np.median]}).reset_index()
acute_df.columns = ["_".join(x) for x in acute_df.columns.ravel()]
acute_df['county_state'] = acute_df['County Name_'] + ', ' + acute_df['State_']
acute_df = acute_df.rename(columns={'Provider ID_count': 'num_acute_care_hospitals',
                                    'Hospital overall rating_median': 'median_acute_care_rating',
                                    'Hospital overall rating_mean': 'avg_acute_care_rating'})
acute_df = acute_df.drop(['County Name_', 'State_'], axis=1)
acute_df['avg_acute_care_rating'] = np.round(acute_df['avg_acute_care_rating'], decimals=2)
acute_df = acute_df.set_index('county_state')


county_df = input_file.groupby(['County Name', 'State']).agg(
    {'Provider ID': 'count'}).reset_index()
county_df['county_state'] = county_df['County Name'] + ', ' + county_df['State']
county_df = county_df.rename(columns={'Provider ID': 'num_hospitals'})
county_df = county_df.drop(['County Name', 'State'], axis=1)
county_df = county_df.set_index('county_state')


county_df= county_df.join(acute_df, on='county_state')
county_df['pct_acute_care'] = np.round((county_df['num_acute_care_hospitals'] /
                                        county_df['num_hospitals'])*100, decimals=2)

county_df = county_df.sort_values(by=['num_hospitals'], ascending=False)
county_df.to_csv('hospitals_by_county.csv')
