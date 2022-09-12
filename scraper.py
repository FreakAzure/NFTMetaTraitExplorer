# Python program to read
# json file
  
from fileinput import filename
import sys
import json
from os import walk
import codecs
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
                    self.matches.append(fileName)
        f.close()

    def getTraits(self) :
    

        traits = []
        for (fileName) in self.filesInDir :
            with codecs.open('./input/' + fileName,'rU','ISO-8859-1') as f:
                fulldata = []
                for line in f:
                    data=json.loads(line)           
                    fulldata.append(data["attributes"])
                    for (attribute) in data["attributes"]:
                        traitType = attribute['trait_type']
                        if not (traitType in traits) :
                            traits.append(traitType)
        return traits

    def getFiles(self) :
        # Search the directory
        for (dirpath, dirnames, filenames) in walk('./input'):
            self.filesInDir.extend(filenames)
            break

    def getFilesWithTrait(self, traitType, traitName): 
        # Open Each File
        self.matches = []
        for (fileName) in self.filesInDir:
            self.searchInFile(fileName, traitType, traitName)
        self.matches.sort()
        return self.matches
