import pandas as pd
import matplotlib.pyplot as plt

print("---------------------LIBRARY MANAGEMENT SYSTEM-----------------------")

#Reading the data from the CSV File
df1=pd.read_csv('student_details.csv')
df2=pd.read_csv('book_details.csv')

def addmember():
    global df1
    #Getting inputs from the user
    print("ENTER YOUR DETAILS TO GET ADDED IN OUR LIBRARY")
    name=input("Enter your name:")
    name=name.lower()
    sapid=int(input("Enter your Sap ID:"))
    if len(str(sapid)) != 9: 
        print("Enter your correct sapid")
        exit()
    password=input("Enter your Password:")

    if(sapid not in df1['Sap ID'].values):
        #Storing the user inputed values in a Dictionary
        dict2={'Student Name':name,'Sap ID':sapid,'Password':password}

        #Creating a DataFrame for the given dictionary
        df=pd.DataFrame(dict2, index=[0])

        #Adding the user inputed values to the CSV file by using concat method
        df1=pd.concat([df1,df],ignore_index=True)

        #Writing the added values to the CSV file
        df1.to_csv("student_details.csv", index=False)
    else:
        print("Name already exist")

def displaymember():
    global df1
    #Displaying the Student details
    print(df1[['Student Name','Sap ID']])

def deletemember():
    global df1
    print("ENTER THE NAME & SAP WHICH YOU WANT TO DELETE")
    name=input("Enter the name:")
    name = name.lower()
    sapid=int(input("Enter the sapid:"))

    #Input name and sapid from the user and check whether the Name exist in the data
    if(name in df1['Student Name'].values and sapid in df1['Sap ID'].values):
        #Getting the index of the name entered by the user
        x = df1.loc[df1['Student Name'] == name].index

        #Deleting the record from the data
        df1 = df1.drop(x, axis=0)
        df1.to_csv("student_details.csv", index=False)
        print(df1)
    else:
        print("Your Student Name or Sap ID is wrong")

def modifymember():
    global df1
    print("ENTER THE DETAILS TO MODIFY THE DETAILS OF STUDENT IN OUR LIBRARY")
    name=input("Enter the Name to be modified:")
    name=name.lower()
    pas=input("Enter the Password to be modified:")
    if(name in df1['Student Name'].values):
        x = df1.loc[df1['Student Name'] == name].index
        df1.loc[x, "Student Name"] = name
        df1.loc[x, "Password"] = pas
    df1.to_csv("student_details.csv", index=False)

def addbook():
    global df2
    print("ENTER THE DETAILS TO ADD THE BOOK IN OUR LIBRARY")
    bookcod=int(input("Enter the Book Code:"))
    booknam=input("Enter the Book Name:")
    authnam=input("Enter the Author Name:")
    genre=input("Enter the Genre:")
    avail=int(input("Enter the Total number of books:"))
    if(bookcod not in df2['Book Code'].values):
        dict1={'Book Code':bookcod,'Book Name':booknam,'Author Name':authnam,'Genre':genre,'Available':avail}
        df=pd.DataFrame(dict1, index=[0])
        df2=pd.concat([df2,df],ignore_index=True)
        df2.to_csv('book_details.csv',index=False)
    else:
        print("Book already exist")

def modifybook():
    global df2
    print("ENTER THE DETAILS TO MODIFY THE BOOK IN OUR LIBRARY")

    ch=int(input("Enter which details to be modified\n1.Book Name\n2.Author Name\n3.Available\n4.Genre\n"))
    bookcod=int(input("Enter the Book Code to be modified:"))
    x = df2.loc[df2['Book Code'] == bookcod].index
    if(bookcod in df2['Book Code'].values):
        if ch==1:
            booknam=input("Enter the Book Name to be modified:")
            df2.loc[x, "Book Name"] = booknam
        elif ch==2:
            authname=input("Enter the Author Name to be modified:")
            df2.loc[x, "Author Name"] = authname
        elif ch==3:
            avail=int(input("Enter the Available books to be modified:"))
            df2.loc[x, "Available"] = avail
        elif ch==4:
            genre=input("Enter the genre to be modified:")
            df2.loc[x, "Genre"] = genre
    df2.to_csv('book_details.csv',index=False)

def displaybook():
    print(df2)

def deletebook():
    global df2
    print("ENTER THE BOOK CODE AND BOOK NAME WHICH YOU WANT TO DELETE")
    bookcod=int(input("Enter the Book Code:"))
    if(bookcod in df2['Book Code'].values):
        x = df2.loc[df2['Book Code'] == bookcod].index
        df2 = df2.drop(x, axis=0)
        df2.to_csv('book_details.csv',index=False)
    else:
        print("Entered Book Code doesn't exist")

def displaygraph():
    x = df2["Book Name"].tolist()
    y = df2["Available"].tolist()

    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.xlabel("Book Name")
    plt.ylabel("Available Books")
    plt.show()

    genre = df2["Genre"].tolist()
    genre_set = list(set(genre))
    genre_count = [0 for x in genre_set]

    for x in genre:
        for j in range(len(genre_set)):
            if genre_set[j] == x:
                genre_count[j] += 1
            
    plt.bar(genre_set, genre_count)
    plt.xlabel("Genre")
    plt.ylabel("Number of Books")
    plt.show()


print("ENTER THE LOGIN DETAILS")
dup_name="Kanishk"
dup_pas="Kanishk123"
name=input("Enter the Name:")
pas=input("Enter the Password:")

if(name == dup_name and pas == dup_pas):
    print("WELCOME!")

def main_program():
    print("\nWHICH OPERATION YOU NEED TO PERFORM")
    ch=int(input("Enter the choice\n1.Add Member\n2.Display Member\n3.Delete Member\n4.Modify Member\n5.Add Book\n6.Modify Book\n7.Display Book\n8.Delete Book\n9.Display Graph\n"))
    if ch==1:
        n=int(input("Enter how many members do you need to add:"))
        for i in range(n):
            addmember()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==2:
        displaymember()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==3:
        n=int(input("Enter how many members do you need to delete:"))
        for i in range(n):
            deletemember()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==4:
        n=int(input("Enter how many members do you need to modify:"))
        for i in range(n):
            modifymember()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==5:
        n=int(input("Enter how many books do you need to add:"))
        for i in range(n):
            addbook()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==6:
        n=int(input("Enter how many books do you need to modify:"))
        for i in range(n):
            modifybook()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==7:
        displaybook()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==8:
        n=int(input("Enter how many books do you need to delete:"))
        for i in range(n):
            deletebook()
        m=input("Do you want to continue(y/n):")
        if m=='y':
            main_program()
        else:
            exit()
    elif ch==9:
        displaygraph()
    else:
        print("Enter the valid choice")

main_program()
