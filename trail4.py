from tkinter import *

#Searches through the available data with the given inputs
#makes a list and calls listsetter function to proceed
def serch():
    global k, n,i
    selected = []
    display_clear()
    n = len(k)
    
    k=[]
    gen = 0
    lang = 0
    if genrevalue.get() == 1:
        for getting in range(0, len(totalgenre), 2):
            if totalgenre[getting].get() == 1:
                selected.append(totalgenre[getting+1])
        gen = 1
    if languagevalue.get() == 1:
        for gettin in range(0, len(totallang), 2):
            if totallang[gettin].get() == 1:
                selected.append(totallang[gettin+1])
        lang = 1
    print(selected)
    if gen ==1 and lang == 1:
        for item in ll:
            if  set(list(item[3].split(","))).intersection(set(selected)) or set(list(item[2].split(","))).intersection(set(selected)):
                k.append(item)

    elif gen == 1 and lang !=1:
        for item in ll:
            if set(list(item[3].split(","))).intersection(set(selected)):
                k.append(item)
    elif gen != 1 and lang == 1:
        for item in ll:
            if set(list(item[2].split(","))).intersection(set(selected)):
                k.append(item)
    listsetter()
    i = 0

#Collects data from searchbar and initializes the search and returns the list to the listsetter function
def callback(event):
    global i, k
    i = 0
    k = []
    valueGot = searchbar.get()
    print(valueGot)
    valueGot = valueGot.lower()
    for item in ll:
        if valueGot in item[0] or valueGot in item[1]:
            k.append(item)
    display_clear()
    listsetter()




#clears all the previous debris left and helps in giving the clean output
def display_clear():
    global lbl
    emptylist = ["  ", "    ", "    ", "    "]
    lbl = [1]*4
    for i in range(4):
        lbl[i] = Label(text = "{}\n {} \n {} \n {}".format(emptylist[0], emptylist[1], emptylist[2], emptylist[3]), bg = 'white', width = 30)
        lbl[i].grid(row = 2+4*i, column = 4, rowspan = 4)
    
    nextbutton = Button(text = 'next', command = nextfunc)
    previousbutton = Button(text = 'previous', command = previousfunc)
    nextbutton.grid(row = 20, column = 4)
    previousbutton.grid(row = 21, column = 4)

#Works with next button to show more results
def nextfunc():
    global i,k
    if i+5 < len(k):
        i = i+4
        display_results()

#Works with previous button to show previous results
def previousfunc():
    global i
    print("previous function called")
    print(i)
    if i>3:
        print("do it")
        i = i -4
        display_results()

#Adds the empty elements to the final list in order to show exactly 4 titles output all the time
#Calls the display_results function to display the final result
def listsetter():
    global k
    if len(k)%4 == 3:
        add_list = [["", "", "", ""]]
        k = k + add_list
    if len(k)%4 == 2:
        add_list = [["", "", "", ""], ["", "", "", '']]
        k = k + add_list
    elif len(k)%4 == 1:
        add_list = [["", '', '', ''], ['', '', '', ''], ['', '', '', '']]
        k = k + add_list
    for item in k:
        print(item)
    print(len(k))
    if len(k) != 0:
        display_results()

#Displays the search results, four at a time
def display_results():
    global i,k, lbl
    print("i value", i)
    showingList = k[i:i+4]
    print(showingList)
    for j in range(4):
        lbl[j].configure(text = "Name: {} \n Hero: {} \n Language: {} \n Genre: {}".format(showingList[j][0], showingList[j][1], showingList[j][2], showingList[j][3]), bg = 'white', width = 38)
        #lbl[i].grid(row = 2+4*i, column = 4, rowspan = 4)

#Lets the users to add their new movies to the data
def add_func():
    global nameEntry, heroEntry, languageEntry, genreEntry, new_window
    new_window = Toplevel()
    nameLabel = Label(new_window, text = 'Movie Name', width = 25)
    nameEntry = Entry(new_window, width = 25)
    nameLabel.grid(row=0, column = 0)
    nameEntry.grid(row = 0, column = 1)
    heroLabel = Label(new_window, text = 'Hero Name', width = 25)
    heroEntry = Entry(new_window, width = 25)
    heroLabel.grid(row = 1, column = 0)
    heroEntry.grid(row = 1, column = 1)
    languageLabel = Label(new_window, text = 'Language', width = 25)
    languageEntry = Entry(new_window, width = 25)
    languageLabel.grid(row = 2, column = 0)
    languageEntry.grid(row = 2, column =1)
    genreLabel = Label(new_window, text = 'Genre', width = 25)
    genreEntry = Entry(new_window, width = 25)
    genreLabel.grid(row = 3, column = 0)
    genreEntry.grid(row = 3, column = 1)
    okbutton = Button(new_window, text = 'Done', command = writingNew )
    okbutton.grid(row = 4, column = 0, columnspan = 2)

#collects the new movie data given by user
def writingNew():
    global nameEntry, heroEntry, languageEntry, genreEntry
    newMovie = []
    nameNew = nameEntry.get()
    newMovie.append(nameNew.lower())
    heroNew = heroEntry.get()
    newMovie.append(heroNew.lower())
    languageNew = languageEntry.get()
    newMovie.append(languageNew.lower())
    genreNew = genreEntry.get()
    newMovie.append(genreNew.lower())
    ll.append(newMovie)
    writetofile()
    new_window.destroy()

