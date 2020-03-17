import scipy.io as sio
import numpy as np

import matplotlib.pyplot as plt

file_read1 = sio.loadmat('/local-scratch/ROV_6d_TEB/V_value_100.mat')

V = file_read1['V_array']

print("Read t = 20 array")
print(V.shape)
print("Getting maximum values")
count =0
for i in [7, 19]:
  for j in [7, 19]:
    for k in [7, 19]:
      for l in [10, 20]:
         count += 1
         V = file_read1['V_array']
         V = V[:, :, i, j, k, l]

         # plotting preparation
         x_alpha = np.linspace(-5.0, 5.0, num = 25)
         z_alpha = np.linspace(-5.0, 5.0, num = 25)
         X, Y = np.meshgrid(x_alpha, z_alpha)

         fig = plt.figure(figsize = (6,5))
         left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
         ax = fig.add_axes([left, bottom, width, height])

         cp = ax.contourf(X, Y, V)
         plt.colorbar(cp)
         if l == 10:
             val4 = 6
         else:
             val4 = 10

         if k == 7:
             val3 = -2.5
         else:
             val3 = 2.5
         if j == 7:
             val2 = -0.35
         else:
             val2 = 0.35
         if i == 7:
             val1 = -0.25
         else:
             val1 = 0.25
             
         #ax.clabel(cp, inline= True, fontsize=10)
         ax.set_title('Distances at t = 20s, u_r = {:2f}, w_r = {:2f}, x, = {:2f}, z = {:2f}'.format(val1, val2, val3, val4))
         ax.set_xlabel('x_alpha')
         ax.set_ylabel('z_alpha')
         #plt.show()
         print("Saving plots")
         fig.savefig('plot2{:d}.png'.format(count))
