# -*- coding: utf-8 -*-

raw_page_copy = """Chikorita sprite
#152
Chikorita
Grass
Bayleef sprite
#153
Bayleef
Grass
Meganium sprite
#154
Meganium
Grass
Cyndaquil sprite
#155
Cyndaquil
Fire
Quilava sprite
#156
Quilava
Fire
Typhlosion sprite
#157
Typhlosion
Fire
Totodile sprite
#158
Totodile
Water
Croconaw sprite
#159
Croconaw
Water
Feraligatr sprite
#160
Feraligatr
Water
Sentret sprite
#161
Sentret
Normal
Furret sprite
#162
Furret
Normal
Hoothoot sprite
#163
Hoothoot
Normal · Flying
Noctowl sprite
#164
Noctowl
Normal · Flying
Ledyba sprite
#165
Ledyba
Bug · Flying
Ledian sprite
#166
Ledian
Bug · Flying
Spinarak sprite
#167
Spinarak
Bug · Poison
Ariados sprite
#168
Ariados
Bug · Poison
Crobat sprite
#169
Crobat
Poison · Flying
Chinchou sprite
#170
Chinchou
Water · Electric
Lanturn sprite
#171
Lanturn
Water · Electric
Pichu sprite
#172
Pichu
Electric
Cleffa sprite
#173
Cleffa
Fairy
Igglybuff sprite
#174
Igglybuff
Normal · Fairy
Togepi sprite
#175
Togepi
Fairy
Togetic sprite
#176
Togetic
Fairy · Flying
Natu sprite
#177
Natu
Psychic · Flying
Xatu sprite
#178
Xatu
Psychic · Flying
Mareep sprite
#179
Mareep
Electric
Flaaffy sprite
#180
Flaaffy
Electric
Ampharos sprite
#181
Ampharos
Electric
Bellossom sprite
#182
Bellossom
Grass
Marill sprite
#183
Marill
Water · Fairy
Azumarill sprite
#184
Azumarill
Water · Fairy
Sudowoodo sprite
#185
Sudowoodo
Rock
Politoed sprite
#186
Politoed
Water
Hoppip sprite
#187
Hoppip
Grass · Flying
Skiploom sprite
#188
Skiploom
Grass · Flying
Jumpluff sprite
#189
Jumpluff
Grass · Flying
Aipom sprite
#190
Aipom
Normal
Sunkern sprite
#191
Sunkern
Grass
Sunflora sprite
#192
Sunflora
Grass
Yanma sprite
#193
Yanma
Bug · Flying
Wooper sprite
#194
Wooper
Water · Ground
Quagsire sprite
#195
Quagsire
Water · Ground
Espeon sprite
#196
Espeon
Psychic
Umbreon sprite
#197
Umbreon
Dark
Murkrow sprite
#198
Murkrow
Dark · Flying
Slowking sprite
#199
Slowking
Water · Psychic
Misdreavus sprite
#200
Misdreavus
Ghost
Unown sprite
#201
Unown
Psychic
Wobbuffet sprite
#202
Wobbuffet
Psychic
Girafarig sprite
#203
Girafarig
Normal · Psychic
Pineco sprite
#204
Pineco
Bug
Forretress sprite
#205
Forretress
Bug · Steel
Dunsparce sprite
#206
Dunsparce
Normal
Gligar sprite
#207
Gligar
Ground · Flying
Steelix sprite
#208
Steelix
Steel · Ground
Snubbull sprite
#209
Snubbull
Fairy
Granbull sprite
#210
Granbull
Fairy
Qwilfish sprite
#211
Qwilfish
Water · Poison
Scizor sprite
#212
Scizor
Bug · Steel
Shuckle sprite
#213
Shuckle
Bug · Rock
Heracross sprite
#214
Heracross
Bug · Fighting
Sneasel sprite
#215
Sneasel
Dark · Ice
Teddiursa sprite
#216
Teddiursa
Normal
Ursaring sprite
#217
Ursaring
Normal
Slugma sprite
#218
Slugma
Fire
Magcargo sprite
#219
Magcargo
Fire · Rock
Swinub sprite
#220
Swinub
Ice · Ground
Piloswine sprite
#221
Piloswine
Ice · Ground
Corsola sprite
#222
Corsola
Water · Rock
Remoraid sprite
#223
Remoraid
Water
Octillery sprite
#224
Octillery
Water
Delibird sprite
#225
Delibird
Ice · Flying
Mantine sprite
#226
Mantine
Water · Flying
Skarmory sprite
#227
Skarmory
Steel · Flying
Houndour sprite
#228
Houndour
Dark · Fire
Houndoom sprite
#229
Houndoom
Dark · Fire
Kingdra sprite
#230
Kingdra
Water · Dragon
Phanpy sprite
#231
Phanpy
Ground
Donphan sprite
#232
Donphan
Ground
Porygon2 sprite
#233
Porygon2
Normal
Stantler sprite
#234
Stantler
Normal
Smeargle sprite
#235
Smeargle
Normal
Tyrogue sprite
#236
Tyrogue
Fighting
Hitmontop sprite
#237
Hitmontop
Fighting
Smoochum sprite
#238
Smoochum
Ice · Psychic
Elekid sprite
#239
Elekid
Electric
Magby sprite
#240
Magby
Fire
Miltank sprite
#241
Miltank
Normal
Blissey sprite
#242
Blissey
Normal
Raikou sprite
#243
Raikou
Electric
Entei sprite
#244
Entei
Fire
Suicune sprite
#245
Suicune
Water
Larvitar sprite
#246
Larvitar
Rock · Ground
Pupitar sprite
#247
Pupitar
Rock · Ground
Tyranitar sprite
#248
Tyranitar
Rock · Dark
Lugia sprite
#249
Lugia
Psychic · Flying
Ho-oh sprite
#250
Ho-oh
Fire · Flying
Celebi sprite
#251
Celebi
Psychic · Grass
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