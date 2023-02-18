import db
import classNote

def checkInList(input):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input == classNote.Note.getId(note):
            return True
      