import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import argparse
import sys
import os



def convolve2d_gray(image , kernel):    

    image = np.asarray(image, dtype = np.float64)
    kernel = np.asarray(kernel, dtype=np.float64)

    

   

    height, width = image.shape

    padded = np.pad(image , pad_width=1 , mode= "constant" , constant_values=0)

   

    flipped_kernel = kernel[::-1,::-1]

    output = np.zeros((height,width),dtype= np.float64)

    for row in range (height) :
        for col in range (width):
            region = padded [row:row + 3 , col:col +3]
            output[row ,col] = np.sum(region * flipped_kernel)
    return output.astype(np.uint8) 



def main():
    parser = argparse.ArgumentParser(description="ابزار پردازش تصویر با کرنل‌های مختلف")

    parser.add_argument(
        "-i" , "--input",
        type=str,
        required=True,
        help="مسیر فایل تصویر ورودی"
    )

    parser.add_argument(
        "-k","--kernel",
        type=str,
        choices=["mean","gaussian","sharpen","sobel_h","sobel_v","sobel_mag"],
        required=True,
        help="نوع کرنل برای اعمال"

    )

    parser.add_argument(
        "-o","--output",
        type=str,
        default=None,
        help="فایل خروجی (اختیاری)"

    )

    args = parser.parse_args()
    try :
        img = Image.open(args.input).convert('L')
        img_array=np.array(img, dtype=np.float64)

    except FileNotFoundError :
        print(f"فایلی با نام'{args.input}' یافت نشد")
        sys.exit(1)
    
    kernel_library ={
        "mean": np.ones((3,3))/9.0,
        "gaussian":np.array([[1,2,1],[2,4,2],[1,2,1]])/16.0,
        "sharpen":np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
        "sobel_h":np.array([[-1,0,1],[-2,0,2],[-1,0,1]]),
        "sobel_v":np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    }            

    if args.kernel == "sobel_mag":
        h = convolve2d_gray(img_array ,kernel_library["sobel_h"])
        v = convolve2d_gray(img_array , kernel_library["sobel_v"]) 
        result = np.sqrt(h**2 + v**2)

    else:
        result = convolve2d_gray(img_array , kernel_library[args.kernel])



        # نمایش را حذف کنید و به جایش ذخیره کنید
    
    if args.output:
        plt.imsave(args.output, result, cmap='gray')
        print(f"عملیات با موفقیت انجام شد. تصویر در فایل '{args.output}' ذخیره شد.")

    else:
        print("ℹ️ نامی برای خروجی مشخص نشده، تصویر نمایش داده نمی‌شود...")
        plt.imshow (result , cmap="gray")
        plt.title(f"Image:{args.input} | kernel : {args.kernel}")
        plt.show

if __name__ == "__main__" :
    main()       
            





#  if image.ndim != 2 :
#         raise ValueError("تصویر باید دو بعدی و خاکستری باشد")
#     if kernel.shape != (3,3):
#         raise ValueError("ابعاد کرنل باید دقیقاً ۳×۳ باشد.")



#            # print(f"چاپ شده قسمت ایمیج:{image}")
#             #print("_" * 20)

#            # print(f"چاپ شده قسمت پدد:{padded}")
#            # print("____________________________________")

#            # print(f"چاپ شده قسمت خروجی:{output[row , col]}")

            


#     output = np.clip(output , 0 , 255)
#     print(f"تعداد کل تکرارها: {image.shape[0] * image.shape[1]}")
#     print(f"چاپ شده قسمت ایمیج:{image}")
#     print("_" * 20)
#     print(f"چاپ شده قسمت پدد:{padded}")
#     print("_" * 20)
#     print(f"چاپ شده قسمت خروجی:{output}")



# img = Image.open('input.jpg').convert('L')
# img_array = np.array (img)   


# kernel_edge = np.array([[-1, -1,-1],
#                         [-1,8,-1],
#                         [-1,-1,-1]])

# result = convolve2d_gray(img_array, kernel_edge)


# fig , ax = plt.subplots(1,2,figsize=(10 ,5))
# ax[0].imshow(img_array, cmap='magma')
# ax[0].set_title('Orginal Image')
# ax[1].imshow(result, cmap='magma')
# ax[1].set_title('Processed Image')
# plt.show()

# Image.fromarray(result).save('output.jpg')