import CSV_Handler as csvh
import UI as gui

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

    #format of dict :   { 'bookID' : { 'name': <> , 'author':<> , 'total':<> , 'available':<> , 'bin':<> , 'borrowers': [ 'rollnumber1','rollnumber2']  } }

    def __init__(self) -> None:
        Books.bookDetails = csvh.CSV_Handler.loadBooks()

    def addBook(self, book : dict = {}) -> None:
        
        try:
            if book == {}: #if nothing is passed
                raise MissingDetailsError
            
            bookID = list(book.keys())[0] #collects bookID
            bookInfo = book[bookID] #collects book information

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
                gui.GUI.success('Info','Book already present! Updated Stock!')
                Books.bookDetails[bookID]['total'] += bookInfo['total'] #update stock
                Books.bookDetails[bookID]['available'] += bookInfo['available'] #update available quantity

        except MissingDetailsError: #if any detail is missing
            gui.GUI.alert('Error','Missing Details!')

        except TypeError:
            gui.GUI.alert('Error','Wrong Information Entered!')
 
        finally: #after handling all errors/tasks
            csvh.CSV_Handler.updateBooks(Books.bookDetails)  #update the CSV file
            
            

#************************************************************************

    def removeBook(self, bookID : str = '') -> None:

        try:
            if bookID == '': #if detail is missing
                raise MissingDetailsError

            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError
            
            else: #if book is stocked
                del Books.bookDetails[bookID]
                gui.GUI.success('Success!','Book Removed!')

        except MissingDetailsError:
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError:
            gui.GUI.alert('Error', 'Book not yet stocked!')

        except TypeError:
            gui.GUI.alert('Error','Wrong Information Entered!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails) #update CSV file
            


#************************************************************************


    def borrowBook(self, bookID : str = '', borrower : str = '') -> None:

        try:
            if bookID == '' or borrower == '': #if any detail is missing
                raise MissingDetailsError
            
            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError()
            
            elif borrower in Books.bookDetails[bookID]['borrowers']: #if the same user has already borrowed this book
                raise BorrowLimitReachedError
        
            elif Books.bookDetails[bookID]['available'] == 0: #if book is out of stock
                raise OutOfStockError
        
            else: #if nothing goes wrong
                Books.bookDetails[bookID]['available'] -= 1
                Books.bookDetails[bookID]['borrowers'].append(borrower)
                gui.GUI.success('Success!', 'Book Borrowed!')

        except MissingDetailsError: #if details are missing
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError: #if book is not stocked in library
            gui.GUI.alert('Error','Book not yet stocked!')

        except BorrowLimitReachedError: #if the same user has already borrowed this book
            gui.GUI.alert('Error','Cannot borrow the same book again before returning!')

        except OutOfStockError: #if book is out of stock
            gui.GUI.alert('Error','Book out of stock!')

        except TypeError:
            gui.GUI.alert('Error','Wrong Information Entered!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails)
            

#*********************************************************************


    def returnBook(self, bookIDs : list = [], borrower : str = '', booksNotBorrowed : list = [], booksNotInStock : list = []) -> None:

        try:
            if bookIDs == [] or borrower == '':
                raise MissingDetailsError
            
            booksReturned = []
            
            for bookID in bookIDs:
                if bookID not in list(Books.bookDetails.keys()):
                    booksNotInStock.append(bookID)
                
                elif borrower not in Books.bookDetails[bookID]['borrowers']:
                    booksNotBorrowed.append(bookID)
                
                else:
                    Books.bookDetails[bookID]['available'] += 1
                    Books.bookDetails[bookID]['borrowers'].remove(borrower)
                    booksReturned.append(bookID)

            if len(booksNotBorrowed) != 0:
                #raise BookNotBorrowedError
                gui.GUI.alert('Error', f'Books with IDs: {booksNotBorrowed} have not been borrowed yet!')
                booksNotBorrowed.clear()
            
            if len(booksNotInStock) != 0:
                #raise BookNotInStockError
                gui.GUI.alert('Error!', f'Books with IDs: {booksNotInStock} have not been stocked yet!')
                booksNotInStock.clear()
            
            if len(booksReturned) != 0:
                gui.GUI.success('Success!', f'Books with IDs: {booksReturned} have been returned!')

        
        except MissingDetailsError: #if details are missing
            gui.GUI.alert('Error!','Missing Details!')

            '''except BookNotBorrowedError:
            gui.GUI.alert('Error!', f'Books with IDs: {booksNotBorrowed} have not been borrowed yet!')

            except BookNotInStockError:
            gui.GUI.alert('Error!', f'Books with IDs: {booksNotInStock} have not yet been stocked!')'''

        except TypeError:
            gui.GUI.alert('Error!', 'Wrong information entered!')

        finally:
            csvh.CSV_Handler.updateBooks(Books.bookDetails)

            


        '''try:
            if bookID == '' or borrower == '': #if any detail is missing
                raise MissingDetailsError

            elif bookID not in list(Books.bookDetails.keys()): #if book is not stocked in library
                raise BookNotInStockError
            
            elif borrower not in Books.bookDetails[bookID]['borrowers']: #if user has not borrowed this book
                raise BookNotBorrowedError
            
            else: #if nothing goes wrong
                Books.bookDetails[bookID]['available'] += 1
                Books.bookDetails[bookID]['borrowers'].remove(borrower)
                gui.GUI.success('Success!','Book Returned!')

        except MissingDetailsError: #if details are missing
            gui.GUI.alert('Error','Missing Details!')

        except BookNotInStockError: #if book is not stocked in library
            gui.GUI.alert('Error','Book not yet stocked!')

        except BookNotBorrowedError: #if book has not been borrowed
            gui.GUI.alert('Error','Book not yet borrowed!')

        except TypeError:
            gui.GUI.alert('Error','Wrong Information Entered!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateBooks(Books.bookDetails)'''
            
            


#**********************************************************************         
        
    def __str__(self) -> str:
        return str(Books.bookDetails)
            
#***********************************************************************


        
    
def main() -> int: #test cases

    books = Books()

    Books.bookDetails = {'abc123':{'name' : 'ABC', 'total' : 5, 'author': 'IMT00', 'available' : 5, 'bin' : 'k123', 'borrowers' : ['BT00', 'BT01']},
                         'def123':{'name' : 'DEF', 'total' : 5, 'author' : 'IMT01','available' : 5, 'bin' : 'p123', 'borrowers' : []}}
    
    print(books)

    books.addBook()
    books.addBook({'xyz123' : {}})
    books.addBook({'xyz123' : {'name' : 'XYZ', 'total' : 5, 'author' : 'IMT02', 'available' : 5, 'bin' : 'q123', 'borrowers' : ['IMT00', 'IMT01', 'IMT02']}})

    print(books)

    books.removeBook('abc123')
    books.removeBook('axy')

    print(books)

    books.borrowBook('abc123')
    books.borrowBook('abc123', 'IMT00')

    print(books)

    books.borrowBook('def123', 'IMT00')
    books.borrowBook('def123', 'IMT00')
    books.borrowBook('def123', 'IMT01')
    books.borrowBook('def123', 'IMT02')
    books.borrowBook('def123', 'IMT03')
    books.borrowBook('def123', 'BT00')
    books.borrowBook('def123', 'BT01')

    print(books)

    books.returnBook()
    books.returnBook(['def'], 'IMT00')
    books.returnBook(['def123','xyz123'], 'IMT00')
    books.returnBook(['def123','xyz'], 'IMT00')
    books.returnBook(['def123'], 'IMT00')

    print(books)

    books.borrowBook('def123','IMT00')

    return 0
    

if __name__ == '__main__':
    main()

