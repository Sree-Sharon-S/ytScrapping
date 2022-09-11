from pathlib import Path
import csv

def csvWriter(lis):
    Path("scrape\\temp\\yt.csv").touch()
    file_to_write = open("scrape\\temp\\yt.csv", 'w', encoding="utf-8")
    pen = csv.writer(file_to_write)
    pen.writerow(["No","Video Links","Thumbnails","Title","Likes","Comments","Views","Download"])
    for record in lis:
        pen.writerow(record)
    file_to_write.close()

