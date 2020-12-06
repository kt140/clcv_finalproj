class Heroes:
    def __init__(self, name, description, story, Gods):
        self.name = name
        self.descri = description
        self.story = story
        self.gods = Gods

    def getName(self):
        return self.name
    
    def getDescrip(self):
        return self.descri
    
    def getStory(self):
        return ", ".join(self.story)

    def getGods(self):
        return ", ".join(self.gods)