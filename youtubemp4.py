from tkinter import StringVar
import pytube
from tkinter import *


def download_video():
    url = (lien.get())

    try:
        youtube =  pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(r"\pythonProject1\Vidéos")
        notif.config(fg="green",text="Video téléchargée BG",bg="#8440A8")
        notif.pack()
    except Exception as e:
        print(e)
        notif.config(fg="red",text="Erreur lors du téléchargement de la vidéo !",bg ="#8440A8" )
        notif.pack()


#afficher la fenêtre
window = Tk()
window.title("JL Youtube.mp4")
window.iconbitmap('algeria.ico')
window.geometry("500x500")
window.config(background="black")
window.minsize(500, 100)
window.maxsize(500, 500)

#petite frame en brrr
frame = Frame(window, bg="#8440A8")

#création de la variable du lien
lien = StringVar()

#afficher un texte
Label_lien = Label(frame, text="Past the link and download !", font=("Full Pack 2025",10), bg="black", fg="white")
Label_lien.pack()

notif = Label(frame, font=("Calibri",15))



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

#affiche la fenetre clebard de merde va
window.mainloop()






