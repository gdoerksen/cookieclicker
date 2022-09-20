from dataclasses import dataclass

@dataclass
class Building:
    """dataclass for holding Building information"""
    name: str
    object_type: str

    left: int
    top: int
    right: int
    bottom: int
    
    base_cost: int
    base_cps: float # cookies per second
    
    next_cost: int
    next_cps: float # cookies per second

    quantity: int
    current_cps: float

    def __init__(self, name, object_type, left, top, right, bottom, base_cost, base_cps):
        self.name = name
        self.object_type = object_type

        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

        self.base_cost = base_cost
        self.base_cps = base_cps

        self.next_cost = 0
        self.next_cps = 0.0

        self.quantity = 0
        self.current_cps = 0.0

    def get_button(self):
        """return the screen location of the building"""
        return (self.left, self.top, self.right, self.bottom)

    def get_clickable(self):
        """return the middle clickable area of the building"""
        return ( (self.right - self.left)//2, (self.bottom - self.top)//2 )

    def get_next_cost(self):
        """return the next cost of the building"""
        self.next_cost = self.base_price * 1.15 ** self.quantity
        return self.next_cost

