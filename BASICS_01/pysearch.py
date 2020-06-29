# search for results in db

database = {
1: {"name": "Ferdi", "profession": "Developer", "age": "28"},
2: {"name": "Lilli", "profession": "Writer", "age": "33"},
3: {"name": "Leo", "profession": "Python-Scientist", "age": "26"}
}
def search(search) :
    found = False
    print("Search result :\n")
    for j in database.keys() :
        for i in database[j].values() :
            if search.lower() in i.lower() :
                print("Name :",[a for a in database[j].values()][0])
                print("Profession :",[a for a in database[j].values()][1])
                print("Age :",[a for a in database[j].values()][2],end="\n\n")
                found = True
                break
    if not found :
        print("No Result")
y = input("Search : ")
print(y)
search(y)

#END