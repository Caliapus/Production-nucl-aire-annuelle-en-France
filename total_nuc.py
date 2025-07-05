import pandas as pd
import locale
import requests
import zipfile
import io
import os
from datetime import datetime


# Define the URL of the zip file
url = 'https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip'

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Open the zip file from the response content
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # Extract all contents to the current directory
    z.extractall()

with open('eCO2mix_RTE_En-cours-TR.xls', encoding='latin1') as f:
    lines = f.readlines()

# Add a fake header name for the empty column
lines[0] = lines[0].strip('\n') + '\tExtra\n'

from io import StringIO
df = pd.read_csv(StringIO(''.join(lines)), sep='\t', encoding='latin1', low_memory=False)

df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Heures'])

df = df[['datetime', 'Nucléaire', 'Consommation']]
df = df.dropna(subset=['Nucléaire'])

# Filter for only rows from this year (useless redundant. But, heck, one never knows)

df = df[df["datetime"].dt.year == datetime.now().year].copy()

# Sort by datetime (just in case)
df.sort_values("datetime", inplace=True)

# Reset index for easy iteration
df.reset_index(drop=True, inplace=True)

# Calculate energy in MWh using trapezoidal integration
df["nuclear_avg"] = (df["Nucléaire"].shift(1) + df["Nucléaire"]) / 2
df["consumption_avg"] = (df["Consommation"].shift(1) + df["Consommation"]) / 2

# Energy over 15-minute intervals = avg power × 0.25h
df["nuclear_MWh"] = df["nuclear_avg"] * 0.25
df["consumption_MWh"] = df["consumption_avg"] * 0.25

# Drop any row with NaN (first one due to shift)
df.dropna(inplace=True)

# Sum totals
total_nuclear = df["nuclear_MWh"].sum()
total_consumption = df["consumption_MWh"].sum()

# Group by month and sum the energies
monthly_energy = df.groupby(df["datetime"].dt.to_period("M")).agg({
    "nuclear_MWh": "sum",
    "consumption_MWh": "sum"
}).reset_index()

#Affichage

# Set locale to French (works on most Unix-based systems)
try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.latin1')
except locale.Error:
    # On Windows, you might need 'French_France' or similar:
    locale.setlocale(locale.LC_TIME, 'French_France')
monthly_energy['Mois'] = monthly_energy['datetime'].dt.strftime('%B %Y').str.capitalize()

# Format energy columns as strings with comma decimal separator and space thousands separator
monthly_energy['Nucléaire (TWh)'] = (monthly_energy['nuclear_MWh']/1000000).map(lambda x: f"{x:,.2f}".replace(',', ' ').replace('.', ','))
monthly_energy['Consommation (TWh)'] = (monthly_energy['consumption_MWh']/1000000).map(lambda x: f"{x:,.2f}".replace(',', ' ').replace('.', ','))

# Select and reorder columns for nicer display
pretty_df = monthly_energy[['Mois', 'Nucléaire (TWh)', 'Consommation (TWh)']]


last_date = df['datetime'].max()
print ("\n-----------------------------\n")
print(last_date.strftime("%A %d %B %Y à %H:%M"))

print ("\n-----------------------------\n")
print(pretty_df.to_string(index=False))

print ("\n-----------------------------\n")
print(f"🔋 Production nucléaire totale en 2025: {f'{total_nuclear/1000000:,.2f}'.replace(',', ' ').replace('.', ',')} TWh")
print(f"⚡ Consommation totale en 2025: {f'{total_consumption/1000000:,.2f}'.replace(',', ' ').replace('.', ',')} TWh")

