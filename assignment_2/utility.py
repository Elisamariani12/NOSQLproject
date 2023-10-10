import json
import re
from io import TextIOWrapper

# mongodb+srv://other:urwsN7C3yvZ4LPlF@cluster0.vtjiu.mongodb.net/test

class RegexPatterns:
    isoDate = r"(\"(ISODate)(\('[1234567890-]*'\))\")" # https://regex101.com/r/yhTm9P/1

class DBDataType:
    def generateId(self) -> str:
        return "UNASSIGNED"
    def toStringDict(self, generateId = False) -> str:
        if generateId:
            self._id = self.generateId()
        return json.dumps(self.__dict__)

class DBCollection:
    def documents(self) -> list[DBDataType]:
        pass
        
        


class DBJsonWriter:
    @staticmethod
    def toFile(fileName : str, jsonString : str, directory : str = "json/") -> None:
        f = open(directory + fileName, "w")
        text = jsonString
        # text = DBJsonWriter.replaceQuotesOnObjects(text)
        f.write(text)
        f.close()
    @staticmethod    
    def toString(jsonString : str) -> str:
        return DBJsonWriter.replaceQuotesOnObjects(jsonString)
    @staticmethod    
    def collectionToFile(fileName : str, collection : DBCollection, directory : str = "json/") -> None:
        f = open(directory + fileName, "w")
        for i, doc in enumerate(collection.documents()):
            if i > 0: f.write("\n")
            f.write(doc.toStringDict())
        f.close()

    @staticmethod
    def replaceQuotesOnObjects(text : str) -> str:
        isoDate = re.search(RegexPatterns.isoDate, text)
        while isoDate:
            dateStr = isoDate.group(0)
            text = text.replace(dateStr, dateStr.replace('"',''))
            isoDate = re.search(RegexPatterns.isoDate, text)
        return text
        
    