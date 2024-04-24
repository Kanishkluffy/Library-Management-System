import matplotlib.pyplot as plt
import pandas as pd

df_borrow = pd.read_csv("Borrow_Details.csv")
df_book = pd.read_csv("book_details.csv")


x = df_book["Book Name"].tolist()
y = df_book["Available"].tolist()

plt.bar(x,y)
plt.xticks(rotation=90)
plt.xlabel("Book Name")
plt.ylabel("Available Books")
plt.show()

genre = df_book["Genre"].tolist()
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
