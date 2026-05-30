
def main():
  pass #code goes here
# File: initials.py
# Description: Print my initials F, B, N in stylized large letters.
# Assignment Number: 1
#
# Name: Faridah Bushani Nasiru
# STUDENT ID:  2425401493
# Email: faridahbushaninasiru@gmail.com
# Grader: Augustus Buckman
#
# On my honor, Faridah Bushani Nasiru, this programming assignment is my own work
# and I have not provided this code to any other student.



def main():
    # Print small initials line with three periods and the initials "FBN"
    print()
    print("...FBN")
    print()

    # Large letter 'F' (12 chars wide, 10 rows)
    f0 = "FFFFFFFFFFFF"
    f1 = "F           "
    f2 = "F           "
    f3 = "F           "
    f4 = "FFFFFFFFFFFF"
    f5 = "F           "
    f6 = "F           "
    f7 = "F           "
    f8 = "F           "
    f9 = "F           "

    # Large letter 'B' (12 chars wide, 10 rows)
    b0 = "BBBBBBBBBBBB"
    b1 = "B          B"
    b2 = "B          B"
    b3 = "B          B"
    b4 = "BBBBBBBBBBBB"
    b5 = "B          B"
    b6 = "B          B"
    b7 = "B          B"
    b8 = "B          B"
    b9 = "BBBBBBBBBBBB"

    # Large letter 'N' (12 chars wide, 10 rows)
    n0 = "N          N"
    n1 = "NN         N"
    n2 = "N N        N"
    n3 = "N  N       N"
    n4 = "N   N      N"
    n5 = "N    N     N"
    n6 = "N     N    N"
    n7 = "N      N   N"
    n8 = "N       N  N"
    n9 = "N          N"

    # Large period (made of 4 asterisks, 5 chars wide, 10 rows)
    p0 = "     "
    p1 = "     "
    p2 = "     "
    p3 = "     "
    p4 = "     "
    p5 = "     "
    p6 = "     "
    p7 = "     "
    p8 = " **  "
    p9 = " **  "

    # Combine each row: left periods + F + period + B + period + N + period
    row0 = "..." + f0 + p0 + "..." + b0 + p0 + "..." + n0 + p0
    row1 = "..." + f1 + p1 + "..." + b1 + p1 + "..." + n1 + p1
    row2 = "..." + f2 + p2 + "..." + b2 + p2 + "..." + n2 + p2
    row3 = "..." + f3 + p3 + "..." + b3 + p3 + "..." + n3 + p3
    row4 = "..." + f4 + p4 + "..." + b4 + p4 + "..." + n4 + p4
    row5 = "..." + f5 + p5 + "..." + b5 + p5 + "..." + n5 + p5
    row6 = "..." + f6 + p6 + "..." + b6 + p6 + "..." + n6 + p6
    row7 = "..." + f7 + p7 + "..." + b7 + p7 + "..." + n7 + p7
    row8 = "..." + f8 + p8 + "..." + b8 + p8 + "..." + n8 + p8
    row9 = "..." + f9 + p9 + "..." + b9 + p9 + "..." + n9 + p9

    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print(row8)
    print(row9)
    print()



main()





