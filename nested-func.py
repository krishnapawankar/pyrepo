#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      krishna
#
# Created:     17/02/2016
# Copyright:   (c) krishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def x():
    a=40
    print("x::")
    def y():
        b=34
        print("y::")
    y()


def main():
    x()
   # y()
   # x.y()
    #y.a=77
   # x.y.b=78
    x.b=55
    x.a=545

    print(x.b, " ", x.a)



if __name__ == '__main__':
    main()
