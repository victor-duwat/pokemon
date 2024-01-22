import random
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

    def __str__(self):
        return self.nom

    def afficher_details(self):
        print("votre pokémon est:",self.nom)
        print("il est de type",self.type,"et à un niveau de:",self.niv)

    def get_en_vie(self):
        return self.pv > 0
    
    def set_full_life(self):
        self.pv_max = self.pv_max

class Pokedex:
    liste_starter = [
        Pokemon(4, "Salamèche", 1, 39, 502, 43, "Feu", 1),
        Pokemon(1, "Bulbizarre", 1, 45, 49, 49, "Plante", 1),
        Pokemon(7, "Carapuce", 1, 44, 48, 65, "Eau", 1),
    ]

    def __init__(self):
        self.pokemons = []
        self.équipe_pokemon = []

    def ajouter_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def ajouter_plusieurs_pokemons(self, liste_pokemons):
        self.pokemons.extend(liste_pokemons)

    def afficher_pokedex(self):
        for pokemon in self.pokemons:
            pokemon.afficher_details()


    def afficher_équipe(self):
        print("votre équipe est composé de:",self.équipe_pokemon)

    def choisir_starter(self):
        print("Choisissez un Pokémon:")
        for i, starter in enumerate(self.liste_starter, start=1):
            print(f"{i}. {starter.nom}")

        choix_utilisateur = input("Entrez le numéro du Pokémon choisi: ")

        try:
            index_choisi = int(choix_utilisateur) - 1
            pokemon_choisi = self.liste_starter[index_choisi]
        except (ValueError, IndexError):
            print("Choix invalide. Veuillez choisir un numéro de 1 à 3.")
            return self.choisir_starter()

        print(f"Vous avez choisi {pokemon_choisi.nom}")
        self.équipe_pokemon.append(pokemon_choisi)
        return pokemon_choisi


pokedex = Pokedex()

def pokemon_aleatoire():
    liste_151_pokemons = [
        Pokemon(1,"Bulbizarre",1,45,49,49,"Plante",1),
        Pokemon(2,"Herbizarre",1,60,62,63,"Plante",2),
        Pokemon(3,"Florizarre",1,80,82,83,"Plante",3),
        Pokemon(4,"Salamèche",1,39,52,43,"Feu",1),
        Pokemon(5,"Reptincel",1,58,64,58,"Feu",2),
        Pokemon(6,"Dracofeu",1,78,84,78,"Feu",3),
        Pokemon(7,"Carapuce",1,44,48,65,"Eau",1),
        Pokemon(8,"Carabaffe",1,59,63,80,"Eau",2),
        Pokemon(9,"Tortank",1,79,83,100,"Eau",3),
        Pokemon(10,"Chenipan",1,45,30,35,"Insecte",1),
        Pokemon(11,"Chrysacier",1,50,20,55,"Insecte",2),
        Pokemon(12,"Papillusion",1,60,45,50,"Insecte",3),
        Pokemon(13,"Aspicot",1,40,35,30,"Insecte",1),
        Pokemon(14,"Coconfort",1,45,25,50,"Insecte",2),
        Pokemon(15,"Dardargnan",1,65,80,40,"Insecte",3),
        Pokemon(16,"Roucool",1,40,45,40,"Vol",1),
        Pokemon(17,"Roucoups",1,63,60,55,"Vol",2),
        Pokemon(18,"Roucarnage",1,83,80,75,"Vol",3),
        Pokemon(19,"Rattata",1,30,56,35,"Normal",1),
        Pokemon(20,"Rattatac",1,55,81,60,"Normal",2),
        Pokemon(21,"Piafabec",1,40,60,30,"Vol",1),
        Pokemon(22,"Rapasdeîc",1,65,90,65,"Vol",2),
        Pokemon(23,"Abo",1,35,60,44,"Poison",1),
        Pokemon(24,"Arbok",1,60,85,69,"Poison",2),
        Pokemon(25,"Pikachu",1,35,55,30,"Electrique",1),
        Pokemon(26,"Raichu",1,60,90,55,"Electrique",2),
        Pokemon(27,"Sabelette",1,50,75,85,"Sol",1),
        Pokemon(28,"Sablaireau",1,75,100,110,"Sol",2),
        Pokemon(29,"Nidorane",1,55,47,52,"Poison",1),
        Pokemon(30,"Nidorina",1,70,62,67,"Poison",2),
        Pokemon(31,"Nidoqueen",1,90,82,87,"Poison",3),
        Pokemon(32,"Nidoran",1,46,57,40,"Poison",1),
        Pokemon(33,"Nidorino",1,61,72,57,"Poison",2),
        Pokemon(34,"Nidoking",1,81,92,77,"Poison",3),
        Pokemon(35,"Mélofée",1,70,45,48,"Fée",1),
        Pokemon(36,"Mélodelfe",1,95,70,73,"Fée",2),
        Pokemon(37,"Goupix",1,38,41,40,"Feu",1),
        Pokemon(38,"Feunard",1,73,76,75,"Feu",2),
        Pokemon(39,"Rondoudou",1,115,45,20,"Fée",1),
        Pokemon(40,"Grodoudou",1,140,70,45,"Fée",2),
        Pokemon(41,"Nosferapti",1,40,45,35,"Poison",1),
        Pokemon(42,"Nosferalto",1,75,80,70,"Poison",2),
        Pokemon(43,"Mystherbe",1,45,50,55,"Plante",1),
        Pokemon(44,"Ortide",1,60,65,70,"Poison",2),
        Pokemon(45,"Rafflesia",1,75,80,85,"Poison",3),
        Pokemon(46,"Paras",1,35,70,55,"Poison",1),
        Pokemon(47,"Parasect",1,60,95,80,"Poison",2),
        Pokemon(48,"Mimitoss",1,60,55,50,"Poison",1),
        Pokemon(49,"Aéromite",1,70,65,60,"Poison",2),
        Pokemon(50,"Taupiqueur",1,10,55,25,"Sol",1),
        Pokemon(51,"Tropikeur",1,35,80,50,"Sol",2),
        Pokemon(52,"Miaouss",1,40,45,35,"Normal",1),
        Pokemon(53,"Persian",1,65,70,60,"Normal",2),
        Pokemon(54,"Psykokwak",1,50,52,48,"Eau",1),
        Pokemon(55,"Akwakwak",1,80,82,78,"Eau",2),
        Pokemon(56,"Féronsinge",1,40,80,35,"Combat",1),
        Pokemon(57,"Colossinge",1,65,105,60,"Combat",2),
        Pokemon(58,"Caninos",1,55,70,45,"Feu",1),
        Pokemon(59,"Arcanin",1,90,110,80,"Feu",2),
        Pokemon(60,"Ptitard",1,40,50,40,"Eau",1),
        Pokemon(61,"Têtarte",1,65,65,65,"Eau",2),
        Pokemon(62,"Tartard",1,90,85,92,"Eau",3),
        Pokemon(63,"Abra",1,25,20,15,"Psy",1),
        Pokemon(64,"Kadabra",1,40,35,30,"Psy",2),
        Pokemon(65,"Alakazam",1,55,50,45,"Psy",3),
        Pokemon(66,"Machoc",1,70,80,50,"Combat",1),
        Pokemon(67,"Machopeur",1,90,80,100,"Combat",2),
        Pokemon(68,"Mackogneur",1,90,130,80,"Combat",3),
        Pokemon(69,"Chétiflor",1,50,75,35,"Plante",1),
        Pokemon(70,"Boustiflor",1,65,90,50,"PLante",2),
        Pokemon(71,"Empiflor",1,80,105,65,"Plante",3),
        Pokemon(72,"Tentacool",1,40,40,35,"Eau",1),
        Pokemon(73,"Tentacruel",1,80,70,65,"Eau",2),
        Pokemon(74,"Racaillou",1,40,80,100,"Sol",1),
        Pokemon(75,"Gravalanche",1,55,95,115,"Sol",2),
        Pokemon(76,"Grolem",1,80,110,130,"Sol",3),
        Pokemon(77,"Ponyta",1,50,85,55,"Feu",1),
        Pokemon(78,"Galopa",1,65,100,70,"Feu",2),
        Pokemon(79,"Ramoloss",1,90,65,65,"Eau",1),
        Pokemon(80,"Flagadoss",1,95,75,110,"Eau",2),
        Pokemon(81,"Magnéti",1,25,35,70,"Electrique",1),
        Pokemon(82,"Magnéton",1,50,60,95,"Electique",2),
        Pokemon(83,"Canarticho",1,65,55,60,"Normal",1),
        Pokemon(84,"Doduo",1,35,85,45,"Normal",1),
        Pokemon(85,"Dodrio",1,60,110,70,"Normal",2),
        Pokemon(86,"Otaria",1,65,45,55,"Eau",1),
        Pokemon(87,"Lamantine",1,90,70,80,"Eau",2),
        Pokemon(88,"Tadmorv",1,80,80,50,"Poison",1),
        Pokemon(89,"Grotadmorv",1,105,105,75,"Poison",2),
        Pokemon(90,"Kokyas",1,30,65,100,"Eau",1),
        Pokemon(91,"Crustabri",1,50,95,180,"Eau",2),
        Pokemon(92,"Fantominus",1,30,35,30,"Spectre",1),
        Pokemon(93,"Spectrum",1,45,50,45,"Spectre",2),
        Pokemon(94,"Ectoplasma",1,60,65,60,"Spectre",3),
        Pokemon(95,"Onix",1,35,45,160,"Normal",1),
        Pokemon(96,"Soporifik",1,60,48,45,"Psy",1),
        Pokemon(97,"Hypnomade",1,85,73,70,"Psy",2),
        Pokemon(98,"Krabby",1,30,105,90,"Eau",1),
        Pokemon(99,"Krabboss",1,55,130,115,"Eau",2),
        Pokemon(100,"Voltorbe",1,40,30,50,"Electrique",1),
        Pokemon(101,"Electrode",1,60,50,70,"Electrique",2),
        Pokemon(102,"noeunoeuf",1,60,40,80,"Plante",1),
        Pokemon(103,"Noadkoko",1,95,95,85,"Plante",2),
        Pokemon(104,"Osselait",1,60,80,110,"Sol",1),
        Pokemon(105,"Ossatueur",1,60,80,110,"Sol",2),
        Pokemon(106,"Kicklee",1,50,120,53,"Combat",1),
        Pokemon(107,"Tygnon",1,50,105,79,"Combat",1),
        Pokemon(108,"Excelangue",1,90,55,75,"Normal",1),
        Pokemon(109,"Smogo",1,40,65,95,"Poison",1),
        Pokemon(110,"Smogogo",1,65,90,120,"Poison",2),
        Pokemon(111,"Rhinocorone",1,80,85,95,"Sol",1),
        Pokemon(112,"Rhinoféros",1,105,130,120,"Sol",2),
        Pokemon(113,"Leveinard",1,250,5,5,"Normal",1),
        Pokemon(114,"Saquedeneu",1,65,55,115,"Normal",1),
        Pokemon(115,"Kangourex",1,105,95,80,"Sol",1),
        Pokemon(116,"Hypotrempe",1,30,40,70,"Eau",1),
        Pokemon(117,"Hypocéan",1,30,40,70,"Eau",2),
        Pokemon(118,"Poissirène",1,45,67,60,"Eau",1),
        Pokemon(119,"Poissoroy",1,80,92,65,"Eau",2),
        Pokemon(120,"Star",1,30,45,55,"Eau",1),
        Pokemon(121,"Starros",1,60,75,85,"Eau",2),
        Pokemon(122,"M.Mime",1,40,45,65,"Normal",1),
        Pokemon(123,"Insécateur",1,70,110,80,"Insecte",1),
        Pokemon(124,"Lippoutou",1,65,50,32,"Psy",1),
        Pokemon(125,"Elektek",1,65,83,57,"Electrique",1),
        Pokemon(126,"Magmar",1,65,95,57,"Feu",1),
        Pokemon(127,"Scarabrute",1,65,125,100,"Insecte",1),
        Pokemon(128,"Tauros",1,75,100,95,"Normal",1),
        Pokemon(129,"Magicarpe",1,20,10,55,"Eau",1),
        Pokemon(130,"Léviator",1,145,89,91,"Eau",2),
        Pokemon(131,"Lokhlass",1,130,85,80,"Eau",1),
        Pokemon(132,"Métamorphe",1,48,48,48,"Normal",1),
        Pokemon(133,"Evoli",1,55,55,50,"Normal",1),
        Pokemon(134,"Aquali",1,130,65,60,"Eau",2),
        Pokemon(135,"Voltali",1,65,65,60,"Electrique",2),
        Pokemon(136,"Pyroli",1,65,130,60,"Feu",2),
        Pokemon(137,"Porygon",1,65,65,70,"Normal",1),
        Pokemon(138,"Amonita",1,35,40,100,"Eau",1),
        Pokemon(139,"Armonistar",1,70,60,125,"Eau",2),
        Pokemon(140,"Kabuto",1,30,80,90,"Eau",1),
        Pokemon(141,"Kabutops",1,60,115,105,"Sol",2),
        Pokemon(142,"Ptéra",1,80,105,65,"Vol",1),
        Pokemon(143,"Ronflex",1,160,110,65,"Normal",1),
        Pokemon(144,"Artikodin",1,120,120,140,"Eau",1),
        Pokemon(145,"Elechtor",1,130,130,125,"Electrique",1),
        Pokemon(146,"sulfura",1,130,140,150,"Feu",1),
        Pokemon(147,"Minidraco",1,41,64,45,"Dragon",1),
        Pokemon(148,"Draco",1,61,84,65,"Dragon",2),
        Pokemon(149,"Dracolosse",1,120,134,95,"Dragon",3),
        Pokemon(150,"Mewtwo",1,150,150,150,"Psy",1),
        Pokemon(151,"Mew",1,100,100,100,"Psy",1)
        ]
    pokemon_choisi=random.choice(liste_151_pokemons)
    return pokemon_choisi


liste_equipe =[
    
]
