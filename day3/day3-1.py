with open('day3.input', 'r') as f:
  input_lines = [i for i in f.read().strip().split('\n')]

nb_inputs = len(input_lines)
bin_size = len(input_lines[0])
ones = [0] * bin_size
for bin in input_lines:
    for i in range(0, bin_size):
        ones[bin_size - i - 1] += (int(bin, 2) >> i) & 0b1
        # if bin[i] == '1':
        #     ones[i] += 1

gamma_bitlist = [str(int(count > nb_inputs / 2)) for count in ones]
gamma = int(''.join(gamma_bitlist), 2)
epsilon_bitlist = [str(int(count <= nb_inputs / 2)) for count in ones]
epsilon = int(''.join(epsilon_bitlist), 2)

print(f'gamma={gamma} ; epsilon={epsilon}')
print(gamma * epsilon)

# gamma=1300 ; epsilon=2795
# 3633500
