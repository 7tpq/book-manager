import csv

class Book:
    def __init__(self,title,author,pages,rating=None,status="not read"):
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = rating
        self.status = status

def main():
    services = ["Add Book", "Change reading status", "Show all the books", "Search for book", "Statistics", "or SHUT DOWN THE PROGRAM"]
    functions = {
         1: add_book,
         2: change_status,
         3: show_all_books,
         4: search_for_books,
         5: Statistics,
        6: shutdown
    }

    print("Welcome to Book Collection Manager\nOur services: ")
    for i, r in enumerate(services, start=1):
        print(f"{i}.{r}")

    while True:
        try:
            ch = int(input("\nPlease pick a service: "))
        except ValueError:
            print(f"Incorrect value, please try input a number from 1 to {len(services)}")
            continue
        if ch-1 in range(len(services)):
            functions[ch]()         
        else:
            print(f"please try input a number from 1 to {len(services)}")
        if ch == 6:
            break    


def add_book():
    while True:
            title = input("Enter the title of the book: ").strip()
            if not title:
                 print("Title is required")
                 continue

            author = input("The author: ").strip()
            if not author:
                 print("Author is required")
                 continue
            break
    while True:
        try:
            pages = int(input("Enter the number of pages: "))
        except ValueError:
            print("Invalid value")
            continue
        if pages <= 0:
            print("The number of pages should be positive")
        else:
            break

    rating = None
    while True:
        user_rate = input("Your rating from 1-10 or skip it by click enter: ")
        if user_rate == "":
            rating = None
            break
        try:
            rating = float(user_rate)
        except ValueError:
            print("Invalid value")
            continue
        if not (1 <= rating <= 10):
            print("The number should be from 1-10")
            continue
        else:
            break
    while True:    
        st = ["Finished","Still read it", "Not read it yet"] 
        for _,p in enumerate(st,start=1):
                print(f"{_}.{p}")
        try:
            status = int(input("Enter the book's condition: "))
        except ValueError:
            print("Invalid value") 
            continue   
        if status-1  in range(len(st)):
            print("correct")
            break 
        else:
            print(f"Pick a number from 1 to {len(st)}")

    with open("book.csv","a",newline="") as file:
        write = csv.writer(file)
        book = Book(title,author,pages,rating,status)
        write.writerow([book.title,book.author,book.pages,book.rating,book.status])
        print("WE SAVE THEM")

def change_status():
    se = input("Search for a book to update: ").strip()

    with open("book.csv", "r", newline="") as file:
        rows = list(csv.reader(file))

    for row in rows:
        if len(row) >= 5 and row[0].strip().lower() == se.lower():
            while True:
                st = ["Finished", "Still read it", "Not read it yet"]
                for _, p in enumerate(st, start=1):
                    print(f"{_}.{p}")
                try:
                    status = int(input("Enter the book's condition: "))
                except ValueError:
                    print("Invalid value")
                    continue

                if status - 1 in range(len(st)):
                    row[4] = str(status)
                    with open("book.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                    print("The book's condition has been changed")
                    return
                else:
                    print(f"Pick a number from 1 to {len(st)}")

    print("Book not found.")

def show_all_books():
    ma = []
    with open("book.csv","r",newline="") as file:
        reader = list(csv.reader(file))
        for i,r in enumerate(reader,start=1):
            ma.append(r)
            print(f"{i}.{r[0]}")
        print(f"The search found books {len(ma)}")
    do = input("Do you want to show books based on book's condition? ").lower().strip() 
    if do == "yes":
        while True:
            tm = ["Finished","Still read it", "Not read it yet"] 
            for _,c in enumerate(tm,start=1):
                print(f"{_}.{c}")
            try:
                ch = int(input("Enter the book's condition: "))
            except ValueError:
                print("Invalid value") 
                continue   
            if ch-1  in range(len(tm)):
                mathes =[]
                for i,r in enumerate(reader,start=1):
                    if len(r) >= 5 and ch == int(r[4]):
                        mathes.append(r)
                for i,r in enumerate(mathes,start=1):       
                        print(f"{i}.{r[0]},{r[4]}")
                break 
            else:
                print(f"Pick a number from 1 to {len(tm)}")
    else:
        print("We finish here!!!")                    
                
def search_for_books():
    
    se = input("Search for a book: ")
    with open("book.csv","r",newline="") as file:
        reader = list(csv.reader(file))
        for n in reader:
            if n[0] == se:
                print(f"The book: {n[0]} by {n[1]}\nThe pages of book:{n[2]},(rating:{n[3]})")
        if n[4] == "1":
                print("You finish read it")
        elif n[4] == "2":
                print("You still read it")
        else:
                print("You haven't read it yet")    

def Statistics():
    b_oo = []
    a_u =[]
    con_1 = []
    con_2 = []
    con_3 = []
    p_g = []
    t_r = []

    with open("book.csv","r",newline="") as file:
        reader = list(csv.reader(file))
        for n in reader:
            b_oo.append(n[0])
            a_u.append(n[1])
            p_g.append(n[2])
            t_r.append(n[3])
            if n[4] == "1":
                con_1.append(n[4])
            elif n[4] == "2":
                con_2.append(n[4])
            else:
                con_3.append(n[4]) 
    print(f"Book:{len(b_oo)}\nAuthors:{len(a_u)}")
    print(f"Books you finish from read them:{len(con_1)}")
    print(f"Books you still read them:{len(con_2)}")
    print(f"Books you haven't finished yet:{len(con_3)}")
    print(f"Total pages:{sum(int(n)for n in p_g)}")
    if len(t_r) == 0:
        print("Average rating: 0.00")
    else:
        print(f"{(sum(float(i)for i in t_r)) / len(t_r):.2f}") 
            
            
def shutdown():
    print("YOU OUT!")
    return 
      







if __name__ == "__main__":
    main()        

    