from colorama import Fore, Style
import logic
import ui
import checks



def start():
    userInput ='0'
    while userInput != '7':
        ui.menu() 
        userInput =input('Введите номер задачи: ').strip()
        print("\n")
        if userInput == '1':
           logic.show()
           ui.continueWork()
        if userInput == '2':
            note =ui.createNote()
            logic.add(note)
            ui.continueWork()
        if userInput == '3':
            logic.show()
            print("\n")
            logic.delete(input("Введите id заметки: "))
            ui.continueWork()
        if userInput == '4':
            logic.show()
            print("\n")
            userInput = input("Введите id заметки: ")
            if checks.checkInList(userInput):
                editNote = ui.editNote()
                logic.edit(userInput, editNote[0], editNote[1])
            else:
                print(Fore.RED + 'Такой заметки нет. Возможно вы ввели неверный id')
                print(Style.RESET_ALL)  
            ui.continueWork()        
        if userInput == '5':
            logic.showByDate(input('Введите дату в формате dd.mm.yyyy: '))
            print('\n')
            ui.continueWork()
        if userInput == '6':
            logic.showAllById()
            print("\n")
            logic.showById(input("Введите id заметки: "))
            ui.continueWork()
        if userInput == '7':
            print("Спасибо, что выбрали наше приложение. До новых встреч!")
            break
        