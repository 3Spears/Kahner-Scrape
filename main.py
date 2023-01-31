import requests
from bs4 import BeautifulSoup
import csv

#make a class that has a name and a title
class Person:
    def __init__(self, name, title):
        self.name = name
        self.title = title





def main():
    URL = "https://www.kahnerglobal.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    #find the data-testid attribute
    results = soup.find('div', {'data-testid': 'matrix-gallery-items-container'})


    children = results.findChildren("div" , recursive=False)

    #make a list of people
    people = []

    for child in children:
        name = child.find('div', {'data-testid': 'gallery-item-title'}).text
        title = child.find('p', {'data-testid': 'gallery-item-description'}).text
        person = Person(name, title)
        people.append(person)



    #make a csv file with a name and title column
    with open('people.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Title"])

        for person in people:
            writer.writerow([person.name, person.title])

if __name__ == "__main__":
    main()

