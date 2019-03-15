import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import matplotlib.pyplot as plt
# Lra=139
# u=1
# rList=[]
# xyzList=[[],[],[]]
# n=0
# for i in np.linspace(0,Lra,Lra*10):
#     Xu=cmath.exp(complex(0,-1)*cmath.pi*u*i*(i+1)/Lra)
#     print((i,Xu.real,Xu.imag))
#     rList.append((i,Xu.real,Xu.imag))
#     xyzList[0].append(i)
#     xyzList[1].append(Xu.real)
#     xyzList[2].append(Xu.imag)
# fig=plt.figure()
# ax=fig.gca(projection='3d')
# # for xyz in rList:
# #     ax.scatter(xyz[0],xyz[1],xyz[2],c='r')
# ax.plot(xyzList[0],xyzList[1],xyzList[2], label='parametric curve')
# plt.savefig("3d_image.png")
# plt.show()

x=np.linspace(0,5,400)
z=np.linspace(0,75,25)
fig=plt.figure()
ax=fig.gca(projection='3d')
yy=0
for i in z:
    y=np.cos(i*x)
    yy+=y
    ax.plot(y,x,i+1, label='parametric curve')
ax.plot(yy,x,0, label='parametric curve')
plt.show()