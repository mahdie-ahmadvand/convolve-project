import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def convolve2d_gray(image , kernel):    

    image = np.asarray(image, dtype = np.float64)
    kernel = np.asarray(kernel, dtype=np.float64)

    

    if image.ndim != 2 :
        raise ValueError("تصویر باید دو بعدی و خاکستری باشد")
    if kernel.shape != (3,3):
        raise ValueError("ابعاد کرنل باید دقیقاً ۳×۳ باشد.")

    height, width = image.shape

    padded = np.pad(image , pad_width=1 , mode= "constant" , constant_values=0)

   

    flipped_kernel = kernel[::-1,::-1]

    output = np.zeros((height,width),dtype= np.float64)

    for row in range (height) :
        for col in range (width):
            region = padded [row:row + 3 , col:col +3]
            output[row ,col] = np.sum(region * flipped_kernel)


           # print(f"چاپ شده قسمت ایمیج:{image}")
            #print("_" * 20)

           # print(f"چاپ شده قسمت پدد:{padded}")
           # print("____________________________________")

           # print(f"چاپ شده قسمت خروجی:{output[row , col]}")

            


    output = np.clip(output , 0 , 255)
    print(f"تعداد کل تکرارها: {image.shape[0] * image.shape[1]}")
    print(f"چاپ شده قسمت ایمیج:{image}")
    print("_" * 20)
    print(f"چاپ شده قسمت پدد:{padded}")
    print("_" * 20)
    print(f"چاپ شده قسمت خروجی:{output}")

    return output.astype(np.uint8) 

img = Image.open('input.jpg').convert('L')
img_array = np.array (img)   


kernel_edge = np.array([[-1, -1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])

result = convolve2d_gray(img_array, kernel_edge)


fig , ax = plt.subplots(1,2,figsize=(10 ,5))
ax[0].imshow(img_array, cmap='magma')
ax[0].set_title('Orginal Image')
ax[1].imshow(result, cmap='magma')
ax[1].set_title('Processed Image')
plt.show()

Image.fromarray(result).save('output.jpg')