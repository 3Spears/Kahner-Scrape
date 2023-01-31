import requests
from bs4 import BeautifulSoup
import csv

#make a class that has a name and a title
class Person:
    def __init__(self, name, last, title):
        self.name = name
        self.last = last
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
        full_name = child.find('div', {'data-testid': 'gallery-item-title'}).text
        name = full_name.split()[0]
        last = full_name.split()[1]
        title = child.find('p', {'data-testid': 'gallery-item-description'}).text
        person = Person(name, last , title)
        people.append(person)



    #make a csv file with a name and title column
    with open('people.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Title"])

        for person in people:
            writer.writerow([person.name, person.last, person.title])

if __name__ == "__main__":
    main()

