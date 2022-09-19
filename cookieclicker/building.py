from dataclasses import dataclass

@dataclass
class Building:
    """dataclass for holding Building information"""
    name: str

    left: int
    top: int
    right: int
    bottom: int
    
    next_cost: int
    next_cps: float # cookies per second
    
    base_price: int
    base_cps: float # cookies per second
    
    quantity: int = 0
    current_cps: float = 0.0


    def get_button(self)->tuple(int, int, int, int):
        """return the screen location of the building"""
        return (self.left, self.top, self.right, self.bottom)

    def get_clickable(self)->tuple(int, int):
        """return the middle clickable area of the building"""
        return ( (self.right - self.left)//2, (self.bottom - self.top)//2 )

    def get_next_cost(self)->int:
        """return the next cost of the building"""
        self.next_cost = self.base_price * 1.15 ** self.quantity
        return self.next_cost

