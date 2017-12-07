GlowScript 2.6 VPython

# Note to player: If you hit the alien, you will be pleasantly surprised!
#
# game_starter.py
#
# building an interaction with 3d graphics using python
#   docs:      http://www.glowscript.org/docs/GlowScriptDocs/index.html
#   examples:  http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.bind('keydown', keydown_fun)
scene.bind('click', click_fun)
scene.background = 0.8*vector(1,1,1)
scene.width = 640
scene.height = 480


# +++ start of object-creation functions...
# these functions create "container" objects, called "compounds"

def make_alien( starting_position, starting_vel=vector(0,0,0) ):
    """ the lines below make a new "frame" == a container with a local coordinate system 
        the inputs to make_alien allow for any initial starting position
        and initial starting velocity, with a default starting velocity of vector(0,0,0)
        
        compounds can have any number of components...  Here are the alien's components:
    """
    alien_body = sphere( size=1.0*vector(1,1,1), pos=vector(0,0,0), color=color.green )
    alien_eye1 = sphere( size=0.3*vector(1,1,1), pos=.42*vector(.7,.5,.2), color=color.white )
    alien_eye2 = sphere( size=0.3*vector(1,1,1), pos=.42*vector(.2,.5,.7), color=color.white )
    alien_hat = cylinder( pos=0.42*vector(0,.9,-.2), axis=vector(.02,.2,-.02), size=vector(0.2,0.7,0.7), color=color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]  # make a list to "fuse" with a compound
    # now, we create a compound - we'll name it com_alien:
    com_alien = compound( alien_objects, pos=starting_position )         
    com_alien.vel = starting_vel   # set the initial velocity
    return com_alien
    
    

# +++ start of OBJECT_CREATION section

# A tree
pyramid(pos=vec(5,5,0), size=vec(6,3,2), color = vec(0,1,0), axis = vec(0,1,0))
cylinder( pos=vec(5,0,0), axis=vec(0,1,0), size=vec(5,1,1), color = vec(2,1,0) )

# the ground - a box (vpython's rectangular solid)
# http://www.glowscript.org/docs/GlowScriptDocs/box.html
ground = box(size=vector(20,1,20), pos=vector(0,-1,0), color=.4*vector(1,1,1))

# two walls, also boxes
wallA = box(pos=vector(0,0,-10), axis=vector(1,0,0), size=vector(20,1,.2), color=vector(1.0,0.7,0.3)) # amber
wallB = box(pos=vector(-10,0,0), axis=vector(0,0,1), size=vector(20,1,.2), color=color.blue)   # blue

# a ball that we will be able to control
ball = sphere(size=1.0*vector(1,1,1), color=vector(0.8,0.5,0.0))   # ball is an object of class sphere
ball.vel = vector(0,0,0)     # this is its initial velocity

# we make two aliens using two calls to the make_alien function (from above)
alien = make_alien( starting_position=vector(6,0,-6), starting_vel=vector(0,0,-1) )
alien2 = make_alien( starting_position=vector(-10,5,0) )  # zero starting velocity


# +++ end of OBJECT_CREATION section


# +++ start of ANIMATION section

# other constants
RATE = 30                # the number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # the time step each time through the while loop
scene.autoscale = False  # avoids changing the view automatically
scene.forward = vector(0,-3,-2)  # bird's-eye view...

