# 1.
import numpy as np

lst = [12.23, 13.32, 100, 36.32]
array_1d = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", array_1d)

# 2. 
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

# 3. 
null_vector = np.zeros(10)
print("Original vector:", null_vector)

null_vector[6] = 11
print("Updated vector:", null_vector)

# 4. array_12_38 = np.arange(12, 38)
print(array_12_38)

# 5. int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)

print("Original array:", int_array)
print("Array in float type:", float_array)

# 6. celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

#7. original = np.array([10, 20, 30])
appended = np.append(original, [40, 50, 60, 70, 80, 90])

print("Original array:", original)
print("After append:", appended)

# 8. 
random_array = np.random.rand(10)

print("Random array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))

# 9.
array_10x10 = np.random.rand(10, 10)

print("10x10 array:\n", array_10x10)
print("Minimum value:", np.min(array_10x10))
print("Maximum value:", np.max(array_10x10))

# 10. 

array_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 array:\n", array_3x3x3)


