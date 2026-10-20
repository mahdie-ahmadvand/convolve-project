# convolve-project
porogram that do convolution processing


Zero padding is used to keep the output size equal to the input image size. As a result, edge pixels are also processed; areas outside the image are treated as zero during calculation.

Convolution can produce negative values or values greater than 255. Using np.clip, the values are restricted to the range [0, 255] and then converted to uint8.

For mathematical convolution, the kernel is rotated by 180 degrees. If “convolution” in your problem context refers to common image filtering, it often implies cross-correlation in practice; in that case, remove the flipped_kernel = ... line and use the kernel directly.


