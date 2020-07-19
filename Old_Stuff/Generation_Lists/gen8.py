# -*- coding: utf-8 -*-

raw_page_copy = """Grookey sprite
#810
Grookey
Grass
Thwackey sprite
#811
Thwackey
Grass
Rillaboom sprite
#812
Rillaboom
Grass
Scorbunny sprite
#813
Scorbunny
Fire
Raboot sprite
#814
Raboot
Fire
Cinderace sprite
#815
Cinderace
Fire
Sobble sprite
#816
Sobble
Water
Drizzile sprite
#817
Drizzile
Water
Inteleon sprite
#818
Inteleon
Water
Skwovet sprite
#819
Skwovet
Normal
Greedent sprite
#820
Greedent
Normal
Rookidee sprite
#821
Rookidee
Flying
Corvisquire sprite
#822
Corvisquire
Flying
Corviknight sprite
#823
Corviknight
Flying · Steel
Blipbug sprite
#824
Blipbug
Bug
Dottler sprite
#825
Dottler
Bug · Psychic
Orbeetle sprite
#826
Orbeetle
Bug · Psychic
Nickit sprite
#827
Nickit
Dark
Thievul sprite
#828
Thievul
Dark
Gossifleur sprite
#829
Gossifleur
Grass
Eldegoss sprite
#830
Eldegoss
Grass
Wooloo sprite
#831
Wooloo
Normal
Dubwool sprite
#832
Dubwool
Normal
Chewtle sprite
#833
Chewtle
Water
Drednaw sprite
#834
Drednaw
Water · Rock
Yamper sprite
#835
Yamper
Electric
Boltund sprite
#836
Boltund
Electric
Rolycoly sprite
#837
Rolycoly
Rock
Carkol sprite
#838
Carkol
Rock · Fire
Coalossal sprite
#839
Coalossal
Rock · Fire
Applin sprite
#840
Applin
Grass · Dragon
Flapple sprite
#841
Flapple
Grass · Dragon
Appletun sprite
#842
Appletun
Grass · Dragon
Silicobra sprite
#843
Silicobra
Ground
Sandaconda sprite
#844
Sandaconda
Ground
Cramorant sprite
#845
Cramorant
Flying · Water
Arrokuda sprite
#846
Arrokuda
Water
Barraskewda sprite
#847
Barraskewda
Water
Toxel sprite
#848
Toxel
Electric · Poison
Toxtricity (Low Key Form) sprite
#849
Toxtricity
Electric · Poison
Sizzlipede sprite
#850
Sizzlipede
Fire · Bug
Centiskorch sprite
#851
Centiskorch
Fire · Bug
Clobbopus sprite
#852
Clobbopus
Fighting
Grapploct sprite
#853
Grapploct
Fighting
Sinistea sprite
#854
Sinistea
Ghost
Polteageist sprite
#855
Polteageist
Ghost
Hatenna sprite
#856
Hatenna
Psychic
Hattrem sprite
#857
Hattrem
Psychic
Hatterene sprite
#858
Hatterene
Psychic · Fairy
Impidimp sprite
#859
Impidimp
Dark · Fairy
Morgrem sprite
#860
Morgrem
Dark · Fairy
Grimmsnarl sprite
#861
Grimmsnarl
Dark · Fairy
Obstagoon sprite
#862
Obstagoon
Dark · Normal
Perrserker sprite
#863
Perrserker
Steel
Cursola sprite
#864
Cursola
Ghost
Sirfetch'd sprite
#865
Sirfetch'd
Fighting
Mr. Rime sprite
#866
Mr. Rime
Psychic · Ice
Runerigus sprite
#867
Runerigus
Ground · Ghost
Milcery sprite
#868
Milcery
Fairy
Alcremie sprite
#869
Alcremie
Fairy
Falinks sprite
#870
Falinks
Fighting
Pincurchin sprite
#871
Pincurchin
Electric
Snom sprite
#872
Snom
Ice · Bug
Frosmoth sprite
#873
Frosmoth
Ice · Bug
Stonjourner sprite
#874
Stonjourner
Rock
Eiscue (Ice Face) sprite
#875
Eiscue
Ice
Indeedee (Male) sprite
#876
Indeedee
Psychic · Normal
Morpeko (Full Belly Mode) sprite
#877
Morpeko
Electric · Dark
Cufant sprite
#878
Cufant
Steel
Copperajah sprite
#879
Copperajah
Steel
Dracozolt sprite
#880
Dracozolt
Electric · Dragon
Arctozolt sprite
#881
Arctozolt
Electric · Ice
Dracovish sprite
#882
Dracovish
Water · Dragon
Arctovish sprite
#883
Arctovish
Water · Ice
Duraludon sprite
#884
Duraludon
Steel · Dragon
Dreepy sprite
#885
Dreepy
Dragon · Ghost
Drakloak sprite
#886
Drakloak
Dragon · Ghost
Dragapult sprite
#887
Dragapult
Dragon · Ghost
Zacian (Crowned Sword) sprite
#888
Zacian
Fairy · Steel
Zamazenta (Crowned Shield) sprite
#889
Zamazenta
Fighting · Steel
Eternatus sprite
#890
Eternatus
Poison · Dragon
Kubfu sprite
#891
Kubfu
Fighting
Urshifu (Single Strike Style) sprite
#892
Urshifu
Fighting · Dark
Zarude sprite
#893
Zarude
Dark · Grass
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