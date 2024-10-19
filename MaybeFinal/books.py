import CSV_Handler as csvh
import UI as gui
import datetime as dt

class MissingDetailsError(Exception):
    def __init__(self) -> None:
        pass

class BookNotInStockError(Exception):
    def __init__(self) -> None:
        pass

class OutOfStockError(Exception):
    def __init__(self) -> None:
        pass

class BorrowLimitReachedError(Exception):
    def __init__(self) -> None:
        pass

class BookNotBorrowedError(Exception):
    def __init__(self) -> None:
        pass


class Books:

    bookDetails = {}
    bookHistory = {}

    #format of details dict :   { 'bookID' : { 'name': <> , 'author':<> , 'total':<> , 'available':<> , 'bin':<> , 'borrowers': [ 'rollnumber1','rollnumber2']  } }
    #{bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ],
                # bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ] }


    def __init__(self) -> None:
        pass

    def addBook(self, book : dict = {}) -> None:

        bookID = list(book.keys())[0] #collects bookID
        bookInfo = book[bookID] #collects book information
        
        try:
            if book == {}: #if nothing is passed
                raise MissingDetailsError

            keys = ('name','author','total','available','bin', 'borrowers') #must be present

            for key in keys:
                if key not in list(bookInfo.keys()) or bookInfo[key] == None or (bookInfo[key] == '' and key != keys[-1]): #if any detail is missing
                    raise MissingDetailsError
                
            
            if bookID not in list(Books.bookDetails.keys()): #if book is not already present
                Books.bookDetails[bookID] = {
                    'name' : bookInfo['name'],
                    'author' : bookInfo['author'],
                    'total' : bookInfo['total'],
                    'available' : bookInfo['available'],
                    'bin' : bookInfo['bin'],
                    'borrowers' : bookInfo['borrowers']
                }

                gui.GUI.success('Success','Book Added!')


            else: #if book is already present
                gui.GUI.success('Success','Book already present! Updated Stock!')
                Books.bookDetails[bookID]['total'] = int(bookInfo['total']) + int(Books.bookDetails[bookID]['total']) #update stock
                Books.bookDetails[bookID]['available'] = int(bookInfo['available']) +int(Books.bookDetails[bookID]['available'])  #update available quantity

        except MissingDetailsError: #if any detail is missing
            gui.GUI.alert('Error','Missing Details!')
 
        finally: #after handling all errors/tasks
            csvh.CSV_Handler.updateBooks(Books.bookDetails)  #update the CSV file
            print("FROM BOOK.PY ++>")
            print(Books.bookDetails)
            
            


