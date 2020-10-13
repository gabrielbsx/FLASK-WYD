from ctypes import *
import re

class STRUCT_ACCOUNTINFO(Structure):
    _fields_ = [
        ('AccountName', (c_char * 16)),
        ('AccountPass', (c_char * 12)),
        ('RealName', (c_char * 24)),
        ('SSN1', c_int),
        ('SSN2', c_int),
        ('Email', (c_char * 48)),
        ('Telephone', (c_char * 16)),
        ('Address', (c_char * 78)),
        ('NumericToken', (c_char * 6)),
        ('Year', c_int),
        ('YearDay', c_int)
    ]

class STRUCT_SCORE(Structure):
    _fields_ = [
        ('Level', c_int),
        ('Ac', c_int),
        ('Damage', c_int),
        ('Merchant', c_ubyte),
        ('AttackRun', c_ubyte),
        ('Direction', c_ubyte),
        ('ChaosRate', c_ubyte),
        ('MaxHp', c_int),
        ('MaxMp', c_int),
        ('Hp', c_int),
        ('Mp', c_int),
        ('Str', c_short),
        ('Int', c_short),
        ('Dex', c_short),
        ('Con', c_short),
        ('Special', (c_short* 4))
    ]

class UNION_ITEMINFO(Structure):
    _fields_ = [
        ('cEffect', c_ubyte),
        ('cValue', c_ubyte)
    ]

class STRUCT_ITEM(Structure):
    _fields_ = [
        ('sIndex', c_short),
        ('stEffect', (UNION_ITEMINFO * 3))
    ]

class STRUCT_MOB(Structure):
    _fields_ = [
        ('MobName', (c_char * 16)),
        ('Clan', c_char),
        ('Merchant', c_ubyte),
        ('Guild', c_ushort),
        ('Class', c_ubyte),
        ('Rsv', c_ushort),
        ('Quest', c_char),
        ('Coin', c_int),
        ('Exp', c_longlong),
        ('SPX', c_short),
        ('SPY', c_short),
        ('BaseScore', STRUCT_SCORE),
        ('CurrentScore', STRUCT_SCORE),
        ('Equip', (STRUCT_ITEM * 16)),
        ('Carry', (STRUCT_ITEM * 64)),
        ('LearnedSkill', c_long),
        ('Magic', c_uint),
        ('ScoreBonus', c_short),
        ('SpecialBonus', c_short),
        ('SkillBonus', c_short),
        ('Critical', c_ubyte),
        ('SaveMana', c_ubyte),
        ('SkillBar', (c_ubyte * 4)),
        ('GuildLevel', c_ubyte),
        ('RegenHP', c_short),
        ('RegenMP', c_short),
        ('Resist', (c_char * 4)),
    ]

class STRUCT_AFFECT(Structure):
    _fields_ = [
        ('Type', c_ubyte),
        ('Value', c_ubyte),
        ('Level', c_ushort),
        ('Time', c_uint)
    ]

class STRUCT_MORTALQUEST(Structure):
    _fields_ = [
        ('newbie', c_char),
        ('TerraMistica', c_char),
        ('MolarGargula', c_char),
        ('PilulaOrc', c_char),
        ('EMPTY', (c_char * 30))
    ]

class STRUCT_ARCHQUEST(Structure):
    _fields_ = [
        ('MortalSlot', c_char),
        ('MortalLevel', c_char),
        ('Level355', c_char),
        ('Level370', c_char),
        ('Cristal', c_char),
        ('EMPTY', (c_char * 30))
    ]

class STRUCT_CELESTIALQUEST(Structure):
    _fields_ = [
        ('ArchLevel', c_short),
        ('CelestialLevel', c_short),
        ('SubCelestialLevel', c_short),
        ('Lv40', c_char),
        ('Lv90', c_char),
        ('Add120', c_char),
        ('Add150', c_char),
        ('Add180', c_char),
        ('Add200', c_char),
        ('Arcana', c_char),
        ('Reset', c_char),
        ('EMPTY', (c_char * 30))
    ]

class STRUCT_QUESTINFOCHAR(Structure):
    _fields_ = [
        ('Mortal', STRUCT_MORTALQUEST),
        ('Arch', STRUCT_ARCHQUEST),
        ('Celestial', STRUCT_CELESTIALQUEST),
        ('Circle', c_char),
        ('EMPTY', (c_char * 30))
    ]

class STRUCT_SAVECELESTIAL(Structure):
    _fields_ = [
        ('Class', c_int),
        ('Exp', c_longlong),
        ('SPX', c_short),
        ('SPY', c_short),
        ('BaseScore', STRUCT_SCORE),
        ('LearnedSkill', c_long),
        ('ScoreBonus', c_ushort),
        ('SpecialBonus', c_ushort),
        ('SkillBonus', c_short),
        ('SkillBar1', (c_ubyte * 4)),
        ('SkillBar2', (c_ubyte * 16)),
        ('Soul', c_char),
        ('EMPTY', (c_char * 30))
    ]

class STRUCT_DAYLOGMOB(Structure):
    _fields_ = [
        ('Exp', c_longlong),
        ('YearDay', c_int)
    ]

class STRUCT_DONATEINFOMOB(Structure):
    _fields_ = [
        ('LastTime', c_uint64),
        ('Count', c_int)
    ]

