# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    jump = 0
    
    while Y > X:
        X = X + D
        jump += 1

    return jump
    
    pass
