# Basic Neurons in Neural Nets

input = [1.2, 1.1, 2.1]
weight = [3.4, 2.4, 2.2]
bias = 4


# Calulate The Neuron, Sum of all input*weight + bias
output = input[0]*weight[0] + input[1]*weight[1] + input[2]*weight[2] + bias
output_format = "{:.2f}".format(output)

print(output_format)
