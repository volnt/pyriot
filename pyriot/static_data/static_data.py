from pyriot.entity import Entity

class ChampionList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.data = {k, Champion(**v) for k, v in self.data.iteritems()}

class Champion(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.recommended = [Recommended(**r) for r in self.recommended]
        self.skins = [Skins(**s) for s in self.skins]
        self.spells = [ChampionSpell(**s) for s in self.spells]
        self.stats = Stats(**self.stats)

class ChampionSpell(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.altimages = [Image(**i) for i in self.altimages]
        self.leveltip = LevelTip(**self.leveltip)
        self.vars = [SpellVars(**v) for v in self.vars]

class Image(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Info(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Passive(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.image = Image(**self.image)
        
class Recommended(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.blocks = [Block(**b) for b in self.blocks]

class Skin(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
 
class Stats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class LevelTip(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class SpellVars(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Block(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.items = [BlockItem(**i) for i in self.items]

class BlockItem(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class ItemList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.data = {k, Item(**v) for k, v in self.data.iteritems()}
        self.groups = [Group(**g) for g in self.groups]
        self.tree = [ItemTree(**t) for t in self.tree]

class BasicData(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.gold = Gold(**self.gold)
        self.image = Image(**self.image)
        self.rune = MetaData(**self.rune)
        self.stats = BasicDataStats(**self.stats)

class Group(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Item(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.gold = Gold(**self.gold)
        self.image = Item(**self.image)
        self.rune = MetaData(**self.rune)
        self.stats = BasicDataStats(**self.stats)

class ItemTree(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class BasicDataStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Gold(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class MetaData(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class MasteryList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.data = {k, Mastery(**v) for k, v in self.data.iteritems()}
        self.tree = MasteryTree(**self.tree)

class Mastery(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.image = Image(**self.image)

class MasteryTree(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.Defense = [MasteryTreeList(**d) for d in self.Defense]
        self.Offense = [MasteryTreeList(**d) for d in self.Offense]
        self.Utility = [MasteryTreeList(**d) for d in self.Utility]

class MasteryTreeList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.masteryTreeItem = [MasteryTreeItem(**i) for i in self.masteryTreeItem]

class MasteryTreeItem(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
    
class Realm(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class RuneList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.basic = BasicData(**self.basic)
        self.data = {k, Rune(**v) for k, v in self.data.iteritems()}

class Rune(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.gold = Gold(**self.gold)
        self.image = Image(**self.image)
        self.rune = MetaData(**self.rune)
        self.stats = BasicDataStats(**self.stats)

class SummonerSpellList(Entity):
    pass # TODO

class SummonerSpell(Entity):
    pass # TODO
