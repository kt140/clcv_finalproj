from gods import gods
from heroes import heroes

if __name__  == "__main__":
    terminal = ""
    print("\n\n\n\n")
    print("Welcome to CLCV 115 Greek Gods and Goddesses Database! \n")
    while(terminal != "EXIT"):
        print("How may I help you today?")
        print("Type 'Gods & Goddesses' or 'Heroes' to terminal. or 'EXIT' to cancel program")
        terminal = input("Enter: ")
        if((terminal == "Gods & Goddesses") | (terminal == "Gods") | (terminal == "Goddesses")):
            counter = 0
            while(counter == 0):
                additional = input("Enter God/Goddess Name: ")
                print("\nAccessing Gods & Goddesses...")
                access = gods(additional)
                if(access == None):
                    print("Invalid Entry, try again.")
                else:
                    additional = input("Access information: ")
                    print("\n\n\n")
                    if(additional == "name"):
                        print(access.getName())
                        counter = 1
                    elif(additional == "classification"):
                        print(access.getClass())
                        counter = 1
                    elif(additional == "parent"):
                        print(access.getParent())
                        counter = 1
                    elif(additional == "description"):
                        print(access.getDescrip())
                        counter = 1
                    elif(additional == "heroes"):
                        print(access.getHeroes())
                        counter = 1
                    elif(additional == "children"):
                        print(access.getChildren())
                        counter = 1
                    else:
                        print("Invalid statement, try again")
                    print("\n\n\n")


        elif (terminal == "Heroes"):
            print("\nAccessing Heroes...")
            counter = 0
            while(counter == 0):
                additional = input("Enter Hero's name: ")
                print("\nAccessing Heroes...")
                access = heroes(additional)
                if(access == None):
                    print("Invalid Entry, try again.")
                else:
                    additional = input("Access information: ")
                    print("\n\n\n")
                    if(additional == "name"):
                        print(access.getName())
                        counter = 1
                    elif(additional == "description"):
                        print(access.getDescrip())
                        counter = 1
                    elif(additional == "story"):
                        print(access.getStory())
                        counter = 1
                    elif(additional == "Gods"):
                        print(access.getGods)
                        counter = 1
                    else:
                        print("Invalid statement, try again")
                    print("\n\n\n")   
        elif (terminal == "EXIT"):
            print("We are done!")
        else:
            print("Invalid command, retry")
        