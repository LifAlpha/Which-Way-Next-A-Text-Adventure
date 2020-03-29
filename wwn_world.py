def tile_at(x,y):
    if x < 0 or y < 0:
        return None
        try:
            return world_map[y][x]
        except IndexError:
            return None

class MapTile:
    def_init_(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")
        
       
class StartTile(MapTile):
    def intro_text(self):
        return """
        You come to in a dark alley, the pitter patter of water dripping from above is the only sound you hear. 
        There is light ahead of you and darkness behind. 
        You make out a door to your right and on your left is the wall you're curled beside. 
        Iron bars dig into your left side - behind them a basement window.
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very boring part of the map.
        """


class Ending1Tile(MapTile):
    def intro_text(self):
        return """
        The lock resists. You jiggle the key and turn it hard.
        The door opens. It's a familiar setting. 
        You feel the warmth of the space heat your bones. 
        A window is open somewhere - you can smell something sweet on the breeze. 
        You let the door fall closed behind you. It clicks shut. 
        The space invites you further in. You barely hear the bolt engage. You don't turn back to see there is no longer a way out. 
        "I am warm and safe," you say to yourself, smiling. You repeat it again and again and again. 
        """
