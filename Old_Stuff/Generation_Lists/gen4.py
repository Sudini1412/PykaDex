# -*- coding: utf-8 -*-

raw_page_copy = """Turtwig sprite
#387
Turtwig
Grass
Grotle sprite
#388
Grotle
Grass
Torterra sprite
#389
Torterra
Grass · Ground
Chimchar sprite
#390
Chimchar
Fire
Monferno sprite
#391
Monferno
Fire · Fighting
Infernape sprite
#392
Infernape
Fire · Fighting
Piplup sprite
#393
Piplup
Water
Prinplup sprite
#394
Prinplup
Water
Empoleon sprite
#395
Empoleon
Water · Steel
Starly sprite
#396
Starly
Normal · Flying
Staravia sprite
#397
Staravia
Normal · Flying
Staraptor sprite
#398
Staraptor
Normal · Flying
Bidoof sprite
#399
Bidoof
Normal
Bibarel sprite
#400
Bibarel
Normal · Water
Kricketot sprite
#401
Kricketot
Bug
Kricketune sprite
#402
Kricketune
Bug
Shinx sprite
#403
Shinx
Electric
Luxio sprite
#404
Luxio
Electric
Luxray sprite
#405
Luxray
Electric
Budew sprite
#406
Budew
Grass · Poison
Roserade sprite
#407
Roserade
Grass · Poison
Cranidos sprite
#408
Cranidos
Rock
Rampardos sprite
#409
Rampardos
Rock
Shieldon sprite
#410
Shieldon
Rock · Steel
Bastiodon sprite
#411
Bastiodon
Rock · Steel
Burmy sprite
#412
Burmy
Bug
Wormadam (Plant Cloak) sprite
#413
Wormadam
Bug · Grass
Mothim sprite
#414
Mothim
Bug · Flying
Combee sprite
#415
Combee
Bug · Flying
Vespiquen sprite
#416
Vespiquen
Bug · Flying
Pachirisu sprite
#417
Pachirisu
Electric
Buizel sprite
#418
Buizel
Water
Floatzel sprite
#419
Floatzel
Water
Cherubi sprite
#420
Cherubi
Grass
Cherrim sprite
#421
Cherrim
Grass
Shellos sprite
#422
Shellos
Water
Gastrodon sprite
#423
Gastrodon
Water · Ground
Ambipom sprite
#424
Ambipom
Normal
Drifloon sprite
#425
Drifloon
Ghost · Flying
Drifblim sprite
#426
Drifblim
Ghost · Flying
Buneary sprite
#427
Buneary
Normal
Lopunny sprite
#428
Lopunny
Normal
Mismagius sprite
#429
Mismagius
Ghost
Honchkrow sprite
#430
Honchkrow
Dark · Flying
Glameow sprite
#431
Glameow
Normal
Purugly sprite
#432
Purugly
Normal
Chingling sprite
#433
Chingling
Psychic
Stunky sprite
#434
Stunky
Poison · Dark
Skuntank sprite
#435
Skuntank
Poison · Dark
Bronzor sprite
#436
Bronzor
Steel · Psychic
Bronzong sprite
#437
Bronzong
Steel · Psychic
Bonsly sprite
#438
Bonsly
Rock
Mime Jr. sprite
#439
Mime Jr.
Psychic · Fairy
Happiny sprite
#440
Happiny
Normal
Chatot sprite
#441
Chatot
Normal · Flying
Spiritomb sprite
#442
Spiritomb
Ghost · Dark
Gible sprite
#443
Gible
Dragon · Ground
Gabite sprite
#444
Gabite
Dragon · Ground
Garchomp sprite
#445
Garchomp
Dragon · Ground
Munchlax sprite
#446
Munchlax
Normal
Riolu sprite
#447
Riolu
Fighting
Lucario sprite
#448
Lucario
Fighting · Steel
Hippopotas sprite
#449
Hippopotas
Ground
Hippowdon sprite
#450
Hippowdon
Ground
Skorupi sprite
#451
Skorupi
Poison · Bug
Drapion sprite
#452
Drapion
Poison · Dark
Croagunk sprite
#453
Croagunk
Poison · Fighting
Toxicroak sprite
#454
Toxicroak
Poison · Fighting
Carnivine sprite
#455
Carnivine
Grass
Finneon sprite
#456
Finneon
Water
Lumineon sprite
#457
Lumineon
Water
Mantyke sprite
#458
Mantyke
Water · Flying
Snover sprite
#459
Snover
Grass · Ice
Abomasnow sprite
#460
Abomasnow
Grass · Ice
Weavile sprite
#461
Weavile
Dark · Ice
Magnezone sprite
#462
Magnezone
Electric · Steel
Lickilicky sprite
#463
Lickilicky
Normal
Rhyperior sprite
#464
Rhyperior
Ground · Rock
Tangrowth sprite
#465
Tangrowth
Grass
Electivire sprite
#466
Electivire
Electric
Magmortar sprite
#467
Magmortar
Fire
Togekiss sprite
#468
Togekiss
Fairy · Flying
Yanmega sprite
#469
Yanmega
Bug · Flying
Leafeon sprite
#470
Leafeon
Grass
Glaceon sprite
#471
Glaceon
Ice
Gliscor sprite
#472
Gliscor
Ground · Flying
Mamoswine sprite
#473
Mamoswine
Ice · Ground
Porygon-Z sprite
#474
Porygon-Z
Normal
Gallade sprite
#475
Gallade
Psychic · Fighting
Probopass sprite
#476
Probopass
Rock · Steel
Dusknoir sprite
#477
Dusknoir
Ghost
Froslass sprite
#478
Froslass
Ice · Ghost
Rotom sprite
#479
Rotom
Electric · Ghost
Uxie sprite
#480
Uxie
Psychic
Mesprit sprite
#481
Mesprit
Psychic
Azelf sprite
#482
Azelf
Psychic
Dialga sprite
#483
Dialga
Steel · Dragon
Palkia sprite
#484
Palkia
Water · Dragon
Heatran sprite
#485
Heatran
Fire · Steel
Regigigas sprite
#486
Regigigas
Normal
Giratina (Altered Forme) sprite
#487
Giratina
Ghost · Dragon
Cresselia sprite
#488
Cresselia
Psychic
Phione sprite
#489
Phione
Water
Manaphy sprite
#490
Manaphy
Water
Darkrai sprite
#491
Darkrai
Dark
Shaymin (Land Forme) sprite
#492
Shaymin
Grass
Arceus sprite
#493
Arceus
Normal
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