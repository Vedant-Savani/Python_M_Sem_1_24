class OutofStockError(Exception):

    def __init__(self) -> None:
        pass

class MissingDetailsError(Exception):

    def __init__(self) -> None:
        pass

class Books:

    bookDetails = {}

    def __init__(self) -> None:
        pass

    def addBook(self, bookDetails : dict) -> dict:

        #input dictionary format = {<bookID> : {'name' : '' , 'total' : <int>, 'available' : <int>, 'binNo' : '', 'borrowers' : []}}

        bookID = list(bookDetails.keys())[0]
        bookInfo = bookDetails[bookID]

        try:
            Books.bookDetails[bookID] = {
                'name' : bookInfo['name'],
                'total' : bookInfo['total'],
                'available' : bookInfo['available'],
                'binNo' : bookInfo['binNo'],
                'borrowers' : bookInfo['borrowers']
            }

        except:
            print('Missing details!')

        finally:
            return Books.bookDetails
        

#**********************************************************************


    def removeBook(self, bookID : str) -> dict:

        try:
            del Books.bookDetails[bookID]
        
        except:
            print('Book not yet stocked!')

        finally:
            return Books.bookDetails
        

#***********************************************************************
        

    def borrowBook(self, bookID : str, borrower : str) -> dict:

        try:

            if borrower == '' or bookID == '':
                raise MissingDetailsError

            if Books.bookDetails[bookID]['available'] > 0:
                Books.bookDetails[bookID]['available'] -= 1
                Books.bookDetails[bookID]['borrowers'].append(borrower)

            else:
                raise OutofStockError
            
        except MissingDetailsError:
            print('Details Missing!')
            
        except OutofStockError:
            print('Book out of stock!')

        except:
            print('Book not yet stocked!')

        finally:
            return Books.bookDetails
        

#**********************************************************************
        
    
    def returnBook(self, bookID : str, borrower):

        try:

            if borrower == '' or bookID == '':
                raise MissingDetailsError
            
            Books.bookDetails[bookID]['available'] += 1
            Books.bookDetails[bookID]['borrowers'].remove(borrower)

        except MissingDetailsError:
            print('Details Missing!')

        except:
            print('Book not yet stocked!')


        
    def __str__(self) -> dict:
        return str(Books.bookDetails)
    

#***********************************************************************
        
    
def main() -> int:

    books = Books()

    Books.bookDetails = {'abc123':{'name' : 'ABC', 'total' : 5, 'available' : 5, 'binNo' : 'k123', 'borrowers' : ['Vedant', 'Sankalp']},
                         'def123':{'name' : 'DEF', 'total' : 5, 'available' : 5, 'binNo' : 'p123', 'borrowers' : ['Anish','Aryan']}}
    
    print(books)

    books.addBook({'xyz123' : {}})

    books.addBook({'xyz123' : {'name' : 'XYZ', 'total' : 5, 'available' : 5, 'binNo' : 'q123', 'borrowers' : ['Anish', 'Teja', 'Bramha']}})

    print(books)

    books.removeBook('abc123')
    books.removeBook('axy')

    print(books)

    books.borrowBook('abc123', '')
    books.borrowBook('abc123', 'Anish')

    print(books)

    for _ in range(5):
        books.borrowBook('def123', 'Anish')

    books.borrowBook('def123', 'Anish')

    print(books)

    books.returnBook('', '')
    books.returnBook('def', 'Anish')
    books.returnBook('def123', 'Anish')

    print(books)

    return 0
    

if __name__ == '__main__':
    main()

