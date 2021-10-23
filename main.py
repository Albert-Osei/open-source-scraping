from bs4 import BeautifulSoup
import csv
import requests

print('Put stack you are not interested in')
not_interested = input('>')
print(f'Filtering out {not_interested}')

web_text = requests.get('https://www.codetriage.com/?language=JavaScript').text
soup = BeautifulSoup(web_text, 'lxml')
projects = soup.find_all('li', class_='repo-item high')

file_name = 'OpenSourceProjects'

file = open(f'{file_name}.csv', 'w')
writer = csv.writer(file)

# write header rows
writer.writerow(['Repo Name', 'Number of Issues', 'Description', 'Stack', 'View Project'])

for project in projects:
    number_of_issues = int(project.find('span', class_='repo-item-issues').text[:4])
    if number_of_issues > 500:
        repo_name = project.find('h3').text
        description = project.find('p').text
        stack = project.find('span', class_='repo-item-full-name').text
        link = ('https://www.codetriage.com'+project.a['href'])
        if not_interested not in stack:
            writer.writerow([repo_name, number_of_issues, description, stack, link])

print(f'{file_name} has saved as csv file')
file.close()
