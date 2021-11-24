import requests
from bs4 import BeautifulSoup as bs
import re

TERMS = [
  "fall2018",
  "winter2019",
  "spring2019",
  "summer2019",
  "fall2019",
  "winter2020",
  "spring2020",
  "summer2020",
  "fall2020",
  "winter2021",
  "spring2021",
  "summer2021",
]

ROOT = "https://classes.engr.oregonstate.edu/"

DISCIPLINES = ["cbee", "cce", "eecs", "engr", "mime"]

f = open("all-engineering-instructors-by-term.csv", "w")

for term in TERMS:
  for discipline in DISCIPLINES:
    page = requests.get(f"{ROOT}/{discipline}/{term}")
    soup = bs(page.content, 'html.parser')
    sections = soup.find_all("li")
    for section in sections:
      if (match := re.match(r"(\S+) (\d+H?) (?:\(Section (\d+)\) )?(.+) \((.+)\)", section.text)):
        code, number, section, coursename, instructor = match.groups()
        if section == '001' or section == None:
          f.write(f'{term},{code},{number},"{instructor.strip()}"\n')

f.close()
