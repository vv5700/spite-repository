
import math

def circle_area(radius):
    ##not using radius = input...
    #^ this does not work
    #**2 works
    area = 3.14159 * (radius * radius)
    return area ##function is returning area value

def my_sqrt(x):
    return math.sqrt(x)

    def hypotenuse(a,b):
        a2 = math.pow(a,2)
        b2 = math,pow(b,2)
        return 

def main():
    #RETURN part
    '''
    area2 = circle_area(10)
    print("Circle area is:",area2)
    print("SQRT of number 5 is:", my_sqrt(5))
    print("Hypotenuse of 10 and 10 is:",hypotenuse(10,10))
    

    ##BOLEAN
    isOk = True
    print(not isOk)
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(a ^ b)
    '''

    ### IF STATEMENT
    x = 5
    if x>=10 and x<=20:
        print("X inside [10,20]")    

    if __name__ =="__main__":
        main()


