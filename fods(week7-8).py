# 1. Write a program to generate a numpy array of numbers (e.g. [1, 2, 3, 4, 5]). Perform the numpy array operations on it such as:
# a)	Sum of elements in array
# b)	Average of elements in array
# c)	Identify maximum and minimum values in the array
import numpy as np

arr = np.array([9, 7, 6, 5, 10])

total_sum = np.sum(arr)

average = np.mean(arr)

max_value = np.max(arr)
min_value = np.min(arr)

print("Array:", arr)
print("Sum of elements:", total_sum)
print("Average of elements:", average)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
# 2. Write a program to input a array of numbers from the user (at least 10 elements in list), sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9.
numbers = []

print("Enter at least 10 numbers:")

while len(numbers) < 10:
    try:
        num = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.append(num)
    except ValueError:
        print("Please enter a valid integer.")

numbers.sort()

print("\nSorted list:", numbers)

slice_2_5 = numbers[2:6]  
slice_5_8 = numbers[5:9]  
slice_2_9 = numbers[2:10] 

print("Elements from index 2 to 5:", slice_2_5)
print("Elements from index 5 to 8:", slice_5_8)
print("Elements from index 2 to 9:", slice_2_9)

numbers = []

print("Enter at least 10 numbers:")

while len(numbers) < 10:
    try:
        num = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.append(num)
    except ValueError:
        print("Please enter a valid integer.")

numbers.sort()

print("\nSorted list:", numbers)

slice_2_5 = numbers[2:6]  
slice_5_8 = numbers[5:9]  
slice_2_9 = numbers[2:10] 

print("Elements from index 2 to 5:", slice_2_5)
print("Elements from index 5 to 8:", slice_5_8)
print("Elements from index 2 to 9:", slice_2_9)
# 3. Create an array of random integer numbers as a numpy array, sort them and perform operations such as reshaping of the array into matrix of feasible dimensions. (e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.) [Hint: Use the array of reshape (row * column) ]
import numpy as np

def input_matrix(rows, cols, name):
    print(f"\nEnter elements for {name} matrix:")
    elements = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        elements.append(row)
    return np.array(elements)

try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix1 = input_matrix(rows, cols, "first")
    matrix2 = input_matrix(rows, cols, "second")

    print("\nFirst Matrix:\n", matrix1)
    print("\nSecond Matrix:\n", matrix2)

    try:
        addition = np.add(matrix1, matrix2)
        print("\nAddition Result:\n", addition)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for addition.")

    try:
        subtraction = np.subtract(matrix1, matrix2)
        print("\nSubtraction Result:\n", subtraction)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for subtraction.")

    try:
        if matrix1.shape[1] != matrix2.shape[0]:
            raise ValueError("Matrix multiplication not possible. Columns of first must equal rows of second.")
        multiplication = np.dot(matrix1, matrix2)
        print("\nMultiplication Result:\n", multiplication)
    except ValueError as e:
        print("\nError:", e)

except Exception as e:
    print("\nAn error occurred:", e)

# 4. Write a program to input 2 matrices of certain dimensions and perform the matrix operations such as additions, subtraction, multiplication using numpy. Validation of matrix size should be done before the operations are performed. Mismatch of size for operations should raise the exception.
import numpy as np

def input_matrix(rows, cols, name):
    print(f"\nEnter elements for {name} matrix:")
    elements = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        elements.append(row)
    return np.array(elements)

try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix1 = input_matrix(rows, cols, "first")
    matrix2 = input_matrix(rows, cols, "second")

    print("\nFirst Matrix:\n", matrix1)
    print("\nSecond Matrix:\n", matrix2)

    try:
        addition = np.add(matrix1, matrix2)
        print("\nAddition Result:\n", addition)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for addition.")

    try:
        subtraction = np.subtract(matrix1, matrix2)
        print("\nSubtraction Result:\n", subtraction)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for subtraction.")

    try:
        if matrix1.shape[1] != matrix2.shape[0]:
            raise ValueError("Matrix multiplication not possible. Columns of first must equal rows of second.")
        multiplication = np.dot(matrix1, matrix2)
        print("\nMultiplication Result:\n", multiplication)
    except ValueError as e:
        print("\nError:", e)

except Exception as e:
    print("\nAn error occurred:", e)

# 5. Write a program to read the csv file “weight_height.csv” using Pandas. Plot the data as a scatterplot (weight vs height, age vs weight, height vs age, gender vs height, gender vs weight) using Matplotlib library.
import pandas as pd
import matplotlib.pyplot as plt

try:
    data = pd.read_csv("weight_height.csv")
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("Error: 'weight_height.csv' file not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the CSV file:", e)
    exit()

print("\nSample data:")
print(data.head())


plt.figure(figsize=(6, 4))
plt.scatter(data['Weight'], data['Height'], color='blue')
plt.title('Weight vs Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.grid(True)
plt.show()

# b) Age vs Weight
plt.figure(figsize=(6, 4))
plt.scatter(data['Age'], data['Weight'], color='green')
plt.title('Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(data['Height'], data['Age'], color='red')
plt.title('Height vs Age')
plt.xlabel('Height')
plt.ylabel('Age')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(data['Gender'], data['Height'], color='purple')
plt.title('Gender vs Height')
plt.xlabel('Gender')
plt.ylabel('Height')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(data['Gender'], data['Weight'], color='orange')
plt.title('Gender vs Weight')
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.grid(True)
plt.show()
# 6. Read the data from csv file “weight_height.csv” in a data frame using Pandas. Add 2 additional columns (BMI and Risk) in the existing dataframe. Add the data according to the calculations given below.
# 	BMI = Weight / Height
# 	Risk values vary according to the conditions given below:
# 		BMI less than 18.5 : Nutrient deficient
# 		BMI between 18.5 and 24.9: lower risk
# 		BMI between 25 and 29.9: Heart disease risk
# 		BMI between 30 and 34.9: Higher risk of diabetes, heart disease
# 		BMI 40 or higher: Serious health condition risk
import pandas as pd

# To read the CSV
try:
    df = pd.read_csv("weight_height.csv")
    print("\nLoaded data:")
    print(df)
except FileNotFoundError:
    print("Error: File not found.")
    exit()

df['Height_m'] = df['Height'] / 100
df['BMI'] = df['Weight'] / (df['Height_m'] ** 2)

def classify_risk(bmi):
    if bmi < 18.5:
        return "Nutrient deficient"
    elif 18.5 <= bmi <= 24.9:
        return "lower risk"
    elif 25 <= bmi <= 29.9:
        return "Heart disease risk"
    elif 30 <= bmi <= 34.9:
        return "Higher risk of diabetes, heart disease"
    elif bmi >= 40:
        return "Serious health condition risk"
    else:
        return "Unknown"

df['Risk'] = df['BMI'].apply(classify_risk)

print("\nData with BMI and Risk:")
print(df)


df.to_csv("weight_height_updated.csv", index=False)
print("\nUpdated file saved as 'weight_height_updated.csv'.")