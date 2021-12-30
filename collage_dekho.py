
import requests, json
from pprint import pprint
from bs4 import BeautifulSoup

link = ("https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/")
res = requests.get(link)
soup = BeautifulSoup(res.content, "html.parser")
name = soup.findAll("div", class_="collegeinfo")
Name = []
for names in name :
    Name.append('https://www.collegedekho.com/'+names.find('div',class_='title').a['href'])

def college_dekho():
    list1 = []
    dict = {}
    for i in Name:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, "html.parser")
        dict["Name"] = soup.find("div", class_="collegeInfo").find('h1',class_="tooltip").text.split('\n')[0].strip()
        dict["Type_of_college"] = soup.find(class_= "data").text
        dict["Address"] = soup.find("span", class_= "location").text
        dict["Email_Address"] = soup.find('div',class_="collegeAddress").findAll('div',class_='data')[1].text.strip()
        # dict["Contact_Number"] = soup.find("div",class_="collegeContacts").find("div", class_="data").text.split()
        dict["Contact_Number"] = soup.find('div',class_="collegeAddress").find('div',class_='data').text.split('\n')[3].strip()
        dict["Facilities"] = soup.find("div", class_="block facilitiesBlock").find("div", class_="box").text
        rates = soup.find_all("div", class_= "rating-per")

        for rate in rates:
            a = (rate.find("div", class_="star-ratings-sprite"))
            b = (str(a).split("=")[-1][7:11])
            dict["Rating"] = (float(b)/20)
        list1.append(dict.copy())
        
    files_name = open("College_dekho_data.json", "w")
    json.dump(list1, files_name, indent = 4)
    files_name.close()
    return list1

college = college_dekho()
# pprint(college)