#writes the new data to the file
def writetofile():
    file1 = open('mov.txt', 'w')
    for item in ll:
        print(":".join(item), file = file1)
    file1.close()
    



#loading all data from the file mov.txt
listMade = [line.strip() for line in open("mov.txt")]
print(listMade)
lbl =[]
k = []
ll = []
n = 0
i = 0

#prepares a list that can be accessed easily
for item in listMade:
        a = item.split(':')
        ll.append(a)






#Opening the tkinter window
root = Tk()

#changing buttons

root.title('Your MOVIEBOOK')

#searchbar
searchframe = Frame()
empty = Label(text = "", width = 30)
search = Label(text = "Search".rjust(0), font = ("Georgia", 28), width = 7)
searchbar = Entry(width = 10, font = ("Verdana", 12))
search.grid(row = 1, column = 0,columnspan = 2)
searchbar.grid(row = 1, column =2)



#searchbar key configuration
root.bind('<Return>', callback)


#empty grid to maintain a constant size window all over the time
empty.grid(row =0, column = 0,columnspan = 4)
empty2 = Label(width = 25)
empty2.grid(row=1, column = 3, columnspan = 4)
#searchframe.grid(row = 1, column = 0)

#filters
pickby = Label(text = "Pick by"
               )
pickby.grid(row = 2, column = 1, padx = 2, pady = 2)


"""
Don't follow this code. This is for other purposes. Don't uncomment this code, it will result in malfunction.
col = Label(text = "Genre")
col.grid(row =3, column = 0)
col2 = Label(text = "c222222")
col2.grid(row = 3, column = 1)
"""
#genre
"""
now we describe all genre and language values and checkbutons
and then collect data through them and store and process in the following steps
"""
genrevalue = IntVar()
genre = Checkbutton(text = 'Genre      ', var = genrevalue, font = ("Arial", 17))
genre.grid(row = 3, column = 1)

actionvalue = IntVar()
horrorvalue = IntVar()
comedyvalue = IntVar()
scifivalue = IntVar()
romcomvalue = IntVar()
animvalue = IntVar()
thrillervalue = IntVar()
dramavalue = IntVar()

actionbut = Checkbutton(text = 'Action'.ljust(12) , var = actionvalue)
actionbut.grid(row = 4, column = 1)
horrorbut = Checkbutton(text = "Horror".ljust(12), var = horrorvalue)
horrorbut.grid(row = 5, column = 1)
comedybut = Checkbutton(text = 'Comedy'.ljust(9), var = comedyvalue)
comedybut.grid(row = 6, column = 1)
scifibut = Checkbutton(text = 'Scifi'.ljust(16), var = scifivalue)
scifibut.grid(row = 7, column = 1)
romcombut = Checkbutton(text = "Romcom".ljust(8), var = romcomvalue)
romcombut.grid(row = 8, column = 1)
animbut = Checkbutton(text = 'anim'.ljust(13), var = animvalue)
animbut.grid(row = 9, column = 1)
thrillerbut = Checkbutton(text ='thriller'.ljust(16), var = thrillervalue)
thrillerbut.grid(row = 10, column =1)
dramabut = Checkbutton(text = 'drama'.ljust(13), var = dramavalue)
dramabut.grid(row = 11, column =1)

#language
languagevalue = IntVar()
language = Checkbutton(text = 'Language', var = languagevalue, font = ("Arial", 17))
language.grid(row = 12, column = 1)

englishvalue = IntVar()
hindivalue = IntVar()
teluguvalue = IntVar()

englishbut = Checkbutton(text = "English".ljust(14), var = englishvalue)
englishbut.grid(row = 13, column = 1)

hindibut = Checkbutton(text = "Hindi".ljust(15), var = hindivalue)
hindibut.grid(row = 14, column = 1)

telugubut = Checkbutton(text = "Telugu".ljust(14), var = teluguvalue)
telugubut.grid(row = 15, column = 1)


#collection list in order to process the user's input concisely
total = [actionvalue, "action", horrorvalue, "horror", comedyvalue, "comedy", dramavalue, "drama",
         thrillervalue, "thriller", scifivalue, "scifi", romcomvalue, "romcom", animvalue, "anim",
         englishvalue, "english", hindivalue, "hindi", teluguvalue, "telugu"]
totalgenre = total[:16]
totallang = total[16:]


#empty in column 4

column4  = Label(width = 40)
column4.grid(row = 0, column = 4)


#searchbutton

searchbutton = Button(text= 'search', command = serch)
searchbutton.grid(row =16, column = 0, columnspan = 3, padx = 15, pady = 15)

#a test Label to find the form factor and correct placement of data in rows and columns
body1 = Label(text = "hello \n hello \n hello \n hello", bg = "red", height = 4, width = 30)
#body1.grid(row = 2, column = 4, rowspan = 4)

#add button to let the user to append new data to the file
add = Button(text = 'Add', bg = 'red', command = add_func)
add.grid(row = 1, column = 4)





mainloop()
