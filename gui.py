from re import search
from site import ENABLE_USER_SITE
from tkinter import *
from scraper import TraitSearcher
from functools import partial
import csv

class ScrapperGUI:
    root = Tk()
    traitType = ""
    searcher = TraitSearcher()
    searcher.getFiles()
    searchButton = None
    traitNameInput = None

    def setTraitType(self, type):
        self.traitType = type
        self.searchButton["state"] = NORMAL


    def searchTrait(self):
        files = self.searcher.getFilesWithTrait(self.traitType, self.traitNameInput.get())
        self.displayMatchingFiles(files)


    def setView(self):
        self.root.geometry("800x800")
        titleLabel = Label(
            self.root,
            text="Selecciona la trait que quieres buscar",
        )
        traitNameLabel = Label(
            self.root, text="Escribe el nombre de la trait que quieres buscar"
        )
        self.traitNameInput = Entry(self.root)
        self.searchButton = Button(
            self.root, text="Buscar!", command=partial(self.searchTrait)
        )
        titleLabel.grid(column=0, row=0)
        traitNameLabel.grid(column=1, row=0, padx=10)
        self.traitNameInput.grid(column=1, row=2, pady=20)
        self.searchButton.grid(column=1, row=3, pady=20)
        self.searchButton["state"] = DISABLED

        self.showTraits()
        self.root.mainloop()

    def showTraits(self):
        traits = self.searcher.getTraits()
        for trait in traits:
            button = Button(self.root, text=trait, command=partial(self.setTraitType, trait))
            button.grid(column=0, pady=5)

    def displayMatchingFiles(self ,files) :
        print('Generating output file...')
        with open('./output/output.txt', 'w') as f:
            for line in files:
                f.write(f"{line}\n")
        print('Output file generated!')
    