import requests
import json


###CHANGE THIS TO DETERMINE HOW MANY TIERS TO FILL, 1 is only t4, while 5 is t4 to t8
###
tiercount = 5





#request in parts by tier
#for all in tier: dict[dict with id to name[item["id(t{}_artefact...)"]]] = item['price']
#for all in sheet: sheet slot = dict[name]



class City:
    _name = ''
    _items = {}
    _runes = {}
    _tier = 0
    def __init__(self,name,items,runes,tier):
        self._name = name
        self._items = dict(items)
        self._runes = dict(runes)
        self._tier = tier

link = 'https://www.albion-online-data.com/api/v2/stats/prices/{}'
cities = ["Fort Sterling",'Bridgewatch','Lymhurst','Martlock','Thetford']

qualities = ['0']

def getData():
    def datarequest(location, qualities,runes,items):
        qualitieslist = ','.join(qualities)
        itemslist = ','.join(items)
        runeslist = ','.join(runes)
        requestlink = link.format(itemslist)
        payload = {
            'locations':location,
            'qualities':qualitieslist
        }
        r = requests.get(requestlink,params = payload)
        r = r.json()
        for x in r:
            if x['sell_price_min'] != 0:
                prices[idtoname[x['item_id']]] = x['sell_price_min']
            else:
                prices[idtoname[x['item_id']]] = x['buy_price_min']

        requestlink = link.format(runeslist)
        r = requests.get(requestlink,params = payload)
        r = r.json()
        for x in r:
            runePrice[x['item_id']] = x['sell_price_min']
    finalarr = []
    for x in range(tiercount):
        tiernum = 4+x
        tier = str(tiernum)
        arr = []
        idtoname = {
            'T{}_ARTEFACT_2H_ARCANESTAFF_HELL'.format(tier):'Occult Orb',
            'T{}_ARTEFACT_2H_BOW_HELL'.format(tier):'Demonic Arrowheads',
            'T{}_ARTEFACT_2H_BOW_KEEPER'.format(tier):'Carved Bone',
            'T{}_ARTEFACT_2H_CLEAVER_HELL'.format(tier):'Demonic Blade',
            'T{}_ARTEFACT_2H_COMBATSTAFF_MORGANA'.format(tier):'Reinforced Morgana Pole',
            'T{}_ARTEFACT_2H_CROSSBOWLARGE_MORGANA'.format(tier):'Alluring Bolts',
            'T{}_ARTEFACT_2H_CURSEDSTAFF_MORGANA'.format(tier):'Bloodforged Catalyst',
            'T{}_ARTEFACT_2H_DUALAXE_KEEPER'.format(tier):'Keeper Axeheads',
            'T{}_ARTEFACT_2H_DUALCROSSBOW_HELL'.format(tier):'Hellish Bolts',
            'T{}_ARTEFACT_2H_DUALHAMMER_HELL'.format(tier):'Hellish Hammer Heads',
            'T{}_ARTEFACT_2H_DUALSCIMITAR_UNDEAD'.format(tier):'Cursed Blades',
            'T{}_ARTEFACT_2H_DUALSICKLE_UNDEAD'.format(tier):'Ghastly Blades',
            'T{}_ARTEFACT_2H_ENIGMATICORB_MORGANA'.format(tier):'Possessed Catalyst',
            'T{}_ARTEFACT_2H_FIRESTAFF_HELL'.format(tier):'Burning Orb',
            'T{}_ARTEFACT_2H_HALBERD_MORGANA'.format(tier):'Morgana Halberd Head',
            'T{}_ARTEFACT_2H_HAMMER_UNDEAD'.format(tier):'Ancient Hammer Head',
            'T{}_ARTEFACT_2H_HARPOON_HELL'.format(tier):'Infernal Harpoon Tip',
            'T{}_ARTEFACT_MAIN_HOLYSTAFF_MORGANA'.format(tier):'Possessed Scroll',
            'T{}_ARTEFACT_2H_HOLYSTAFF_HELL'.format(tier):'Infernal Scroll',
            'T{}_ARTEFACT_2H_HOLYSTAFF_UNDEAD'.format(tier):'Ghastly Scroll',
            'T{}_ARTEFACT_2H_ICECRYSTAL_UNDEAD'.format(tier):'Cursed Frozen Crystal',
            'T{}_ARTEFACT_2H_ICEGAUNTLETS_HELL'.format(tier):'Icicle Orb',
            'T{}_ARTEFACT_2H_INFERNOSTAFF_MORGANA'.format(tier):'Unholy Scroll',
            'T{}_ARTEFACT_2H_IRONGAUNTLETS_HELL'.format(tier):'Black Leather',
            'T{}_ARTEFACT_2H_LONGBOW_UNDEAD'.format(tier):'Ghastly Arrows',
            'T{}_ARTEFACT_2H_MACE_MORGANA'.format(tier):'Imbued Mace Head',
            'T{}_ARTEFACT_2H_NATURESTAFF_HELL'.format(tier):'Symbol Of Blight',
            'T{}_ARTEFACT_2H_NATURESTAFF_KEEPER'.format(tier):'Preserved Log',
            'T{}_ARTEFACT_2H_RAM_KEEPER'.format(tier):'Engraved Log',
            'T{}_ARTEFACT_2H_REPEATINGCROSSBOW_UNDEAD'.format(tier):'Lost Crossbow Mechanism',
            'T{}_ARTEFACT_2H_ROCKSTAFF_KEEPER'.format(tier):'Preserved Rocks',
            'T{}_ARTEFACT_2H_SKULLORB_HELL'.format(tier):'Cursed Jawbone',
            'T{}_ARTEFACT_2H_TRIDENT_UNDEAD'.format(tier):'Cursed Barbs',
            'T{}_ARTEFACT_2H_TWINSCYTHE_HELL'.format(tier):'Hellish Sicklehead Pair',
            'T{}_ARTEFACT_MAIN_ARCANESTAFF_UNDEAD'.format(tier):'Lost Arcane Crystal',
            'T{}_ARTEFACT_MAIN_CURSEDSTAFF_UNDEAD'.format(tier):'Lost Cursed Crystal',
            'T{}_ARTEFACT_MAIN_FIRESTAFF_KEEPER'.format(tier):'Wildfire Orb',
            'T{}_ARTEFACT_MAIN_FROSTSTAFF_KEEPER'.format(tier):'Hoarfrost Orb',
            'T{}_ARTEFACT_MAIN_MACE_HELL'.format(tier):'Infernal Mace Head',
            'T{}_ARTEFACT_MAIN_NATURESTAFF_KEEPER'.format(tier):'Druidic Inscriptions',
            'T{}_ARTEFACT_MAIN_RAPIER_MORGANA'.format(tier):'Hardened Debole',
            'T{}_ARTEFACT_MAIN_ROCKMACE_KEEPER'.format(tier):'Runed Rock',
            'T{}_ARTEFACT_MAIN_SCIMITAR_MORGANA'.format(tier):'Bloodforged Blade',
            'T{}_ARTEFACT_MAIN_SPEAR_KEEPER'.format(tier):'Keeper Spearhead',
            'T{}_ARTEFACT_2H_SCYTHE_HELL'.format(tier):'Hellish Sicklehead',
            'T{}_ARTEFACT_2H_DAGGER_KATAR_AVALON'.format(tier):'Bloodstained Antiquities',
            'T{}_ARTEFACT_MAIN_SPEAR_LANCE_AVALON'.format(tier):'Ruined Ancestral Vamplate',
            'T{}_ARTEFACT_2H_AXE_AVALON'.format(tier):'Avalonian Battle Memoir',
            'T{}_ARTEFACT_2H_CLAYMORE_AVALON'.format(tier):'Remnants of the Old King',
            'T{}_ARTEFACT_2H_QUARTERSTAFF_AVALON'.format(tier):'Timeworn Walking Staff',
            'T{}_ARTEFACT_2H_HAMMER_AVALON'.format(tier):'Metallic Hand',
            'T{}_ARTEFACT_2H_DUALMACE_AVALON'.format(tier):'Broken Oaths',
            'T{}_ARTEFACT_2H_BOW_AVALON'.format(tier):'Immaculately Crafted Riser',
            'T{}_ARTEFACT_2H_CROSSBOW_CANNON_AVALON'.format(tier):'Humming Avalonian Whirligig',
            'T{}_ARTEFACT_MAIN_CURSEDSTAFF_AVALON'.format(tier).format(tier):'Fractured Opaque Orb',
            'T{}_ARTEFACT_2H_FIRE_RINGPAIR_AVALON':'Glowing Harmonic Ring',
            'T{}_ARTEFACT_MAIN_FROSTSTAFF_AVALON'.format(tier):'Chilled Crystaline Shard',
            'T{}_ARTEFACT_2H_ARCANE_RINGPAIR_AVALON'.format(tier):'Hypnotic Harmonic Ring',
            'T{}_ARTEFACT_MAIN_HOLYSTAFF_AVALON'.format(tier):'Messianic Curio',
            'T{}_ARTEFACT_MAIN_NATURESTAFF_AVALON'.format(tier):'Uprooted Perennial Sapling',
            'T{}_ARTEFACT_OFF_TOWERSHIELD_UNDEAD'.format(tier):'Ancient Shield Core',
            'T{}_ARTEFACT_OFF_SHIELD_HELL'.format(tier):'Infernal Shield Core',
            'T{}_ARTEFACT_OFF_SPIKEDSHIELD_MORGANA'.format(tier):'Bloodforged Spikes',
            'T{}_ARTEFACT_OFF_SHIELD_AVALON'.format(tier):'Crushed Avalonian Heirloom',
            'T{}_ARTEFACT_OFF_ORB_MORGANA'.format(tier):'Alluring Crystal',
            'T{}_ARTEFACT_OFF_DEMONSKULL_HELL'.format(tier):'Demonic Jawbone',
            'T{}_ARTEFACT_OFF_TOTEM_KEEPER'.format(tier):'Inscribed Stone',
            'T{}_ARTEFACT_OFF_CENSER_AVALON'.format(tier):'Severed Celestial Keepsake',
            'T{}_ARTEFACT_OFF_HORN_KEEPER'.format(tier):'Runed Horn',
            'T{}_ARTEFACT_OFF_JESTERCANE_HELL'.format(tier):'Hellish Handle',
            'T{}_ARTEFACT_OFF_LAMP_UNDEAD'.format(tier):'Ghastly Candle',
            'T{}_ARTEFACT_OFF_TALISMAN_AVALON'.format(tier):'Shattered Avalonian Memento',
            'T{}_ARTEFACT_HEAD_PLATE_UNDEAD'.format(tier):'Ancient Padding',
            'T{}_ARTEFACT_ARMOR_PLATE_UNDEAD'.format(tier):'Ancient Chain Rings',
            'T{}_ARTEFACT_SHOES_PLATE_UNDEAD'.format(tier):'Ancient Bindings',
            'T{}_ARTEFACT_HEAD_PLATE_HELL'.format(tier):'Demonic Scraps',
            'T{}_ARTEFACT_ARMOR_PLATE_HELL'.format(tier):'Demonic Plates',
            'T{}_ARTEFACT_SHOES_PLATE_HELL'.format(tier):'Demonic Filling',
            'T{}_ARTEFACT_HEAD_PLATE_KEEPER'.format(tier):'Carved Skull Padding',
            'T{}_ARTEFACT_ARMOR_PLATE_KEEPER'.format(tier):'Preserved Animal Fur',
            'T{}_ARTEFACT_SHOES_PLATE_KEEPER'.format(tier):'Inscribed Bindings',
            'T{}_ARTEFACT_HEAD_PLATE_AVALON'.format(tier):'Exalted Visor',
            'T{}_ARTEFACT_ARMOR_PLATE_AVALON'.format(tier):'Exalted Plating',
            'T{}_ARTEFACT_SHOES_PLATE_AVALON'.format(tier):'Exalted Greave',
            'T{}_ARTEFACT_HEAD_LEATHER_MORGANA'.format(tier):'Imbued Visor',
            'T{}_ARTEFACT_ARMOR_LEATHER_MORGANA'.format(tier):'Imbued Leather Folds',
            'T{}_ARTEFACT_SHOES_LEATHER_MORGANA'.format(tier):'Imbued Soles',
            'T{}_ARTEFACT_HEAD_LEATHER_HELL'.format(tier):'Demonhide Padding',
            'T{}_ARTEFACT_ARMOR_LEATHER_HELL'.format(tier):'Demonhide Leather',
            'T{}_ARTEFACT_SHOES_LEATHER_HELL'.format(tier):'Demonhide Bindings',
            'T{}_ARTEFACT_HEAD_LEATHER_UNDEAD'.format(tier):'Ghastly Visor',
            'T{}_ARTEFACT_ARMOR_LEATHER_UNDEAD'.format(tier):'Ghastly Leather',
            'T{}_ARTEFACT_SHOES_LEATHER_UNDEAD'.format(tier):'Ghastly Bindings',
            'T{}_ARTEFACT_HEAD_LEATHER_AVALON'.format(tier):'Augured Padding',
            'T{}_ARTEFACT_ARMOR_LEATHER_AVALON'.format(tier):'Augured Sash',
            'T{}_ARTEFACT_SHOES_LEATHER_AVALON'.format(tier):'Augured Fasteners',
            'T{}_ARTEFACT_HEAD_CLOTH_KEEPER'.format(tier):'Druidic Preserved Beak',
            'T{}_ARTEFACT_ARMOR_CLOTH_KEEPER'.format(tier):'Druidic Feathers',
            'T{}_ARTEFACT_SHOES_CLOTH_KEEPER'.format(tier):'Druidic Bindings',
            'T{}_ARTEFACT_HEAD_CLOTH_HELL'.format(tier):'Infernal Cloth Visor',
            'T{}_ARTEFACT_ARMOR_CLOTH_HELL'.format(tier):'Infernal Cloth Folds',
            'T{}_ARTEFACT_SHOES_CLOTH_HELL'.format(tier):'Infernal Cloth Bindings',
            'T{}_ARTEFACT_HEAD_CLOTH_MORGANA'.format(tier):'Alluring Padding',
            'T{}_ARTEFACT_ARMOR_CLOTH_MORGANA'.format(tier):'Alluring Amulet',
            'T{}_ARTEFACT_SHOES_CLOTH_MORGANA'.format(tier):'Alluring Bindings',
            'T{}_ARTEFACT_HEAD_CLOTH_AVALON'.format(tier):'Sanctified Mask',
            'T{}_ARTEFACT_ARMOR_CLOTH_AVALON'.format(tier):'Sanctified Belt',
            'T{}_ARTEFACT_SHOES_CLOTH_AVALON'.format(tier):'Sanctified Bindings'
        }

        prices = {
            'Occult Orb':0,
            'Demonic Arrowheads':0,
            'Carved Bone':0,
            'Demonic Blade':0,
            'Reinforced Morgana Pole':0,
            'Alluring Bolts':0,
            'Bloodforged Catalyst':0,
            'Keeper Axeheads':0,
            'Hellish Bolts':0,
            'Hellish Hammer Heads':0,
            'Cursed Blades':0,
            'Ghastly Blades':0,
            'Possessed Catalyst':0,
            'Burning Orb':0,
            'Morgana Halberd Head':0,
            'Ancient Hammer Head':0,
            'Infernal Harpoon Tip':0,
            'Possessed Scroll':0,
            'Infernal Scroll':0,
            'Ghastly Scroll':0,
            'Cursed Frozen Crystal':0,
            'Icicle Orb':0,
            'Unholy Scroll':0,
            'Black Leather':0,
            'Ghastly Arrows':0,
            'Imbued Mace Head':0,
            'Symbol Of Blight':0,
            'Preserved Log':0,
            'Engraved Log':0,
            'Lost Crossbow Mechanism':0,
            'Preserved Rocks':0,
            'Cursed Jawbone':0,
            'Cursed Barbs':0,
            'Hellish Sicklehead Pair':0,
            'Lost Arcane Crystal':0,
            'Lost Cursed Crystal':0,
            'Wildfire Orb':0,
            'Hoarfrost Orb':0,
            'Infernal Mace Head':0,
            'Druidic Inscriptions':0,
            'Hardened Debole':0,
            'Runed Rock':0,
            'Bloodforged Blade':0,
            'Keeper Spearhead':0,
            'Hellish Sicklehead':0,
            'Bloodstained Antiquities':0,
            'Ruined Ancestral Vamplate':0,
            'Avalonian Battle Memoir':0,
            'Remnants of the Old King':0,
            'Timeworn Walking Staff':0,
            'Metallic Hand':0,
            'Broken Oaths':0,
            'Immaculately Crafted Riser':0,
            'Humming Avalonian Whirligig':0,
            'Fractured Opaque Orb':0,
            'Glowing Harmonic Ring':0,
            'Chilled Crystaline Shard':0,
            'Hypnotic Harmonic Ring':0,
            'Messianic Curio':0,
            'Uprooted Perennial Sapling':0,
            'Ancient Shield Core':0,
            'Infernal Shield Core':0,
            'Bloodforged Spikes':0,
            'Crushed Avalonian Heirloom':0,
            'Alluring Crystal':0,
            'Demonic Jawbone':0,
            'Inscribed Stone':0,
            'Severed Celestial Keepsake':0,
            'Runed Horn':0,
            'Hellish Handle':0,
            'Ghastly Candle':0,
            'Shattered Avalonian Memento':0,
            'Ancient Padding':0,
            'Ancient Chain Rings':0,
            'Ancient Bindings':0,
            'Demonic Scraps':0,
            'Demonic Plates':0,
            'Demonic Filling':0,
            'Carved Skull Padding':0,
            'Preserved Animal Fur':0,
            'Inscribed Bindings':0,
            'Exalted Visor':0,
            'Exalted Plating':0,
            'Exalted Greave':0,
            'Imbued Visor':0,
            'Imbued Leather Folds':0,
            'Imbued Soles':0,
            'Demonhide Padding':0,
            'Demonhide Leather':0,
            'Demonhide Bindings':0,
            'Ghastly Visor':0,
            'Ghastly Leather':0,
            'Ghastly Bindings':0,
            'Augured Padding':0,
            'Augured Sash':0,
            'Augured Fasteners':0,
            'Druidic Preserved Beak':0,
            'Druidic Feathers':0,
            'Druidic Bindings':0,
            'Infernal Cloth Visor':0,
            'Infernal Cloth Folds':0,
            'Infernal Cloth Bindings':0,
            'Alluring Padding':0,
            'Alluring Amulet':0,
            'Alluring Bindings':0,
            'Sanctified Mask':0,
            'Sanctified Belt':0,
            'Sanctified Bindings':0,
        }
        runePrice = {
            "T{}_RUNE".format(tier) :0,
            "T{}_SOUL".format(tier) : 0,
            "T{}_RELIC".format(tier):0,
            "T{}_SHARD_AVALONIAN".format(tier):0
        }
        items = idtoname.keys()
        runes = runePrice.keys()    
        for i in cities:
            datarequest(i,qualities,runes,items)
            arr.append(City(i,prices,runePrice,4+x))
        finalarr.append(arr)
    return finalarr
