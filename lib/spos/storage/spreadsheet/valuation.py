# -*- coding: iso-8859-1 -*-
from spos.storage.spreadsheet.xlsx import DB
import random
import time

class ValuationClass:
    alias = None
    marks = None
    
    def __init__(self):
        self.mark = None
        self.load()
        
    def set_mark(self, mark):
        self.mark = mark
   
    def get_randomized_raiting(self):
        raitings = self.__class__.marks[self.mark]
        pos = random.randrange(0, len(raitings))
        raiting = raitings[pos]
        
        return raiting
        
    def load(self):
        for sheet in DB.wb.worksheets:
            if "BKategorie_{}".format(self.__class__.alias) == sheet.title:
                result = {}
                if self.__class__.marks is None:
                    for row in sheet.iter_rows(2):
                        if row[0].value is None:
                            break
                        
                        note = row[0].value
                        
                        bewertungen = []
                        for bewertung in row[1:]:
                            if bewertung.value is None:
                                break
                            
                            bewertungen.append(bewertung.value)
                            
                        result[note] = bewertungen
        
                    self.__class__.marks = result

class Speaches(ValuationClass):
    alias = "Wortmeldung"
    
class Attention(ValuationClass):
    alias = "Aufmerksamkeit"
    
class Care(ValuationClass):
    alias = "Care"
    
class WillingnessToLearn(ValuationClass):
    alias = "Lernbereitschaft"
    
class Relayiability(ValuationClass):
    alias = "Zuverlässigkeit"
    
class SocialBehaviour(ValuationClass):
    alias = "Sozialverhalten"
    
class Pupil:
    
    def __init__(self, name = None):
        self.name = name
        
        self.speaches = Speaches()
        self.attention = Attention()
        self.care = Care()
        self.willingness_to_learn = WillingnessToLearn()
        self.relayiability = Relayiability()
        self.social_behaviour = SocialBehaviour()
        

class Class:
    
    def __init__(self, name="Klasse_1"):
        self.name = name
        self.pupils = []
        self.load()
    
    def load(self):
        for sheet in DB.wb.worksheets:
            if "{}".format(self.name) == sheet.title:
                
                kathegory_to_col = {}
                for cols in sheet.iter_cols(2):
                    col0 = cols[0]
                    if col0.value is None:
                        break
                    
                    kathegory_to_col[col0.column] = col0.value
                    
                for row in sheet.iter_rows(2):
                    if row[0].value is None:
                        break
                    
                    pupil = Pupil(row[0].value)
                    
                    for col in row[1:]:
                        mark = col.value
                        kathegory = kathegory_to_col[col.column]
                        
                        if kathegory in [Speaches.alias]:
                            pupil.speaches.set_mark(mark)
                        
                        elif kathegory in [Attention.alias]:
                            pupil.attention.set_mark(mark)
                        
                        elif kathegory in [Care.alias]:
                            pupil.care.set_mark(mark)
                        
                        elif kathegory in [WillingnessToLearn.alias]:
                            pupil.willingness_to_learn.set_mark(mark)
                        
                        elif kathegory in [Relayiability.alias]:
                            pupil.relayiability.set_mark(mark)
                        
                        elif kathegory in [SocialBehaviour.alias]:
                            pupil.social_behaviour.set_mark(mark)
                            
                    self.pupils.append(pupil)
                                                
                            