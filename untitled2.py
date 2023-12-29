# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:42:36 2023

@author: Shashank
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_educational_institutions_in_Patna'

try:
    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table containing information about institutions
        table = soup.find('table', {'class': 'wikitable sortable'})

        # Check if the table is found
        if table:
            # Extract table rows
            rows = table.find_all('tr')

            # Lists to store extracted data
            institution_names = []
            types = []
            locations = []
            affiliations = []

            # Extract information for each row (skipping header row)
            for row in rows[1:]:
                columns = row.find_all('td')

                # Extracting data from columns
                name = columns[0].text.strip()
                inst_type = columns[1].text.strip()
                location = columns[2].text.strip()
                affiliation = columns[3].text.strip()

                # Appending data to respective lists
                institution_names.append(name)
                types.append(inst_type)
                locations.append(location)
                affiliations.append(affiliation)

            # Creating a DataFrame with the extracted data
            data = {
                'Institution Name': institution_names,
                'Type': types,
                'Location': locations,
                'Affiliation': affiliations
            }

            df = pd.DataFrame(data)

            # Writing data to an Excel file
            excel_file = 'Institutions_Patna_Wikipedia.xlsx'
            df.to_excel(excel_file, index=False)

            print(f'Excel file "{excel_file}" has been created with scraped data.')
        else:
            print("Table not found on the page.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Request error occurred: {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
