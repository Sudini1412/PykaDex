# -*- coding: utf-8 -*-

raw_page_copy = """Rowlet sprite
#722
Rowlet
Grass · Flying
Dartrix sprite
#723
Dartrix
Grass · Flying
Decidueye sprite
#724
Decidueye
Grass · Ghost
Litten sprite
#725
Litten
Fire
Torracat sprite
#726
Torracat
Fire
Incineroar sprite
#727
Incineroar
Fire · Dark
Popplio sprite
#728
Popplio
Water
Brionne sprite
#729
Brionne
Water
Primarina sprite
#730
Primarina
Water · Fairy
Pikipek sprite
#731
Pikipek
Normal · Flying
Trumbeak sprite
#732
Trumbeak
Normal · Flying
Toucannon sprite
#733
Toucannon
Normal · Flying
Yungoos sprite
#734
Yungoos
Normal
Gumshoos sprite
#735
Gumshoos
Normal
Grubbin sprite
#736
Grubbin
Bug
Charjabug sprite
#737
Charjabug
Bug · Electric
Vikavolt sprite
#738
Vikavolt
Bug · Electric
Crabrawler sprite
#739
Crabrawler
Fighting
Crabominable sprite
#740
Crabominable
Fighting · Ice
Oricorio (Baile Style) sprite
#741
Oricorio
Fire · Flying
Cutiefly sprite
#742
Cutiefly
Bug · Fairy
Ribombee sprite
#743
Ribombee
Bug · Fairy
Rockruff sprite
#744
Rockruff
Rock
Lycanroc (Midday Form) sprite
#745
Lycanroc
Rock
Wishiwashi (Solo Form) sprite
#746
Wishiwashi
Water
Mareanie sprite
#747
Mareanie
Poison · Water
Toxapex sprite
#748
Toxapex
Poison · Water
Mudbray sprite
#749
Mudbray
Ground
Mudsdale sprite
#750
Mudsdale
Ground
Dewpider sprite
#751
Dewpider
Water · Bug
Araquanid sprite
#752
Araquanid
Water · Bug
Fomantis sprite
#753
Fomantis
Grass
Lurantis sprite
#754
Lurantis
Grass
Morelull sprite
#755
Morelull
Grass · Fairy
Shiinotic sprite
#756
Shiinotic
Grass · Fairy
Salandit sprite
#757
Salandit
Poison · Fire
Salazzle sprite
#758
Salazzle
Poison · Fire
Stufful sprite
#759
Stufful
Normal · Fighting
Bewear sprite
#760
Bewear
Normal · Fighting
Bounsweet sprite
#761
Bounsweet
Grass
Steenee sprite
#762
Steenee
Grass
Tsareena sprite
#763
Tsareena
Grass
Comfey sprite
#764
Comfey
Fairy
Oranguru sprite
#765
Oranguru
Normal · Psychic
Passimian sprite
#766
Passimian
Fighting
Wimpod sprite
#767
Wimpod
Bug · Water
Golisopod sprite
#768
Golisopod
Bug · Water
Sandygast sprite
#769
Sandygast
Ghost · Ground
Palossand sprite
#770
Palossand
Ghost · Ground
Pyukumuku sprite
#771
Pyukumuku
Water
Type: Null sprite
#772
Type: Null
Normal
Silvally sprite
#773
Silvally
Normal
Minior (Meteor Form) sprite
#774
Minior
Rock · Flying
Komala sprite
#775
Komala
Normal
Turtonator sprite
#776
Turtonator
Fire · Dragon
Togedemaru sprite
#777
Togedemaru
Electric · Steel
Mimikyu sprite
#778
Mimikyu
Ghost · Fairy
Bruxish sprite
#779
Bruxish
Water · Psychic
Drampa sprite
#780
Drampa
Normal · Dragon
Dhelmise sprite
#781
Dhelmise
Ghost · Grass
Jangmo-o sprite
#782
Jangmo-o
Dragon
Hakamo-o sprite
#783
Hakamo-o
Dragon · Fighting
Kommo-o sprite
#784
Kommo-o
Dragon · Fighting
Tapu Koko sprite
#785
Tapu Koko
Electric · Fairy
Tapu Lele sprite
#786
Tapu Lele
Psychic · Fairy
Tapu Bulu sprite
#787
Tapu Bulu
Grass · Fairy
Tapu Fini sprite
#788
Tapu Fini
Water · Fairy
Cosmog sprite
#789
Cosmog
Psychic
Cosmoem sprite
#790
Cosmoem
Psychic
Solgaleo sprite
#791
Solgaleo
Psychic · Steel
Lunala sprite
#792
Lunala
Psychic · Ghost
Nihilego sprite
#793
Nihilego
Rock · Poison
Buzzwole sprite
#794
Buzzwole
Bug · Fighting
Pheromosa sprite
#795
Pheromosa
Bug · Fighting
Xurkitree sprite
#796
Xurkitree
Electric
Celesteela sprite
#797
Celesteela
Steel · Flying
Kartana sprite
#798
Kartana
Grass · Steel
Guzzlord sprite
#799
Guzzlord
Dark · Dragon
Necrozma sprite
#800
Necrozma
Psychic
Magearna sprite
#801
Magearna
Steel · Fairy
Marshadow sprite
#802
Marshadow
Fighting · Ghost
Poipole sprite
#803
Poipole
Poison
Naganadel sprite
#804
Naganadel
Poison · Dragon
Stakataka sprite
#805
Stakataka
Rock · Steel
Blacephalon sprite
#806
Blacephalon
Fire · Ghost
Zeraora sprite
#807
Zeraora
Electric
Meltan sprite
#808
Meltan
Steel
Melmetal sprite
#809
Melmetal
Steel
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