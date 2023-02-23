def main():
    qty = None
    cost = None

    

def fetch_quantity():
    try:
        """
        Returns a number, any number
        """
        ...
        return ...
    except:
        print("unsupported operand type(s) for /: 'ellipsis' and 'ellipsis'")

def fetch_cost():
    try:
        """
        Returns a number, any number
        """
        ...
        return ...
    except:
        pass

def compute_cost_per_quantity():
    try:
        qty = fetch_quantity()
        cost = fetch_cost()
        cost_per_quantity = cost/qty
        return cost_per_quantity
    except:
        print("TypeError: unsupported operand type(s) for /: 'ellipsis' and 'ellipsis'")
        
cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)