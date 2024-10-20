import csv
from encryption import Encryption as E


class CSV_Handler:   

    #nested Dictionary
    #format of dict :   { 'bookID' : { 'name': <> , 'author':<> , 'total':<> , 'available':<> , 'bin':<> , 'borrowers': [ 'rollnumber1','rollnumber2']  } }
    @staticmethod
    def loadBooks():     #returns a dict containing information about Books
        dict={}
        with open('books.csv', mode ='r')as file:
            reader = csv.reader(file)
            for row in reader:    #format of row in CSV file: BookID , Name , Author , total , available , bin , <borrowerRollNumber:data(dd/mm/yyyy) seperated by spaces>
                dict[row[0]]={'name':row[1] , 'author':row[2] , 'total':row[3] , 'available':row[4]
                              ,'bin':row[5] , 'borrowers':row[6].strip().split(" ")}       
        return dict


#===============================================================================================================================================


    #nested Dictionary 
    #format of dict { "RollNumber" : { 'name':<name> , 'password':<pass> } }s
    @staticmethod
    def loadMembers():     #returns a dict containing information about memebers
        dict={}
        with open('members.csv', mode ='r')as file:
            reader = csv.reader(file)
            for row in reader:    #format of row in CSV file: Roll Number , Name , Password , Books Issued <seperated by " "spaces>
                dict[row[0]]={'name':row[1] , 'password':E.decrypt(row[2]) }       
        return dict
    


#===============================================================================================================================================


    #takes a dict of books (in the format as specified above)
    #and updates the books.csv file
    @staticmethod
    def updateBooks(dict):
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                borrowers=''
                for roll in dict[key]['borrowers']:
                    borrowers+=roll+" "
                row=[key,dict[key]['name'],dict[key]['author'],dict[key]['total'],dict[key]['available'],dict[key]['bin'],borrowers]
                writer.writerow(row)


#===============================================================================================================================================

    #takes a dict of memebers (in the format as specified above)
    #and updates the members.csv file
    @staticmethod
    def updateMembers(dict):
        with open('members.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                row=[key,dict[key]['name'],E.encrypt(dict[key]['password'])]
                writer.writerow(row)            


#===============================================================================================================================================


  
 
    @staticmethod
    def loadHistory():
        dict={}
        with open('history.csv', mode ='r')as file:
            reader = csv.reader(file)
            for row in reader:  
                dict[row[0]]= []
                for i in row[1].split(" "):
                    j=i.split("->")
                    roll=j[0]
                    k=j[1].split("~")
                    issued=k[0]
                    returned=k[1]
                    dict[row[0]].append({roll : [issued, returned]})
        return dict
    

    
    @staticmethod
    def updateHistory(dict):
        with open('history.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                data = ""
                for infoDict in dict[key]:
                    data += list(infoDict.keys())[0] + '->' + str(infoDict[list(infoDict.keys())[0]][0]) + '~' + str(infoDict[list(infoDict.keys())[0]][1]) + ' '                   

                writer.writerow([key, data.strip()])   

