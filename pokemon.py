class Pokemon:

    def __init__(self,num,nom,niv,pv,att,défense,type,évol,image=None):
        self.num = num
        self.nom = nom
        self.pv = pv
        self.niv = niv
        self.att = att 
        self.défense = défense
        self.type = type
        self.évol = évol
        self.pv_max = pv

    def gagner_xp(self, quantite):
        self.xp += quantite

    def __str__(self):
        return self.nom

    def afficher_details(self):
        print("votre pokémon est:",self.nom)
        print("il est de type",self.type,"et à un niveau de:",self.niv)

    def get_en_vie(self):
        return self.pv > 0
    
    def set_full_life(self):
        self.pv_max = self.pv_max
