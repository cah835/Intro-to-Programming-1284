#Corey Henry & Geoffrey Sanchez              #Date Assigned: 29Oct2014
#                                            #
#Course CSE 1284 Sec 02                      #Date Due: 05Nov2014
#File name: lab8.py
#
#Program description - online department of gallery of arts that allows
#you to search through peices of art.

#define the main function
def main():
    title, genre, artist, date, value = [],[],[],[],[]
    options(title, genre, artist, date, value)

#create a function that allows you to call your options.
def options(title, genre, artist, date, value):
    print('\n')
    print("1. Insert a artwork")
    print("2. Find maximum valued art")
    print("3. Find minimum valued art")
    print("4. Show average value of my gallery")
    print("5. Delete an artwork")
    print("6. Find your art by title")
    print("7. Find your arts by year")
    print("8. Quit")
    option = int(input("Your option: "))
# if statements that will excute your options depending on your answer
    if option == 1:
        InsertArtwork(title, genre, artist, date, value)
    elif option == 2:
        FindMaximum(title, genre, artist, date, value)
    elif option == 3:
        FindMinimum(title, genre, artist, date, value)
    elif option == 4:
        ShowAverage(title, genre, artist, date, value)
    elif option == 5:
        DeleteArtwork(title, genre, artist, date, value)
    elif option == 6:
        FindByTitle(title, genre, artist, date, value)
    elif option == 7:
        FindByYear(title, genre, artist, date, value)    
    else:
        quit


#define function that will insert a new artwork
def InsertArtwork(title, genre, artist, date, value):
    new_title = input('title: ')
    new_genre = input('genre: ')
    new_artist = input('Artist name: ')
    new_date = input('Year Created: ')
    new_value = int(input('value: '))
    #add items to the lists
    title.append(new_title)
    genre.append(new_genre)
    artist.append(new_artist)
    date.append(new_date)
    value.append(new_value)
    print('New artwork added!')
#recall options function
    options(title, genre, artist, date, value)
    
#define function that will find the maxium value and call corrosponding indexs
def FindMaximum(title, genre, artist, date, value):
    index = value.index(max(value))
    print("Maximum valued art: " + title[index])
    print("Genre: " + genre[index])
    print("Artist: " + artist[index])
    print("Date: " + date[index])
    print("Value: ", max(value))
#recall options functions
    options(title, genre, artist, date, value)

#define function that will find the min value and call corrosponding indexs
def FindMinimum(title, genre, artist, date, value):
    index = value.index(min(value))
    print("Minimum valued art: " + title[index])
    print("Genre: " + genre[index])
    print("Artist: " + artist[index])
    print("Date: " + date[index])
    print("Value: ", min(value))
#recall options function
    options(title, genre, artist, date, value)

#define the average function calling your sum devided by your len to get average
def ShowAverage(title, genre, artist, date, value):
    average = sum(value)/len(value)
    print("Average value of your gallery is: ", average)
#recall options function
    options(title, genre, artist, date, value)

#define function that will remove artwork based on title and corrosponding indexs
def DeleteArtwork(title, genre, artist, date, value):
    remove_item = input("Give a title: ")
    index = title.index(remove_item)
    title.remove(remove_item)
    genre.remove(genre[index])
    artist.remove(artist[index])
    date.remove(date[index])
    value.remove(value[index])
#recall options   
    options(title, genre, artist, date, value)

#create function that will call title and corrosponding indexs
def FindByTitle(title, genre, artist, date, value):
    item = input("Give a title: ")
    index = title.index(item)
    print("Title: " + title[index])
    print("Genre: " + genre[index])
    print("Artist: " + artist[index])
    print("Date: " + date[index])
    print("Value: ", value[index])
#recall options    
    options(title, genre, artist, date, value)

#define function that will call year and corrosponding indexs    
def FindByYear(title, genre, artist, date, value):   
    year = input("Give a year: ")
    index = date.index(year)
    print("Title: " + title[index])
    print("Genre: " + genre[index])
    print("Artist: " + artist[index])
    print("Date: " + date[index])
    print("Value: ", value[index])
#recall options    
    options(title, genre, artist, date, value)

main()








    
