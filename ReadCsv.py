import pymongo
import csv as csv_reader
mongo_connection = pymongo.MongoClient("mongodb://localhost")
db = mongo_connection.mathpix

#Reads CSV file from Local disk
def readCsvFile():
    with open('/Users/lingaraj/Desktop/questions_info_search.csv') as csv_file:
        row_count = 0
        read_csv = csv_reader.reader(csv_file,delimiter=',')
        db.drop_collection('questions')
        for row in read_csv:
           row_count = row_count + 1
           writeToCollection(row)
        print("Data Count:",row_count)
        pass

def writeToCollection(row):
    record = {'questionId':row[0],'questionText':row[1]}
    db.questions.insert_one(record)
    pass
if __name__ == '__main__':
    readCsvFile()