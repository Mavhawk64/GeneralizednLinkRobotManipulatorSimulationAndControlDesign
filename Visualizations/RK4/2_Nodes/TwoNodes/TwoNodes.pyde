from math import *
from numpy import *
import matplotlib.pyplot as plt
from datetime import datetime
import os

# FOLDER_PATH = f"Output Files/{datetime.today().year}-{str(datetime.today().month).zfill(2)}-{str(datetime.today().day).zfill(2)}_{str(datetime.today().hour).zfill(2)}_{str(datetime.today().minute).zfill(2)}_{str(datetime.today().second).zfill(2)}"

# os.mkdir(FOLDER_PATH)

def M(x,y,m):
  s = 0
  for i in range(x,y+1):
    s += m[i-1]
  return s

def delta(p,n,m):
  return M(n,len(m),m) / M(p,len(m),m)

def c(p,N,l,m,theta,dottheta):
  cp = 0
  for i in range(p,N):
    n = i + 1
    cp += M(n,N,m) * l[p-1] * l[i] * dottheta[i] ** 2 * sin(theta[p-1] - theta[i])
  for j in range(1,p):
    cp -= M(p,N,m) * l[p-1] * l[j-1] * dottheta[j-1] ** 2 * sin(theta[j-1] - theta[p-1])
  return cp

def G(p,N,l,m,g,theta):
  return M(p,N,m) * l[p-1] * g * cos(theta[p-1])

# This is the element calculation of the M(Theta) matrix.
# x is the column, y is the row
def Mtrx(x,y,N,l,m,theta):
  return M(max(x,y),N,m) * l[x-1] * l[y-1] * cos(theta[min(x-1,y-1)] - theta[max(x-1,y-1)])

def Fatrx(p,N,thetaf,u,KP,KD,KI):
  return KP[p-1] * (thetaf[p-1] - u[N+p-1]) - KD[p-1] * u[2*N+p-1] + KI[p-1] * u[p-1]

# returns c(theta,dottheta), G(theta), and M(theta) as a tuple
def create_matrices(N,l,m,g,u,KP,KD,KI,thetaf):
  # u = [x1,x2,...,xN,t1,t2,...,tN,d1,d2,...,dN] = [u1,u2,...,u3N] -> [u[1-1=0],u[1],...,u[3N-1]]
  x, theta, dottheta = array_split(array(u),3)
  ctrx = []
  gtrx = []
  mtrx = []
  fatrx = []
  for i in range(0,N):
    ctrx.append([c(i+1,N,l,m,theta,dottheta)])
    gtrx.append([G(i+1,N,l,m,g,theta)])
    mtrx.append([])
    fatrx.append([Fatrx(i+1,N,thetaf,u,KP,KD,KI)])
    for j in range(0,N):
      mtrx[i].append(Mtrx(i+1,j+1,N,l,m,theta))
  return ctrx,gtrx,mtrx,fatrx

h = 0.1
t = 0
g = 0.01
times = [0]

# USER INPUTS

N = 3
thetaf = [pi / 4, pi / 4, pi / 4]

# OPTIONAL USER INPUTS

m = []
l = []
KP = [0,0,0]
KD = [0,0,0]
KI = [0,0,0]
u = []

#-- BEGIN PROGRAM --#

#-- FILL IN OPTIONAL PARAMETERS --#
if len(m) < N:
  for i in range(len(m),N):
    m.append(1)
if len(l) < N:
  for i in range(len(l),N):
    l.append(1)
if len(KP) < N:
  for i in range(len(KP),N):
    KP.append(10)
if len(KD) < N:
  for i in range(len(KD),N):
    KD.append(10)
if len(KI) < N:
  for i in range(len(KI),N):
    KI.append(10)
if len(u) < 3*N:
  for i in range(len(u),3*N):
    u.append(0)

def step():
  ctrx,gtrx,mtrx,fatrx = create_matrices(N,l,m,g,u,KP,KD,KI,thetaf)
  phi = matmul(-linalg.inv(mtrx),array(ctrx) + array(gtrx)) + array(fatrx)

  F = matmul(mtrx,fatrx)  

  tau = transpose(F)[0]
  ddt = transpose(phi)[0]


  k1 = []
  for j in range(0,N):
    k1.append(thetaf[j]-u[N+j])
  for j in range(0,N):
    k1.append(u[2*N+j])
  for j in ddt:
    k1.append(j)
  k1 = array(k1)

  k2 = []
  for j in range(0,N):
    k2.append(thetaf[j] - (u[N+j] + h/2 * k1[j]))
  for j in range(0,N):
    k2.append(u[2*N+j] + h/2 * k1[N+j])
  for j in range(0,N):
    k2.append(ddt[j] + h/2 * k1[2*N+j])
  k2 = array(k2)

  k3 = []
  for j in range(0,N):
    k3.append(thetaf[j] - (u[N+j] + h/2 * k2[j]))
  for j in range(0,N):
    k3.append(u[2*N+j] + h/2 * k2[N+j])
  for j in range(0,N):
    k3.append(ddt[j] + h/2 * k2[2*N+j])
  k3 = array(k3)

  k4 = []
  for j in range(0,N):
    k4.append(thetaf[j] - (u[N+j] + h * k3[j]))
  for j in range(0,N):
    k4.append(u[2*N+j] + h * k3[N+j])
  for j in range(0,N):
    k4.append(ddt[j] + h * k3[2*N+j])
  k4 = array(k4)


  u = u + multiply(k1 + multiply(k2,2) + multiply(k3,2) + k4,h/6)

def setup():
    size(800,800)
    
  
def draw():
    background(51)
    translate(width / 2, height / 2)
    step()
    line(0,0,100*l[0]*cos(u[0]),-100*l[0]*sin(u[0]))
    line(100*l[0]*cos(u[0]),-100*l[0]*sin(u[0]),100*l[0]*cos(u[0]) + 100*l[1]*cos(u[1]),-100*l[0]*sin(u[0]) - 100*l[1]*sin(u[1]))
    circle(100*l[0]*cos(u[0]),-100*l[0]*sin(u[0]),20)
    circle(100*l[0]*cos(u[0]) + 100*l[1]*cos(u[1]),-100*l[0]*sin(u[0]) - 100*l[1]*sin(u[1]),20)
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
