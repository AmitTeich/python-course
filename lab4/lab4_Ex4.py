import math
def roots(a,b,c):
    if a==0 : return False
    insqrt = b**2-4*a*c
    if(insqrt<0) : return False
    roots1 = (-b+math.sqrt(insqrt))/ (2*a)
    roots2 = (-b - math.sqrt(insqrt)) / (2 * a)
    return [roots1,roots2]


def test ():
    print(roots(1,0,-64))
    print(roots(2, -14, 24))
    print(roots(0, 2, -6))
    print(roots(1, 0, 64))
    print(roots(0, 0, 5))

test()