from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image

# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#e5e5e5" # Cinza
co3 = "#00a095" # Verde
co4 = "#403d3d" # letra
co6 = "#003452" # azul
co7 = "#ef5350" # vermelha

co6 = "#038cfc" # azul
co8 = "#263238" # + verde
co9 = "#e9edf5" # + + verde

janela = Tk()
janela.title("")
janela.geometry('850x652')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Frames

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0,padx=0,pady=0,sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

logo = Image.open('./imgs/logo.png')
logo = logo.resize((50,50))
logo = ImageTk.PhotoImage(logo)
app_logo = Label(frame_logo,image=logo, text='Cadastro de Moveis',width=850, compound=LEFT, relief=RAISED,anchor=NW, font=('Ivy 15 bold'),bg=co6,fg=co1)
app_logo.place(x=0,y=0)


janela.mainloop()
