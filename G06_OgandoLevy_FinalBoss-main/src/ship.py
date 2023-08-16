class Ship:
    def __init__(self, draft, crew):
        self.crew = crew
        self.draft = (1.5 * self.crew) + draft

    def is_worth_it(self):
        try:
            peso = self.draft - (self.crew * 1.5)
            if peso < 20:
                    raise TypeError("No merece ser  saqueado")
                    return 1
            else:
                print("Merece ser saqueado")
                return 2
        except TypeError as error:
                  print(error)