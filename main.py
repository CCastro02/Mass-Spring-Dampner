from vpython import *

m = 0.1
k = 10.5
g = vector(0, -9.8, 0)
L0 = 0.07
damping = 2

ground = box(pos=vector(0, L0, 0), length=0.4, height=0.005, width=0.005)

mass1 = sphere(pos=ground.pos-vector(.3*L0, L0, 0), radius=0.01,
               color=color.yellow, make_trail=True)

spring1 = helix(pos=ground.pos, axis=mass1.pos-ground.pos,
                radius=0.005, thickness=0.003, color=color.yellow)

mass2 = sphere(pos=ground.pos-vector(L0, 2.5*L0, 0), radius=0.01,
               color=color.red, make_trail=True)

spring2a = helix(pos=mass1.pos, axis=(mass2.pos-mass1.pos),
                 radius=0.005, thickness=0.003, color=color.orange)

spring2b = helix(pos=ground.pos, axis=mass2.pos-ground.pos,
                 radius=0.005, thickness=0.003, color=color.red)

mass3 = sphere(pos=ground.pos-vector(1.3*L0, 3.5*L0, 0), radius=0.01,
               color=color.blue, make_trail=True)

spring3 = helix(pos=mass2.pos, axis=mass3.pos-mass2.pos,
                radius=0.005, thickness=0.003, color=color.purple)

mass1.p = m*vector(0.5, 0, 0.7)
mass2.p = m*vector(0.2, 0, 0.4)
mass3.p = m*vector(0.5, 0, -0.7)

t = 0
dt = 0.01

while t < 5:
    rate(100)

    # Movement for mass and spring 1
    L1 = mass1.pos - ground.pos
    spring1.axis = L1
    F1 = -k*(mag(L1)-L0)*norm(L1) + m*g
    mass1.p = mass1.p + F1*dt
    mass1.pos = mass1.pos + mass1.p*dt/m

    # Movement for mass and spring 2a
    L2a = mass2.pos - mass1.pos
    spring2a.axis = L2a
    spring2a.pos = mass1.pos
    F2a = -k*(mag(L2a)-L0)*norm(L2a) + m*g - damping*mass2.p
    mass2.p = mass2.p + F2a*dt
    mass2.pos = mass2.pos + mass2.p*dt/m

    # Movement for spring 2b
    L2b = mass2.pos - ground.pos
    spring2b.axis = L2b
    F2b = -k*(mag(L2b)-L0)*norm(L2b) + m*g
    mass2.p = mass2.p + F2b*dt
    mass2.pos = mass2.pos + mass2.p*dt/m

    # Movement for mass and spring 3
    L3 = mass3.pos - mass2.pos
    spring3.axis = L3
    spring3.pos = mass2.pos
    F3 = -k*(mag(L3)-L0)*norm(L3) + m*g - damping*mass3.p
    mass3.p = mass3.p + F3*dt
    mass3.pos = mass3.pos + mass3.p*dt/m

    t = t + dt