#*************************************************************************

    def removeBook(self, bookID : str = '') -> None:

        try:
            if bookID == '': #if detail is missing
                raise MissingDetailsError

            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError
            
            else: #if book is stocked
                del Books.bookDetails[bookID]
                gui.GUI.success('Success!', f'Book with ID \'{bookID}\' Removed!')

        except MissingDetailsError:
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError:
            gui.GUI.alert('Error','Book not yet stocked!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails) #update CSV file
            


#***********************************************************************


    def borrowBook(self, bookID : str = '', borrower : str = '') -> None:

        try:
            if bookID == '' or borrower == '': #if any detail is missing
                raise MissingDetailsError
            
            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError
            
            elif borrower in Books.bookDetails[bookID]['borrowers']: #if the same user has already borrowed this book
                raise BorrowLimitReachedError
        
            elif Books.bookDetails[bookID]['available'] == 0: #if book is out of stock
                raise OutOfStockError
        
            else: #if nothing goes wrong
                Books.bookDetails[bookID]['available'] = int(Books.bookDetails[bookID]['available'])-1
                Books.bookDetails[bookID]['borrowers'].append(borrower)
                gui.GUI.success('Success!', f'Book with ID \'{bookID}\' Borrowed!')

                #{bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ],
                # bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ] }

                if bookID not in list(Books.bookHistory.keys()): #if book has not been modified yet
                    Books.bookHistory[bookID] = []    
                   
                Books.bookHistory[bookID].append({borrower : [str(dt.date.today()), None]})

                csvh.CSV_Handler.updateHistory(Books.bookHistory)



        except MissingDetailsError: #if details are missing
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError: #if book is not stocked in library
            gui.GUI.alert('Error','Book not yet stocked!')

        except BorrowLimitReachedError: #if the same user has already borrowed this book
            gui.GUI.alert('Error','Cannot borrow the same book again before returning!')

        except OutOfStockError: #if book is out of stock
            gui.GUI.alert('Error','Book out of stock!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails)
            


#**********************************************************************


    def returnBook(self, bookID : str = '', borrower : str = '') -> None:

        try:
            if bookID == '' or borrower == '': #if any detail is missing
                raise MissingDetailsError

            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError
            
            elif borrower not in Books.bookDetails[bookID]['borrowers']: #if user has not borrowed this book
                raise BookNotBorrowedError
            
            else: #if nothing goes wrong
                Books.bookDetails[bookID]['available'] = int(Books.bookDetails[bookID]['available'])+1
                Books.bookDetails[bookID]['borrowers'].remove(borrower)
                gui.GUI.success('Success!','Book Returned!')

                #{bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ],
                # bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ], bookID : [ {<roll>:[bd,rd]} ,  {<roll>:[bd,rd]} ] }

                for bookIDs in list(Books.bookHistory.keys()):
                    for infoDict in Books.bookHistory[bookIDs]:
                        if infoDict[list(infoDict.keys())[0]][1] == None and borrower == list(infoDict.keys())[0] and bookIDs == bookID:
                            infoDict[list(infoDict.keys())[0]][1] = str(dt.date.today())
                            

        except MissingDetailsError: #if details are missing
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError: #if book is not stocked in library
            gui.GUI.alert('Error','Book not yet stocked!')

        except BookNotBorrowedError: #if book has not been borrowed
            gui.GUI.alert('Error','Book not yet borrowed!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails)

        
        csvh.CSV_Handler.updateHistory(Books.bookHistory)



#***********************************************************************         
        
    def __str__(self) -> str:
        return str(Books.bookDetails)
            
#************************************************************************


        
    
def main() -> int: #test cases

    books = Books()

    '''

    Books.bookDetails = {'abc123':{'name' : 'ABC', 'total' : 5, 'author': 'Anish', 'available' : 5, 'bin' : 'k123', 'borrowers' : ['Vedant', 'Sankalp']},
                         'def123':{'name' : 'DEF', 'total' : 5, 'author' : 'Teja','available' : 5, 'bin' : 'p123', 'borrowers' : ['Aryan']}}
    
    print(books)

    books.addBook({'xyz123' : {}})

    books.addBook({'xyz123' : {'name' : 'XYZ', 'total' : 5, 'author' : 'Bramha', 'available' : 5, 'bin' : 'q123', 'borrowers' : ['Anish', 'Teja', 'Bramha']}})

    print(books)

    books.removeBook('abc123')
    books.removeBook('axy')

    print(books)

    books.borrowBook('abc123')
    books.borrowBook('abc123', 'Anish')

    print(books)

    books.borrowBook('def123', 'Anish')
    books.borrowBook('def123', 'Anish')
    books.borrowBook('def123', 'Teja')
    books.borrowBook('def123', 'Bramha')
    books.borrowBook('def123', 'Vedant')
    books.borrowBook('def123', 'Aryan')
    books.borrowBook('def123', 'Sankalp')
    books.borrowBook('def123', 'Person')
    books.borrowBook('def123', 'People')

    print(books)

    books.returnBook()
    books.returnBook('def', 'Anish')
    books.returnBook('def123', 'Anish')
    books.returnBook('def123', 'Anish')

    print(books)

    books.borrowBook('def123','Anish')

    '''

    books.addBook({'abcxyz' : {'name' : 'Demo Book', 'total' : 5, 'author' : 'Anish', 'available' : 5, 'bin' : 'K123', 'borrowers' : []}})
    books.borrowBook('abcxyz', 'IMT2024029')
    # books.returnBook('abcxyz', 'IMT2024029')

    books.addBook({'VedantID' : {'name' : 'Vedant', 'total' : 5, 'author' : 'Sankalp', 'available' : 5, 'bin' : 'BIN', 'borrowers' : []}})
    books.borrowBook('abcxyz', 'Anish')
    books.returnBook('abcxyz', 'IMT2024029')
    books.returnBook('abcxyz', 'Anish')
    # books.borrowBook('abcxyz', 'Anish')

    

    return 0
    

if __name__ == '__main__':
    main()
