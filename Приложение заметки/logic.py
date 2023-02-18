import db
import classNote
from colorama import Fore, Style

def add(input):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if classNote.Note.getId(input) == classNote.Note.getId(note):
                classNote.Note.setId(input)
    listOfNotes.append(input)
    db.writeTofileList(listOfNotes, 'a')
    print(Fore.GREEN + "Заметка добавлена")
    print(Style.RESET_ALL)    
    
def showAllById():
    try:
        listOfNotes = db.readFromFile()
        for note in listOfNotes:
            print('id: ' + classNote.Note.getId(note))
    except Exception:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  

def show():
    try:
        listOfNotes = db.readFromFile()
        for note in listOfNotes:
            print(classNote.Note.forShow(note))
    except Exception:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  

def showByDate(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input in classNote.Note.getDate(note) :
            print(classNote.Note.forShow(note))
            isEmpty =False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def showById(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
       if input == classNote.Note.getId(note):
            print(classNote.Note.forShow(note))
            isEmpty = False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def delete(input):
    isDeleted = False
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input == classNote.Note.getId(note) :
            isDeleted = True
            listOfNotes.remove(note)
            print(Fore.GREEN + "Заметка удалена")
            print(Style.RESET_ALL)  
    db.writeTofileList(listOfNotes, 'a')
    if isDeleted == False :
        print(Fore.RED + 'Такой заметки нет. Возможно вы ввели неверный id')
        print(Style.RESET_ALL)  


def edit(input, newTitle, newBody):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input == classNote.Note.getId(note) :
            classNote.Note.setTitle(note,newTitle)
            classNote.Note.setBody(note, newBody)
            classNote.Note.setDate(note)
            print(Fore.GREEN + 'Заметка изменена')
            print(Style.RESET_ALL)  
    db.writeTofileList(listOfNotes, 'a')
     