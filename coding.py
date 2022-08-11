
class standards():

    def view(self,book):

        book=["biology","physics","chemistry"]
        print(book)

    def borrow(self,):
        ai=['biology',"chemistry","physics"]
        print(ai)
        a=input("enter the book you want to return: ")
        if a in ai:
            ai.remove(a)
            print("book has been borrowed")
        else:
            print("sorry ,book has been borrowed ")
        print(ai)

    def return_book(self):
        ai=['biology',"chemistry","physics"]
        print(ai)
        a=input("enter the book you want to return: ")
        if a in ai:
            print("sorry you have not borrowed the book and trying to submit it")
        else:
            ai.append(a)
            print("your book has been submitted ")
        print(ai)



class student(standards):
    pass

if __name__=='__main__':
    while True:
        CENTRALLIBRARY=student
        print("*********welcome to the library*********\n")
        a=int(input('''type 1 to view the books 
        type 2 to borrow the book
        type 3 to return the book
        type 4 to exit the application\n'''))

        if a==1:
            CENTRALLIBRARY.view("a","b")
        elif a==2:
            CENTRALLIBRARY.borrow("a")
        elif a==3:
            CENTRALLIBRARY.return_book("a")
        elif a==4:
            exit()
        else:
            print("sorry invalid choice")

    
    
