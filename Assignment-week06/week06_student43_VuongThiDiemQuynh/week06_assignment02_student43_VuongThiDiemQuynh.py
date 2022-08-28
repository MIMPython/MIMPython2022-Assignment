'''
Bài tập 2. (numpy methods)
Một số hàm trong thư viện numpy được liệt kê dưới đây.

- mean, median
- max, min
- argmax, argmin
- linspace, arange
- repeat, random
- all, any
- ones, zeros
- savetxt, loadtxt
- apply_along_axis
- where
- isclose
- polyfit, polyval
- roots
Hãy tìm hiểu một số hàm trong thư viện numpy (không nhất thiết thuộc danh sách trên) và thực hiện những yêu cầu sau:

Nêu ý nghĩa của hàm, cho ví dụ.
Viết chương trình thực hiện đúng ý nghĩa đó mà hạn chế sử dụng thư viện numpy. Có thể sử dụng thư viện để khởi tạo mảng số nếu cần thiết.
So sánh tốc độ thực thi giữa hai cách làm: phương pháp thủ công và phương pháp sử dụng numpy.
'''

# dtype: Checking the Data Type of an Array
'''
Example
Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
'''
'''

FUNCTION	DESCRIPTION
add()	Add arguments element-wise.
positive()	Numerical positive, element-wise.
negative()	Numerical negative, element-wise.
multiply()	Multiply arguments element-wise.
power()	First array elements raised to powers from second array, element-wise.
subtract()	Subtract arguments, element-wise.
true_divide()	Returns a true division of the inputs, element-wise.
floor_divide()	Return the largest integer smaller or equal to the division of the inputs.
float_power()	First array elements raised to powers from second array, element-wise.
mod()	Return the element-wise remainder of division.
remainder()	Return element-wise remainder of division.
divmod()	Return element-wise quotient and remainder simultaneously.
convolve()	Returns the discrete, linear convolution of two one-dimensional sequences.
sqrt()	Return the non-negative square-root of an array, element-wise.
square()	Return the element-wise square of the input.
absolute()	Calculate the absolute value element-wise.
fabs()	Compute the absolute values element-wise.
sign()	Returns an element-wise indication of the sign of a number.
interp()	One-dimensional linear interpolation.
maximum()	Element-wise maximum of array elements.
minimum()	Element-wise minimum of array elements.
real_if_close()	If complex input returns a real array if complex parts are close to zero.
nan_to_num()	Replace NaN with zero and infinity with large finite numbers.
heaviside()	Compute the Heaviside step function.

apply_along_axis(func1d, axis, arr, *args, ...) Apply a function to 1-D slices along the given axis.

apply_over_axes(func, a, axes) Apply a function repeatedly over multiple axes.

vectorize(pyfunc[, otypes, doc, excluded, ...]) Generalized function class.

frompyfunc(func, /, nin, nout, *[, identity]) Takes an arbitrary Python function and returns a NumPy ufunc.

piecewise(x, condlist, funclist, *args, **kw) Evaluate a piecewise-defined function.

'''

# So sanh
#  Dung numpy:
import numpy as np

a = np.array([[0, 1, 6],[2, 4, 1]])
maxValue = np.max(a)
print(maxValue) # 6

# Khong dung numpy:
def getMax(array):
    maxValue = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if maxValue < array[i][j]:
                maxValue = array[i][j]
    return maxValue

print(getMax(a)) # 6