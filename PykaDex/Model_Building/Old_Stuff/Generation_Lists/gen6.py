# -*- coding: utf-8 -*-

raw_page_copy = """Chespin sprite
#650
Chespin
Grass
Quilladin sprite
#651
Quilladin
Grass
Chesnaught sprite
#652
Chesnaught
Grass · Fighting
Fennekin sprite
#653
Fennekin
Fire
Braixen sprite
#654
Braixen
Fire
Delphox sprite
#655
Delphox
Fire · Psychic
Froakie sprite
#656
Froakie
Water
Frogadier sprite
#657
Frogadier
Water
Greninja sprite
#658
Greninja
Water · Dark
Bunnelby sprite
#659
Bunnelby
Normal
Diggersby sprite
#660
Diggersby
Normal · Ground
Fletchling sprite
#661
Fletchling
Normal · Flying
Fletchinder sprite
#662
Fletchinder
Fire · Flying
Talonflame sprite
#663
Talonflame
Fire · Flying
Scatterbug sprite
#664
Scatterbug
Bug
Spewpa sprite
#665
Spewpa
Bug
Vivillon sprite
#666
Vivillon
Bug · Flying
Litleo sprite
#667
Litleo
Fire · Normal
Pyroar sprite
#668
Pyroar
Fire · Normal
Flabébé sprite
#669
Flabébé
Fairy
Floette sprite
#670
Floette
Fairy
Florges sprite
#671
Florges
Fairy
Skiddo sprite
#672
Skiddo
Grass
Gogoat sprite
#673
Gogoat
Grass
Pancham sprite
#674
Pancham
Fighting
Pangoro sprite
#675
Pangoro
Fighting · Dark
Furfrou sprite
#676
Furfrou
Normal
Espurr sprite
#677
Espurr
Psychic
Meowstic (Male) sprite
#678
Meowstic
Psychic
Honedge sprite
#679
Honedge
Steel · Ghost
Doublade sprite
#680
Doublade
Steel · Ghost
Aegislash (Shield Forme) sprite
#681
Aegislash
Steel · Ghost
Spritzee sprite
#682
Spritzee
Fairy
Aromatisse sprite
#683
Aromatisse
Fairy
Swirlix sprite
#684
Swirlix
Fairy
Slurpuff sprite
#685
Slurpuff
Fairy
Inkay sprite
#686
Inkay
Dark · Psychic
Malamar sprite
#687
Malamar
Dark · Psychic
Binacle sprite
#688
Binacle
Rock · Water
Barbaracle sprite
#689
Barbaracle
Rock · Water
Skrelp sprite
#690
Skrelp
Poison · Water
Dragalge sprite
#691
Dragalge
Poison · Dragon
Clauncher sprite
#692
Clauncher
Water
Clawitzer sprite
#693
Clawitzer
Water
Helioptile sprite
#694
Helioptile
Electric · Normal
Heliolisk sprite
#695
Heliolisk
Electric · Normal
Tyrunt sprite
#696
Tyrunt
Rock · Dragon
Tyrantrum sprite
#697
Tyrantrum
Rock · Dragon
Amaura sprite
#698
Amaura
Rock · Ice
Aurorus sprite
#699
Aurorus
Rock · Ice
Sylveon sprite
#700
Sylveon
Fairy
Hawlucha sprite
#701
Hawlucha
Fighting · Flying
Dedenne sprite
#702
Dedenne
Electric · Fairy
Carbink sprite
#703
Carbink
Rock · Fairy
Goomy sprite
#704
Goomy
Dragon
Sliggoo sprite
#705
Sliggoo
Dragon
Goodra sprite
#706
Goodra
Dragon
Klefki sprite
#707
Klefki
Steel · Fairy
Phantump sprite
#708
Phantump
Ghost · Grass
Trevenant sprite
#709
Trevenant
Ghost · Grass
Pumpkaboo (Average Size) sprite
#710
Pumpkaboo
Ghost · Grass
Gourgeist (Average Size) sprite
#711
Gourgeist
Ghost · Grass
Bergmite sprite
#712
Bergmite
Ice
Avalugg sprite
#713
Avalugg
Ice
Noibat sprite
#714
Noibat
Flying · Dragon
Noivern sprite
#715
Noivern
Flying · Dragon
Xerneas sprite
#716
Xerneas
Fairy
Yveltal sprite
#717
Yveltal
Dark · Flying
Zygarde (50% Forme) sprite
#718
Zygarde
Dragon · Ground
Diancie sprite
#719
Diancie
Rock · Fairy
Hoopa (Hoopa Confined) sprite
#720
Hoopa
Psychic · Ghost
Volcanion sprite
#721
Volcanion
Fire · Water
"""

#print(raw_page_copy)
replaced = raw_page_copy.replace('\xc2\xb7','#')
seperated = list(raw_page_copy.split('\n'))
#print (seperated)

nums_removed = []

for i in range(0,len(seperated)-1):
    if seperated[i][0] != '#':
        nums_removed.append(seperated[i])

#print(nums_removed)

sprite_removed = []

for i in range(0,len(nums_removed)):
    if nums_removed[i][-6:] != 'sprite':
        sprite_removed.append(nums_removed[i])

#print(sprite_removed)

types = ['Normal','Fire',
 'Water','Grass',
 'Electric','Ice',
 'Fighting','Poison',
 'Ground','Flying',
 'Psychic','Bug',
 'Rock','Ghost',
 'Dark','Dragon',
 'Steel','Fairy']

types_removed = []

for i in range(0,int(len(sprite_removed)/2.)):
    types_removed.append(sprite_removed[i*2])

print(types_removed)