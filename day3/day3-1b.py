with open('day3.input', 'r') as f:
  inputs = f.read().strip().split('\n')

nb_inputs = len(inputs)
bin_size = len(inputs[0])

def list_to_int(l):
  out = 0
  for bit in l:
    out = (out << 1) | bit
  return out

# count 1s in each column
ones = list(map(lambda x: sum(map(int, x)), zip(*inputs)))

majority = [int(count > nb_inputs / 2) for count in ones]
gamma = list_to_int(majority)
minority = [int(count < nb_inputs / 2) for count in ones]
epsilon = list_to_int(minority)

# gamma_bitlist = [str(int(count > nb_inputs / 2)) for count in ones]
# gamma = int(''.join(gamma_bitlist), 2)
# epsilon_bitlist = [str(int(count <= nb_inputs / 2)) for count in ones]
# epsilon = int(''.join(epsilon_bitlist), 2)

print(f'gamma={gamma} ; epsilon={epsilon}')
print(gamma * epsilon)

# gamma=1300 ; epsilon=2795
# 3633500
