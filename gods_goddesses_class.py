class GodsandGoddess:
    def __init__(self, name, description, classification, parents, kids, heroes):
        self.name = name
        self.classi = classification
        self.descrip = description
        self.parents = parents
        self.children = kids
        self.assoc_heroes = heroes

    def getName(self):
        return self.name
    
    def getClass(self):
        return self.classi

    def getParent(self):
        if(self.parents == []):
            return "No Parents"
        return ", ".join(self.parents)

    def getDescrip(self):
        return self.descrip
    
    def getHeroes(self):
        if(self.assoc_heroes == []):
            return "No associated heroes"
        return ", ".join(self.assoc_heroes)
    
    def getChildren(self):
        if(self.children == []):
            return "No associated children"
        return ", ".join(self.children)
