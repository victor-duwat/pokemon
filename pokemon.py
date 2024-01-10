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
        self.pv_max = pv

    def get_en_vie(self):
        return self.pv > 0
    
    def set_full_life(self, pv_max):
        self.pv_max = self.pv

