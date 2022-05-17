import math
import conv
import matplotlib.pyplot as plt
import numpy as np

print("Enter the number of samples")
N = int(input("Number of samples: "))
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

h_impulse = []

print("Compute the Impulse Response ")

# iterating till the range
for i in range(0, 30):
    if(i == 0):
        ele = 1 * 2 / N
    else:
        first =1/math.pi 
        sec = 2*math.pi/N
        ele = (first/i) * math.sin(sec*i)
        
    if(ele is not None):
        h_impulse.append(ele) # adding the element


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
	


