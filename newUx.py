class crossSection:
    def __init__(self, shape, area):
        self.shape = shape
        self.area = area

class pier:
    def __init__(self, index, label, height, shape, area):
        self.index = index
        self.label = label
        self.height = height
        self.cross_section = crossSection(shape, area)
        self.deck = None

class deck:
    def __init__(self, label, num_of_piers):
        self.label = label
        self.num_of_piers = num_of_piers
        self.piers = []

    def add_pier(self, pier):
        self.piers.append(pier)

class bridge:
    def __init__(self):
        self.label = input("Please input the \033[1m Bridge label \033[0m: ")
        self.length = input("Please input the length of the bridge: ")
        self.num_of_decks = int(input("Please input the number of decks the " + self.label + " bridge will have: "))
        self.num_of_piers = 0
        self.decks = []
        self.pierTypes = []
        self.run()

    def run(self):
        for i in range(self.num_of_decks):
            new_deck = self.deckCreator(i)
            for j in range(new_deck.num_of_piers):
                new_pier = self.pierCreator(j, new_deck, new_deck.label)
                new_deck.add_pier(new_pier)
            self.decks.append(new_deck)
        self.run2()
    
    def pierAssembly(self, new_deck):
        for j in range(new_deck.num_of_piers):
            new_pier = self.pierCreator(j, new_deck, new_deck.label)
            new_deck.add_pier(new_pier)
    
    def deckCreator(self, i):
        uses_pier_types = False
        label = input("Please input the \033[1m label \033[0m for \033[1m deck " + str(i+1) + "\033[0m: ")
        deck_num_of_piers = int(input("Please input the \033[1m number of piers \033[0m for \033[1m" + label + " deck\033[0m: "))
        self.num_of_piers += deck_num_of_piers
        new_deck = deck(label, deck_num_of_piers)
        return new_deck

    def pierCreator(self, j, new_deck, label):
        pier_label = input("Please input the \033[1m label \033[0m for \033[1m pier " + str(j+1) + "\033[0m  on \033[1m " + label + " deck \033[0m: ")
        pier_height = float(input("Please input the \033[1m height \033[0m for \033[1m pier " + str(j+1) + "\033[0m  on \033[1m " + label + " deck\033[0m: "))
        pier_shape = input("Please input the \033[1m shape \033[0m for \033[1m pier " + str(j+1) + "\033[0m on \033[1m " + label + " deck\033[0m: ")
        pier_area = float(input("Please input the \033[1m area \033[0m for \033[1m pier " + str(j+1) + " \033[0m on \033[1m " + label + " deck\033[0m: "))
        pier_index = self.num_of_piers
        new_pier = pier(pier_index, pier_label, pier_height, pier_shape, pier_area)
        new_pier.deck = new_deck
        return new_pier

    def pierTypeCreator(self):
        pierTypeLabel = input("Please input the \033[1m pier type label \033[0m: ")
        pierTypeHeight = float(input("Please input the \033[1m pier type height \033[0m: "))
        pierTypeShape = input("Please input the \033[1m pier type shape \033[0m: ")
        pierTypeArea = float(input("Please input the \033[1m pier type area \033[0m: "))
        new_pierType = pier(1, pierTypeLabel, pierTypeHeight, pierTypeShape, pierTypeArea)
        self.pierTypes.append(new_pierType)

    def printer(self, option):
        if option == "B":
            print("\n\nBridge: " + self.label)
            print("   Bridge length: " + self.length)
            print("   Number of decks: " + str(self.num_of_decks))
            for deck in self.decks:
                print("    ↳  Deck: " + deck.label)
                print("         ↳  Number of piers: " + str(deck.num_of_piers))
                for pier in deck.piers:
                    print("               ↳ Pier: " + pier.label)
                    print("                    ↳  Pier height: " + str(pier.height))
                    print("                    ↳  Pier shape: " + pier.cross_section.shape)
                    print("                    ↳  Pier area: " + str(pier.cross_section.area))
        elif option == "D":
            print("what deck do you want to find info about?")
            #print a list of decks with an index so that the user can select the index
            for i in range(len(self.decks)):
                print(str(i+1) + ". " + self.decks[i].label)
            deck_label = input("Please input the \033[1m label \033[0m for the \033[1m deck \033[0m: ")
            for deck in self.decks:
                if deck.label == deck_label:
                    print("Deck: " + deck.label)
                    print("   ↳  Number of piers: " + str(deck.num_of_piers))
                    for pier in deck.piers:
                        print("         ↳ Pier: " + pier.label)
                        print("              ↳  Pier height: " + str(pier.height))
                        print("              ↳  Pier shape: " + pier.cross_section.shape)
                        print("              ↳  Pier area: " + str(pier.cross_section.area))
        elif option == "P":
            for deck in self.decks:
                for pier in deck.piers:
                    print(pier.label)
            pier_label = input("Please input the \033[1m label \033[0m for the \033[1m pier \033[0m: ")
            for deck in self.decks:
                for pier in deck.piers:
                    if pier.label == pier_label:
                        print("Pier: " + pier.label + " on deck " + deck.label)
                        print("   ↳  Pier height: " + str(pier.height))
                        print("   ↳  Pier shape: " + pier.cross_section.shape)
                        print("   ↳  Pier area: " + str(pier.cross_section.area))
    
    def numOfDecksChanger(self):
        tmp_num_of_decks = self.num_of_decks
        self.num_of_decks = int(input(f"Number of decks was: {self.num_of_decks}, please input a new number of decks: "))
        if self.num_of_decks > tmp_num_of_decks:
            for i in range(tmp_num_of_decks, self.num_of_decks):
                new_deck = self.deckCreator(i)
                for j in range(new_deck.num_of_piers):
                    new_pier = self.pierCreator(j, new_deck, new_deck.label)
                    new_deck.add_pier(new_pier)
                self.decks.append(new_deck)
                print(f"Number of decks changed from {tmp_num_of_decks} to {self.num_of_decks}")
        elif self.num_of_decks < tmp_num_of_decks:
            for deck in self.decks:
                print(deck.label)
            deck_to_remove = input("What deck do you want to remove? ")
            for deck in self.decks:
                if deck.label == deck_to_remove:
                    self.decks.remove(deck)
                
                print(f"Number of decks changed from {tmp_num_of_decks} to {self.num_of_decks}")
        else:
            print("Number of decks unchanged")

    def bridgeEditor(self):
        print("The following options are available to edit. Please select the option you want to edit.")
        bridge_option = input(f"1  Bridge label: {self.label}\n2  Bridge length: {self.length}\n3  Bridge number of decks: {self.num_of_decks}\nOption to edit: ")
        if bridge_option == "1":
            tmp_label = self.label
            self.label = input(f"Bridge Label was: {self.label}, please input a new label: ")
            print(f"Bridge label changed from {tmp_label} to {self.label}")
        elif bridge_option == "2":
            tmp_length = self.length
            self.length = input(f"Bridge Length was: {self.length}, please input a new length: ")
            print(f"Bridge length changed from {tmp_length} to {self.length}")
        elif bridge_option == "3":
            self.numOfDecksChanger()
        else:
            print("Invalid option")
    
    def numOfPiersChanger(self, tmp_num_of_piers, deck):
        tmp_num_of_piers = deck.num_of_piers
        deck.num_of_piers = int(input(f"Deck Number of piers was: {deck.num_of_piers}, please input the new number of piers: "))
        if deck.num_of_piers > tmp_num_of_piers:
            for i in range(deck.num_of_piers - tmp_num_of_piers):
                new_pier = self.pierCreator(i,  deck.label, deck.label)
                deck.add_pier(new_pier)
        elif deck.num_of_piers < tmp_num_of_piers:
            for pier in deck.piers:
                print(pier.label)
            pierToRemove = input("Which pier do you want to remove? ")
            for pier in deck.piers:
                if pier.label == pierToRemove:
                    deck.piers.remove(pier)
        print(f"Deck number of piers changed from {tmp_num_of_piers} to {deck.num_of_piers}")

    def deckEditor(self):
        print("The current decks available to edit are:")
        for deck in self.decks:
            print(deck.label)
        deck_label = input("Please input the label for the deck to edit info about: ")
        for deck in self.decks:
            if deck.label == deck_label:
                print("The following options are available to edit. Please select the option you want to edit.")
                deck_option = input(f"1  Deck label: {deck.label}\n2  Deck number of piers: {deck.num_of_piers}\nOption to edit: ")
                if deck_option == "1":
                    tmp_label = deck.label
                    deck.label = input(f"Deck Label was: {deck.label}, please input a new label: ")
                    print(f"Deck label changed from {tmp_label} to {deck.label}")
                elif deck_option == "2":
                    tmp_num_of_piers = deck.num_of_piers
                    confirmation = input("To alter the number of piers, either a new pier must be added or an existing pier must be deleted.\nDo you wish to proceed? (Y/N) ")
                    if confirmation == "Y":
                        self.numOfPiersChanger(tmp_num_of_piers, deck)
                    else:
                        print("Deck number of piers unchanged")
                else:
                    print("Invalid option")

    def pierTypeApplicator(self, pier):
        print("The following pier types are available:")
        for pier_type in self.pier_types:
            print(pier_type.label)
        pier_type_label = input("Please input the label for the pier type to apply: ")
        for pier_type in self.pier_types:
            if pier_type.label == pier_type_label:
                pier.cross_section = pier_type.cross_section
                print(f"Pier type applied to pier {pier.label}")
    
    def pierEditor(self):
        print("The current Piers available to edit are:")
        for deck in self.decks:
            for pier in deck.piers:
                print(pier.label)
        pier_label = input("Please input the label for the pier to edit info about: ")
        for deck in self.decks:
            for pier in deck.piers:
                if pier.label == pier_label:
                    print("The following options are available to edit. Please select the option you want to edit.")
                    pier_option = input(f"1  Pier label: {pier.label}\n2  Pier height: {pier.height}\n3  Pier shape: {pier.cross_section.shape}\n4  Pier area: {pier.cross_section.area}\n5 Apply Pier type.\nOption to edit: ")
                    if pier_option == "1":
                        tmp_label = pier.label
                        pier.label = input(f"Pier Label was: {pier.label}, please input a new label: ")
                        print(f"Pier label changed from {tmp_label} to {pier.label}")
                    elif pier_option == "2":
                        tmp_height = pier.height
                        pier.height = input(f"Pier height was: {pier.height}, please input a new height: ")
                        print(f"Pier height changed from {tmp_height} to {pier.height}")
                    elif pier_option == "3":
                        tmp_shape = pier.cross_section.shape
                        pier.cross_section.shape = input(f"Pier shape was: {pier.cross_section.shape}, please input a new shape: ")
                        print(f"Pier width changed from {tmp_shape} to {pier.cross_section.shape}")
                    elif pier_option == "4":
                        tmp_area = pier.cross_section.area
                        pier.cross_section.area = input(f"Pier area was: {pier.cross_section.area}, please input a new area: ")
                        print(f"Pier area changed from {tmp_area} to {pier.cross_section.area}")
                    elif pier_option == "5":
                        if len(self.pierTypes) == 0:
                            print("No pier types available to apply, please create a pier type first.")
                            self.pierTypeCreator()
                            pass
                        if len(self.pierTypes) > 0:
                            print("The current pier types available to apply are:")
                            for pierType in self.pierTypes:
                                print(pierType.label)
                            pierType_label = input("Please input the label for the pier type to apply: ")
                            for pierType in self.pierTypes:
                                if pierType.label == pierType_label:
                                    pier.height = pierType.height
                                    pier.cross_section.shape = pierType.cross_section.shape
                                    pier.cross_section.area = pierType.cross_section.area
                                    print(f"Pier type applied: {pierType.label}")

                    else:
                        print("Invalid option")

    def editorCaller(self, data_to_edit):
        if data_to_edit == "B":
            self.bridgeEditor()
        elif data_to_edit == "D":
            self.deckEditor()
        elif data_to_edit == "P":
            self.pierEditor()

    def run2(self):
        while True:
            option = input("\n\nFind info about (B)ridge, (D)eck, (P)ier, (E)dit current info, (S)ave and exit: ")
            if option == "B" or option == "D" or option == "P":
                self.printer(option)
            elif option == "E":
                data_to_edit = input("What data do you want to edit? Press (B) for bridge, (D) for deck or (P) for pier -> ")
                self.editorCaller(data_to_edit)
            elif option == "S":
                exit()
            else:
                print("Please input a valid option")

def main():
    bridge()

if __name__ == "__main__":
    main()