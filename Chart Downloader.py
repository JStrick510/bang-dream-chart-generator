#12 is url
#2 (romanji name), 4 (level), 7 (band)
#3 (difficulty), 5 (duration), 6 (max combo), 8 (release date), 9 (avg note density), 10 (main BPM), 11 (BPM range)

import csv
from bs4 import BeautifulSoup
import requests


def imageDownloader(filename):
    with open('chartscsv.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            file_name = row[2] + "-" + row[7] + "-" + row[4]
            print(file_name)

def main():
    imageDownloader('chartscsv.csv')

if __name__ == "__main__":
    main()
