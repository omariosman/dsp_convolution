def pad_zeros(n, lst):
    for i in range(n-1):
        lst.append(0)

# creating an empty list

def conv_preprocessing():

    x_input = []

    print("Input signal")
    # number of elements as input
    Lx = int(input("Enter number of elements : "))


    # iterating till the range
    for i in range(0, Lx):
        ele = int(input())

        x_input.append(ele) # adding the element
        
    print(x_input)




    # creating an empty list
    h_impulse = []

    print("Impulse Response ")

    # number of elements as input
    Lh = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, Lh):
        ele = int(input())

        h_impulse.append(ele) # adding the element
        

def custom_convolute(Lx, Lh, x_input, h_impulse):
    print("before: ", h_impulse)
    h_impulse.reverse()
    print("after: ", h_impulse)


    #create signal input with zero paddings
    x_signal = []

    pad_zeros(Lh, x_signal)

    for i in range(len(x_input)):
        x_signal.append(x_input[i])

    pad_zeros(Lh, x_signal)


    print("x signal: ", x_signal)

#calculate Ly

    Ly = Lx + Lh - 1
    y = []

    for i in range(Ly):
        y.append(0)

    for i in range(Ly):
        for j in range(Lh):
            y[i] += h_impulse[j] * x_signal[i+j]

    print("output: ", y)
    return y





#my_output = custom_convolute(Lx, Lh, x_input, h_impulse)
#print("out: ", my_output)



"""
Ly = Lx + Lh - 1

y = []

for i in range(Ly):
    y.append(0)

for i in range(Ly):
    for j in range(Lh):
        y[i] += h_impulse[j] * x_signal[i+j]

print("output: ", y)
"""


