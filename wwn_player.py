


class Player:
    def_init_(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          'Gold(5)',
                          'Crusty Bread']
                          
        self.x = 1
        self.y = 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def move(self, dex, dy):
            self.x += dx
            self.y += dy
            
        def move_north(self):
            self.move(dx=0, dy=-1)
            
        def move_south(self):
            self.move(dx=0, dy=1)
            
        def move_east(self):
            self.move(dx=1, dy=0)
            
        def move_west(self):
            self.move(dx=-1, dy=0)
