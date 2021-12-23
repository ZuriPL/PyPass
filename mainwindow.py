#Hello
from os import path
import sys
import tkinter as tk
import re, pickle, keyboard
from tkinter import ttk
from tkinter.constants import DISABLED, HIDDEN, NORMAL
from tkinter.messagebox import askyesno, showinfo, showwarning
from languages import Polski, English

defaultSettings = {"0": {"password": '', "keybind": "Tab", "counter": 0, "rollover": True, "theme": "vista"}}

Languages = {"Polski": Polski, "English": English}

class FirstPassword:
    Pswd = ''
    Language = "Polski"

s = FirstPassword
        
def LoginWindow(pswd):

    loginW = tk.Tk()
    
    loginW.geometry("350x70")
    loginW.resizable(0, 0)
    loginW.title(Languages[s.Language]["Str1"]) #Zaloguj się "Log into Pypass"

    loginW.protocol("WM_DELETE_WINDOW", sys.exit)

    def CheckThePassword(*args):
        x = Password1Entry.get()
        if x == pswd:
            loginW.destroy()
        else:
            showwarning(message=Languages[s.Language]["Str2"]) #Nieprawidłowe hasło
            Password1Entry["textvariable"] = tk.StringVar()

    FrameX = tk.Frame(loginW, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[s.Language]["Str3"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) #Hasło
    Password1Entry = ttk.Entry(FrameX, show='*')
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password1Entry.bind('<KeyPress-Return>', CheckThePassword)
    ttk.Button(FrameX, text=Languages[s.Language]["Str9"], command=CheckThePassword).grid(column=1, row=1, sticky="nse", padx=10, pady=5)

    loginW.mainloop()



def CreatePasswordWindow():

    loginW = tk.Tk()
    
    loginW.geometry("350x100")
    loginW.resizable(0, 0)
    loginW.title(Languages[s.Language]["Str4"]) #Stwórz hasło

    loginW.protocol("WM_DELETE_WINDOW", sys.exit)

        

    FrameX = tk.Frame(loginW, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[s.Language]["Str5"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) #Podaj swoje hasło
    ttk.Label(FrameX, text=Languages[s.Language]["Str6"]).grid(column=0, row=1, sticky="nsew", padx=10, pady=5) # Powtórz swoje hasło
    Password1Entry = ttk.Entry(FrameX)
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password2Entry = ttk.Entry(FrameX)
    Password2Entry.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        
        
    def CheckThePassword(*args):
        if Password1Entry.get() == Password2Entry.get():
            if Password1Entry.get() == '':
                showwarning(message=Languages[s.Language]["Str7"], title=Languages[s.Language]["Str4"]) #Nie stworzyłeś hasła. Po zalogowaniu się wejdż w ustawienia i stwórz hasło aby chronić swoje dane // #Str4
            s.Pswd = Password1Entry.get()
            loginW.destroy()
        else:
            showwarning(message=Languages[s.Language]["Str8"]) #Podane hasła nie są takie same
            Password1Entry["textvariable"] = tk.StringVar()
            Password2Entry["textvariable"] = tk.StringVar()

    Password2Entry.bind('<KeyPress-Return>', CheckThePassword)

    ttk.Button(FrameX, text=Languages[s.Language]["Str9"], command=CheckThePassword).grid(column=1, row=2, sticky="nse", padx=10, pady=5) #Zaloguj

    loginW.mainloop()

try:
    with open('data.pickle', 'rb') as handle:
        savedata = pickle.load(handle)
    LoginWindow(savedata["0"]["password"])
except FileNotFoundError:
    CreatePasswordWindow()
    with open('data.pickle', 'wb') as handle:
        pickle.dump(defaultSettings, handle)
    with open('data.pickle', 'rb') as handle:
        savedata = pickle.load(handle)
    


window = tk.Tk()
window.focus()
window.focus_force()
window.geometry("450x550")
window.title(Languages[s.Language]["Str10"]) #Menedżer Haseł
window.resizable(0, 0)

class GlobalVars:
    whichButton = savedata["0"]["keybind"]
    name = ''
    login = ''
    password = ''
    PyPassVersion = '0.5.1 BETA'
    GlobalPassword = savedata["0"]["password"]
    globalX = 0
    counter = savedata["0"]["counter"]
    theme = savedata["0"]["theme"]
    delete = 0
    whattopaste = "login"
    element = ''
    rollover = savedata["0"]["rollover"]
    FirstPassword = False
    ChangeRolloverVariable = tk.StringVar()
    if rollover == True:
        ChangeRolloverVariable.set('1')
    else:
        ChangeRolloverVariable.set('0')
    savedata = savedata

kp = GlobalVars
#print(kp.counter)
ElementsList = ["0"]

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=10)
window.rowconfigure(1, weight=30)
window.rowconfigure(2, weight=7)

kp.savedata["0"]["password"] = s.Pswd

def HardResetContinue():
    kp.savedata = {"0": {"password": kp.GlobalPassword, "keybind": "Tab", "counter": 0, "rollover": True, "theme": "vista"}}
    kp.counter = 0
    kp.theme = "vista"
    kp.rollover = True
    showinfo(message=Languages[s.Language]["Str11"]) #Program się zamknie, aby zastosować zmiany
    closeEvent()

def AskForPassword2():
    child2 = tk.Toplevel()
    child2.geometry("350x70")
    child2.resizable(0, 0)
    child2.grab_set()
    child2.focus()
    child2.transient()

    def SetTheNewPassword2(x, *args):
        kp.GlobalPassword = x
        HardResetContinue()

    FrameX = tk.Frame(child2, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[s.Language]["Str33"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) #Nowe Hasło
    Password1Entry = ttk.Entry(FrameX)
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password1Entry.bind('<KeyPress-Return>', SetTheNewPassword2)
    ttk.Button(FrameX, text=Languages[s.Language]["Str38"], command=lambda: SetTheNewPassword2(Password1Entry.get())).grid(column=1, row=1, sticky="nse", padx=10, pady=5) #Kontynuuj

def HardReset(): #!
    showwarning(title=Languages[s.Language]["Str44"], message=Languages[s.Language]["Str45"])
    answer = askyesno(title=Languages[s.Language]["Str43"], message=Languages[s.Language]["Str37"])
    if answer:
        answer2 = askyesno(title=Languages[s.Language]["Str46"], message=Languages[s.Language]["Str47"])
        if answer2 == False:
            AskForPassword2()
        else:
            HardResetContinue()

FrameTop = ttk.Frame(window, width=350)
FrameTop.grid(row=0, column=0, sticky="nsew")

TopLabel = ttk.Label(FrameTop, text=Languages[s.Language]["Str43"]) #Wybierz serwis do którego chcesz się zalogować
TopLabel.place(relx=0.5, rely=0.5, anchor="center")

FrameMiddle = ttk.Frame(window)
FrameMiddle.grid(column=0, row=1, sticky="ns")
FrameMiddle["relief"] = "sunken"
FrameMiddle["borderwidth"] = 5



PasswordList = tk.Canvas(FrameMiddle)
PasswordList.pack(side="left", fill="both", expand=True)


AnchoredMiddleFrame = ttk.Frame(PasswordList)


scrollbar = ttk.Scrollbar(
    FrameMiddle,
    orient='vertical',
    command=PasswordList.yview
)



def PasswordEnter():
    child2 = tk.Toplevel()
    child2.geometry("420x100")
    child2.grab_set()
    child2.resizable(0, 0)
    child2.focus()
    child2.attributes('-topmost', True)
    child2.transient()
    FrameX = ttk.Frame(child2)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure([0, 1], weight=1, minsize=100)
    FrameX.columnconfigure(2, weight=2, minsize=200)
    FrameX.rowconfigure([0, 1, 2], weight=1)

    kp.whattopaste = 'login'

    def changewhatToPaste(what):
        kp.whattopaste = what
        if what == "login" or what == "password":
            PasteLabel["text"] = Languages[s.Language]["Str13"] + what #Pole: 
        else:
            PasteLabel["text"] = what

    def TypeOutThePassword(*args):
        if kp.whattopaste == 'login':
            keyboard.write(kp.savedata[str(kp.element)]["login"])
            if kp.rollover:
                changewhatToPaste(Languages[s.Language]["Str3"]) #Str3
        elif kp.whattopaste == 'password':
            keyboard.write(kp.savedata[str(kp.element)]["password"])
            if kp.rollover:
                changewhatToPaste(Languages[s.Language]["Str12"]) #Koniec
        else:
            Exit()
        

    ttk.Label(FrameX, text=Languages[s.Language]["Str49"] + kp.whichButton).grid(column=0, row=0, sticky="nsew", padx=10, pady=5, columnspan=2)
    ttk.Label(FrameX, text=Languages[s.Language]["Str28"] + str(kp.rollover)).grid(column=2, row=0, sticky="nsew", padx=10, pady=5)

    ttk.Button(FrameX, text="Login", command=lambda: changewhatToPaste("login")).grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
    ttk.Button(FrameX, text="Password", command=lambda: changewhatToPaste("password")).grid(column=1, row=1, sticky="nsew", padx=10, pady=5)

    PasteLabel = ttk.Label(FrameX, text=Languages[s.Language]["Str13"] + kp.whattopaste) #Str13
    PasteLabel.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)

    def Exit():
        child2.destroy()
        keyboard.remove_hotkey(kp.whichButton)

    ttk.Button(FrameX, text=Languages[s.Language]["Str14"], command=Exit).grid(column=2, row=2, sticky="nse", padx=10, pady=5) #Zamknij

    child2.protocol("WM_DELETE_WINDOW", lambda: Exit())

    keyboard.add_hotkey(kp.whichButton, TypeOutThePassword, suppress=True)



def MainButtonAction(element):
    #element = ElementsList.index(element)
    if kp.delete == 0:
        kp.element = element
        PasswordEnter()
        #print(savedata[str(element)]["login"] + ' ' + savedata[str(element)]["password"])
    else:
        element2 = ElementsList[element]
        element2.destroy()
        kp.counter = kp.counter - 1
        if kp.counter == 0:
            k.SorryNoPswds.pack()
        del kp.savedata[str(element)]
        DeleteButtonMode()
        EnterDeleteMode()

class MainButton:
    def __init__(self, x):
        Element = tk.Button(AnchoredMiddleFrame, text=kp.savedata[str(x)]["name"], wraplength=FrameWidth, width=53, height=4, command=lambda: MainButtonAction(x))
        Element.pack()
        ElementsList.append(Element)


FrameWidth = 350
class PopulatePswdButttons:
    UseScrollbar = False
    SorryNoPswds = tk.Label(AnchoredMiddleFrame, text=Languages[s.Language]["Str15"], width=56, height=5, fg="gray") #Chwilowo nie masz żadnych haseł.\nDodaj hasła używając przycisku 'Dodaj' 
    def __init__(self):
        if kp.counter == 0:
            self.SorryNoPswds.pack()
        else:
            self.CreateButtons(kp.counter)
            self.ScrollbarCheck(kp.counter)

    def CreateButtons(self, x):
        for i in range(x + 1):
            if i != 0:
                MainButton(i)

    def ScrollbarCheck(self, x):
        if x > 6:
            self.UseScrollbar = True

k = PopulatePswdButttons()

def CreateButton(name, login, pswd):
    ObjToAdd = {"name": name, "login": login, "password": pswd}
    kp.counter += 1
    kp.savedata[str(kp.counter)] = ObjToAdd
    MainButton(kp.counter)
    k.ScrollbarCheck(kp.counter)
    DeleteButtonMode()

    

PasswordList.create_window(0, 0, window=AnchoredMiddleFrame, anchor="nw")
PasswordList.update_idletasks()
PasswordList.configure(scrollregion=PasswordList.bbox("all"), yscrollcommand=scrollbar.set)

def ShowScrollbarWhenNeeded():
    k.ScrollbarCheck(kp.counter)
    if k.UseScrollbar == True:
        scrollbar.pack(side="right", fill="y")
ShowScrollbarWhenNeeded()

FrameBottom = ttk.Frame(window)
FrameBottom.grid(column=0, row=2, sticky="nsew")

FrameBottom.rowconfigure(0, weight=1)
FrameBottom.columnconfigure([0, 1, 2], weight=1)

AddButton = ttk.Button(FrameBottom, text=Languages[s.Language]["Str16"], width=10, command=lambda: AddNewEntryWindow()) #Dodaj
AddButton.grid(row=0, column=0, padx=40)
SettingsButton = ttk.Button(FrameBottom, text=Languages[s.Language]["Str17"], width=10, command=lambda: SettingsWindow()) #Ustawienia
SettingsButton.grid(row=0, column=1, padx=40)
DeleteButton = ttk.Button(FrameBottom, text=Languages[s.Language]["Str18"], width=10, command=lambda: EnterDeleteMode()) #Usuń
DeleteButton.grid(row=0, column=2, padx=40)

def DeleteButtonMode():
    if kp.counter == 0:
        DeleteButton["state"] = DISABLED
    else: 
        DeleteButton["state"] = NORMAL
DeleteButtonMode()

def EnterDeleteMode():
    if kp.delete == 0:
        kp.delete = 1
        DeleteButton["text"] = Languages[s.Language]["Str19"] #Anuluj
        AddButton["state"] = DISABLED
        SettingsButton["state"] = DISABLED
        TopLabel["text"] = Languages[s.Language]["Str20"] #Wybierz pozycję do usunięcia
    else: 
        kp.delete = 0
        DeleteButton["text"] = Languages[s.Language]["Str18"] #Str18
        AddButton["state"] = NORMAL
        SettingsButton["state"] = NORMAL
        TopLabel["text"] = Languages[s.Language]["Str43"]
    


def AddNewEntryWindow():
    child = tk.Toplevel()
    child.geometry("350x140")
    child.resizable(0, 0)
    child.title(Languages[s.Language]["Str21"]) #Dodaj nową pozycję
    child.transient()
    child.focus()
    child.grab_set()

    def PassAndClose(name, login, pswd):
        if name != '' and login != '' and pswd != '':
            child.destroy()
            kp.name = name
            kp.login = login
            kp.password = pswd
            if k.SorryNoPswds.winfo_exists() == True:
                k.SorryNoPswds.pack_forget()
            CreateButton(name, login, pswd)
            ShowScrollbarWhenNeeded()
            PasswordList.update_idletasks()
            PasswordList.configure(scrollregion=PasswordList.bbox("all"), yscrollcommand=scrollbar.set)
        else:
            showwarning(message=Languages[s.Language]["Str22"]) #Pola nie mogą pozostać puste

    child.columnconfigure(0, weight=1)
    child.columnconfigure(1, weight=4)
    child.rowconfigure([0, 1, 2, 3], weight=1)
    ttk.Label(child, text=Languages[s.Language]["Str23"]).grid(column=0, row=0, sticky="e", padx=5) #Nazwa
    ttk.Label(child, text="Login").grid(column=0, row=1, sticky="e", padx=5) 
    ttk.Label(child, text=Languages[s.Language]["Str3"]).grid(column=0, row=2, sticky="e", padx=5) #Str3
    NameEnter = ttk.Entry(child)
    NameEnter.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    LoginEnter = ttk.Entry(child)
    LoginEnter.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
    PswdEnter = ttk.Entry(child)
    PswdEnter.grid(column=1, row=2, sticky="nsew", padx=10, pady=5)
    ttk.Button(child, text=Languages[s.Language]["Str24"], command=lambda: PassAndClose(NameEnter.get(), LoginEnter.get(), PswdEnter.get())).grid(column=1, row=3, sticky="e", padx=10, pady=5) #Zapisz


ButtonPressed = tk.StringVar()


if kp.GlobalPassword == '':
    ButtonPressed.set("Tab")
else:
    ButtonPressed.set(kp.GlobalPassword)

def SettingsWindow():
    child = tk.Toplevel()
    child.geometry("350x450")
    child.resizable(0, 1)
    child.title(Languages[s.Language]["Str17"]) #Str17
    child.transient()
    child.focus()
    child.grab_set()

    SettingsFrameOne = ttk.LabelFrame(child, text=Languages[s.Language]["Str25"]) #Motywy
    SettingsFrameOne.pack(fill="x", padx=10)
    SettingsFrameOne.columnconfigure([0, 1], weight=1)

    Option = tk.StringVar()
    DropdownList = []
    styles = ttk.Style()
    for i in styles.theme_names():
        DropdownList.append(i)

    x = styles.theme_use()

    def ThemeChange(*args):
        styles.theme_use(Option.get())
        kp.theme = Option.get()

    ttk.Label(SettingsFrameOne, text=Languages[s.Language]["Str26"]).grid(column=0, row=0, sticky="w", padx=10, pady=5) #Wybierz motyw
    ttk.OptionMenu(SettingsFrameOne, Option, x, *DropdownList, command=ThemeChange).grid(column=1, row=0, sticky="e", padx=10, pady=5)



    SettingsFrameTwo = ttk.LabelFrame(child, text=Languages[s.Language]["Str27"]) #Przyciski
    SettingsFrameTwo.pack(fill="x", padx=10)
    SettingsFrameTwo.columnconfigure([0, 1], weight=1)

    ttk.Label(SettingsFrameTwo, text=Languages[s.Language]["Str49"]).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    KeyButton = ttk.Button(SettingsFrameTwo, text=kp.whichButton, command=lambda: RegisterTheButton())
    KeyButton.grid(row=0, column=1, sticky="e", padx=10, pady=5)
    
    

    def ChangeRollover(*args):
        if kp.ChangeRolloverVariable.get() == '1':
            kp.rollover = True
        else:
            kp.rollover = False

    ttk.Label(SettingsFrameTwo, text=Languages[s.Language]["Str28"]).grid(row=1, column=0, sticky="w", padx=10, pady=5) #Automatyczna zmiana wklejania
    ttk.Checkbutton(SettingsFrameTwo, onvalue=True, offvalue=False, variable=kp.ChangeRolloverVariable, command=ChangeRollover).grid(row=1, column=1, sticky="e", padx=10, pady=5)

    
    def RegisterTheButton():
        meanwhile = KeyButton["text"]
        KeyButton["text"] = Languages[s.Language]["Str29"] #Wciśnij przycisk do ustawienia, Esc do anulowania
        def SaveKeypress(x):
            x = re.split('=', re.split(' ', str(x))[3])[1]
            if x == 'Escape':
                KeyButton["text"] = meanwhile
            else:
                KeyButton["text"] = x
                ButtonPressed.set(x)
            KeyButton.unbind('<Any-KeyPress>')
            kp.whichButton = ButtonPressed.get()
            kp.savedata["0"]["keybind"] = kp.whichButton
            
        KeyButton.bind('<Any-KeyPress>', SaveKeypress)

    

    SettingsFrameThree = ttk.LabelFrame(child, text=Languages[s.Language]["Str30"]) #Zarządzaj
    SettingsFrameThree.pack(fill="x", padx=10)
    SettingsFrameThree.rowconfigure([0, 1, 2], weight=1)
    SettingsFrameThree.columnconfigure(0, weight=1)

        

    CreateNewFileButton = ttk.Button(SettingsFrameThree, text=Languages[s.Language]["Str31"], command=lambda: HardReset()) #Przywróc do ustawień początkowych (razem z hasłami)
    CreateNewFileButton.grid(column=0, row=0, sticky="nsew", padx=10, pady=5)


    def SetTheNewPassword(x, y, z, child, *args):
        if x == kp.GlobalPassword and y == z:
            kp.GlobalPassword = y
            kp.savedata["0"]["password"] = y
        child.destroy()
         
           
                

    def AskForANewPassword():
        child2 = tk.Toplevel()
        child2.geometry("350x140")
        child2.grab_set()
        child2.resizable(0, 0)
        child2.focus()
        child2.transient()
        FrameX = ttk.Frame(child2)
        FrameX.pack(expand=True, fill="both")

        FrameX.columnconfigure(0, weight=1)
        FrameX.columnconfigure(1, weight=4)
        FrameX.rowconfigure([0, 1, 2, 3], weight=1)
        ttk.Label(FrameX, text=Languages[s.Language]["Str32"]).grid(column=0, row=0, sticky="e", padx=5) #Stare hasło
        ttk.Label(FrameX, text=Languages[s.Language]["Str33"]).grid(column=0, row=1, sticky="e", padx=5) #Nowe hasło
        ttk.Label(FrameX, text=Languages[s.Language]["Str34"]).grid(column=0, row=2, sticky="e", padx=5) #Powtórz nowe hasło
        oldEnter = ttk.Entry(FrameX)
        oldEnter.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
        newEnter = ttk.Entry(FrameX)
        newEnter.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        new2Enter = ttk.Entry(FrameX)
        new2Enter.grid(column=1, row=2, sticky="nsew", padx=10, pady=5)
        ttk.Button(FrameX, text=Languages[s.Language]["Str24"], command=lambda: SetTheNewPassword(oldEnter.get(), newEnter.get(), new2Enter.get(), child2)).grid(column=1, row=3, sticky="e", padx=10, pady=5) #Str24

    def ChangePasswordWarning():
        showwarning(title=Languages[s.Language]["Str35"], message=Languages[s.Language]["Str36"]) #Zmień Hasło / UWAGA: Stare hasło nie będzie aktywne, upewnij się, że zapamiętasz nowe hasło
        answer = askyesno(title=Languages[s.Language]["Str35"], message=Languages[s.Language]["Str37"]) # Str35 / Kontynuować
        if answer:
            AskForANewPassword()

    ChangePasswordButton = ttk.Button(SettingsFrameThree, text=Languages[s.Language]["Str35"], command=lambda: ChangePasswordWarning()) #Str35
    ChangePasswordButton.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
    
    def AskForPassword():
        child2 = tk.Toplevel()
        child2.geometry("350x70")
        child2.grab_set()
        child2.resizable(0, 0)
        child2.focus()
        child2.transient()

        def ActuallyExtractPasswords(*args):
            if Password1Entry.get() == kp.GlobalPassword:
                for i in kp.savedata:
                    if i != "0":
                        with open("passwords.txt", "a") as f:
                            f.write(kp.savedata[i]["name"] + ": " + str(kp.savedata[i]["login"]) + ', ' + str(kp.savedata[i]["password"]) + '\n')
                child2.destroy()
            else:
                showwarning(message=Languages[s.Language]["Str2"]) #Str2
                Password1Entry["textvariable"] = tk.StringVar()

        FrameX = tk.Frame(child2, height=100, width=320)
        FrameX.pack(expand=True, fill="both")

        FrameX.columnconfigure(0, weight=1)
        FrameX.columnconfigure(1, weight=7)

        ttk.Label(FrameX, text=Languages[s.Language]["Str5"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) #Str5
        Password1Entry = ttk.Entry(FrameX, show="*")
        Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
        Password1Entry.focus()
        Password1Entry.bind('<KeyPress-Return>', ActuallyExtractPasswords)
        ttk.Button(FrameX, text=Languages[s.Language]["Str38"], command=ActuallyExtractPasswords).grid(column=1, row=1, sticky="nse", padx=10, pady=5) #Kontynuuj

    def ExtractPasswords():
        showwarning(title=Languages[s.Language]["Str39"], message=Languages[s.Language]["Str40"]) # Wyeksportuj Hasła / UWAGA: Hasła zostaną zapisane w pliku tekstowym. Upewnij się, że plik będzie przechowywany w bezpiecznym miejscu
        answer = askyesno(title=Languages[s.Language]["Str39"], message=Languages[s.Language]["Str37"]) #Str39 / # Str37
        if answer:
            AskForPassword()

    ExtractFilesButton = ttk.Button(SettingsFrameThree, text=Languages[s.Language]["Str39"], command=lambda: ExtractPasswords()) #Str39
    ExtractFilesButton.grid(column=0, row=2, sticky="nsew", padx=10, pady=5)

    SettingsFrameFour = ttk.LabelFrame(child, text=Languages[s.Language]["Str50"])
    SettingsFrameFour.pack(fill="x", padx=10)
    SettingsFrameFour.rowconfigure([0, 1, 2], weight=1)
    SettingsFrameFour.columnconfigure([0, 1], weight=1)

    ttk.Label(SettingsFrameFour, text=Languages[s.Language]["Str41"], wraplength=315).grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=5) #Menadżer hasłe PyPass napisany w pythonie

    ttk.Label(SettingsFrameFour, text=Languages[s.Language]["Str42"]).grid(row=1, sticky="nsew", padx=10, pady=5, column=0) #Wersja
    ttk.Label(SettingsFrameFour, text=kp.PyPassVersion).grid(row=1, sticky="nse", padx=10, pady=5, column=1)

    ttk.Label(SettingsFrameFour, text=Languages[s.Language]["Str48"]).grid(row=2, sticky="new", padx=10, pady=5, column=0) #Miejsce pliku z hasłami 
    PathText = tk.Text(SettingsFrameFour, height=5, width=18) #, text=path.abspath('data.pickle')
    PathText.grid(row=2, sticky="nsew", padx=10, pady=5, column=1)
    PathText.insert('1.0', path.abspath('data.pickle'))
    PathText["relief"] = 'flat'
    PathText["state"] = DISABLED
    
        
def closeEvent():
    kp.savedata["0"]["counter"] = kp.counter
    kp.savedata["0"]["theme"] = kp.theme
    kp.savedata["0"]["rollover"] = kp.rollover
    kp.savedata["0"]["password"] = kp.GlobalPassword
    if s.Pswd != '':
        kp.savedata["0"]["password"] = s.Pswd
    #print(kp.counter)
    with open('data.pickle', 'wb') as handle:
        pickle.dump(kp.savedata, handle)
    window.destroy()

themeset = ttk.Style()
themeset.theme_use(kp.theme)

window.protocol("WM_DELETE_WINDOW", lambda: closeEvent())



window.mainloop()
