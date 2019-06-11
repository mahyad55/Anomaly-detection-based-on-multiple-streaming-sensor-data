import math

'''
% GaussianKernel1D( sigma, deriv, width ) Creates a centered Gaussian
% kernel of the specified derivative order and the specified scale. The
% width parameter specifies how many sigma from the center the kernel
% should extend.
'''

def GaussianKernel1D(scale = 1, deriv = 1, width = 3):

    sigma = scale
    Range = []
    derivs = []
    kernel = []
    derivs.clear()
    kernel.clear()
    length = 2 * width * (math.ceil( sigma)) + 1
    for j in range(1,length+1):
        Range.append(j)

    center = math.ceil(length / 2)

    for j in range(0,Range.__len__()):
        derivs.append(-((Range[j] - center) / (sigma ** 2)))

    for j in range (0,Range.__len__()):
        temp = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((Range[j] - center) ** 2) / (2 * sigma ** 2))
        kernel.append(temp)
    for j in range (0,Range.__len__()):
        kernel[j] = kernel[j] * derivs[j]

    #print(derivs)
    #print(kernel)
    return kernel

