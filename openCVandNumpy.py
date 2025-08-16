import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg')

if img is None:
    print("Error: Could not read the image.")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.canvas.manager.set_window_title('Image Transformations')
    
    axes[0, 0].imshow(img_rgb)
    axes[0, 0].set_title('1. Original Image')
    axes[0, 0].axis('off')

    if len(img.shape) == 3:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = img
    axes[0, 1].imshow(img_gray, cmap='gray')
    axes[0, 1].set_title('2. Grayscale Image')
    axes[0, 1].axis('off')

    img_cmy = 255 - img
    img_cmy_rgb = cv2.cvtColor(img_cmy, cv2.COLOR_BGR2RGB)
    axes[1, 0].imshow(img_cmy_rgb)
    axes[1, 0].set_title('3. CMY Image')
    axes[1, 0].axis('off')
    
    img_inverted_gray = cv2.bitwise_not(img_gray)
    axes[1, 1].imshow(img_inverted_gray, cmap='gray')
    axes[1, 1].set_title('4. Inverted (Grayscale Negative) Image')
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print('All images are subplotted in a single window.')
