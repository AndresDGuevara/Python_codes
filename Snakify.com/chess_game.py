"""Rook move:
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, 
determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, 
first two - for the first cell, and then the last two - for the second cell. 
The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

"""Chess board - same color:
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a 
different color - NO. The program receives the input of four numbers from 1 to 8, each specifying 
the column and row number, first two - for the first cell, and then the last two - for the second cell.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

"""King move:
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of 
the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, 
first two - for the first cell, and then the last two - for the second cell. The program should output YES 
if a king can go from the first cell to the second in one move, or NO otherwise.
"""
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if abs(x1 - y1) <= 1 and abs(x2 - y2) <= 1:
    print('YES')
else: 
    print('NO')

"""Bishop moves:
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, 
determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting 
square and the column and row numbers of the ending square. The program should output YES if a Bishop can go 
from the first square to the second in one move, or NO otherwise.
"""
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if abs(x1 - y1) == abs(x2 - y2):
    print('YES')
else: 
    print('NO')

"""Queen move:
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of 
the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - 
for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go 
from the first cell to the second in one move, or NO otherwise.
"""
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if abs(x1 - y1) == abs(x2 - y2) or x1 == y1 or x2 == y2:
    print('YES')
else:
    print('NO')

"""Knight move
Statement
Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells 
vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight 
can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - 
for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go 
from the first cell to the second in one move, or NO otherwise.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x2-x1)==2 and abs(y2-y1)==1 or abs(x2-x1)==1 and abs(y2-y1)==2:
    print('YES')
else:
    print('NO')

"""or"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')