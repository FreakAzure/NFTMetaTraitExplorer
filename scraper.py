# Python program to read
# json file
  
import sys
import json
from os import walk

class TraitSearcher:
    #SysArgs = Attribute Name
    filesInDir = []
    matches =  []

    def searchInFile(self, fileName, traitType, traitValue) :
        attributeName = traitType
        attributeValue = traitValue
        # Opening JSON file
        f = open('./input/' + fileName)
        data = json.load(f)
        # Iterating through the json
        for (attribute) in data['attributes']:
            if(attribute['trait_type'] == traitType):
                if (attribute['value'] ==  traitValue):
                    self.matches.append(data['name'])
        f.close()

    def getTraits(self) :
        traits = []
        for (fileName) in self.filesInDir :
            file = open('./input/' + fileName)
            data = json.load(file)
            for (attribute) in data['attributes']:
                traitType = attribute['trait_type']
                if not (traitType in traits) :
                    traits.append(traitType)
            file.close()
        return traits

    def getFiles(self) :
        # Search the directory
        for (dirpath, dirnames, filenames) in walk('./input'):
            self.filesInDir.extend(filenames)
            break

    def getFilesWithTrait(self, traitType, traitName): 
        # Open Each File
        for (fileName) in self.filesInDir:
            self.searchInFile(fileName, traitType, traitName)
        return self.matches
