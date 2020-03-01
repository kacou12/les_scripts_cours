class MaClasse:
    def __init__(self):
        self.x=23
        self.y=self.x+5
    
    def affiche(self):
        z=42
        print("y = ",self.y,"z=", z)
    
terminale = MaClasse()
terminale.affiche()