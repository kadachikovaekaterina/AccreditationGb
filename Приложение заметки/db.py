import classNote

def writeTofile(note, mode):
    f = open ("db.csv", mode = mode, encoding='utf-8')
    strNote = classNote.Note.toString(note)
    f.write(strNote)
    f.write('\n')
    f.close


def writeTofileList(listOfNote, mode):
    f = open ("db.csv", mode = 'w', encoding='utf-8')
    f.seek(0)
    f.close()
    f = open ("db.csv", mode = mode, encoding='utf-8')
    for note in listOfNote:
        strNote = classNote.Note.toString(note)
        f.write(strNote)
        f.write('\n')
    f.close    


def readFromFile():
    try:
        f = open("db.csv", "r",encoding='utf-8')
        notes = f.read().strip().split("\n")
        listNotes =[]
        for n in notes:
            splitedNote = n.split(',')
            note = classNote.Note(id = splitedNote[0], title=splitedNote[1], body = splitedNote[2], date = splitedNote[3])
            listNotes.append(note)
    except Exception:   
        print('Нет заметок')
    finally:    
        return listNotes    