from precision import *

'''
Holds a vector in 3 dimensions. Four data members are allocated
to ensure alignment in an array.
'''
class Vector3:
    # Holds the value along the x axis.
    x: real
    # Holds the value along the y axis.
    y: real
    # Holds the value along the z axis.
    z: real

    # Padding to ensure 4-word alignment.
    __pad: real

    # The default constructor creates a zero vector.
    def __init__(self):
        self.x(0)
        self.y(0)
        self.z(0)

    # The explicit constructor creates a vector with the given components.
    def __init__(self, x, y, z):
        self.x(x)
        self.y(y)
        self.z(z)

    def invert(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    # Gets the magnitude of this vector.
    def magnitude(self) -> real: 
        return real_sqrt(self.x*self.x+self.y*self.y+self.z*self.z)

    # Gets the squared magnitude of this vector.
    def squareMagnitude(self) -> real:
        return self.x*self.x+self.y*self.y+self.z*self.z

    # Turns a non-zero vector into a vector of unit length.
    def normalize(self):
        l: real = self.magnitude()
        if (l > 0):
            l = real(1)/l
    
    # Multiplies this vector by the given scalar.
    def operator (self, value: real):
        self.x *= value
        self.y *= value
        self.z *= value

    # Returns a copy of this vector scaled to the given value.
    def operator(self, value: real):
        return Vector3(self.x*value, self.y*value, self.z*value)

    # Adds the given vector to this.
    def operator(self, v: "Vector3"):
        self.x += v.x
        self.y += v.y
        self.z += v.z

    # Returns the value of the given vector added to this.
    def operator(self, v: "Vector3"):
        return Vector3(self.x+v.x, self.y+v.y, self.z+v.z)

    # Subtracts the given vector from this.
    def operator(self, v: "Vector3"):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        
    # Returns the value of the given vector subtracted from this.
    def operator(self, v: "Vector3"):
        return Vector3(self.x-v.x, self.y-v.y, self.z-v.z)

    # Adds the given vector to this, scaled by the given amount.
    def addScaledVector(self, vector: "Vector3", scale: real):
        self.x += vector.x * scale
        self.y += vector.y * scale
        self.z += vector.z * scale

    '''
    Calculates and returns a component-wise product of this
    vector with the given vector.
    '''
    def componentProduct(self, vector: "Vector3"):
        return Vector3(self.x * vector.x, self.y * vector.y, self.z * vector.z)

    '''
    Performs a component-wise product with the given vector and
    sets this vector to its result.
    '''
    def componentProductUpdate(self, vector: "Vector3"):
        self.x *= vector.x
        self.y *= vector.y
        self.z *= vector.z

    '''
    Calculates and returns the scalar product of this vector
    with the given vector.
    '''
    def scalarProduct(self, vector: "Vector3") -> real:
        return self.x*vector.x + self.y*vector.y + self.z*vector.z

    '''
    Calculates and returns the scalar product of this vector
    with the given vector.
    '''
    def operator (self, vector: "Vector3") -> real:
        return self.x*vector.x + self.y*vector.y + self.z*vector.z

    '''
    Calculates and returns the vector product of this vector
    with the given vector.
    '''
    def vectorProduct(self, vector: "Vector3"):
        return Vector3(self.y*vector.z-self.z*vector.y,
            self.z*vector.x-self.x*vector.z,
            self.x*vector.y-self.y*vector.x)

    '''
    Updates this vector to be the vector product of its current
    value and the given vector.
    '''
    def operator (self, vector: "Vector3"):
        vector = self.vectorProduct(vector)
    
    '''
    Calculates and returns the vector product of this vector
    with the given vector.
    '''
    def operator(self, vector: "Vector3"):
        return Vector3(self.y*vector.z-self.z*vector.y,
            self.z*vector.x-self.x*vector.z,
            self.x*vector.y-self.y*vector.x)