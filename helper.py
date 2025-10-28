# module example

def calcCircumfrence(radious: float) -> float:
    '''
    returns the circumfrence based on the radius
    '''
    return 2 * (22/7) * radious

def calcAreaOfCircle(radious=None,diameter=None):
    """
    returns area of circle based on radious or diameter 
    """
    pi = 22/7
    if radious is not None:
        return pi *radious ** 2
    elif diameter is not None:
        return pi * (diameter/2) ** 2