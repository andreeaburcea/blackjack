# Food class is going to know how to render itself as a small circle
# on the creen. and then everytime the snake touches the food,
# then that food is going to move to a new random location.
# we want to be able to do is we actually want this class food
# to inherit from the turtle class
# so that way this food class is going to have all of the capabilities of the turtle class
# but it's also going to have some specific things we want


from turtle import Turtle
import random
# all of this is going to happend when we create a new food obj from the food class
class Food(Turtle): # turtle is the superclass

    def __init__(self): # we create te initializer for this class
        super().__init__() # we can not start using things that are from the turtle class
        self.shape("circle") # this method that the turle class has that i m now going to modify in my food class# the new piece of food will has a circular shape
        self.penup() # will not draw
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # to stretch the turtle along its length and along its width
# will be 10 x 10 circle ( all these methods comes from the turtle superclass
# we are abla to inheriting from the superclass
        self.color("blue")
        self.speed("fastest") # will set speed like that because this way i don't have to look at the animation
        # of the food being created at the center of the screen, and then moving to the location t
        # hat I want it to.
        self.refresh() # inside the init we can simply just call self.refresh
# we want the food to go to a new random location we create this method and this method is going to create a new random x and y and get the food  to a new random location
    def refresh(self):
        random_x = random.randint(-280, 280)  # we don t put 300 bcs we don t want the snake to touch the wall # our screen is 600 x 600  # we create a random x and a random y position
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # we need to use the goto to get it to go a random X Y location
"""
So why don't we go ahead and create a new method which we'll call refresh.

And this refresh method is going to create a new random X,

a new random Y, and then get the food to go to that new, random location.

Then inside our init, we can simply just call self.refresh.

So be careful that you didn't right reset because that's one of the methods from

the turtle class that we're inheriting from.
"""