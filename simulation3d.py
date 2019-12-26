from vpython import *

ball= sphere(pos=vector(-5,0,0,),radius=0.5,color=color.green)
ball.trail = curve(color=ball.color)

wallR = box (pos=vector(6,0,0),size=vector(0.1,12,12),color = color.blue)
wallL = box (pos=vector(-6,0,0),size=vector(0.1,12,12),color = color.blue)
wallU = box (pos=vector(0,6,0),size=vector(12,0.1,12),color = color.red)
wallD = box (pos=vector(0,-6,0),size=vector(12,0.1,12),color = color.red)
wallB = box (pos=vector(0,0,-6),size=vector(12,12,0.1),color = color.orange)


ball.velocity=vector(25,5,15)
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)

deltat= 0.005
t=0
#scene.autoscale = False
#while t<3:
while True:
    rate(100)
    ball.trail.append(pos =ball.pos)
    ball.pos = ball.pos+ball.velocity*deltat
    #if wallR.pos.x<ball.pos.x :
    #    ball.velocity.x = -ball.velocity.x
    if not(wallR.pos.x>ball.pos.x> -wallR.pos.x):
        ball.velocity.x = -ball.velocity.x

    if not(wallU.pos.y>ball.pos.y> -wallU.pos.y):
        ball.velocity.y = -ball.velocity.y

    #print (ball.pos.z)
    if not(6>ball.pos.z> -6):
        ball.velocity.z = -ball.velocity.z

    #t= t+ deltat
    #print(t)
