class Pokemon:
    def __init__(self,num,nom,niv,pv,att,defense,type,evol):
        self.num = num
        self.nom = nom
        self.pv = pv
        self.niv = niv
        self.att = att 
        self.defense = defense
        self.type = type
        self.evol = evol

    def get_en_vie(self):
        return self.pv > 0

    def attaquer(self, adversaire):
        degats = adversaire.subir_degats(self.att, self.type, adversaire.type)
        print(f"{self.nom} inflige {degats} points de dégâts à {adversaire.nom}.")

    def subir_degats(self, attaque_adversaire, type_attaquant, type_defenseur):
        multiplicateur_type = {
        'Eau': {'Feu': 2, 'Plante': 0.5, 'Terre': 0.5},
        'Feu': {'Eau': 0.5, 'Plante': 2, 'Terre': 0.5},
        'Plante': {'Eau': 2, 'Feu': 0.5, 'Terre': 2},
        'Terre': {'Eau': 2, 'Feu': 2, 'Plante': 0.5},
        'Insecte': {'Plante': 2, 'Feu': 0.5, 'Terre': 1},
        'Eclair': {'Eau': 2, 'Terre': 0.5, 'Vol': 2}
        }

        if type_attaquant in multiplicateur_type and type_defenseur in multiplicateur_type[type_attaquant]:
            multiplier = multiplicateur_type[type_attaquant][type_defenseur]
            degats = int((2 * self.niv / 5 + 2) * attaque_adversaire * multiplier / self.defense)
            self.pv = max(0, self.pv - degats)
            print(f"{self.nom} a maintenant {self.pv} points de vie.")
            return degats
