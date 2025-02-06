import pandas as pd
import numpy as np

# Read in bank_marketing.csv
bank_marketing = pd.read_csv("bank_marketing.csv")

# Create client dataframe
client = bank_marketing[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]
# Create campaign dataframe
campaign = bank_marketing[['client_id', 'number_contacts', 'month', 'day', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome']]
# Create economics dataframe
economics = bank_marketing[['client_id', 'cons_price_idx', 'euribor_three_months']]

# Clean client dataframe
client['job'] = client['job'].replace('.', '_')
client['education'] = client['education'].replace(('.', '_'), ('unknown', np.NaN))
client[['credit_default', 'mortgage']] = client[['credit_default', 'mortgage']].astype('bool')

# Clean campaign dataframe
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1, 'no': 0})
campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 0, 'nonexistent': 0})
campaign['day'] = campaign['day'].astype(str)
campaign['month'] = campaign['month'].str.capitalize()
campaign['year'] = '2022'
campaign['last_contact_date'] = campaign['year'] + '-' + campaign['month'] + '-' + campaign['day']
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'], format="%Y-%b-%d")

for col in ["campaign_outcome", "previous_outcome"]:
    campaign[col] = campaign[col].astype(bool)

campaign.drop(columns=['day', 'month', 'year'], inplace=True)

client.to_csv('client.csv', index=False)
campaign.to_csv('campaign.csv', index=False)
economics.to_csv('economics.csv', index=False)