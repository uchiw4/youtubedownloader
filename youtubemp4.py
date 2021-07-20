from tkinter import StringVar, Label
from pytube import YouTube
from tkinter import *
from tkinter import filedialog




def download_video():
    url = (lien.get())
    try:
        print(url)
        print("0")
        youtube =YouTube(url)
        print("1")
        video = youtube.streams.get_highest_resolution()
        print("2")
        video.download(filedialog.asksaveasfilename())
        print("3")
        notif.config(fg="green",text="Video downloaded !",bg="black")
        print("4")
        notif.pack()


    except Exception as e:
        print(e)
        notif.config(fg="red",text="Error while downloading the video !",bg ="black" )
        notif.pack()





#afficher la fenêtre
window = Tk()
photo1 = PhotoImage(file = f"\Algerie.png")
window.title("JL Youtube.mp4")
window.geometry("500x500")
window.iconphoto(False, photo1)
window.config(background= "black")
window.minsize(500, 100)
window.maxsize(500, 500)

#petite frame en brrr
frame = Frame(window, bg="black")



#création de la variable du lien
lien = StringVar()

place = StringVar()

#afficher un texte

Label_lien = Label(frame, text="Past the link and download !", font=("Full Pack 2025",10), bg="black", fg="white")
Label_lien.pack()

notif = Label(frame, font=("Calibri",15), bg ="black")



#nouvelle frame
frame_2 = Frame(window, bg="black")

# Créez un champ
videolink_entry = Entry(frame_2, font=("Calibri",15), textvariable = lien )
videolink_entry.pack(fill=X)


#petitbouton
boutontelecharger = Button(frame_2, text="Download", font=("Full Pack 2025", 10), bg="black", fg="white", command=download_video)
boutontelecharger.pack(fill=X)


#placer la frame
frame.grid(padx=1,row=0)

#afficher la frame
frame.pack(expand=YES)
frame_2.pack(expand=YES)

#affiche la fenetre
window.mainloop()









