#!/usr/bin/env python3

class Fridge:
    
    def __init__(self):
        self.mainls = []

    def store(self, item):
        self.mainls.append(item)
        self.mainls.sort()
        
    def take(self, item):
        if item in self.mainls:
            self.mainls.remove(item)
            return item
        else:
            raise Warning("My request no worky")
        
    def find(self, itemname):
        for item in self.mainls:
            if itemname in item:
                return item
        return None

    def take_before(self, itemdate):
        returnls = []
        for item in self.mainls:
            if itemdate > item[0]:
                self.mainls.remove(item)
                returnls.append(item)
        return returnls
        
    def __iter__(self):
        return iter(self.mainls)
        
    def __next__(self):
        return next(self.mainls)

    def __len__(self):
        return len(self.mainls)

