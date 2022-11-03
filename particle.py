from core import *
from precision import *

class Particle:
    '''
    Holds the linear position of the particle in
    world space.
    '''
    position: Vector3

    ''' 
    Holds the linear velocity of the particle in
    world space.
    '''
    velocity: Vector3

    '''
    Holds the acceleration of the particle. This value
    can be used to set acceleration due to gravity (its primary
    use) or any other constant acceleration.
    '''
    acceleration: Vector3

    '''
    Holds the amount of damping applied to linear
    motion. Damping is required to remove energy added
    through numerical instability in the integrator.
    '''
    damping: real

    '''
    Holds the inverse of the mass of the particle. It
    is more useful to hold the inverse mass because
    integration is simpler and because in real-time
    simulation it is more useful to have objects with
    infinite mass (immovable) than zero mass
    (completely unstable in numerical simulation).
    '''
    inverseMass: real