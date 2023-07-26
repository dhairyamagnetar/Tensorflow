import requests
from bs4 import BeautifulSoup
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

scheduler = BlockingScheduler()
# Use panda to structure the data into a format and convert it into csv or json file.
# header file to interact with the website like a user.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


# Function created to scrape fram a given url and store it into fiel on the path.
def scrapeAndStore(path, url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    contentList = soup.find_all(class_="cor-p2")

    # Open the file in write mode
    with open(path, "w") as file:
        # for item in contentList:
        #     content = item.get_text(strip=True)
        #     file.write(content + "\n")
        # Write the content to the file
        # for item in contentList:
        #     pElements = item.find_all()
        #     for p in pElements:
        #         file.write(p.get_text() + "\n")
        with open(path, "w") as file:
            for item in contentList:
                for element in item:
                    file.write(element.get_text())
                file.write("\n")


# Extract the information of imtech cse into the "imtech" file in data folder
path = "data/imtechCSE.txt"
url = "https://www.iiitb.ac.in/academics/integrated-programmes/integrated-mtech-computer-science-and-engineering"
scheduler.add_job(scrapeAndStore, "interval", seconds=3, args=[path, url])


path = "data/mtechCSE.txt"
url = "https://www.iiitb.ac.in/academics/masters-programmes/mtech-computer-science-and-engineering"
scrapeAndStore(path, url)

path = "data/imtech.txt"
url = "https://www.iiitb.ac.in/courses/integrated-mtech"
scrapeAndStore(path, url)

# start the scheduling
scheduler.start()
