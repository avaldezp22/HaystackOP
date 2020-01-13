from vpython import *
#myell = ellipsoid(pos=vector(0,0,0),length=8, height=8, width=3)
scene.background = color.gray(0.8)
scene.forward = vec(0,-0.2,-1)
scene.fov = 0.2
scene.range = 3.8
scene.caption ="""To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
"""
'''
E1 = extrusion(path=[vec(0,0,0), vec(0,0,-0.7)], texture=textures.wood_old,
    shape=[ shapes.circle(radius=3),
            shapes.triangle(pos=[0,-0.6], length=1.),
            shapes.trapezoid(pos=[0,0.6], width=1.6,
              height=1, top=0.6) ], pos=vec(0,0,0))
'''
copper = vec(0.722,0.451,0.200)
E2 = extrusion(path=paths.arc(radius=1, angle2=pi), texture=textures.metal,
    shape=[ [shapes.triangle(length=2), shapes.circle(pos=[0,.5], radius=0.2),
    shapes.trapezoid(pos=[0,-0.2],
    width=0.6, height=0.4)],
    [shapes.rectangle(pos=[0,1.8],
    width=1,height=0.3)] ],
    start_face_color=copper, end_face_color=copper)
E2center = E2.pos    # initial pos of center of extrusion
E2.pos = vec(3,2,0)  # new pos of center of extrsion
E2rot = E2.pos+vec(0,0,-E2center.z) # a location at the front of the extrusion


run = True

scene.waitfor('textures')

t = 0
dt = 0.01
dtheta = 0.01
while True:
    rate(100)
    if run:
        #E1.rotate(angle=dtheta, axis=vec(0,1,0))
        E2.rotate(angle=-dtheta, axis=vec(1,0,0), origin=E2rot)

        t += dt
