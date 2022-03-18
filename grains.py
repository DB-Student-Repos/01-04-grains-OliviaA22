def square(number):
    if number < 1 or number > 64:
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")
    y = 0.5
    for x in range (number):
        y = y * 2
    return int(y)
    
def total():
    y = 0
    for x in range(1, 65):
        y = y + square(x)
    return y
