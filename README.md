# Bank Marketing Campaign

This project focuses on transforming raw bank marketing data into structured, clean datasets that can be seamlessly integrated into a PostgreSQL database. By organizing data into separate CSV files for client information, campaign interactions, and economic indicators, the project ensures future scalability for marketing analysis.

## Objectives
1. **Subset** the original dataset into three separate DataFrames: **client**, **campaign**, and **economics**.
2. **Clean** and **format** the data according to specified data types.
3. **Save** the cleaned DataFrames as CSV files.

## Dataset Description
- The original dataset, **bank_marketing.csv**, was processed and split into the following files:
- **client.csv** - Contains **demographic** and **financial information** about clients.
- **campaign.csv** - Records **details of marketing campaigns** and client interactions.
- **economics.csv** - Stores **economic indicators** related to the clients.

## Installation
Clone this repository and install the necessary libraries if required:
```bash
git clone https://github.com/JReaves10/BankMarketingCampaign
cd BankMarketingCampaign
```
Ensure you have Python and required libraries (pandas, numpy) installed.
Place the original **bank_marketing.csv** file in the working directory.
Run the script to generate the three CSV files.

Code Explanation

1. Reading the Dataset

import pandas as pd
import numpy as np

# Read in bank_marketing.csv
bank_marketing = pd.read_csv("bank_marketing.csv")

We begin by importing necessary libraries (pandas and numpy) and reading the dataset using pd.read_csv().

2. Creating DataFrames

Client DataFrame

Extract columns related to client information:

client = bank_marketing[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]

Campaign DataFrame

Select columns related to marketing campaign details:

campaign = bank_marketing[['client_id', 'number_contacts', 'month', 'day', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome']]

Economics DataFrame

Subset columns with economic indicators:

economics = bank_marketing[['client_id', 'cons_price_idx', 'euribor_three_months']]

3. Cleaning and Formatting

Client DataFrame Cleaning

Replace . with _ in the job column.

Replace unknown in the education column with NaN.

Convert credit_default and mortgage columns to boolean values.

client['job'] = client['job'].replace('.', '_')
client['education'] = client['education'].replace(('.', '_'), ('unknown', np.NaN))
client[['credit_default', 'mortgage']] = client[['credit_default', 'mortgage']].astype('bool')

Campaign DataFrame Cleaning

Map campaign_outcome and previous_outcome to binary values.

Format the day and month columns, and create a last_contact_date column.

Convert date column to datetime format and remove unnecessary columns.

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

4. Saving DataFrames as CSV Files

Each DataFrame is saved to a CSV file without including the index.

client.to_csv('client.csv', index=False)
campaign.to_csv('campaign.csv', index=False)
economics.to_csv('economics.csv', index=False)

Results

Three cleaned and formatted CSV files were generated: client.csv, campaign.csv, and economics.csv.

The data is now structured and ready for storage in a PostgreSQL database, enabling easier analysis and integration of future campaigns.

Conclusion

This project successfully demonstrates the process of data cleaning, reformatting, and storage for future marketing campaign analysis.

Technology Used

Programming Languages: Python

Libraries: Pandas, NumPy

