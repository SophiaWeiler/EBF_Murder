import tkinter as tkr
#from tkinter import ttk
from PIL import Image, ImageTk
import time

objects={"body": "The body has a bullet wound on its back.", 
        "tox":"The tox report has shown that there was alchohol in the dead body's system.",
        "gun":"The gun was discovered 2 feet away from the body. It appears to be the murder weapon.",
        "knife":"A knife was found buried in the snow, with some blood it.",
        "pans":"There were leftover pan and food found from the night before.",
        "drinks":"Some drinks were left on the kitchen table from last night.",
        "broken glass": "One of the glasses was found shattered on the floor of the dining room.",
        "missing knife":"One of the knifes is missing from the kitchen.",
        "footprints":"The footprints on the floor leads to the garden outside",
        "clothes":"Lydia's clothes were found in David's room, which is across the hall from her own.",
        "phone":"Andrew appears to have recieved a call in the middle of the night. Did this wake him up?",
        "missing gun":"There is a gun missing from the gun closet.",
        "laundry":"The laundry hanging outside is still wet and has not been touched since the night before.",
        "no footprints":"There are no footprints leading from the house to the garden, despite the damp ground.",
        "shoes":"In the bedroom there is a pair of running shoes that appear to belong to Jimmy.",
        "footprints2": "The trail of footprints continue to the gun closet. It appears that these footprints belon to Andrew"}

class Day:
    def __init__(self):
        self.num=0
        self.day=1
        self.clues=[3,3,2,3,2,2]
        #self.cluesLeft=clues
        self.journal=[]
        self.depoJournal = []
    def ShowJournal(self):
        tkr.myWindow = tkr.Tk()
        tkr.myWindow.title("Evidences")
        tkr.myWindow.configure(background="white")
        for i in range(len(self.journal)):
            tkr.Label(tkr.myWindow, text=self.journal[i]).pack()
        tkr.myWindow.mainloop()
        
    def ShowDepoJournal(self):
        tkr.DJounal = tkr.Tk()
        tkr.DJounal.title("Depositions")
        tkr.DJounal.configure(background="white")
        for i in range(len(self.depoJournal)):
            tkr.Label(tkr.DJounal, text=self.depoJournal[i]).pack()
        tkr.DJounal.mainloop()
            
    def ShowInfo(self,key):
        if objects[key] in self.journal:
            None
        else:
            print(objects[key])
            self.journal.append(objects[key])
            #Window.LabelInfo(GUI, key)
            self.num+=1

add = Day()

