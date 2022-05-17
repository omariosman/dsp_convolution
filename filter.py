import math
import conv
import matplotlib.pyplot as plt
import numpy as np


h_impulse = []

#Low-pass filter
def low_pass_filter():
    N = int(input("Enter the number of samples: "))
    omega = 2*math.pi/N
    for n in range(0, 30):
        if(n == 0):
            ele = 1 * 2 / N
        else:
            one_over_pi =1/math.pi 
            ele = (one_over_pi*1/n) * math.sin(omega*n)
            
        if(ele is not None):
            h_impulse.append(ele) # adding the element


#High-pass filter
def high_pass_filter():
    N = int(input("Enter the number of samples: "))
    omega = 2*math.pi/N
    for n in range(0, 30):
        if(n == 0):
            ele = 1- (omega / math.pi)
        else:
            numerator = math.sin(omega * n)
            deno = math.pi * n
            ele = -1 * (numerator / deno) 
            
        if(ele is not None):
            h_impulse.append(ele) # adding the element

#Band-pass filter
def band_pass_filter():
    N_first = int(input("Enter N1: "))
    N_second = int(input("Enter N2: "))
    omega_c1 = 2 * math.pi / N_first
    omega_c2 = 2 * math.pi / N_second
    
    for n in range(0, 30):
        if(n == 0):
            ele = (omega_c2 - omega_c1) / math.pi
        else:
            deno = math.pi * n
            first_part = (math.sin(omega_c1 * n)) / (deno)
            second_part = (math.sin(omega_c2 * n)) / (deno)
            ele = first_part - second_part
            
        if(ele is not None):
            h_impulse.append(ele) # adding the element

#Band-stop filter
def band_stop_filter():
    N_first = int(input("Enter N1: "))
    N_second = int(input("Enter N2: "))
    omega_c1 = 2 * math.pi / N_first
    omega_c2 = 2 * math.pi / N_second
    
    for n in range(0, 30):
        if(n == 0):
            ele = 1- (omega_c2 - omega_c1) / math.pi
        else:
            deno = math.pi * n
            first_part = (math.sin(omega_c2 * n)) / (deno)
            second_part = (math.sin(omega_c1 * n)) / (deno)
            ele = first_part - second_part
            
        if(ele is not None):
            h_impulse.append(ele) # adding the element


print("The available filter options")
print("1. Low-pass filter")
print("2. High-pass filter")
print("3. Band-pass filter")
print("4. Band-stop filter")
filter_type_input = input("Enter the type of the filter: ")
if(filter_type_input == "1"):
    low_pass_filter()
elif(filter_type_input == "2"):
    high_pass_filter()
elif(filter_type_input == "3"):
    band_pass_filter()
elif(filter_type_input == "4"):
    band_stop_filter()
else:
    print("This type is not available")


# creating an empty list
x_input = []

print("Input signal")
# number of elements as input
Lx = int(input("Enter number of elements : "))

print("Taking Filter paramaters ...")


# iterating till the range
for i in range(0, Lx):
	ele = int(input())

	x_input.append(ele) # adding the element
	
print(x_input)

print("Impulse repsonse")
print(x_input)
h_graph = plt.figure(1)
plt.title('x input signal')
plt.xlabel("n")
plt.ylabel("x[n]")
plt.stem(np.arange(len(x_input)), x_input)

#calcualate the h[n]
print("Compute the Impulse Response ")




print("Impulse repsonse")
print(h_impulse)
h_graph = plt.figure(2)
plt.title('h impulse response')
plt.xlabel("n")
plt.ylabel("h[n]")
plt.stem(np.arange(30), h_impulse)
#plt.show()
	

#custom_convolute(Lx, Lh, x_signal, h_impulse):

convolution_output = conv.custom_convolute(Lx, Lx, x_input, h_impulse)
print("convlution: ", convolution_output)
y_graph = plt.figure(3)
plt.title('y output')
plt.xlabel("n")
plt.ylabel("y[n]")
plt.stem(np.arange(len(convolution_output)), convolution_output)
plt.show()
	


