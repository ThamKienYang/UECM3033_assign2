import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp

# function for picture compressing
def picture_compress(k):
    
    # copy the sigma so that no influence of previous
    r1 = Sigma_r.copy()
    g1 = Sigma_g.copy()
    b1 = Sigma_b.copy()
    
    # keep the rest k onwards non zero elements to zero
    r1[k:800] = np.zeros_like(Sigma_r[k:800])
    g1[k:800] = np.zeros_like(Sigma_g[k:800])
    b1[k:800] = np.zeros_like(Sigma_b[k:800])
    
    # change dimension for dot multiplication
    r2 = sp.linalg.diagsvd(r1,800,1000)
    g2 = sp.linalg.diagsvd(g1,800,1000)
    b2 = sp.linalg.diagsvd(b1,800,1000)
    
    # dot multiplication for new matrix
    r_new = np.dot(np.dot(U_r,r2), V_r)
    g_new = np.dot(np.dot(U_g,g2), V_g)
    b_new = np.dot(np.dot(U_b,b2), V_b)
    
    # new matrix image plotting
    img[:,:,0] = r_new
    img[:,:,1] = g_new
    img[:,:,2] = b_new
    
    fig2 = plt.figure(k)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()

# Load picture, split into 3 matrices for red, green and blue components
# and display the three components
img=mpimg.imread('chelsea.png')
[r,g,b] = [img[:,:,i] for i in range(3)]

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

# Sigma, U and V for reds, greens and blues
U_r, Sigma_r, V_r = sp.linalg.svd(r)
U_g, Sigma_g, V_g = sp.linalg.svd(g)
U_b, Sigma_b, V_b = sp.linalg.svd(b)

# None zero elements in Sigma for reds, greens and blues
nonzero_Sigma_r = np.count_nonzero(Sigma_r)
nonzero_Sigma_g = np.count_nonzero(Sigma_g)
nonzero_Sigma_b = np.count_nonzero(Sigma_b)
print("The non zero elements in Sigma are ",nonzero_Sigma_r," for red, "
        ,nonzero_Sigma_g, " for green and ",nonzero_Sigma_b, " for blue")
        
        
picture_compress(30)

picture_compress(200)