class STRUCT_MOBEXTRA(Structure):
    _fields_ = [
        ('ClassMaster', c_short),
        ('Citizen', c_char),
        ('Fame', c_int),
        ('Soul', c_char),
        ('MortalFace', c_short),
        ('QuestInfo', STRUCT_QUESTINFOCHAR),
        ('SaveCelestial', (STRUCT_SAVECELESTIAL * 2)),
        ('LastNT', c_uint64),
        ('NT', c_int),
        ('KefraTicket', c_int),
        ('DivinaEnd', c_uint64),
        ('Hold', c_uint),
        ('DayLog', STRUCT_DAYLOGMOB),
        ('DonateInfo', STRUCT_DONATEINFOMOB),
        ('EMPTY', (c_int * 30))
    ]

class STRUCT_ACCOUNTFILE(Structure):
    _fields_ = [
        ('Info', STRUCT_ACCOUNTINFO),
        ('Char', (STRUCT_MOB * 4)),
        ('Cargo', (STRUCT_ITEM * 128)),
        ('Coin', c_int),
        ('ShortSkill', ((c_ubyte * 4) * 16)),
        ('affect', ((STRUCT_AFFECT * 4) * 32)),
        ('mobExtra', (STRUCT_MOBEXTRA * 4)),
        ('Donate', c_int),
        ('TempKey', (c_char * 52)),
    ]

class STRUCT_STEFFECTITEMLIST(Structure):
    _fields_ = [
        ('sEffect', c_short),
        ('sValue', c_short)
    ]

class STRUCT_ITEMLIST(Structure):
    _fields_ = [
        ('Name', (c_char * 64)),
        ('IndexMesh', c_short),
        ('IndexTexture', c_short),
        ('IndexVisualEffect', c_short),
        ('ReqLvl', c_short),
        ('ReqStr', c_short),
        ('ReqInt', c_short),
        ('ReqDex', c_short),
        ('ReqCon', c_short),
        ('stEffect', (STRUCT_STEFFECTITEMLIST * 12)),
        ('Price', c_int),
        ('nUnique', c_short),
        ('nPos', c_short),
        ('Extra', c_short),
        ('Grade', c_short)
    ]

class STRUCT_INITITEM(Structure):
    _fields_ = [
        ('PosX', c_short),
        ('PosY', c_short),
        ('ItemIndex', c_short),
        ('Rotate', c_short)
    ]

class STRUCT_LEVELBONUS(Structure):
    _fields_ = [
        ('Level', c_ushort),
        ('ScoreBonus', c_ushort),
        ('SpecialBonus', c_ushort),
        ('SkillBonus', c_ushort),
        ('Ac', c_ushort),
    ]

class STRUCT_GUILDZONE(Structure):
    _fields_ = [
        ('ChargeGuild', c_int),
        ('ChallangeGuild', c_int),
        ('GuildSpawnX', c_int),
        ('GuildSpawnY', c_int),
        ('CitySpawnX', c_int),
        ('CitySpawnY', c_int),
        ('CityLimitX1', c_int),
        ('CityLimitY1', c_int),
        ('CityLimitX2', c_int),
        ('CityLimitY2', c_int),
        ('WarAreaX1', c_int),
        ('WarAreaY1', c_int),
        ('WarAreaX2', c_int),
        ('WarAreaY2', c_int),
        ('ChargeWarSpawnX', c_int),
        ('ChargeWarSpawnY', c_int),
        ('ChallangeWarSpawnX', c_int),
        ('ChallangeWarSpawnY', c_int),
        ('CityTax', c_int),
        ('Clan', c_int),
        ('Victory', c_int)
    ]

class STRUCT_GUILDINFO(Structure):
    _fields_ = [
        ('Fame', c_short),
        ('Clan', c_char),
        ('Citizen', c_char),
        ('Sub1', c_char),
        ('Sub2', c_char),
        ('Sub3', c_char)
    ]

class STRUCT_SPELL(Structure):
    _fields_ = [
        ('SkillPoint', c_int),
        ('TargetType', c_int),
        ('ManaSpent', c_int),
        ('Delay', c_int),
        ('Range', c_int),
        ('InstanceType', c_int),
        ('InstanceValue', c_int),
        ('TickType', c_int),
        ('TickValue', c_int),
        ('AffectType', c_int),
        ('AffectValue', c_int),
        ('AffectTime', c_int),
        ('Act', (c_ubyte * 8)),
        ('InstanceAttribute', c_int),
        ('TickAttribute', c_int),
        ('Aggressive', c_int),
        ('MaxTarget', c_int),
        ('bParty', c_int),
        ('AffectResist', c_int),
        ('Passive', c_int)
    ]

class STRUCT_GUILDINFOALL(Structure):
    _fields_ = [
        ('GuildInfo', (STRUCT_GUILDINFO * 65536))
    ]

class STRUCT_ITEMLISTALL(Structure):
    _fields_ = [
        ('id', (STRUCT_ITEMLIST * 6500))
    ]

class STRUCT_SPELLALL(Structure):
    _fields_ = [
        ('skill', (STRUCT_SPELL * 103))
    ]

def BASE_GetSum2(p, size):
    sum = 0
    for i in range(0, size):
        mod = (i % 9)
        if (mod == 0):
            sum = sum + p[i] * 2
    
        if (mod == 1):
            sum = sum + (p[i] ^ 0xFF)
    
        if (mod == 2):
            sum = sum + p[i] / 3
    
        if (mod == 3):
            sum = sum + p[i] * 2
    
        if (mod == 4):
            sum = sum - (p[i] ^ 0x5A)
    
        if (mod == 5):
            sum = sum - p[i]
        else:
            sum = sum + (p[i] / 5)
        i = i + 1
    return sum

def xor_c(a):
    return bytearray([b^0x5A for b in bytearray(a)])
    