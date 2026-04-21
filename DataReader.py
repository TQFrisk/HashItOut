#DataReader.py for HashSomething Out hw 4 -2
#Purpose: reads a csv file (MOCK_DATA.csv in HashItOutMaker) and
#cleans up the data and assigns to 'records' using csv's dictreader

import csv

#handleBlank
#parameter:
    #field: the field/value for the csv
    #tries to account for empty, and extra spaces
#return:
#   returns cleaned up field entry
def handleBlank(field):
    if field is None:
        return ""
    field = field.strip()
    if field =="":
        return ""
    
    return field
        
#MovieRecord
#parameter: row
#   the rows in the .csv file
#purpose: This class defines the MovieRecord object by taking in the items, with
#each variable representing one of the columns from the csv
class MovieRecord:
    def __init__(self, row):
        self.movie_title = handleBlank(row["movie_title"])
        self.genre = handleBlank(row["genre"])
        self.release_date = handleBlank(row["release_date"])
        self.director = handleBlank(row["director"])
        self.box_office_revenue = handleBlank(row["box_office_revenue"])
        self.rating = handleBlank(row["rating"])
        self.duration_minutes = handleBlank(row["duration_minutes"])
        self.production_company = handleBlank(row["production_company"])
        self.quote = handleBlank(row["quote"])
        self.row = row


#standard csv.DictReader 
def loadData(filename):
    data = []

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            record = MovieRecord(row)
            data.append(record)

    return data