while True:    # this is the "event loop": each loop is one step in time, dt

    rate(RATE) # maximum number of times per second the while loop runs 

    # +++ start of PHYSICS UPDATES - update all positions here, every time step

    alien.pos = alien.pos + alien.vel*dt   # update the alien's position 
    ball.pos = ball.pos + ball.vel*dt      # update the ball's position

    # +++ end of PHYSICS UPDATES - be sure new objects are updated appropriately!


    # +++ start of COLLISIONS - check for collisions + do the "right" thing
    
    # if the ball hits wallA
    if ball.pos.z < wallA.pos.z: # hit - check for z
        ball.pos.z = wallA.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity
        
    # if the ball hits wallB
    if ball.pos.x < wallB.pos.x: # hit - check for x
        ball.pos.x = wallB.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
        
        
    # if the ball collides with the alien, give the alien a vertical velocity
    if mag( ball.pos - alien.pos ) < 1.0:
    
    # I tried to implement the alien spawning a while loop but I was met with a scary error :(
        make_alien( starting_position=vector(-10,5,-10) )
        make_alien( starting_position=vector(-10,5,-9) ) 
        make_alien( starting_position=vector(-10,5,-8) ) 
        make_alien( starting_position=vector(-10,5,-7) ) 
        make_alien( starting_position=vector(-10,5,-6) ) 
        make_alien( starting_position=vector(-10,5,-5) ) 
        make_alien( starting_position=vector(-10,5,-4) ) 
        make_alien( starting_position=vector(-10,5,-3) ) 
        make_alien( starting_position=vector(-10,5,-2) ) 
        make_alien( starting_position=vector(-10,5,-1) )
        make_alien( starting_position=vector(-10,5,0) ) 
        make_alien( starting_position=vector(-10,5,1) ) 
        make_alien( starting_position=vector(-10,5,2) ) 
        make_alien( starting_position=vector(-10,5,3) ) 
        make_alien( starting_position=vector(-10,5,4) ) 
        make_alien( starting_position=vector(-10,5,5) ) 
        make_alien( starting_position=vector(-10,5,6) ) 
        make_alien( starting_position=vector(-10,5,7) ) 
        make_alien( starting_position=vector(-10,5,8) ) 
        make_alien( starting_position=vector(-10,5,9) ) 
        make_alien( starting_position=vector(-10,5,10) ) 
        
        make_alien( starting_position=vector(10,5,-10) )
        make_alien( starting_position=vector(10,5,-9) ) 
        make_alien( starting_position=vector(10,5,-8) ) 
        make_alien( starting_position=vector(10,5,-7) ) 
        make_alien( starting_position=vector(10,5,-6) ) 
        make_alien( starting_position=vector(10,5,-5) ) 
        make_alien( starting_position=vector(10,5,-4) ) 
        make_alien( starting_position=vector(10,5,-3) ) 
        make_alien( starting_position=vector(10,5,-2) ) 
        make_alien( starting_position=vector(10,5,-1) )
        make_alien( starting_position=vector(10,5,0) ) 
        make_alien( starting_position=vector(10,5,1) ) 
        make_alien( starting_position=vector(10,5,2) ) 
        make_alien( starting_position=vector(10,5,3) ) 
        make_alien( starting_position=vector(10,5,4) ) 
        make_alien( starting_position=vector(10,5,5) ) 
        make_alien( starting_position=vector(10,5,6) ) 
        make_alien( starting_position=vector(10,5,7) ) 
        make_alien( starting_position=vector(10,5,8) ) 
        make_alien( starting_position=vector(10,5,9) ) 
        make_alien( starting_position=vector(10,5,10) ) 

        print("To infinity and beyond!")
        alien.color = color.gray(.8)
        alien.vel = vector(0,1,0)
    
    # if the alien ventures too far, restart randomly
    if mag(alien.pos) > 10 and alien.vel.y < 1:
        alien.pos.x = choice([-6,6])
        alien.pos.z = choice([-6,6])
        alien.vel = 2*vector.random() # library-supplied random vector
        alien.vel.y = 0.0             # no vertical component of velocity

    # +++ end of COLLISIONS
    
    

# +++ start of EVENT_HANDLING section - separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """ function called with each key pressed """
    ball.color = randcolor()
    key = chr(event.which)
    ri = randint( 0, 10 )
    print("key:", key, ri)  # prints the key pressed - caps only...
    
    amt = 0.42   # "strength" of the keypress's velocity changes
    if key in 'WI&': # all capitals!
        ball.vel = ball.vel + vector(0,0,-amt)
    if key in 'A%J': 
        ball.vel = ball.vel + vector(-amt,0,0)
    if key in 'S(K': # all capitals!
        ball.vel = ball.vel + vector(0,0,amt)
    if key in "D'L": 
        ball.vel = ball.vel + vector(amt,0,0)
    if key in " ":
        ball.vel = vector(0,0,0) # reset! via the spacebar, " "
        ball.pos = vector(0,0,0)
    
def click_fun(event):
    """ function called with each mouse click """
    print("event is", event.event, event.which)
    
# +++ end of EVENT_HANDLING section
    
    
    
# +++ other functions can go here...

def choice( L ):
    """ implements Python's choice using the random() function """
    LEN = len(L)   # get the length
    randomindex = int( LEN*random() )  # get a random index
    return L[randomindex]     # return that element
    
def randint( low, hi ):
    """ implements Python's randint using the random() function 
        returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:  low, hi = hi, low  # swap if out of order!
    LEN = int(hi)-int(low)+1   # get the span and add 1
    randvalue = LEN*random()   # get a random value
    return int(randvalue)      # return the integer part of it
    
def randcolor():
    """ returns a vector of (r,g,b) random from 0.0 to 1.0
    """
    r = random(0.0,1.0)
    g = random(0.0,1.0)
    b = random(0.0,1.0)
    return vector(r,g,b)  # a color is a three-element tuple