def fortytwo(number):
    if number == 0:
        return
    
    else:
        #Creating 4
        down()
        right(90)
        forward(10)
        left(90)
        forward(15)
        left(90)
        forward(10)
        backward(20)
        up()
        right(90)
        forward (3)

        #Creating 2
        left(90)
        forward(20)
        down()
        right(90)
        forward(15)
        right(90)
        forward(10)
        right(90)
        forward(15)
        left(90)
        forward(10)
        left(90)
        forward(15)
        up()
        forward(10)
        left(90)
        forward(20)
        right(90)

        fortytwo(number - 1)