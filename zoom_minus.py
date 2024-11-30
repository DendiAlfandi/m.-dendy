import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)
    
    for y in range(new_height):
        for x in range(new_width):
           
            ori_y = int(y / factor)
            ori_x = int(x / factor)
    
            ori_y = min(ori_y, height - 1) 
            ori_x = min(ori_x, width - 1)
            imgZoom[y, x] = image[ori_y, ori_x]
    
    return imgZoom

image = img.imread('D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s6\\tiger.jpg')

skala = 0.5

imgZoom = zoomMinus(image, skala)

img.imwrite("D:\\z.jpg", imgZoom)

# Menampilkan gambar asli dan gambar yang sudah diperkecil
plt.figure(figsize=(12, 6))

# Gambar asli dengan teks ukuran
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title(f'Original Image\nSize: {image.shape[0]}x{image.shape[1]}')
plt.axis('off')

# Gambar hasil zoom dengan teks ukuran
plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title(f'Zoom Minus (Reduced)\nSize: {imgZoom.shape[0]}x{imgZoom.shape[1]}')
plt.axis('off')

plt.show()
