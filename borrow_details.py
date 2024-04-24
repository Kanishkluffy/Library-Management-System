import pandas as pd 
import random

df1=pd.read_csv('student_details.csv')
df5=pd.read_csv("Borrow_Details.csv")
df3=pd.read_csv("book_details.csv")

def borrowbook():
    global df5
    L=[]
    booknam=input("Enter your book name:")
    bookcod=int(input("Enter the book code:"))
    copi=int(input("Enter the number of Copies you want:"))
    g = df3.loc[df3['Book Code'] == bookcod].index
    if(bookcod in df3['Book Code'][g].values and df3['Available'][g].values[0] >= copi):
        while(copi):
            j=random.randint(100,999)
            bookid=f"DDN{bookcod}.{j}"
            df3.loc[g,'Available'] = df3['Available'][g]-1
            f = df5.loc[df5['Book ID'] == bookid].index
            status=df5.loc[f,'Status'] = "Borrowed"
            d={'Student Name':name,'Sap ID':sapid,'Book Name':df3['Book Name'][g].values[0],'Author Name':df3['Author Name'][g].values[0],
               'Genre':df3['Genre'][g].values[0],'Book Code':bookcod,'Book ID':bookid,'Status':status}
            L.append(d)
            copi -= 1
        print(df3)
        df5 = pd.DataFrame(L, columns=['Student Name','Sap ID','Book Name','Author Name','Genre','Book Code','Book ID','Status'])
        df5.to_csv('Borrow_Details.csv', index=False)
        df3.to_csv('book_details.csv',index=False)
    else:
        print("Entered book code or Copies doesn't exist")

def returnbook():
    global df5
    booknam=input("Enter your book name:")
    bookcod=int(input("Enter the Book Code:"))
    copi=int(input("Enter the number of Copies you need to return:"))
    count=len(df5[(df5['Book Code']==bookcod) & (df5['Student Name']==name)])
    if(copi<=count):
        for i in range(copi):
            f = df3.loc[df3['Book Code'] == bookcod].index
            bookid=input("Enter your book ID:")
            a = df5.loc[df5['Book ID'] == bookid].index
            df5.loc[a,'Status'] = "Returned"
            df3.loc[f,'Available'] = df3['Available'][f]+1
            print(df3)
    else:
        print("Enter the valid copies")
        exit()
    df5.to_csv('Borrow_Details.csv', index=False)
    df3.to_csv('book_details.csv', index=False)

def displaybook():
    print(df3)


print("ENTER THE LOGIN DETAILS")
name=input("Enter your Name:")
name=name.lower()
sapid=int(input("Enter your Sap ID:"))
pas=input("Enter your Password:")
b = df1.loc[df1['Sap ID'] == sapid].index
f = df1.loc[df1['Password'] == pas].index
c = df1.loc[df1['Student Name'] == name].index
if(sapid in df1['Sap ID'][b].values and pas in df1['Password'][f].values and name in df1['Student Name'][c].values):
    ch=int(input((("ENTER THE OPERATION NEED TO PERFORM\n1.Borrow Book\n2.Return Book\n3.Display Book\n"))))
    if ch==1:
        borrowbook()
    elif ch==2:
        returnbook()
    elif ch==3:
        displaybook()
    else:
        print('Enter the valid choice')
else:
    print("Entered Student details doesn't exist")