class Window(tkr.Frame):
    def __init__(self, master=None):

        tkr.Frame.__init__(self, master)
        self.master = master

        #Setup images
        self.titleImage = "ArtAssets/TitlePage.png"
        self.WinImage = "ArtAssets/Win.png"
        self.WinText = tkr.PhotoImage(file = "ArtAssets/WinText.png")
        self.LoseText = tkr.PhotoImage(file = "ArtAssets/LoseText.png")
        self.LoseImage = "ArtAssets/Lose.png"
        
        self.bgImage = "ArtAssets/WhiteBG.png"
        
        self.LivingRoomImage = "ArtAssets/LivingRoomFolder/LivingRoom.png"
        self.deadBody = tkr.PhotoImage(file = "ArtAssets/LivingRoomFolder/DeadBody.png")
        self.gun = tkr.PhotoImage(file = "ArtAssets/LivingRoomFolder/Gun.png")
        self.knife = tkr.PhotoImage(file = "ArtAssets/LivingRoomFolder/Knife.png")
        self.tox = tkr.PhotoImage(file = "ArtAssets/LivingRoomFolder/ToxReport.png")
        
        self.KitchenImage = "ArtAssets/KitchenFolder/Kitchen.png"
        self.Drinks = tkr.PhotoImage(file = "ArtAssets/KitchenFolder/Drinks.png")
        self.MissingKnife = tkr.PhotoImage(file = "ArtAssets/KitchenFolder/MissingKnife.png")
        self.FryingPan = tkr.PhotoImage(file = "ArtAssets/KitchenFolder/FryingPan.png")
        
        self.DiningRoomImage = "ArtAssets/DiningRoomFolder/DiningRoom.png"
        self.BrokenGlass = tkr.PhotoImage(file = "ArtAssets/DiningRoomFolder/BrokenGlass.png")
        self.Footprints = tkr.PhotoImage(file = "ArtAssets/DiningRoomFolder/Footprints.png")
        
        self.BedroomImage = "ArtAssets/BedroomFolder/Bedroom.png"
        self.DrawerInit = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/DrawerInit.png")
        self.Drawer1 = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/Drawer1.png")
        self.Drawer2 = "ArtAssets/BedroomFolder/Drawer2.png"
        self.Dress = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/Dress.png")
        self.Shoes = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/Shoes.png")
        self.PhoneInit = tkr.PhotoImage(file = "ArtAssets/BedroomFOlder/PhoneInit.png")
        self.Phone1 = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/Phone1.png")
        self.Phone2 = "ArtAssets/BedroomFolder/Phone2.png"
        self.Phone = tkr.PhotoImage(file = "ArtAssets/BedroomFolder/Phone.png")
        
        self.GardenImage = "ArtAssets/GardenFolder/Garden.png"
        self.Laundry = tkr.PhotoImage(file = "ArtAssets/GardenFolder/Laundry.png")
        self.KnifeInit = tkr.PhotoImage(file = "ArtAssets/GardenFolder/KnifeInit.png")
        self.Knife1 = tkr.PhotoImage(file = "ArtAssets/GardenFolder/Knife1.png")
        self.Knife2 = tkr.PhotoImage(file = "ArtAssets/GardenFolder/Knife2.png")
        self.Knife3 = "ArtAssets/GardenFolder/Knife3.png"
        self.KnifeImage = tkr.PhotoImage(file = "ArtAssets/GardenFolder/Knife.png")
        
        self.GunClosetImage = "ArtAssets/GunClosetFolder/GunCloset.png"
        self.MissingGun = tkr.PhotoImage(file = "ArtAssets/GunClosetFolder/MissingGun.png")
        self.Footprints2 = tkr.PhotoImage(file = "ArtAssets/GunClosetFolder/Footprints2.png")
        
        self.PrologueImage = "ArtAssets/Prologue.png"
        self.Tips = "ArtAssets/Tips.png"
        
        self.StartImage = tkr.PhotoImage(file = "ArtAssets/Start.png")
        self.NextImage = tkr.PhotoImage(file = "ArtAssets/Next.png")
        self.QuitImage = tkr.PhotoImage(file = "ArtAssets/Quit.png")
        
        self.depoImage = "ArtAssets/Depos/Depo1.png"
        self.depo2Image = "ArtAssets/Depos/Depo2.png"
        self.depo3Image = "ArtAssets/Depos/Depo3.png"
        self.LydiaDepo2Image="ArtAssets/Depos/Lydia2.png"
        self.JimmyDepo2Image="ArtAssets/Depos/Jimmy2.png"
        self.DavidDepo2Image="ArtAssets/Depos/David2.png"
        self.JimmyDepo3Image="ArtAssets/Depos/Jimmy3.png"
        self.LydiaDepo3Image="ArtAssets/Depos/Lydia3.png"
        self.DavidDepo3Image="ArtAssets/Depos/David3.png"
        self.JimmyDepo4Image="ArtAssets/Depos/Jimmy4.png"
        
        self.FinalImage = "ArtAssets/Final.png"
        self.lydia = tkr.PhotoImage(file = "ArtAssets/Lydia.png")
        self.jimmy = tkr.PhotoImage(file = "ArtAssets/Jimmy.png")
        self.david = tkr.PhotoImage(file = "ArtAssets/David.png")
        
        
        self.title_window()

    def title_window(self):
        self.master.title("Murder in the Broccoli Forest")
        self.pack(fill=tkr.BOTH, expand=1)

        # define menu and where it goes. Menu is built in to tkinter
        menuBar = tkr.Menu(self.master)
        self.master.config(menu=menuBar)

        # add 'file' = menu
        file = tkr.Menu(menuBar)
        #make this into a button so that starting a game is just a start button
        file.add_command(label="Quit", command=self.client_exit)
        menuBar.add_cascade(label="File", menu=file)

        records = tkr.Menu(menuBar)
        records.add_command(label="Evidences", command = add.ShowJournal)
        records.add_command(label="Depositions", command = add.ShowDepoJournal)
        menuBar.add_cascade(label="Journal", menu=records)
        

        startImage = self.ProcessImage(Image.open(self.titleImage))
        self.PlaceImage(startImage, 0, 0)
        
        Quit = tkr.Button(self, image=self.QuitImage, command = self.client_exit)
        Quit.place(x=450, y=538)
        
        Start = tkr.Button(self, image=self.StartImage, command = self.Prologue)
        Start.place(x=352, y=540)

    def Prologue(self):
        bgImage = self.ProcessImage(Image.open(self.PrologueImage))
        self.PlaceImage(bgImage, 0, 0)
        
        nextButton=tkr.Button(self, image=self.NextImage, command= self.TipsPage)
        nextButton.place(x=368, y=500)
        
    def TipsPage(self):
        tips = self.ProcessImage(Image.open(self.Tips))
        self.PlaceImage(tips, 0, 0)
        
        nextButton=tkr.Button(self, image=self.NextImage, command= self.Depo1)
        nextButton.place(x=368, y=500)

    def Depo1(self):
        depoImage = self.ProcessImage(Image.open(self.depoImage))
        self.PlaceImage(depoImage, 0, 0)
        
        add.depoJournal.append("Lydia's Deposition:")
        add.depoJournal.append("Was sleeping until she heard gun shot")
        add.depoJournal.append("Saw David applying pressure to Andrew’s wounds")
        add.depoJournal.append("Jimmy wasn't there and came back after the police arrived")
        add.depoJournal.append("Lydia is in love with Andrew")
        add.depoJournal.append("\n")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= self.Depo2)
        nextButton.place(x=368, y=500)
        
    def Depo2(self):
        depo2Image = self.ProcessImage(Image.open(self.depo2Image))
        self.PlaceImage(depo2Image, 0, 0)
     
        add.depoJournal.append("David's Deposition:")
        add.depoJournal.append("First to wake up")
        add.depoJournal.append("Was going to make breakfast, but then decided to take down laundry")
        add.depoJournal.append("Heard a strange noise from the woods")
        add.depoJournal.append("While he was checking, David heard the gun shot from the house")
        add.depoJournal.append("Ran back and injured himself on the bushes")
        add.depoJournal.append("Saw Andrew on the floor when he came back and tried to help him")
        add.depoJournal.append("Claimed that he is not the murderer and Andrew's closest friend")
        add.depoJournal.append("\n")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= self.Depo3)
        nextButton.place(x=368, y=500)
        
    def Depo3(self):
        depo3Image = self.ProcessImage(Image.open(self.depo3Image))
        self.PlaceImage(depo3Image, 0, 0)
        
        add.depoJournal.append("Jimmy's Deposition:")
        add.depoJournal.append("Wasn't in the house during the event and came back when the police already arrived")
        add.depoJournal.append("Claimed that he didn't heard the gun shot")
        add.depoJournal.append("Heard something coming from either David's or Andrew's rooms")
        add.depoJournal.append("Heard David and Lydia were having a fight the night before regarding Andrew")
        add.depoJournal.append("Admitted that he is jealous of Andrew")
        add.depoJournal.append("\n")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= self.Day1)
        nextButton.place(x=368, y=500)
        
    def Day1(self):
        add.num = 0
        add.day = 1
        livingImage = self.ProcessImage(Image.open(self.LivingRoomImage))
        self.PlaceImage(livingImage, 0, 0)
      
        clue1 = tkr.Button(self, image=self.deadBody, command = lambda: add.ShowInfo("body"))
        clue1.place(x=146, y=326)

        clue2 = tkr.Button(self, image=self.gun, command=lambda: add.ShowInfo("gun"))
        clue2.place(x=62, y=484)
        
        
        clue3 = tkr.Button(self, image=self.tox, command=lambda:add.ShowInfo("tox"))
        clue3.place(x=281, y=477)
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
         
            
    def Day2(self):
        add.num = 0
        add.day = 2
        kitchenImage = self.ProcessImage(Image.open(self.KitchenImage))
        self.PlaceImage(kitchenImage, 0, 0)
      
        clue1 = tkr.Button(self, image=self.Drinks, command = lambda: add.ShowInfo("drinks"))
        clue1.place(x=611, y=132)

        clue2 = tkr.Button(self, image=self.MissingKnife, command=lambda: add.ShowInfo("missing knife"))
        clue2.place(x=195, y=131)
        
        clue3 = tkr.Button(self, image=self.FryingPan, command=lambda: add.ShowInfo("pans"))
        clue3.place(x=100, y=214)
      
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
          
    def Day3(self):
        add.num = 0
        add.day = 3
        diningImage = self.ProcessImage(Image.open(self.DiningRoomImage))
        self.PlaceImage(diningImage, 0, 0)
      
        clue1 = tkr.Button(self, image=self.BrokenGlass, command = lambda: add.ShowInfo("broken glass"))
        clue1.place(x=498, y=417)
        
        clue2 = tkr.Button(self, image=self.Footprints, command = lambda: add.ShowInfo("footprints"))
        clue2.place(x=1, y=499)

        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
         
    def Day4Init(self):
        add.num = 0
        add.day = 4
        self.Day4()
        
    def Day4(self):
        bedroomImage = self.ProcessImage(Image.open(self.BedroomImage))
        self.PlaceImage(bedroomImage, 0, 0)
      
        clue1 = tkr.Button(self, image=self.DrawerInit, command = lambda: self.DrawerPuzzle())
        clue1.place(x=113, y=275)

        puzzle1 = tkr.Button(self, image=self.PhoneInit, command=lambda: self.BedroomPuzzle())
        puzzle1.place(x=114, y=244)
        
        clue3 = tkr.Button(self, image=self.Shoes, command=lambda: add.ShowInfo("shoes"))
        clue3.place(x=201, y=486)

        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
      
    def DrawerPuzzle(self):
        drawer2 = self.ProcessImage(Image.open(self.Drawer2))
        self.PlaceImage(drawer2, 0, 0)
        
        drawerFinal = tkr.Button(self, image = self.Dress, command = lambda: self.dress())
        drawerFinal.place(x=210, y=104)
        
        drawer1 = tkr.Button(self, image = self.Drawer1, command = lambda: self.Delete(drawer1))
        drawer1.place(x=0, y=0)
        
    def dress(self):
        add.ShowInfo("clothes")
        self.Day4()
        
    def BedroomPuzzle(self):
        phone2 = self.ProcessImage(Image.open(self.Phone2))
        self.PlaceImage(phone2, 0, 0)
        
        phoneFinal = tkr.Button(self, image = self.Phone, command = lambda: self.phone())
        phoneFinal.place(x=268, y=110)
        
        phone1 = tkr.Button(self, image = self.Phone1, command = lambda: self.Delete(phone1))
        phone1.place(x=0, y=0)
        
    def phone(self):
        add.ShowInfo("phone")
        self.Day4()
        
    def Day5Init(self):
        add.num = 0
        add.day = 5
        self.Day5()
        
    def Day5(self):
        gardenImage = self.ProcessImage(Image.open(self.GardenImage))
        self.PlaceImage(gardenImage, 0, 0)
        
        clue1 = tkr.Button(self, image=self.Laundry, command = lambda: add.ShowInfo("laundry"))
        clue1.place(x=68, y=157)
        
        Puzzle1 = tkr.Button(self, image = self.KnifeInit, command = self.GardenPuzzle)
        Puzzle1.place(x=393, y=333)
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
      
    def GardenPuzzle(self):
        Knife3 = self.ProcessImage(Image.open(self.Knife3))
        self.PlaceImage(Knife3, 0, 0)
    
        knifeFinal = tkr.Button(self, image = self.KnifeImage, command = lambda: self.Knife())
        knifeFinal.place(x=256, y=322)
        
        knife2 = tkr.Button(self, image = self.Knife2, command = lambda: self.Delete(knife2))
        knife2.place(x=0, y=0)
        
        knife1 = tkr.Button(self, image = self.Knife1, command = lambda: self.Delete(knife1))
        knife1.place(x=0, y=0)
         
    def Day6(self):
        add.num = 0
        add.day = 6
        
        gunClosetImage = self.ProcessImage(Image.open(self.GunClosetImage))
        self.PlaceImage(gunClosetImage, 0, 0)
        
        clue1 = tkr.Button(self, image=self.MissingGun, command = lambda: add.ShowInfo("missing gun"))
        clue1.place(x=312, y=182)
        
        clue2 = tkr.Button(self, image=self.Footprints2, command = lambda: add.ShowInfo("footprints2"))
        clue2.place(x=274, y=423)
         
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Next(add.num,add.day))
        nextButton.place(x=734, y=574)
        
    def Knife(self):
        add.ShowInfo("knife")
        self.Day5()
        
        
    def DepoDay1(self):
         add.num = 0
         add.day = 1
       
         lydiaDepo2Image = self.ProcessImage(Image.open(self.LydiaDepo2Image))
         self.PlaceImage(lydiaDepo2Image, 0, 0)
       
         add.depoJournal.append("Lydia's 2nd Deposition")
         add.depoJournal.append("Does not recognise the gun and claims to have little experience with guns")
         add.depoJournal.append("Believes that Jimmy is the one to ask as he is skilful with guns")
         add.depoJournal.append("\n")
        
         nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Depo2Day1())
         nextButton.place(x=734, y=574) 
         
    def Depo2Day1(self):
        add.num = 0
        add.day = 1
       
        jimmyDepo2Image = self.ProcessImage(Image.open(self.JimmyDepo2Image))
        self.PlaceImage(jimmyDepo2Image, 0, 0)
      
        add.depoJournal.append("Jimmy's 2nd Deposition")
        add.depoJournal.append("Admitted that he has experience with guns")
        add.depoJournal.append("Claims that a good hunter won't shoot someone in such a close distance by that gun")
        add.depoJournal.append("Thus claims that the murderer has limited knowledges about the gun")
        add.depoJournal.append("\n")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Day2())
        nextButton.place(x=734, y=574)
        
    def DepoDay2(self):
        add.num = 0
        add.day = 1
        
        davidDepo2Image = self.ProcessImage(Image.open(self.DavidDepo2Image))
        self.PlaceImage(davidDepo2Image, 0, 0)
       
        add.depoJournal.append("David's 2nd Deposition:")
        add.depoJournal.append("Claims that the drinks were from the night before")
        add.depoJournal.append("However, the broken glass wasn't there")
        add.depoJournal.append("Claims that all the knives where in the kitchen when he went to make breakfast")
        add.depoJournal.append("Clueless about the missing knife")
        add.depoJournal.append("\n")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Day3())
        nextButton.place(x=734, y=574)
        
    def DepoDay3(self):
        add.num = 0
        add.day = 1
        
        jimmyDepo3Image = self.ProcessImage(Image.open(self.JimmyDepo3Image))
        self.PlaceImage(jimmyDepo3Image, 0, 0)
        
        add.depoJournal.append("Jimmy's 3rd Deposition")
        add.depoJournal.append("Wasn't any broken glass on the floor when he went running")
       
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Day4Init())
        nextButton.place(x=734, y=574)
        
    def DepoDay4(self):
        add.num = 0
        add.day = 1
       
        lydiaDepo3Image = self.ProcessImage(Image.open(self.LydiaDepo3Image))
        self.PlaceImage(lydiaDepo3Image, 0, 0)
       
        add.depoJournal.append("Lydia's 3rd Deposition")
        add.depoJournal.append("Has no idea why her clothes were in David's room")
        add.depoJournal.append("Believes that it is just an accident")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Depo2Day4())
        nextButton.place(x=734, y=574)
        
    def Depo2Day4(self):
        add.num = 0
        add.day = 1
       
        davidDepo3Image = self.ProcessImage(Image.open(self.DavidDepo3Image))
        self.PlaceImage(davidDepo3Image, 0, 0)
       
        add.depoJournal.append("Jimmy's 4th Deposition")
        add.depoJournal.append("Clothes were still wet when he left the house")
        add.depoJournal.append("Windows were blurred a year ago so it's really hard to see through them")
        
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.Day5Init())
        nextButton.place(x=734, y=574)
        
    def DepoDay5(self):
        add.num = 0
        add.day = 1
       
        jimmyDepo4Image = self.ProcessImage(Image.open(self.JimmyDepo4Image))
        self.PlaceImage(jimmyDepo4Image, 0, 0)
       
        nextButton=tkr.Button(self, image=self.NextImage, command= lambda: self.FinalDay())
        nextButton.place(x=734, y=574)
        
    def Next(self,clueNum,dayNum):
        if clueNum == add.clues[dayNum-1]:
            if dayNum == 1:
                self.DepoDay1()
            elif dayNum == 2:
                self.DepoDay2()
            elif dayNum == 3:
                self.DepoDay3()
            elif dayNum == 4:
                self.DepoDay4()
            elif dayNum==5:
                self.Day6()
            elif dayNum == 6:
                self.DepoDay5()
        else:
            return
        
    def FinalDay(self):
        add.num=0
        add.num=6
           
        bg=self.ProcessImage(Image.open(self.FinalImage))
        self.PlaceImage(bg,0,0)
           
        lydia=tkr.Button(self,image=self.lydia, command= lambda: self.Lose())
        lydia.place(x=28, y=180)
           
        david=tkr.Button(self,image=self.david, command= lambda: self.Win())
        david.place(x=286, y=180)
          
        jimmy=tkr.Button(self,image=self.jimmy, command= lambda: self.Lose())
        jimmy.place(x=544, y=180)
       
    def Lose(self):
        print("lost")
        loseImage=self.ProcessImage(Image.open(self.LoseImage))
        self.PlaceImage(loseImage,0,0)
       
        Quit = tkr.Button(self, image=self.QuitImage, command = self.client_exit)
        Quit.place(x=744, y=572)
        
        lostText=tkr.Button(self,image=self.LoseText, command= lambda: self.Delete(lostText))
        lostText.place(x=0, y=0)
       
    def Win(self):
        print("won")
        winImage=self.ProcessImage(Image.open(self.WinImage))
        self.PlaceImage(winImage,0,0)
       
        Quit = tkr.Button(self, image=self.QuitImage, command = self.client_exit)
        Quit.place(x=744, y=572)
        
        winText=tkr.Button(self,image=self.WinText, command= lambda: self.Delete(winText))
        winText.place(x=0, y=0)
        
    def Delete(self, Object):
        Object.destroy()
        
    def LabelInfo(self, Key):
        textLabel = tkr.Label(self, text = objects[Key])
        textLabel.pack(side = tkr.BOTTOM)
        
        time.sleep(2.0)
        self.Delete(textLabel)
        
    def PasteOverBackground(self, foreground, background):
        background = Image.open(self.bgImage)
        for image in foreground:
            background.paste(image, (0, 0), image)
        return background

    def ProcessImage(self, path):
        render = ImageTk.PhotoImage(path)
        processedImage = tkr.Label(self, image=render)
        processedImage.image = render
        return processedImage

    def PlaceImage(self, image, xPos, yPos):
        image.place(x=xPos, y=yPos)

    def client_exit(self):
        self.master.destroy()

def DisplayGUI():
    
    Frame = tkr.Tk()
    Frame.geometry("800x600")
    
    GUI = Window(Frame)
    
    GUI.mainloop()

add = Day()
DisplayGUI()