import tkinter as tk
import re, pickle, keyboard, string, random, sys, locale, os
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from os import path
from tkinter.messagebox import askyesno, showinfo, showwarning
from languages import *



defaultSettings = {"0": {"password": '', "keybind": "Tab", "counter": 0, "rollover": True, "theme": "vista", "language": "English"}}
Languages = {"Polski": Polski, "English": English}



class InitialVars:
    try:
        with open('data.pickle', 'rb') as handle:
            languagedata = pickle.load(handle)
            Language = languagedata["0"]["language"]
    except FileNotFoundError:
        if locale.getdefaultlocale()[0] == 'pl_PL':
            Language = "Polski"
        else:
            Language = "English"
    Pswd = ''

I = InitialVars
        
def LoginWindow(pswd):

    loginW = tk.Tk()
    
    loginW.geometry("350x70")
    loginW.resizable(0, 0)
    loginW.title(Languages[I.Language]["Str1"]) 

    loginW.protocol("WM_DELETE_WINDOW", sys.exit)

    def CheckThePassword(*args):
        x = Password1Entry.get()
        if x == pswd:
            loginW.destroy()
        else:
            showwarning(message=Languages[I.Language]["Str2"], title=Languages[I.Language]["Str2"]) 
            Password1Entry["textvariable"] = tk.StringVar()

    FrameX = tk.Frame(loginW, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[I.Language]["Str3"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry = ttk.Entry(FrameX, show='*')
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password1Entry.bind('<KeyPress-Return>', CheckThePassword)
    ttk.Button(FrameX, text=Languages[I.Language]["Str9"], command=CheckThePassword).grid(column=1, row=1, sticky="nse", padx=10, pady=5)

    loginW.mainloop()



def CreatePasswordWindow():
    loginW = tk.Tk()
    
    loginW.geometry("350x100")
    loginW.resizable(0, 0)
    loginW.title(Languages[I.Language]["Str4"])

    loginW.protocol("WM_DELETE_WINDOW", sys.exit)

        
    FrameX = tk.Frame(loginW, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[I.Language]["Str5"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) 
    ttk.Label(FrameX, text=Languages[I.Language]["Str6"]).grid(column=0, row=1, sticky="nsew", padx=10, pady=5) 
    Password1Entry = ttk.Entry(FrameX)
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password2Entry = ttk.Entry(FrameX)
    Password2Entry.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        
        
    def CheckThePassword(*args):
        if Password1Entry.get() == Password2Entry.get():
            if Password1Entry.get() == '':
                showwarning(message=Languages[I.Language]["Str7"], title=Languages[I.Language]["Str4"]) 
            I.Pswd = Password1Entry.get()
            loginW.destroy()
        else:
            showwarning(message=Languages[I.Language]["Str8"])
            Password1Entry["textvariable"] = tk.StringVar()
            Password2Entry["textvariable"] = tk.StringVar()

    Password2Entry.bind('<KeyPress-Return>', CheckThePassword)

    ttk.Button(FrameX, text=Languages[I.Language]["Str9"], command=CheckThePassword).grid(column=1, row=2, sticky="nse", padx=10, pady=5)

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
window.title(Languages[I.Language]["Str10"])
window.resizable(0, 0)

class GlobalVars:
    whichButton = savedata["0"]["keybind"]
    PyPassVersion = '0.6.1 DEV'
    GlobalPassword = savedata["0"]["password"]
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
    isAdvanced = False
    RandomString = ""
    current_value = tk.IntVar()
    Use2FAVariable = tk.StringVar()

G = GlobalVars
ElementsList = ["0"]
NumbersList = [0]

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=10)
window.rowconfigure(1, weight=30)
window.rowconfigure(2, weight=7)


if I.Pswd != '':
        G.savedata["0"]["password"] = I.Pswd

def HardResetContinue():
    G.savedata = {"0": {"password": G.GlobalPassword, "keybind": "Tab", "counter": 0, "rollover": True, "theme": "vista", "language": "English"}}
    G.counter = 0
    G.theme = "vista"
    G.rollover = True
    showinfo(message=Languages[I.Language]["Str11"], title=Languages[I.Language]["Str44"])
    closeEvent()

def AskForPassword2():
    child2 = tk.Toplevel()
    child2.geometry("350x70")
    child2.title(Languages[I.Language]["Str55"]) 
    child2.resizable(0, 0)
    child2.grab_set()
    child2.focus()
    child2.transient()

    def SetTheNewPassword2(x, *args):
        G.GlobalPassword = x

    FrameX = tk.Frame(child2, height=100, width=320)
    FrameX.pack(expand=True, fill="both")

    FrameX.columnconfigure(0, weight=1)
    FrameX.columnconfigure(1, weight=7)

    ttk.Label(FrameX, text=Languages[I.Language]["Str33"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) 
    Password1Entry = ttk.Entry(FrameX)
    Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    Password1Entry.focus()
    Password1Entry.bind('<KeyPress-Return>', SetTheNewPassword2)
    ttk.Button(FrameX, text=Languages[I.Language]["Str38"], command=lambda: SetTheNewPassword2(Password1Entry.get())).grid(column=1, row=1, sticky="nse", padx=10, pady=5)

def HardReset():
    showwarning(title=Languages[I.Language]["Str44"], message=Languages[I.Language]["Str45"])
    answer = askyesno(title=Languages[I.Language]["Str44"], message=Languages[I.Language]["Str37"])
    if answer:
        answer2 = askyesno(title=Languages[I.Language]["Str46"], message=Languages[I.Language]["Str47"])
        if answer2 == False:
            AskForPassword2()
        HardResetContinue()

FrameTop = ttk.Frame(window, width=350)
FrameTop.grid(row=0, column=0, sticky="nsew")

TopLabel = ttk.Label(FrameTop, text=Languages[I.Language]["Str43"])
TopLabel.place(relx=0.5, rely=0.5, anchor="center")

FrameMiddle = ttk.Frame(window, relief="sunken", borderwidth=5)
FrameMiddle.grid(column=0, row=1, sticky="ns")



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
    child2.title(G.savedata[str(G.element)]["name"])
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

    G.whattopaste = 'Login'

    def changewhatToPaste(what):
        G.whattopaste = what
        if what == Languages[I.Language]["Str1"] or what == Languages[I.Language]["Str3"]:
            PasteLabel["text"] = Languages[I.Language]["Str13"] + what
        else:
            PasteLabel["text"] = what

    def TypeOutThePassword(*args):
        if G.whattopaste == Languages[I.Language]["Str1"]:
            keyboard.write(G.savedata[str(G.element)]["login"])
            if G.rollover:
                changewhatToPaste(Languages[I.Language]["Str3"]) 
        elif G.whattopaste == Languages[I.Language]["Str3"]:
            keyboard.write(G.savedata[str(G.element)]["password"])
            if G.rollover:
                changewhatToPaste(Languages[I.Language]["Str12"])
        else:
            Exit()
        

    ttk.Label(FrameX, text=Languages[I.Language]["Str49"] + G.whichButton).grid(column=0, row=0, sticky="nsew", padx=10, pady=5, columnspan=2)
    ttk.Label(FrameX, text=Languages[I.Language]["Str28"] + str(G.rollover)).grid(column=2, row=0, sticky="nsew", padx=10, pady=5)

    ttk.Button(FrameX, text="Login", command=lambda: changewhatToPaste(Languages[I.Language]["Str1"])).grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
    ttk.Button(FrameX, text="Password", command=lambda: changewhatToPaste(Languages[I.Language]["Str3"])).grid(column=1, row=1, sticky="nsew", padx=10, pady=5)

    PasteLabel = ttk.Label(FrameX, text=Languages[I.Language]["Str13"] + G.whattopaste) 
    PasteLabel.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)

    def Exit():
        child2.destroy()
        keyboard.remove_hotkey(G.whichButton)

    ttk.Button(FrameX, text=Languages[I.Language]["Str14"], command=Exit).grid(column=2, row=2, sticky="nse", padx=10, pady=5) 

    child2.protocol("WM_DELETE_WINDOW", lambda: Exit())

    keyboard.add_hotkey(G.whichButton, TypeOutThePassword, suppress=True)



def MainButtonAction(element):
    if G.delete == 0:
        G.element = element
        PasswordEnter()
    else:
        #print("-------------------------------\n-------------------------------\n-------------------------------")
        #print("!ElementsList")
        #print(ElementsList)
        #print("!G.savedata")
        #print(G.savedata)
        #print("!Element " + str(element))
        #print("!Counter " + str(G.counter))
        #print("!element")
        #print(element)
        #print("!NumbersList")
        #print(NumbersList)
        #print("!NumbersList.index(element)")
        #print(NumbersList.index(element))
        #print("!ElementsList[NumbersList.index(element)]")
        #print(ElementsList[NumbersList.index(element)])
        #print("-------------------------------")

        element2 = ElementsList[NumbersList.index(element)]
        element2.pack_forget()
        G.counter = G.counter - 1
        if G.counter == 0:
            k.SorryNoPswds.pack()
        del G.savedata[str(element)]
        del ElementsList[NumbersList.index(element)]
        del NumbersList[NumbersList.index(element)]

        #print("!ElementsList")
        #print(ElementsList)
        #print("!G.savedata")
        #print(G.savedata)
        #print("!Element " + str(element))
        #print("!Counter " + str(G.counter))
        #print("!element")
        #print(element)
        #print("!NumbersList")
        #print(NumbersList)

        ShowScrollbarWhenNeeded()
        EnterDeleteMode()
        DeleteButtonMode()

class MainButton:
    def __init__(self, x):
        Element = tk.Button(AnchoredMiddleFrame, text=G.savedata[str(x)]["name"], wraplength=FrameWidth, width=53, height=4, command=lambda: MainButtonAction(x))
        Element.pack()
        ElementsList.append(Element)
        NumbersList.append(x)
        


FrameWidth = 350
class PopulatePswdButttons:
    UseScrollbar = False
    SorryNoPswds = tk.Label(AnchoredMiddleFrame, text=Languages[I.Language]["Str15"], width=56, height=5, fg="gray")
    def __init__(self):
        if G.counter == 0:
            self.SorryNoPswds.pack()
        else:
            self.CreateButtons(G.counter)
            self.ScrollbarCheck(G.counter)

    def CreateButtons(self, x):
        for i in range(x + 1):
            if i != 0:
                MainButton(i)

    def ScrollbarCheck(self, x):
        if x > 6:
            self.UseScrollbar = True
        else:
            self.UseScrollbar = False

k = PopulatePswdButttons()

def CreateButton(name, login, pswd):
    ObjToAdd = {"name": name, "login": login, "password": pswd}
    G.counter += 1
    G.savedata[str(G.counter)] = ObjToAdd
    MainButton(G.counter)
    k.ScrollbarCheck(G.counter)
    DeleteButtonMode()

    

PasswordList.create_window(0, 0, window=AnchoredMiddleFrame, anchor="nw")
PasswordList.update_idletasks()
PasswordList.configure(scrollregion=PasswordList.bbox("all"), yscrollcommand=scrollbar.set)

def ShowScrollbarWhenNeeded():
    k.ScrollbarCheck(G.counter)
    if k.UseScrollbar:
        scrollbar.pack(side="right", fill="y")
    else:
        scrollbar.pack_forget()

ShowScrollbarWhenNeeded()

FrameBottom = ttk.Frame(window)
FrameBottom.grid(column=0, row=2, sticky="nsew")

FrameBottom.rowconfigure(0, weight=1)
FrameBottom.columnconfigure([0, 1, 2], weight=1)

AddButton = ttk.Button(FrameBottom, text=Languages[I.Language]["Str16"], width=10, command=lambda: AddNewEntryWindow())
AddButton.grid(row=0, column=0, padx=40)
SettingsButton = ttk.Button(FrameBottom, text=Languages[I.Language]["Str17"], width=10, command=lambda: SettingsWindow()) 
SettingsButton.grid(row=0, column=1, padx=40)
DeleteButton = ttk.Button(FrameBottom, text=Languages[I.Language]["Str18"], width=10, command=lambda: EnterDeleteMode()) 
DeleteButton.grid(row=0, column=2, padx=40)

def DeleteButtonMode():
    if G.counter == 0:
        DeleteButton["state"] = DISABLED
    else: 
        DeleteButton["state"] = NORMAL
DeleteButtonMode()

def EnterDeleteMode():
    if G.delete == 0:
        G.delete = 1
        DeleteButton["text"] = Languages[I.Language]["Str19"] 
        AddButton["state"] = DISABLED
        SettingsButton["state"] = DISABLED
        TopLabel["text"] = Languages[I.Language]["Str20"] 
    else: 
        G.delete = 0
        DeleteButton["text"] = Languages[I.Language]["Str18"]
        AddButton["state"] = NORMAL
        SettingsButton["state"] = NORMAL
        TopLabel["text"] = Languages[I.Language]["Str43"]
    


def AddNewEntryWindow():
    child = tk.Toplevel()
    child.geometry("350x139")
    child.resizable(0, 0)
    child.title(Languages[I.Language]["Str21"]) 
    child.transient()
    child.focus()
    child.grab_set()
    G.current_value.set(24)

    def PassAndClose(name, login, pswd):
        if name != '' and login != '' and pswd != '':
            child.destroy()
            if k.SorryNoPswds.winfo_exists() == True:
                k.SorryNoPswds.pack_forget()
            CreateButton(name, login, pswd)
            ShowScrollbarWhenNeeded()
            PasswordList.update_idletasks()
            PasswordList.configure(scrollregion=PasswordList.bbox("all"), yscrollcommand=scrollbar.set)
        else:
            showwarning(message=Languages[I.Language]["Str22"]) 

    EntryTKStringVar = tk.StringVar()
    child.columnconfigure(0, weight=1)
    child.columnconfigure(1, weight=4)
    child.rowconfigure([0, 1, 2, 3, 4], weight=1)
    ttk.Label(child, text=Languages[I.Language]["Str23"]).grid(column=0, row=0, sticky="e", padx=5) 
    ttk.Label(child, text="Login").grid(column=0, row=1, sticky="e", padx=5) 
    ttk.Label(child, text=Languages[I.Language]["Str3"]).grid(column=0, row=2, sticky="e", padx=5) 
    NameEnter = ttk.Entry(child)
    NameEnter.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
    LoginEnter = ttk.Entry(child)
    LoginEnter.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
    PswdEnter = ttk.Entry(child, textvariable=EntryTKStringVar)
    PswdEnter.grid(column=1, row=2, sticky="nsew", padx=10, pady=5)
    ttk.Button(child, text=Languages[I.Language]["Str24"], command=lambda: PassAndClose(NameEnter.get(), LoginEnter.get(), PswdEnter.get())).grid(column=1, row=3, sticky="e", padx=10, pady=5) 

    def SliderValueCallback(*args):
        SliderValue["text"] = G.current_value.get()

    def GenerateRandomString(*args):
        for i in range(G.current_value.get()):
            G.RandomString = G.RandomString + random.choice(string.ascii_letters + string.digits + "#@!$%^&*()-_=+")
        EntryTKStringVar.set(G.RandomString)
        G.RandomString = ''


    AdvFrame = ttk.Frame(child)
    AdvFrame.columnconfigure(0, weight=1)
    AdvFrame.columnconfigure(1, minsize=253)
    AdvFrame.rowconfigure([0, 1, 2], weight=1)
    AdvFrame.rowconfigure(3, minsize=33)
    ttk.Label(AdvFrame, text="Generate a random password:").grid(row=0, column=0, columnspan=2, sticky="nsw", padx=10, pady=5)
    SliderFrame = ttk.Frame(AdvFrame)
    SliderFrame.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
    ttk.Button(AdvFrame, text="Generate", command=GenerateRandomString).grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
    slider = ttk.Scale(SliderFrame, from_=8, to=32, variable=G.current_value, command=SliderValueCallback)
    SliderValue = ttk.Label(SliderFrame, text=G.current_value.get())
    SliderValue.pack(side="left", ipadx=10)
    slider.pack(side="right", expand=True, fill="x")

    def ToggleAdvancedMode():
        if G.isAdvanced:
            child.geometry("350x139")
            AdvFrame.grid_forget()
            G.isAdvanced = False
        else:
            child.geometry("350x275")
            AdvFrame.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=5, padx=5)
            G.isAdvanced = True

    ttk.Button(child, text="Advanced", command=ToggleAdvancedMode).grid(row=3, column=1, padx=10, pady=5)


    ttk.Label(AdvFrame, text="Configure 2FA: (doesn't work yet)").grid(row=2, column=0, columnspan=2, sticky="nsw", padx=10, pady=5) #!
    
    def Use2FAChange():
        if G.Use2FAVariable.get() == '1':
            MFAEntry["state"] = NORMAL
        else:
            MFAEntry["state"] = DISABLED
            MFAEntry["textvariable"] = tk.StringVar()

    MFACheck = ttk.Checkbutton(AdvFrame, text="Use 2FA", onvalue=True, offvalue=False, variable=G.Use2FAVariable, command=Use2FAChange)
    MFACheck.grid(column=0, row=3, sticky="nsw", padx=10, pady=5)
    MFAEntry = ttk.Entry(AdvFrame, state=DISABLED)
    MFAEntry.grid(column=1, row=3, sticky="nsew", padx=10, pady=5)




ButtonPressed = tk.StringVar()


if G.GlobalPassword == '':
    ButtonPressed.set("Tab")
else:
    ButtonPressed.set(G.GlobalPassword)

def SettingsWindow():
    child = tk.Toplevel()
    child.geometry("350x490")
    child.resizable(0, 1)
    child.title(Languages[I.Language]["Str17"]) 
    child.transient()
    child.focus()
    child.grab_set()

    SettingsFrameOne = ttk.LabelFrame(child, text=Languages[I.Language]["Str25"])
    SettingsFrameOne.pack(fill="x", padx=10) 
    SettingsFrameOne.columnconfigure([0, 1], weight=1)
    SettingsFrameOne.rowconfigure([0, 1], weight=1)

    ThemeOption = tk.StringVar()
    ThemeList = []
    styles = ttk.Style()
    for i in styles.theme_names():
        ThemeList.append(i)

    x = styles.theme_use()

    def ThemeChange(*args):
        styles.theme_use(ThemeOption.get())
        G.theme = ThemeOption.get()

    ttk.Label(SettingsFrameOne, text=Languages[I.Language]["Str26"]).grid(column=0, row=0, sticky="w", padx=10, pady=5) 
    ttk.OptionMenu(SettingsFrameOne, ThemeOption, x, *ThemeList, command=ThemeChange).grid(column=1, row=0, sticky="e", padx=10, pady=5)

    LanguageOption = tk.StringVar()
    LanguageList = []
    for i in Languages:
        LanguageList.append(i)

    def ChangeLanguage(*args):
        I.Language = LanguageOption.get()
        showinfo(message=Languages[I.Language]["Str52"], title=Languages[I.Language]["Str53"])

    ttk.Label(SettingsFrameOne, text=Languages[I.Language]["Str51"]).grid(column=0, row=1, sticky="w", padx=10, pady=5) 
    ttk.OptionMenu(SettingsFrameOne, LanguageOption, I.Language, *LanguageList, command=ChangeLanguage).grid(column=1, row=1, sticky="e", padx=10, pady=5)

    SettingsFrameTwo = ttk.LabelFrame(child, text=Languages[I.Language]["Str27"]) 
    SettingsFrameTwo.pack(fill="x", padx=10)
    SettingsFrameTwo.columnconfigure([0, 1], weight=1)

    ttk.Label(SettingsFrameTwo, text=Languages[I.Language]["Str49"]).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    KeyButton = ttk.Button(SettingsFrameTwo, text=G.whichButton, command=lambda: RegisterTheButton())
    KeyButton.grid(row=0, column=1, sticky="e", padx=10, pady=5)
    
    

    def ChangeRollover(*args):
        if G.ChangeRolloverVariable.get() == '1':
            G.rollover = True
        else:
            G.rollover = False

    ttk.Label(SettingsFrameTwo, text=Languages[I.Language]["Str28"]).grid(row=1, column=0, sticky="w", padx=10, pady=5) 
    ttk.Checkbutton(SettingsFrameTwo, onvalue=True, offvalue=False, variable=G.ChangeRolloverVariable, command=ChangeRollover).grid(row=1, column=1, sticky="e", padx=10, pady=5)

    
    def RegisterTheButton():
        meanwhile = KeyButton["text"]
        KeyButton["text"] = Languages[I.Language]["Str29"] 
        def SaveKeypress(x):
            x = re.split('=', re.split(' ', str(x))[3])[1]
            if x == 'Escape':
                KeyButton["text"] = meanwhile
            else:
                KeyButton["text"] = x
                ButtonPressed.set(x)
            KeyButton.unbind('<Any-KeyPress>')
            G.whichButton = ButtonPressed.get()
            G.savedata["0"]["keybind"] = G.whichButton
            
        KeyButton.bind('<Any-KeyPress>', SaveKeypress)

    

    SettingsFrameThree = ttk.LabelFrame(child, text=Languages[I.Language]["Str30"]) 
    SettingsFrameThree.pack(fill="x", padx=10)
    SettingsFrameThree.rowconfigure([0, 1, 2], weight=1)
    SettingsFrameThree.columnconfigure(0, weight=1)

        

    CreateNewFileButton = ttk.Button(SettingsFrameThree, text=Languages[I.Language]["Str31"], command=HardReset)
    CreateNewFileButton.grid(column=0, row=0, sticky="nsew", padx=10, pady=5)


    def SetTheNewPassword(x, y, z, child, *args):
        if x == G.GlobalPassword and y == z:
            G.GlobalPassword = y
            G.savedata["0"]["password"] = y
        child.destroy()
         
           
                

    def AskForANewPassword():
        child2 = tk.Toplevel()
        child2.geometry("350x140")
        child2.title(Languages[I.Language]["Str35"])
        child2.grab_set()
        child2.resizable(0, 0)
        child2.focus()
        child2.transient()
        FrameX = ttk.Frame(child2)
        FrameX.pack(expand=True, fill="both")

        FrameX.columnconfigure(0, weight=1)
        FrameX.columnconfigure(1, weight=4)
        FrameX.rowconfigure([0, 1, 2, 3], weight=1)
        ttk.Label(FrameX, text=Languages[I.Language]["Str32"]).grid(column=0, row=0, sticky="e", padx=5) 
        ttk.Label(FrameX, text=Languages[I.Language]["Str33"]).grid(column=0, row=1, sticky="e", padx=5) 
        ttk.Label(FrameX, text=Languages[I.Language]["Str34"]).grid(column=0, row=2, sticky="e", padx=5) 
        oldEnter = ttk.Entry(FrameX)
        oldEnter.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
        newEnter = ttk.Entry(FrameX)
        newEnter.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        new2Enter = ttk.Entry(FrameX)
        new2Enter.grid(column=1, row=2, sticky="nsew", padx=10, pady=5)
        ttk.Button(FrameX, text=Languages[I.Language]["Str24"], command=lambda: SetTheNewPassword(oldEnter.get(), newEnter.get(), new2Enter.get(), child2)).grid(column=1, row=3, sticky="e", padx=10, pady=5) 

    def ChangePasswordWarning():
        showwarning(title=Languages[I.Language]["Str35"], message=Languages[I.Language]["Str36"]) 
        answer = askyesno(title=Languages[I.Language]["Str35"], message=Languages[I.Language]["Str37"]) 
        if answer:
            AskForANewPassword()

    ChangePasswordButton = ttk.Button(SettingsFrameThree, text=Languages[I.Language]["Str35"], command=lambda: ChangePasswordWarning())
    ChangePasswordButton.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
    
    def AskForPassword():
        child2 = tk.Toplevel()
        child2.geometry("350x70")
        child2.grab_set(Languages[I.Language]["Str5"])
        child2.title()
        child2.resizable(0, 0)
        child2.focus()
        child2.transient()

        def ActuallyExtractPasswords(*args):
            if Password1Entry.get() == G.GlobalPassword:
                for i in G.savedata:
                    if i != "0":
                        with open("passwords.txt", "a") as f:
                            f.write(G.savedata[i]["name"] + ": " + str(G.savedata[i]["login"]) + ', ' + str(G.savedata[i]["password"]) + '\n')
                child2.destroy()
            else:
                showwarning(message=Languages[I.Language]["Str2"])
                Password1Entry["textvariable"] = tk.StringVar()

        FrameX = tk.Frame(child2, height=100, width=320)
        FrameX.pack(expand=True, fill="both")

        FrameX.columnconfigure(0, weight=1)
        FrameX.columnconfigure(1, weight=7)

        ttk.Label(FrameX, text=Languages[I.Language]["Str5"]).grid(column=0, row=0, sticky="nsew", padx=10, pady=5) 
        Password1Entry = ttk.Entry(FrameX, show="*")
        Password1Entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=5)
        Password1Entry.focus()
        Password1Entry.bind('<KeyPress-Return>', ActuallyExtractPasswords)
        ttk.Button(FrameX, text=Languages[I.Language]["Str38"], command=ActuallyExtractPasswords).grid(column=1, row=1, sticky="nse", padx=10, pady=5) 

    def ExtractPasswords():
        showwarning(title=Languages[I.Language]["Str39"], message=Languages[I.Language]["Str40"]) 
        answer = askyesno(title=Languages[I.Language]["Str39"], message=Languages[I.Language]["Str37"]) 
        if answer:
            AskForPassword()

    ExtractFilesButton = ttk.Button(SettingsFrameThree, text=Languages[I.Language]["Str39"], command=lambda: ExtractPasswords())
    ExtractFilesButton.grid(column=0, row=2, sticky="nsew", padx=10, pady=5)

    SettingsFrameFour = ttk.LabelFrame(child, text=Languages[I.Language]["Str50"])
    SettingsFrameFour.pack(fill="x", padx=10)
    SettingsFrameFour.rowconfigure([0, 1, 2], weight=1)
    SettingsFrameFour.columnconfigure([0, 1], weight=1)

    ttk.Label(SettingsFrameFour, text=Languages[I.Language]["Str41"], wraplength=315).grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=5) 

    ttk.Label(SettingsFrameFour, text=Languages[I.Language]["Str42"]).grid(row=1, sticky="nsew", padx=10, pady=5, column=0) 
    ttk.Label(SettingsFrameFour, text=G.PyPassVersion).grid(row=1, sticky="nse", padx=10, pady=5, column=1)

    ttk.Label(SettingsFrameFour, text=Languages[I.Language]["Str48"]).grid(row=2, sticky="new", padx=10, pady=5, column=0) 
    PathText = tk.Text(SettingsFrameFour, height=5, width=18, relief="flat") 
    PathText.grid(row=2, sticky="nsew", padx=10, pady=5, column=1)
    PathText.insert('1.0', path.abspath('data.pickle'))
    PathText["state"] = DISABLED
    
meanwhile_dict = {}
     
def closeEvent():
    G.savedata["0"]["counter"] = G.counter
    G.savedata["0"]["theme"] = G.theme
    G.savedata["0"]["rollover"] = G.rollover
    G.savedata["0"]["password"] = G.GlobalPassword
    G.savedata["0"]["language"] = I.Language
    for i in range(len(G.savedata)):
        meanwhile_dict[str(i)] = G.savedata[list(G.savedata.keys())[i]]
    G.savedata = meanwhile_dict
    #print(G.counter)
    with open('data.pickle', 'wb') as handle:
        pickle.dump(G.savedata, handle)
    window.destroy()

themeset = ttk.Style()
themeset.theme_use(G.theme)

window.protocol("WM_DELETE_WINDOW", closeEvent)



window.mainloop()
