#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


t = np.linspace(0,2*np.pi,100000)
t2 = np.linspace(0,np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*(np.exp(1j*w*t).imag+np.exp(1j*w*t2).real)
y = 5*(np.exp(1j*w*t).imag+np.exp(1j*w*t2).imag)
z = 5*np.exp(1j*w*t).real

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[3]:


t = np.linspace(0,2*np.pi,1000000)

x = 0
y = 0

w = 10

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*x).real

plt.plot(x,y)


# In[4]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 1

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).imag
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*x).imag
z = 5*np.exp(1j*w*x).real

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[5]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*x).real
z = t

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[6]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*x).real
z = t

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[7]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).real**2+np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag**2+np.exp(1j*w*x).real
z = t

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[8]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).imag
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*y).imag
z = 5*np.exp(1j*w*x).real

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[9]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).imag*np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag*np.exp(1j*w*x).imag
z = 5*np.exp(1j*w*x).real

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[10]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 5

x = 5*np.exp(1j*w*t).imag*np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag*np.exp(1j*w*x).imag
z = 5*np.exp(1j*w*x).real

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[11]:


t = np.linspace(0,2*np.pi,100000)

x = 0
y = 0
z = 0

w = 10

x = 5*np.exp(1j*w*t).real+np.exp(1j*w*x).real
y = 5*np.exp(1j*w*t).imag+np.exp(1j*w*x).real
z = t

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)


# In[12]:


import math


