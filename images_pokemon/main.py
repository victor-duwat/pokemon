import pygame

# Classe Pokemon et liste_151_pokemons
class Pokemon:
    def __init__(self, numero, nom, niveau, pv, attaque, defense, type, evolue):
        self.numero = numero
        self.nom = nom
        self.niveau = niveau
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.type = type
        self.evolue = evolue

liste_151_pokemons = [
    Pokemon(1,"Bulbizarre",1,45,49,49,"Plante",1),
    Pokemon(2,"Herbizarre",1,60,62,63,"Plante",2),
    Pokemon(3,"Florizarre",1,80,82,83,"Plante",3),
    Pokemon(4,"Salamèche",1,39,52,43,"Feu",1),
    Pokemon(5,"Reptincel",1,58,64,58,"Feu",2),
    Pokemon(6,"Dracaufeu",1,78,84,78,"Feu",3),
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

# Initialisation de Pygame
pygame.init()
LARGEUR = 800
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Pokémon")

# Chargement de l'image des pokemons
bulbizarre_image = pygame.image.load("bulbizarre.png").convert_alpha()
herbizarre_image = pygame.image.load("herbizarre.png").convert_alpha()
florizarre_image = pygame.image.load("florizarre.png").convert_alpha()
salameche_image = pygame.image.load("salameche.png").convert_alpha()
reptincel_image = pygame.image.load("reptincel.png").convert_alpha()
dracaufeu_image = pygame.image.load("dracaufeu.png").convert_alpha()
carapuce_image = pygame.image.load("carapuce.png").convert_alpha()
carabaffe_image = pygame.image.load("carabaffe.png").convert_alpha()
tortank_image = pygame.image.load("tortank.png").convert_alpha()
chenipan_image = pygame.image.load("chenipan.png").convert_alpha()
chrysacier_image = pygame.image.load("chrysacier.png").convert_alpha()
papillusion_image = pygame.image.load("papillusion.png").convert_alpha()
aspicot_image = pygame.image.load("aspicot.png").convert_alpha()
coconfort_image = pygame.image.load("coconfort.png").convert_alpha()
dardargnan_image = pygame.image.load("dardargnan.png").convert_alpha()
roucool_image = pygame.image.load("roucool.png").convert_alpha()
roucoups_image = pygame.image.load("roucoups.png").convert_alpha()
roucarnage_image = pygame.image.load("roucarnage.png").convert_alpha()
rattata_image = pygame.image.load("rattata.png").convert_alpha()
rattatac_image = pygame.image.load("rattatac.png").convert_alpha()
piafabec_image = pygame.image.load("piafabec.png").convert_alpha()
piafabec_image = pygame.image.load("piafabec.png").convert_alpha()
rapasdeic_image = pygame.image.load("rapasdeic.png").convert_alpha()
abo_image = pygame.image.load("abo.png").convert_alpha()
arbok_image = pygame.image.load("arbok.png").convert_alpha()
pikachu_image = pygame.image.load("pikachu.png").convert_alpha()
raichu_image = pygame.image.load("raichu.png").convert_alpha()
sabelette_image = pygame.image.load("sabelette.png").convert_alpha()
sablaireau_image = pygame.image.load("sablaireau.png").convert_alpha()
nidorane_image = pygame.image.load("nidorane.png").convert_alpha()
nidorina_image = pygame.image.load("nidorina.png").convert_alpha()
nidoqueen_image = pygame.image.load("nidoqueen.png").convert_alpha()
nidoran_image = pygame.image.load("nidoran.png").convert_alpha()
nidorino_image = pygame.image.load("nidorino.png").convert_alpha()
nidoking_image = pygame.image.load("nidoking.png").convert_alpha()
melofee_image = pygame.image.load("melofee.png").convert_alpha()
melodelfe_image = pygame.image.load("melodelfe.png").convert_alpha()
goupix_image = pygame.image.load("goupix.png").convert_alpha()
feunard_image = pygame.image.load("feunard.png").convert_alpha()
rondoudou_image = pygame.image.load("rondoudou.png").convert_alpha()
grodoudou_image = pygame.image.load("grodoudou.png").convert_alpha()
nosferapti_image = pygame.image.load("nosferapti.png").convert_alpha()
nosferalto_image = pygame.image.load("nosferalto.png").convert_alpha()
mystherbe_image = pygame.image.load("mystherbe.png").convert_alpha()
ortide_image = pygame.image.load("ortide.png").convert_alpha()
rafflesia_image = pygame.image.load("rafflesia.png").convert_alpha()
paras_image = pygame.image.load("paras.png").convert_alpha()
parasect_image = pygame.image.load("parasect.png").convert_alpha()
mimitoss_image = pygame.image.load("mimitoss.png").convert_alpha()
aeromite_image = pygame.image.load("aeromite.png").convert_alpha()
taupiqueur_image = pygame.image.load("taupiqueur.png").convert_alpha()
tropikeur_image = pygame.image.load("tropikeur.png").convert_alpha()
miaouss_image = pygame.image.load("miaouss.png").convert_alpha()
persian_image = pygame.image.load("persian.png").convert_alpha()
psykokwak_image = pygame.image.load("psykokwak.png").convert_alpha()
akwakwak_image = pygame.image.load("akwakwak.png").convert_alpha()
ferosinge_image = pygame.image.load("ferosinge.png").convert_alpha()
colossinge_image = pygame.image.load("colossinge.png").convert_alpha()
caninos_image = pygame.image.load("caninos.png").convert_alpha()
arcanin_image = pygame.image.load("arcanin.png").convert_alpha()
ptitard_image = pygame.image.load("ptitard.png").convert_alpha()
tetarte_image = pygame.image.load("tetarte.png").convert_alpha()
tartard_image = pygame.image.load("tartard.png").convert_alpha()
abra_image = pygame.image.load("abra.png").convert_alpha()
kadabra_image = pygame.image.load("kadabra.png").convert_alpha()
alakazam_image = pygame.image.load("alakazam.png").convert_alpha()
machoc_image = pygame.image.load("machoc.png").convert_alpha()
machopeur_image = pygame.image.load("machopeur.png").convert_alpha()
mackogneur_image = pygame.image.load("mackogneur.png").convert_alpha()
chetiflor_image = pygame.image.load("chetiflor.png").convert_alpha()
boustiflor_image = pygame.image.load("boustiflor.png").convert_alpha()
empiflor_image = pygame.image.load("empiflor.png").convert_alpha()
tentacool_image = pygame.image.load("tentacool.png").convert_alpha()
tentacruel_image = pygame.image.load("tentacruel.png").convert_alpha()
racaillou_image = pygame.image.load("racaillou.png").convert_alpha()
gravalanche_image = pygame.image.load("gravalanche.png").convert_alpha()
grolem_image = pygame.image.load("grolem.png").convert_alpha()
ponyta_image = pygame.image.load("ponyta.png").convert_alpha()
galopa_image = pygame.image.load("galopa.png").convert_alpha()
ramoloss_image = pygame.image.load("ramoloss.png").convert_alpha()
flagadoss_image = pygame.image.load("flagadoss.png").convert_alpha()
magneti_image = pygame.image.load("magneti.png").convert_alpha()
magneton_image = pygame.image.load("magneton.png").convert_alpha()
canarticho_image = pygame.image.load("canarticho.png").convert_alpha()
doduo_image = pygame.image.load("doduo.png").convert_alpha()
dodrio_image = pygame.image.load("dodrio.png").convert_alpha()
otaria_image = pygame.image.load("otaria.png").convert_alpha()
lamantine_image = pygame.image.load("lamantine.png").convert_alpha()
tadmorv_image = pygame.image.load("tadmorv.png").convert_alpha()
grotadmorv_image = pygame.image.load("grotadmorv.png").convert_alpha()
kokyas_image = pygame.image.load("kokyas.png").convert_alpha()
crustabri_image = pygame.image.load("crustabri.png").convert_alpha()
fantominus_image = pygame.image.load("fantominus.png").convert_alpha()
spectrum_image = pygame.image.load("spectrum.png").convert_alpha()
ectoplasma_image = pygame.image.load("ectoplasma.png").convert_alpha()
onix_image = pygame.image.load("onix.png").convert_alpha()
soporifik_image = pygame.image.load("soporifik.png").convert_alpha()
hypnomade_image = pygame.image.load("hypnomade.png").convert_alpha()
krabby_image = pygame.image.load("krabby.png").convert_alpha()
voltorbe_image = pygame.image.load("voltorbe.png").convert_alpha()
electrode_image = pygame.image.load("electrode.png").convert_alpha()
noeufnoeuf_image = pygame.image.load("noeufnoeuf.png").convert_alpha()
noadkoko_image = pygame.image.load("noadkoko.png").convert_alpha()
osselait_image = pygame.image.load("osselait.png").convert_alpha()
ossatueur_image = pygame.image.load("ossatueur.png").convert_alpha()
kicklee_image = pygame.image.load("kicklee.png").convert_alpha()
tygnon_image = pygame.image.load("tygnon.png").convert_alpha()
excelangue_image = pygame.image.load("excelangue.png").convert_alpha()
smogo_image = pygame.image.load("smogo.png").convert_alpha()
smogogo_image = pygame.image.load("smogogo.png").convert_alpha()
rhinocorone_image = pygame.image.load("rhinocorone.png").convert_alpha()
rhinoferos_image = pygame.image.load("rhinoferos.png").convert_alpha()
leveinard_image = pygame.image.load("leveinard.png").convert_alpha()
saquedeneu_image = pygame.image.load("saquedeneu.png").convert_alpha()
kangourex_image = pygame.image.load("kangourex.png").convert_alpha()
hypotrempe_image = pygame.image.load("hypotrempe.png").convert_alpha()
hypocean_image = pygame.image.load("hypocean.png").convert_alpha()
poissirene_image = pygame.image.load("poissirene.png").convert_alpha()
poissoroy_image = pygame.image.load("poissoroy.png").convert_alpha()
star_image = pygame.image.load("star.png").convert_alpha()
starros_image = pygame.image.load("starros.png").convert_alpha()
mmime_image = pygame.image.load("mmime.png").convert_alpha()
insecateur_image = pygame.image.load("insecateur.png").convert_alpha()
lippoutou_image = pygame.image.load("lippoutou.png").convert_alpha()
elektek_image = pygame.image.load("elektek.png").convert_alpha()
magmar_image = pygame.image.load("magmar.png").convert_alpha()
scarabrute_image = pygame.image.load("scarabrute.png").convert_alpha()
tauros_image = pygame.image.load("tauros.png").convert_alpha()
magicarpe_image = pygame.image.load("magicarpe.png").convert_alpha()
leviator_image = pygame.image.load("leviator.png").convert_alpha()
lokhlass_image = pygame.image.load("lokhlass.png").convert_alpha()
metamorphe_image = pygame.image.load("metamorphe.png").convert_alpha()
evoli_image = pygame.image.load("evoli.png").convert_alpha()
aquali_image = pygame.image.load("aquali.png").convert_alpha()
voltali_image = pygame.image.load("voltali.png").convert_alpha()
pyroli_image = pygame.image.load("pyroli.png").convert_alpha()
porygon_image = pygame.image.load("porygon.png").convert_alpha()
amonita_image = pygame.image.load("amonita.png").convert_alpha()
armonistar_image = pygame.image.load("armonistar.png").convert_alpha()
kabuto_image = pygame.image.load("kabuto.png").convert_alpha()
kabutops_image = pygame.image.load("kabutops.png").convert_alpha()
ptera_image = pygame.image.load("ptera.png").convert_alpha()
ronflex_image = pygame.image.load("ronflex.png").convert_alpha()
artikodin_image = pygame.image.load("artikodin.png").convert_alpha()
elechtor_image = pygame.image.load("elechtor.png").convert_alpha()
sulfura_image = pygame.image.load("sulfura.png").convert_alpha()
minidraco_image = pygame.image.load("minidraco.png").convert_alpha()
draco_image = pygame.image.load("draco.png").convert_alpha()
dracolosse_image = pygame.image.load("dracolosse.png").convert_alpha()
mewtwo_image = pygame.image.load("mewtwo.png").convert_alpha()



# Associer l'image à Bulbizarre dans un dictionnaire
images_pokemons = {}
for pokemon in liste_151_pokemons:
    if pokemon.nom == "Bulbizarre":
        images_pokemons[pokemon.nom] = bulbizarre_image
    if pokemon.nom == "Herbizarre":
        images_pokemons[pokemon.nom] = herbizarre_image
    if pokemon.nom == "Florizarre":
        images_pokemons[pokemon.nom] = florizarre_image
    if pokemon.nom == "Salamèche":
        images_pokemons[pokemon.nom] = salameche_image
    if pokemon.nom == "Reptincel":
        images_pokemons[pokemon.nom] = reptincel_image
    if pokemon.nom == "Dracaufeu":
        images_pokemons[pokemon.nom] = dracaufeu_image
    if pokemon.nom == "Carapuce":
        images_pokemons[pokemon.nom] = carapuce_image
    if pokemon.nom == "Carabaffe":
        images_pokemons[pokemon.nom] = carabaffe_image    
    if pokemon.nom == "Tortank":
        images_pokemons[pokemon.nom] = tortank_image
    if pokemon.nom == "Chenipan":
        images_pokemons[pokemon.nom] = chenipan_image  
    if pokemon.nom == "Chrysacier":
        images_pokemons[pokemon.nom] = chrysacier_image
    if pokemon.nom == "Papillusion":
        images_pokemons[pokemon.nom] = papillusion_image  
    if pokemon.nom == "Aspicot":
        images_pokemons[pokemon.nom] = aspicot_image
    if pokemon.nom == "Coconfort":
        images_pokemons[pokemon.nom] = coconfort_image
    if pokemon.nom == "Dardargnan":
        images_pokemons[pokemon.nom] = dardargnan_image
    if pokemon.nom == "Roucool":
        images_pokemons[pokemon.nom] = roucool_image
    if pokemon.nom == "Roucoups":
        images_pokemons[pokemon.nom] = roucoups_image
    if pokemon.nom == "Roucarnage":
        images_pokemons[pokemon.nom] = roucarnage_image
    if pokemon.nom == "Rattata":
        images_pokemons[pokemon.nom] = rattata_image
    if pokemon.nom == "Rattatac":
        images_pokemons[pokemon.nom] = rattatac_image
    if pokemon.nom == "Piafabec":
        images_pokemons[pokemon.nom] = piafabec_image
    if pokemon.nom == "Rapasdeîc":
        images_pokemons[pokemon.nom] = rapasdeic_image
    if pokemon.nom == "Abo":
        images_pokemons[pokemon.nom] = abo_image
    if pokemon.nom == "Arbok":
        images_pokemons[pokemon.nom] = arbok_image
    if pokemon.nom == "Pikachu":
        images_pokemons[pokemon.nom] = pikachu_image
    if pokemon.nom == "Raichu":
        images_pokemons[pokemon.nom] = raichu_image
    if pokemon.nom == "Sabelette":
        images_pokemons[pokemon.nom] = sabelette_image
    if pokemon.nom == "Sablaireau":
        images_pokemons[pokemon.nom] = sablaireau_image
    if pokemon.nom == "Nidorane":
        images_pokemons[pokemon.nom] = nidorane_image
    if pokemon.nom == "Nidorina":
        images_pokemons[pokemon.nom] = nidorina_image
    if pokemon.nom == "Nidoqueen":
        images_pokemons[pokemon.nom] = nidoqueen_image
    if pokemon.nom == "Nidoran":
        images_pokemons[pokemon.nom] = nidoran_image
    if pokemon.nom == "Nidorino":
        images_pokemons[pokemon.nom] = nidorino_image
    if pokemon.nom == "Nidoking":
        images_pokemons[pokemon.nom] = nidoking_image
    if pokemon.nom == "Mélofée":
        images_pokemons[pokemon.nom] = melofee_image
    if pokemon.nom == "Mélodelfe":
        images_pokemons[pokemon.nom] = melodelfe_image
    if pokemon.nom == "Goupix":
        images_pokemons[pokemon.nom] = goupix_image
    if pokemon.nom == "Feunard":
        images_pokemons[pokemon.nom] = feunard_image
    if pokemon.nom == "Rondoudou":
        images_pokemons[pokemon.nom] = rondoudou_image
    if pokemon.nom == "Grodoudou":
        images_pokemons[pokemon.nom] = grodoudou_image
    if pokemon.nom == "Nosferapti":
        images_pokemons[pokemon.nom] = nosferapti_image
    if pokemon.nom == "Nosferalto":
        images_pokemons[pokemon.nom] = nosferalto_image
    if pokemon.nom == "Mystherbe":
        images_pokemons[pokemon.nom] = mystherbe_image
    if pokemon.nom == "Ortide":
        images_pokemons[pokemon.nom] = ortide_image
    if pokemon.nom == "Rafflesia":
        images_pokemons[pokemon.nom] = rafflesia_image
    if pokemon.nom == "Paras":
        images_pokemons[pokemon.nom] = paras_image
    if pokemon.nom == "Parasect":
        images_pokemons[pokemon.nom] = parasect_image
    if pokemon.nom == "Mimitoss":
        images_pokemons[pokemon.nom] = mimitoss_image
    if pokemon.nom == "Aéromite":
        images_pokemons[pokemon.nom] = aeromite_image
    if pokemon.nom == "Taupiqueur":
        images_pokemons[pokemon.nom] = taupiqueur_image
    if pokemon.nom == "Tropikeur":
        images_pokemons[pokemon.nom] = tropikeur_image
    if pokemon.nom == "Miaouss":
        images_pokemons[pokemon.nom] = miaouss_image
    if pokemon.nom == "Persian":
        images_pokemons[pokemon.nom] = persian_image
    if pokemon.nom == "Psykokwak":
        images_pokemons[pokemon.nom] = psykokwak_image
    if pokemon.nom == "Akwakwak":
        images_pokemons[pokemon.nom] = akwakwak_image
    if pokemon.nom == "Férosinge":
        images_pokemons[pokemon.nom] = ferosinge_image
    if pokemon.nom == "Colossinge":
        images_pokemons[pokemon.nom] = colossinge_image
    if pokemon.nom == "Caninos":
        images_pokemons[pokemon.nom] = caninos_image
    if pokemon.nom == "Arcanin":
        images_pokemons[pokemon.nom] = arcanin_image
    if pokemon.nom == "Ptitard":
        images_pokemons[pokemon.nom] = ptitard_image
    if pokemon.nom == "Têtarte":
        images_pokemons[pokemon.nom] = tetarte_image
    if pokemon.nom == "Tartard":
        images_pokemons[pokemon.nom] = tartard_image
    if pokemon.nom == "Abra":
        images_pokemons[pokemon.nom] = abra_image
    if pokemon.nom == "Kadabra":
        images_pokemons[pokemon.nom] = kadabra_image
    if pokemon.nom == "Alakazam":
        images_pokemons[pokemon.nom] = alakazam_image
    if pokemon.nom == "Machoc":
        images_pokemons[pokemon.nom] = machoc_image
    if pokemon.nom == "Machopeur":
        images_pokemons[pokemon.nom] = machopeur_image
    if pokemon.nom == "Mackogneur":
        images_pokemons[pokemon.nom] = mackogneur_image
    if pokemon.nom == "Chetiflor":
        images_pokemons[pokemon.nom] = chetiflor_image
    if pokemon.nom == "Boustiflor":
        images_pokemons[pokemon.nom] = boustiflor_image
    if pokemon.nom == "Empiflor":
        images_pokemons[pokemon.nom] = empiflor_image
    if pokemon.nom == "Tentacool":
        images_pokemons[pokemon.nom] = tentacool_image
    if pokemon.nom == "Tentacruel":
        images_pokemons[pokemon.nom] = tentacruel_image
    if pokemon.nom == "Racaillou":
        images_pokemons[pokemon.nom] = racaillou_image
    if pokemon.nom == "Gravalanche":
        images_pokemons[pokemon.nom] = racaillou_image
    if pokemon.nom == "Grolem":
        images_pokemons[pokemon.nom] = grolem_image
    if pokemon.nom == "Ponyta":
        images_pokemons[pokemon.nom] = ponyta_image
    if pokemon.nom == "Galopa":
        images_pokemons[pokemon.nom] = galopa_image
    if pokemon.nom == "Ramoloss":
        images_pokemons[pokemon.nom] = ramoloss_image
    if pokemon.nom == "Flagadoss":
        images_pokemons[pokemon.nom] = flagadoss_image
    if pokemon.nom == "Magnéti":
        images_pokemons[pokemon.nom] = magneti_image
    if pokemon.nom == "Magnéton":
        images_pokemons[pokemon.nom] = magneton_image
    if pokemon.nom == "Canarticho":
        images_pokemons[pokemon.nom] = canarticho_image
    if pokemon.nom == "Doduo":
        images_pokemons[pokemon.nom] = doduo_image
    if pokemon.nom == "Dodrio":
        images_pokemons[pokemon.nom] = dodrio_image
    if pokemon.nom == "Otaria":
        images_pokemons[pokemon.nom] = otaria_image
    if pokemon.nom == "Lamantine":
        images_pokemons[pokemon.nom] = lamantine_image
    if pokemon.nom == "Tadmorv":
        images_pokemons[pokemon.nom] = tadmorv_image
    if pokemon.nom == "Grotadmorv":
        images_pokemons[pokemon.nom] = grotadmorv_image
    if pokemon.nom == "Kokyas":
        images_pokemons[pokemon.nom] = kokyas_image
    if pokemon.nom == "Crustabri":
        images_pokemons[pokemon.nom] = crustabri_image
    if pokemon.nom == "Fantominus":
        images_pokemons[pokemon.nom] = fantominus_image
    if pokemon.nom == "Spectrum":
        images_pokemons[pokemon.nom] = spectrum_image
    if pokemon.nom == "Ectoplasma":
        images_pokemons[pokemon.nom] = ectoplasma_image
    if pokemon.nom == "Onix":
        images_pokemons[pokemon.nom] = onix_image
    if pokemon.nom == "Soporifik":
        images_pokemons[pokemon.nom] = soporifik_image
    if pokemon.nom == "Hypnomade":
        images_pokemons[pokemon.nom] = hypnomade_image
    if pokemon.nom == "Krabby":
        images_pokemons[pokemon.nom] = krabby_image
    if pokemon.nom == "Voltorbe":
        images_pokemons[pokemon.nom] = voltorbe_image
    if pokemon.nom == "Electrode":
        images_pokemons[pokemon.nom] = electrode_image
    if pokemon.nom == "noeufnoeuf":
        images_pokemons[pokemon.nom] = noeufnoeuf_image
    if pokemon.nom == "Noadkoko":
        images_pokemons[pokemon.nom] = noadkoko_image
    if pokemon.nom == "Osselait":
        images_pokemons[pokemon.nom] = osselait_image
    if pokemon.nom == "Ossatueur":
        images_pokemons[pokemon.nom] = ossatueur_image
    if pokemon.nom == "Kicklee":
        images_pokemons[pokemon.nom] = kicklee_image
    if pokemon.nom == "Tygnon":
        images_pokemons[pokemon.nom] = tygnon_image
    if pokemon.nom == "Excelangue":
        images_pokemons[pokemon.nom] = excelangue_image
    if pokemon.nom == "Smogo":
        images_pokemons[pokemon.nom] = smogo_image
    if pokemon.nom == "Smogogo":
        images_pokemons[pokemon.nom] = smogogo_image
    if pokemon.nom == "Rhinocorone":
        images_pokemons[pokemon.nom] = rhinocorone_image
    if pokemon.nom == "Rhinoféros":
        images_pokemons[pokemon.nom] = rhinoferos_image
    if pokemon.nom == "Leveinard":
        images_pokemons[pokemon.nom] = leveinard_image
    if pokemon.nom == "Saquedeneu":
        images_pokemons[pokemon.nom] = saquedeneu_image
    if pokemon.nom == "Kangourex":
        images_pokemons[pokemon.nom] = kangourex_image
    if pokemon.nom == "Hypotrempe":
        images_pokemons[pokemon.nom] = hypotrempe_image
    if pokemon.nom == "Hypocéan":
        images_pokemons[pokemon.nom] = hypocean_image
    if pokemon.nom == "Poissirène":
        images_pokemons[pokemon.nom] = poissirene_image
    if pokemon.nom == "Poissoroy":
        images_pokemons[pokemon.nom] = poissoroy_image
    if pokemon.nom == "Star":
        images_pokemons[pokemon.nom] = star_image
    if pokemon.nom == "Starros":
        images_pokemons[pokemon.nom] = starros_image
    if pokemon.nom == "M.Mime":
        images_pokemons[pokemon.nom] = mmime_image
    if pokemon.nom == "Insécateur":
        images_pokemons[pokemon.nom] = insecateur_image
    if pokemon.nom == "Lippoutou":
        images_pokemons[pokemon.nom] = lippoutou_image
    if pokemon.nom == "Elektek":
        images_pokemons[pokemon.nom] = elektek_image
    if pokemon.nom == "Magmar":
        images_pokemons[pokemon.nom] = magmar_image
    if pokemon.nom == "Scarabrute":
        images_pokemons[pokemon.nom] = scarabrute_image
    if pokemon.nom == "Tauros":
        images_pokemons[pokemon.nom] = tauros_image
    if pokemon.nom == "Magicarpe":
        images_pokemons[pokemon.nom] = magicarpe_image
    if pokemon.nom == "Léviator":
        images_pokemons[pokemon.nom] = leviator_image
    if pokemon.nom == "Lokhlass":
        images_pokemons[pokemon.nom] = lokhlass_image
    if pokemon.nom == "Métamorphe":
        images_pokemons[pokemon.nom] = metamorphe_image
    if pokemon.nom == "Evoli":
        images_pokemons[pokemon.nom] = evoli_image
    if pokemon.nom == "Aquali":
        images_pokemons[pokemon.nom] = aquali_image
    if pokemon.nom == "Voltali":
        images_pokemons[pokemon.nom] = voltali_image
    if pokemon.nom == "Pyroli":
        images_pokemons[pokemon.nom] = pyroli_image
    if pokemon.nom == "Porygon":
        images_pokemons[pokemon.nom] = porygon_image
    if pokemon.nom == "Amonita":
        images_pokemons[pokemon.nom] = amonita_image
    if pokemon.nom == "Armonistar":
        images_pokemons[pokemon.nom] = armonistar_image
    if pokemon.nom == "Kabuto":
        images_pokemons[pokemon.nom] = kabuto_image
    if pokemon.nom == "Kabutops":
        images_pokemons[pokemon.nom] = kabutops_image
    if pokemon.nom == "Ptéra":
        images_pokemons[pokemon.nom] = ptera_image
    if pokemon.nom == "Ronflex":
        images_pokemons[pokemon.nom] = ronflex_image
    if pokemon.nom == "Artikodin":
        images_pokemons[pokemon.nom] = artikodin_image
    if pokemon.nom == "Elechtor":
        images_pokemons[pokemon.nom] = elechtor_image
    if pokemon.nom == "sulfura":
        images_pokemons[pokemon.nom] = sulfura_image
    if pokemon.nom == "Minidraco":
        images_pokemons[pokemon.nom] = minidraco_image
    if pokemon.nom == "Draco":
        images_pokemons[pokemon.nom] = draco_image
    if pokemon.nom == "Dracolosse":
        images_pokemons[pokemon.nom] = dracolosse_image
    if pokemon.nom == "Mewtwo":
        images_pokemons[pokemon.nom] = mewtwo_image

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.fill((255, 255, 255))  # Fond blanc pour la fenêtre

    # Affichage des pokemons à une position spécifique (par exemple : position (100, 100))
    fenetre.blit(images_pokemons["Bulbizarre"], (1, 1))
    fenetre.blit(images_pokemons["Herbizarre"], (2, 2))

    pygame.display.flip()

pygame.quit()
