import addition
import subtraction
import multiplication
import squareroot

print("Using addition")
x = addition.add_two_numbers(1, 2)
print("1 + 2 = " + str(x))

print("Using subtraction")
y = subtraction.subtract_two_numbers(5, 3)
print("5 - 3 = " + str(y))

print("Using multiplication")
z = multiplication.multiply_two_numbers(3, 4)
print("3 * 4 = " + str(z))

print("Using square root")
sqrt_result = squareroot.square_root(16)
print("Square root of 16 = " + str(sqrt_result))