def fibonacci_sphere(samples, amplitude, xc, yc, zc):

    points = []
    phi = np.pi * (3. - np.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = amplitude[i]*(1 - (i / float(samples - 1)) * 2)  # y goes from 1 to -1
        radius = np.sqrt(amplitude[i]**2 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        points.append((x+xc, y+yc, z+zc))

    return np.transpose(points)


# In[13]:


lamb = 1E-10
Nbody = 200
xyz = np.linspace(-1,1,Nbody)
A = 100*np.cos(2*np.pi/lamb * xyz)

s = fibonacci_sphere(Nbody,A,10,10,10)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(s[0],s[1],s[2], alpha = np.mean(abs(A)))

ax.scatter3D(s[0],s[1],s[2], color = 'r')


# In[14]:


Nbody = 100
xyz = np.linspace(-1,1,Nbody)

lamb1 = 1E-300
A1 = 50*np.cos(2*np.pi/lamb1 * xyz) # wave function amplitude
s1 = fibonacci_sphere(Nbody,A1,-50,-50,-50)


lamb2 = 1E300
A2 = 100*np.cos(2*np.pi/lamb2 * xyz) # wave function amplitude
s2 = fibonacci_sphere(Nbody,A2,50,50,50)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(s1[0],s1[1],s1[2], alpha = np.mean(abs(A1)))
ax.plot3D(s2[0],s2[1],s2[2], alpha = np.mean(abs(A2)))


# In[15]:


fig = plt.figure()
ax = plt.axes(projection='3d')

s = np.zeros([Nbody,2*Nbody])
s[0] = np.append(s1[0],s2[0])
s[1] = np.append(s1[1],s2[1])
s[2] = np.append(s1[2],s2[2])

ax.plot3D(s[0],s[1],s[2])

ax.scatter3D(s[0],s[1],s[2],color = 'r')


# In[16]:


Nbody = 1000
xyz = np.linspace(-1,1,Nbody)

lamb1 = 1E1
A1 = 100*np.cos(2*np.pi/lamb1 * xyz) # wave function amplitude
s1 = fibonacci_sphere(Nbody,A1,0,0,0)


lamb2 = 1E1
A2 = 100*np.cos(2*np.pi/lamb2 * xyz) # wave function amplitude
s2 = fibonacci_sphere(Nbody,A2,500,500,0)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(s1[0],s1[1],s1[2], alpha = np.mean(abs(A1)))
ax.plot3D(s2[0],s2[1],s2[2], alpha = np.mean(abs(A2)))


# In[17]:


# Sequence

fig = plt.figure()
ax = plt.axes(projection='3d')

s = np.zeros([Nbody,2*Nbody])
s[0] = np.append(s1[0],s2[0])
s[1] = np.append(s1[1],s2[1])
s[2] = np.append(s1[2],s2[2])


xyz = np.linspace(-1,1,2*Nbody)

ax.plot3D(s[0],s[1],s[2])
ax.scatter3D(s[0],s[1],s[2], color = 'r')


# In[18]:


# Summation

fig = plt.figure()
ax = plt.axes(projection='3d')

s = np.zeros([Nbody,Nbody])
s[0] = (s1[0]+s2[0])
s[1] = (s1[1]+s2[1])
s[2] = (s1[2]+s2[2])

s = s 

ax.plot3D(s[0],s[1],s[2])
ax.scatter3D(s[0],s[1],s[2], color = 'r')


# In[19]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 656

s = np.zeros([Nbody-T,2*(Nbody-T)])
s[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
s[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
s[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])

s[0][2*Nbody-3*T:] = (s1[0][Nbody-T:]+s2[0][Nbody-T:])/2
s[1][2*Nbody-3*T:] = (s1[1][Nbody-T:]+s2[1][Nbody-T:])/2
s[2][2*Nbody-3*T:] = (s1[2][Nbody-T:]+s2[2][Nbody-T:])/2

ax.plot3D(s[0],s[1],s[2])
ax.scatter3D(s[0],s[1],s[2], color = 'r')


# In[20]:


import matplotlib.animation as animation


# In[21]:


from matplotlib import rc
rc('animation', html='jshtml')


# In[22]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 0

def frame(w):
    ax.clear()
    global T

    s = np.zeros([Nbody-T,2*(Nbody-T)])
    s[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
    s[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
    s[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])

    s[0][2*Nbody+1-3*T:] = (s1[0][Nbody+1-T:]+s2[0][Nbody+1-T:])//2
    s[1][2*Nbody+1-3*T:] = (s1[1][Nbody+1-T:]+s2[1][Nbody+1-T:])//2
    s[2][2*Nbody+1-3*T:] = (s1[2][Nbody+1-T:]+s2[2][Nbody+1-T:])//2

    ax.plot3D(s[0],s[1],s[2])
    plot = ax.scatter3D(s[0],s[1],s[2], color = 'r')

    T+=6

    return plot

plt.close()

anim = animation.FuncAnimation(fig, frame, frames=111, blit=False, repeat=True)
anim


# In[23]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 3

dt = 4

s = np.zeros([Nbody-T,2*(Nbody-T)])

# intial sequence
s[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
s[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
s[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])

# final summation
s[0][2*Nbody-3*T:] = (s1[0][Nbody-T:]+s2[0][Nbody-T:])/2
s[1][2*Nbody-3*T:] = (s1[1][Nbody-T:]+s2[1][Nbody-T:])/2
s[2][2*Nbody-3*T:] = (s1[2][Nbody-T:]+s2[2][Nbody-T:])/2

ax.plot3D(s[0],s[1],s[2])
ax.scatter3D(s[0],s[1],s[2], color = 'r')


# In[24]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 400

DT = 8
dt = DT
F = 111

def frame(w):
    ax.clear()
    global T
    global dt
    global DT
    global F

    s = np.zeros([Nbody-T,2*(Nbody-T)])
    s[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
    s[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
    s[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])


    s[0][2*Nbody+1-3*T:] = (s1[0][Nbody+1-T:]+s2[0][Nbody+1-T:])//(dt)
    s[1][2*Nbody+1-3*T:] = (s1[1][Nbody+1-T:]+s2[1][Nbody+1-T:])//(dt)
    s[2][2*Nbody+1-3*T:] = (s1[2][Nbody+1-T:]+s2[2][Nbody+1-T:])//(dt)

    ax.plot3D(s[0],s[1],s[2])
    plot = ax.scatter3D(s[0],s[1],s[2], color = 'r')
    
    #ax.axes.set_xlim3d(left=-150, right=150) 
    #ax.axes.set_ylim3d(bottom=-150, top=150) 
    #ax.axes.set_zlim3d(bottom=0, top=1200) 
    
    dt -= (DT-1)/F
    
    T+=0

    return plot

plt.close()

anim = animation.FuncAnimation(fig, frame, frames=F, blit=False, repeat=True)
anim


# In[25]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 0

DT = 7
dt = DT

def frame(w):
    ax.clear()
    global T
    global dt
    global DT

    s = np.zeros([Nbody-T,2*(Nbody-T)])
    s[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
    s[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
    s[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])


    s[0][2*Nbody+1-3*T:] = (s1[0][Nbody+1-T:]+s2[0][Nbody+1-T:])/(dt)
    s[1][2*Nbody+1-3*T:] = (s1[1][Nbody+1-T:]+s2[1][Nbody+1-T:])/(dt)
    s[2][2*Nbody+1-3*T:] = (s1[2][Nbody+1-T:]+s2[2][Nbody+1-T:])/(dt)

    ax.plot3D(s[0],s[1],s[2])
    plot = ax.scatter3D(s[0],s[1],s[2], color = 'r')
    
    dt -= (DT-1)/111
    
    T+=6

    return plot

plt.close()

anim = animation.FuncAnimation(fig, frame, frames=111, blit=False, repeat=True)
anim


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


Nbody = 1000
xyz = np.linspace(-1,1,Nbody)

lamb1 = 1E20
A1 = 20*np.cos(2*np.pi/lamb1 * xyz) # wave function amplitude
s1 = fibonacci_sphere(Nbody,A1,100,100,0)


lamb2 = 1E100
A2 = 100*np.cos(2*np.pi/lamb2 * xyz) # wave function amplitude
s2 = fibonacci_sphere(Nbody,A2,300,300,0)


lamb3 = 1E30
A3 = 50*np.cos(2*np.pi/lamb3 * xyz) # wave function amplitude
s3 = fibonacci_sphere(Nbody,A3,100,0,100)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(s1[0],s1[1],s1[2], alpha = np.mean(abs(A1)))
ax.plot3D(s2[0],s2[1],s2[2], alpha = np.mean(abs(A2)))
ax.plot3D(s3[0],s3[1],s3[2], alpha = np.mean(abs(A3)))


# In[27]:


# Sequence

fig = plt.figure()
ax = plt.axes(projection='3d')

w1 = np.zeros([Nbody,2*Nbody])

w1[0] = np.append(s1[0],s2[0])
w1[1] = np.append(s1[1],s2[1])
w1[2] = np.append(s1[2],s2[2])

w2 = np.zeros([Nbody,3*Nbody])

w2[0] = np.append(w1[0],s3[0])
w2[1] = np.append(w1[1],s3[1])
w2[2] = np.append(w1[2],s3[2])


xyz = np.linspace(-1,1,3*Nbody)

ax.plot3D(w2[0],w2[1],w2[2])
ax.scatter3D(w2[0],w2[1],w2[2], color = 'r')


# In[28]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 1

w1 = np.zeros([Nbody-T,2*(Nbody-T)])

w1[0][0:(2*Nbody-T)] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
w1[1][0:(2*Nbody-T)] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
w1[2][0:(2*Nbody-T)] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])

w2 = np.zeros([Nbody,3*Nbody])

w2[0][0:3*(Nbody-T)] = np.append(w1[0],s3[0][0:Nbody-T])
w2[1][0:3*(Nbody-T)] = np.append(w1[1],s3[1][0:Nbody-T])
w2[2][0:3*(Nbody-T)] = np.append(w1[2],s3[2][0:Nbody-T])
    
w2[0][3*Nbody-T:] = (s1[0][Nbody-T:]+s2[0][Nbody-T:]+s3[0][Nbody-T:])//1
w2[1][3*Nbody-T:] = (s1[1][Nbody-T:]+s2[1][Nbody-T:]+s3[0][Nbody-T:])//1
w2[2][3*Nbody-T:] = (s1[2][Nbody-T:]+s2[2][Nbody-T:]+s3[0][Nbody-T:])//1

    
ax.plot3D(w2[0],w2[1],w2[2])
plot = ax.scatter3D(w2[0],w2[1],w2[2], color = 'r')


# In[29]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 100

w1 = np.zeros([Nbody,2*(Nbody)])
    
w1[0] = np.append(s1[0],s2[0])
w1[1] = np.append(s1[1],s2[1])
w1[2] = np.append(s1[2],s2[2])

w2 = np.zeros([Nbody,3*Nbody])

w2[0][0:3*Nbody-T] = np.append(w1[0],s3[0][0:Nbody-T])
w2[1][0:3*Nbody-T] = np.append(w1[1],s3[1][0:Nbody-T])
w2[2][0:3*Nbody-T] = np.append(w1[2],s3[2][0:Nbody-T])

w2[0][3*Nbody-T:] = (s1[0][Nbody-T:]+s2[0][Nbody-T:]+s3[0][Nbody-T:])//3
w2[1][3*Nbody-T:] = (s1[1][Nbody-T:]+s2[1][Nbody-T:]+s3[0][Nbody-T:])//3
w2[2][3*Nbody-T:] = (s1[2][Nbody-T:]+s2[2][Nbody-T:]+s3[0][Nbody-T:])//3

    
ax.plot3D(w2[0],w2[1],w2[2])
plot = ax.scatter3D(w2[0],w2[1],w2[2], color = 'r')


# In[30]:


fig = plt.figure()
ax = plt.axes(projection='3d')

T = 0

def frame(w):
    ax.clear()
    global T
    
    w1 = np.zeros([Nbody-T,2*(Nbody-T)])

    w1[0] = np.append(s1[0][0:Nbody-T],s2[0][0:Nbody-T])
    w1[1] = np.append(s1[1][0:Nbody-T],s2[1][0:Nbody-T])
    w1[2] = np.append(s1[2][0:Nbody-T],s2[2][0:Nbody-T])

    w2 = np.zeros([Nbody,3*Nbody])

    w2[0][0:3*(Nbody-T)] = np.append(w1[0],s3[0][0:Nbody-T])
    w2[1][0:3*(Nbody-T)] = np.append(w1[1],s3[1][0:Nbody-T])
    w2[2][0:3*(Nbody-T)] = np.append(w1[2],s3[2][0:Nbody-T])

    w2[0][3*Nbody-T:] = (s1[0][Nbody-T:]+s2[0][Nbody-T:]+s3[0][Nbody-T:])//3
    w2[1][3*Nbody-T:] = (s1[1][Nbody-T:]+s2[1][Nbody-T:]+s3[0][Nbody-T:])//3
    w2[2][3*Nbody-T:] = (s1[2][Nbody-T:]+s2[2][Nbody-T:]+s3[0][Nbody-T:])//3

    #ax.axes.set_xlim3d(left=-250, right=100) 
    #ax.axes.set_ylim3d(bottom=-250, top=100) 
    #ax.axes.set_zlim3d(bottom=-100, top=150) 
    
    ax.plot3D(w2[0],w2[1],w2[2])
    plot = ax.scatter3D(w2[0],w2[1],w2[2], color = 'r')

    T+=5

    return plot

plt.close()

anim = animation.FuncAnimation(fig, frame, frames=996//5, blit=False, repeat=True)
anim


# In[ ]:





# In[ ]:





# In[ ]:




