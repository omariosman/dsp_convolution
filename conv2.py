from tracemalloc import start
import matplotlib.pyplot as plt
import numpy as np



def pad_zeros(n, lst):
    for i in range(n-1):
        lst.append(0)



def delta_params(global_ctr, x_input):
    delta = []
    for i in range(1000):
        delta.append(0)
    shift = int(input("Enter the t0: "))
    delta[500-shift] = 1
    
    delta_graph = plt.figure(2)
    plt.title('impulse response')
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.stem(np.arange(-len(delta)/2, len(delta)/2, 1), delta)

    conv_output = []
    for i in range(500-shift):
        conv_output.append(0)
    print("size input: ", len(x_input))
    conv_output[500-shift:] = x_input
    print(len(conv_output), "sizeeeeeeeee")
    for i in range(1000-len(conv_output)):
        conv_output.append(1)
    
    output_graph = plt.figure(3)
    plt.title('output')
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.stem(np.arange(-len(conv_output)/2, len(conv_output)/2, 1), conv_output)
    
    #finished 
    plt.show()
    exit(0)


def draw_output(x_input, h_impulse):
    conv_output = custom_convolute(len(x_input), len(h_impulse), x_input, h_impulse)
    output_graph = plt.figure(3)
    plt.title('output')
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.stem(np.arange(-len(conv_output)/2, len(conv_output)/2, 1), conv_output)

    #finished 
    plt.show()


h_impulse = []
def take_impulse_manually():
    # creating an empty list
    print("Impulse Response ")

    # number of elements as input
    Lh = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, Lh):
        ele = int(input())
        h_impulse.append(ele) # adding the element
    
    h_graph = plt.figure(2)
    plt.title('impulse response function')
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.stem(np.arange(-len(h_impulse)/2, len(h_impulse)/2, 1), h_impulse)
    return h_impulse

x_input = []
def take_input_signal_manually():
    print("Input signal")
    # number of elements as input
    Lx = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, Lx):
        ele = int(input())
        x_input.append(ele) # adding the element
    
    x_graph = plt.figure(1)
    plt.title('Input function')
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.stem(np.arange(len(x_input)), x_input)
    return x_input

def unit_step_params(global_ctr):
    global global_input
    unit_step = []
    for i in range(1000):
        unit_step.append(0)
    shift = int(input("Enter the t0: "))
    for i in range(500-shift, 1000):
        unit_step[i] = 1
    u_graph = plt.figure(global_ctr)
    if (global_ctr == 1):
        plt.title('unit step function | x[n]')
    elif(global_ctr == 2):
        plt.title('unit step function | h[n]')
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.stem(np.arange(-500, 500, 1), unit_step)
    global_input = unit_step
    unit_step = unit_step[500-shift:]
    return unit_step
    #plt.show()

def rect_params(global_ctr):
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))
    amplitude = int(input("Enter the amplitude: "))
    rect = []
    width = end_limit - start_limit
    for i in range(width):
        rect.append(amplitude)
    rect_graph = plt.figure(global_ctr)
    if (global_ctr == 1):
        plt.title('rectangle function | x[n]')
    elif(global_ctr == 2):
        plt.title('rectangle function | h[n]')
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.stem(np.arange(start_limit, end_limit, 1), rect)
    return rect

def starter():
    global_ctr = 0
    print("^^^^^^^ ....... Welcome to our app ....... ^^^^^^^\n\n\n")
    print("\t 1. Enter the input signal manually")
    print("\t 2. Choose one of the known input signals")
    input_signal_choice = int(input("\nSelect one of either options: "))

    
    if(input_signal_choice == 1):
        x_input = take_input_signal_manually()

    elif(input_signal_choice == 2):
        print("\t 1. Unit step function")
        print("\t 2. Unit impulse function")
        print("\t 3. Triangle")
        print("\t 4. Rectangle")
        print("\t 5. Straight line\n")
        signal_choice = int(input("Choose the signal: "))

        
        if(signal_choice == 1):
            global_ctr = global_ctr + 1
            x_input = unit_step_params(global_ctr)
            
        elif(signal_choice == 2):
            global_ctr = global_ctr + 1
            x_input = delta_params(global_ctr)
        elif(signal_choice == 3):
            pass
        elif(signal_choice == 4):
            global_ctr = global_ctr + 1
            x_input = rect_params(global_ctr)
        elif(signal_choice == 5):
            pass           
        else:
            print("This is not avaiable")
            print("Try again!!!")
            starter()
    else:
        print("Try Again!!")
        starter()
    

    print("\nSelect one of either options: ")
    print("\t 1. Enter the impulse response manually")
    print("\t 2. Choose one of the known impulse response")
    impulse_choice = int(input("Choose an option: "))

    if(impulse_choice == 1):
    
        h_impulse = take_impulse_manually()

    elif (impulse_choice == 2):
        print("\t 1. Unit step function")
        print("\t 2. Unit impulse function")
        print("\t 3. Triangle")
        print("\t 4. Rectangle")
        print("\t 5. Straight line\n")
        signal_choice = int(input("Choose the signal: "))

        if(signal_choice == 1):
            global_ctr = global_ctr + 1
            h_impulse = unit_step_params(global_ctr)
            
        elif(signal_choice == 2):
            global_ctr = global_ctr + 1
            delta_params(global_ctr, x_input)
        elif(signal_choice == 3):
            pass
        elif(signal_choice == 4):
            global_ctr = global_ctr + 1
            h_impulse = rect_params(global_ctr)
        elif(signal_choice == 5):
            pass           
        else:
            print("This is not avaiable")
            print("Try again!!!")
            starter()

    else:
        print("Try Again!!")
        starter()

    #call convlution
    #print("inputtttttt: ", x_input)
    #print("impulseeeee: ", h_impulse)
    draw_output(x_input, h_impulse)

    


def conv_preprocessing():
    x_input = take_input_signal_manually()
    h_impulse = take_impulse_manually()


def custom_convolute(Lx, Lh, x_input, h_impulse):
    h_impulse.reverse()


    #create signal input with zero paddings
    x_signal = []

    pad_zeros(Lh, x_signal)

    for i in range(len(x_input)):
        x_signal.append(x_input[i])

    pad_zeros(Lh, x_signal)



#calculate Ly

    Ly = Lx + Lh - 1
    y = []

    for i in range(Ly):
        y.append(0)

    for i in range(Ly):
        for j in range(Lh):
            y[i] += h_impulse[j] * x_signal[i+j]

    return y





#my_output = custom_convolute(Lx, Lh, x_input, h_impulse)
#print("out: ", my_output)

def handler():
    starter()


handler()
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


