# Mondrian.py
# Lab 10
# Yvonne Zhu & Codi Elliott

from graphics import *
from random import randint

def PaintPartition( win, square, depth ):
    ''' Paints a partition of the window
    '''
    colors = [ 'white', 'yellow', 'red', 'blue', 'black' ]
    
    if depth <= 6:
        quadrants = getQuadrants( square )
        for i in range( len(quadrants) - randint(0,2) ):
            obj = quadrants[i]
            randcolor = colors[ randint( 0, 4 ) ]
            obj.setFill( randcolor )
            obj.draw( win )
            PaintPartition( win, obj, depth+1 )
    else:
        return None

                       
def getQuadrants( sq ):
    '''Returns a list of 4 subsquare objects
    '''
    p1 = sq.getP1()
    p2 = sq.getP2()
    p5 = sq.getCenter()

    p3 = Point( p2.getX(), p1.getY() )
    p4 = Point( p1.getX(), p2.getY() )
    p6 = Point( p1.getX(), p5.getY() )
    p7 = Point( p5.getX(), p2.getY() )
    p8 = Point( p2.getX(), p5.getY() )
    p9 = Point( p5.getX(), p1.getY() )

    s1 = Rectangle( p9, p8 )
    s2 = Rectangle( p1, p5 )
    s3 = Rectangle( p6, p7 )
    s4 = Rectangle( p5, p2 )

    return [ s1, s2, s3, s4 ]

def main():
    
    #Set up the window
    win = GraphWin( 'Mondrian', 500, 500 )
    win.setBackground( 'dimgray' )
    w = 100
    win.setCoords( -w, -w, w, w )

    #Create the largest square
    square = Rectangle( Point( -w, -w ), Point( w, w ) )
    square.setFill( 'white' )
    square.draw( win )

    PaintPartition( win, square, 0 )

main()
