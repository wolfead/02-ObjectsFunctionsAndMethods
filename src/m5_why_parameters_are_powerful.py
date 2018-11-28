"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Alex Wolfe .
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """
    Calls the other functions in this module to test and/or demonstrate them.
    """
    drawing_speed = 10  # Bigger numbers mean faster drawing
    window = rg.TurtleWindow()
    window.tracer(drawing_speed)

    # -------------------------------------------------------------------------
    # When the _TODO_s ask you to test YOUR code,
    # comment-out the following two statements and replace them
    # by calls to   better_draw_circles   et al as needed.
    # -------------------------------------------------------------------------
    #draw_circles(rg.Point(100, 50))
    #draw_circles(rg.Point(-200, 0))
    #better_draw_circles(rg.Point(100,50),4)
    #better_draw_circles(rg.Point(100,50),35)
    #even_better_draw_circles(rg.Point(-100,-40),6,30,'red',2)
    #even_better_draw_circles(rg.Point(100,20),11,20,'blue',2)
    even_better_draw_circles(rg.Point(-400,-200),15,0,100,'green',2,10)
    even_better_draw_circles(rg.Point(-450,-300),50,0,100,'brown',4,15)
    even_better_draw_circles(rg.Point(200,200),100,0,1,'yellow',3,1)
    even_better_draw_circles(rg.Point(-350,-190),5,0.25,8,'purple',8,100)
    even_better_draw_circles(rg.Point(-400,-190),2,0,10,'yellow',9,100)
    even_better_draw_circles(rg.Point(-300,180),20,0,15,'lightgray',3,9)
    even_better_draw_circles(rg.Point(-270,170),18,0,19,'lightgray',2,9)
    even_better_draw_circles(rg.Point(-150, 100), 19, 0, 29, 'lightgray', 3, 9)
    turtle1 = rg.SimpleTurtle()
    turtle1 = rg.SimpleTurtle()
    turtle1.pen = rg.Pen('yellow', 2)
    turtle1.pen_up()
    turtle1.go_to(rg.Point(255, 205))
    turtle1.pen_down()
    turtle1.right(90)
    for k in range(1, 8):
        turtle1.forward(3)
        turtle1.left(90)
        turtle1.forward(2)
        turtle1.right(90)
        turtle1.forward(4)


    turtle2 = rg.SimpleTurtle()
    turtle2.pen = rg.Pen('yellow',2)
    turtle2.pen_up()
    turtle2.go_to(rg.Point(170,200))
    turtle2.pen_down()
    turtle2.right(90)
    for k in range(1,8):
        turtle2.forward(5)
        turtle2.right(90)
        turtle2.forward(2)
        turtle2.left(90)
        turtle2.forward(5)

    turtle3 = rg.SimpleTurtle()
    turtle3.pen = rg.Pen('yellow', 2)
    turtle3.pen_up()
    turtle3.go_to(rg.Point(105, 250))
    turtle3.pen_down()
    turtle3.right(90)
    for k in range(1, 8):
        turtle3.forward(3)
        turtle3.right(90)
        turtle3.forward(7)
        turtle3.left(90)
        turtle3.forward(2)

    turtle4 = rg.SimpleTurtle()
    turtle4.pen = rg.Pen('yellow', 2)
    turtle4.pen_up()
    turtle4.go_to(rg.Point(310, 275))
    turtle4.pen_down()
    turtle4.right(90)
    for k in range(1, 8):
        turtle4.forward(3)
        turtle4.left(90)
        turtle4.forward(6)
        turtle4.right(90)
        turtle4.forward(2)

    window.update()
    window.close_on_mouse_click()


###############################################################################
# done cc: 2.
#   First, RUN this program.  You will see that it draws concentric circles
#   whose radii vary by 15.
#
#   Next, READ:
#     -- main.
#          Note that it  constructs a TurtleWindow and then calls the function
#             draw_circles
#          twice, sending   draw_circles  one Point the first time
#          and another Point the second time.
#     -- The function  draw_circles  is defined immediately below this _TODO_.
#            Be sure that you understand its code!  Ask questions as needed!
#
#   After you have done the above, change the above _TODO_ to DONE
#   and continue to the next _TODO_ below.
#
###############################################################################


