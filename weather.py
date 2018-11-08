import requests
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt
import os.path
import csv
url = "http://www.seismonepal.gov.np/"
# get the response from the server
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# two li
time_in_hours = []
richter_scale = []
for rows in soup.find_all("tr"):
    for time in rows.find_all("td", class_="table-time"):
        time_real = time.get_text()

        print(time_real)

        time_in_hours.extend([time_real])
    for mag in rows.find_all("td", class_="table-magnitude"):
        magnitude = mag.get_text()
        print(magnitude)
        richter_scale.extend([magnitude])

with open("data.csv", 'w', encoding="utf-8", newline='') as toWrite:
    writer = csv.writer(toWrite)
    writer.writerows(time_in_hours)
    writer.writerows(richter_scale)

    # Matplotlib to plot data
plt.plot(richter_scale, time_in_hours)
plt.ylabel("Time in Hours")
plt.xlabel("Richter Scale")
plt.show()
