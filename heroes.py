from heroes_class import Heroes

def heroes(hero):
      #  def __init__(self, name, description, story, Gods):
  Heracles = Heroes("Heracles or Hercules", "All mighty warrior, son of Zeus and Alcmene.", ["Odyssey", "Metamorphoses"], ["Zeus", "Hera", "Athena"])
  Odysseus = Heroes("Odysseus", "King of the Island of Ithaca", ["Odyssey"], ["Poseidon"])

  if((hero == "Heracles" )|(hero == "Hercules")):
    return Heracles
  elif(hero == Odysseus):
    return Odysseus
  else:
    return None
