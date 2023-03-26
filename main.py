from back import Czlowiek,Miesiace
from tkinter import *
import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("System logowania")   
        self.geometry("900x900")

        self.name = ctk.CTkLabel(self, text="Imie")
        self.name.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.nameLabel = ctk.CTkEntry(self)
        self.nameLabel.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.nameLabel.bind("<Key>", self.checkImie)

        self.surname = ctk.CTkLabel(self, text="Nazwisko")
        self.surname.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.surnameLabel = ctk.CTkEntry(self)
        self.surnameLabel.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.surnameLabel.bind("<Key>", self.checkNaziwsko)

        self.wiek = ctk.CTkLabel(self, text="Wiek")
        self.wiek.grid(row=2, column=0,padx=20, pady=20, sticky="ew")

        self.wiekSlider = ctk.CTkSlider(self, from_=0, to=100, command=self.wiekChange)
        self.wiekSlider.grid(row=2, column=1, padx=20, pady=20)
        self.wiekSlider.set(0)

        self.wiekCounter = ctk.CTkLabel(self, text="0")
        self.wiekCounter.grid(row=2, column=2, padx=20, pady=20, sticky="w")

        self.miesiac = ctk.CTkLabel(self, text="Miesiac")
        self.miesiac.grid(row=3,column=0,padx=20, pady=20, sticky="ew")

        self.combobox = ctk.CTkOptionMenu(self, values=[month.name for month in Miesiace])
        self.combobox.grid(row=3, column=1,padx=20, pady=20, sticky="ew")

        self.pesel = ctk.CTkLabel(self, text="Pesel")
        self.pesel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.peselLabel = ctk.CTkEntry(self,validate='key')
        self.peselLabel.configure(validatecommand=(self.checkPesel, '%P'))
        self.peselLabel.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.button = ctk.CTkButton(self, text = "Zarejestruj sie", command = self.register)
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER)
    def wiekChange(self, wiek):
        self.wiekCounter.configure(text=int(wiek))
    
    def checkImie(self,event) -> bool:
        if len(self.nameLabel.get()) <= 2:
            self.nameLabel.configure(text_color="red")
            return False
        else:
            self.nameLabel.configure(text_color="white")
            return True

    def checkNaziwsko(self,event)  -> bool:
        if len(self.surnameLabel.get()) <= 2:
            self.surnameLabel.configure(text_color="red")
            return False
        else:
            self.surnameLabel.configure(text_color="white")
            return True
    def checkPesel(self,value):
        print(value)
        if value.isdigit() and len(value) == 11:
            return True
        else:
            return False
    
    def register(self):
        if self.checkImie == True and self.checkNaziwsko == True:
            try:
                czlowiek = Czlowiek(str(self.nameLabel.get()), str(self.surnameLabel.get()), str(self.wiekCounter.cget('text')), Miesiace[str(self.combobox.get()).upper()], (str(self.peselLabel.get()) if len(self.peselLabel.get()) == 11 else "brak"))
                print(czlowiek)
            except Exception as ex:
                print(ex)
        else:
            self.error = ctk.CTkLabel(self, text="BŁĄD, musisz podać imie oraz naziwsko",text_color="red", font=("Arial", 40))
            self.error.place(relx=0.5, rely=0.6, anchor=CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()