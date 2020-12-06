from gods_goddesses_class import GodsandGoddess
#def __init__(self, name, description, classification, parents, kids, heroes)
def gods(GodName):

    #defining Gods and Goddesses
    Chaos = GodsandGoddess("Chaos", "Nothingness", "Primordial", [], [], [])
    Uranus = GodsandGoddess("Uranus", "The Sky", "Primordial", [], [], [])
    Aphrodite = GodsandGoddess("Aphrodite", "Goddess of Love", "Olympian", ["Uranus"], [], [])
    Nyx = GodsandGoddess("Nyx", "Goddess of the Night", "Primordial", [], [], [])
    Tartarus = GodsandGoddess("Tartarus", "The deep abyss of the Underworld", "Primordial", [], [], [])
    Gaia = GodsandGoddess("Gaia", "Earth Goddess", "Primordial", [], ["Kronos", "Rhea"], [])
    Kronos = GodsandGoddess("Kronos", "Titan of Time", "Titan", ["Uranus", "Gaia"], [], [])
    Rhea = GodsandGoddess("Rhea", "The Mother of the Gods", "Titan", ["Uranus", "Gaia"], [], [])
    Zeus = GodsandGoddess("Zeus", "King of Gods", "Olympian", ["Kronos", "Rhea"], ["Ares", "Athena", "Hephaestus", "Apollo", "Artemis", "Persephone", "Hermes"], ["Hercules"])
    Hera = GodsandGoddess("Hera", "Queen of the Gods", "Olympian", ["Kronos", "Rhea"], [], [])
    Poseidon = GodsandGoddess("Poseidon", "God of the Sea", "Olympian", ["Kronos", "Rhea"], [], [])
    Hades = GodsandGoddess("Hades", "God of the Underworld", "Olympian", ["Kronos", "Rhea"], [], [])
    Demeter = GodsandGoddess("Demeter", "Goddess of Vegetation and Agriculture", "Olympian", ["Kronos", "Rhea"], [], [])
    Persephone = GodsandGoddess("Persephone", "Goddess of Agriculture", "Olympians", ["Zeus", "Demeter"], [], [])
    Athena = GodsandGoddess("Athena", "Goddess of Wisdom", "Olympians", ["Zeus"], [], [])
    Ares = GodsandGoddess("Ares", "God of War", "Olympians", ["Zeus", "Hera"], [], [])
    Hestia = GodsandGoddess("Hestia", "Goddess of Hearth", "Olympians", ["Kronos", "Rhea"], [], [])
    Hephaestus = GodsandGoddess("Hephaestus", "God of Fire, Metallurgy, and Forges", "Olympians", ["Zeus", "Hera"], [], [])

    if(GodName == "Kronos"):
        return Kronos
    elif (GodName == "Zeus"):
        return Zeus
    elif(GodName == "Hestia"):
        return Hestia
    elif(GodName == "Hephaestus"):
        return Hephaestus
    elif(GodName == "Persephone"):
        return Ares
    elif(GodName == "Uranus"):
        return Uranus
    elif(GodName == "Tartarus"):
        return Tartarus
    elif (GodName == "Chaos"):
        return Chaos
    else:
        return None