def draw_circles(point):
    """
    Constructs a SimpleTurtle, then uses the SimpleTurtle to draw 10 circles
    such that:
      -- Each is centered at the given Point, and
      -- They have radii:  15  30  45  60  75  ..., respectively.
    """
    turtle = rg.SimpleTurtle()

    # -------------------------------------------------------------------------
    # Draw circles centered at the given Point, by telling the SimpleTurtle to:
    #  Step 1: Go to the given Point and point east (towards the right).
    #  Step 2: Go 15 pixels DOWN, with its Pen up.
    #          Then draw a radius R circle.
    #    Note: The circle will be centered at the given Point,
    #    because of the way that the SimpleTurtle  draw_circle  method works.
    #  Step 3: Repeat Step 2, but using 30 pixels instead of 15, in both places
    #  Step 4: Repeat Step 2, but using 45 pixels instead of 15
    #  Step 5: Repeat Step 2, but using 60 pixels instead of 15
    #    etc.
    # -------------------------------------------------------------------------

    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...


###############################################################################
# done: 3a.
#   The function
#       better_draw_circles
#   defined below this _TODO_ starts out exactly the same as the code for
#       draw_circles
#   that you read above.
#
#   Your job is to make
#       better_draw_circles
#   "better" than   draw_circles   by adding a PARAMETER for the amount
#   by which the radii of the concentric circles increase, as described below.
#
#   The new   better_draw_circles   function can do the same  thing as
#   the   draw_circles  function, but additionally allows for the radii to
#   vary by ANY desired amount.  Hence, the new version will be MORE POWERFUL.
#
#   So, modify the   better_draw_circles   function defined BELOW so that
#   it has a single ADDITIONAL PARAMETER that is the amount
#   by which the radii of the circles increase.
#
#   For example, if that new parameter is given the value 15,
#   then the circles should have radii:  15  30  45  60  75 ..., respectively,
#   just as in   draw_circles.  But if that new parameter is given the value 3,
#   then the circles should have radii:  3  6  9  12  15  18 ..., respectively.
#
# done: 3b.
#   In   main  at the place indicated, comment-out the two existing calls
#   to  draw_circles  and add at least two calls to the improved
#   better_draw_circles  function, to TEST that your modified code is correct
#   and does indeed allow for different amounts by which the radii can vary.
#
# #############################################################################


def better_draw_circles(point,changeinradius):
    """
    Starts out the same as the   draw_circles   function defined ABOVE.
    You Will make it an IMPROVED, MORE POWERFUL function per the above _TODO_.
    """
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(0,11+1):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(changeinradius * k)  # Radius 15, 30, 45, 60, ...


###############################################################################
# done: 4a.
#   In the previous _TODO_, you made a MORE POWERFUL version
#   of   draw_circles   by introducing a new PARAMETER for the amount
#   by which the radii of the concentric circles increase.
#
#   In this _TODO_, you will implement a function called
#      even_better_draw_circles
#   that has FIVE parameters, for:
#     -- The center of the concentric circles (as it started with)
#     -- The amount by which the radii vary (as you did above)
#     -- The number of concentric circles drawn
#     -- The pen color of each of the concentric circles
#     -- The pen thickness of each of the concentric circles
#
#   Hence, this   even_better_draw_circles   function will be
#   even more POWERFUL than the previous functions,
#   in that it can draw LOTS of different kinds of circles.
#
#   Start by copy-and-pasting the code from   better_draw_circles  above
#   to the body of the   even_better_draw_circles   function defined below.
#   Then add parameters and modify the code to make them work!
#
# done: 4b.
#   In   main  at the place indicated, comment-out the existing calls
#   to  better_draw_circles  and add at least two calls to the improved
#   even_better_draw_circles  function, to TEST that your modified code is
#   correct and does indeed use its parameters per their descriptions above.
#
###############################################################################

def even_better_draw_circles(point,radius,changeinradius,circlesdrawn,color,penthickness,changeinposition):
    """ An improved version of draw_circles, per the _TODO_ above. """
    # READ the above _TODO_ and then copy-paste code from better_circles here:


    turtle = rg.SimpleTurtle()
    turtle.pen = rg.Pen(color,penthickness)
    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, circlesdrawn+1):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again

        turtle.forward(changeinposition)


        turtle.pen_down()
        turtle.draw_circle(radius + changeinradius * k)
###############################################################################
# done: 5.
#
# Finally, comment-out the existing calls to  even_better_draw_circles  and
# add code in   main  to draw various circles that form a BEAUTIFUL picture!
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
