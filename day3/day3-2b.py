with open('day3.input', 'r') as f:
  inputs = f.read().strip().split('\n')


# sum of ones in each column
ones = list(map(lambda x: sum(map(int, x)), zip(*inputs)))

input_bins = [int(i, 2) for i in inputs]

nb_inputs = len(input_bins)
bin_size = 12

def bit(bin, pos):
  return (bin >> (bin_size - pos - 1)) & 0b1
  # return int(f'{bin:>012b}'[pos])

def majority(a, b):
  return int(a >= len(b)/2)

def minority(a, b):
  return int(a < len(b)/2)

# compute a bitmask for out list l with the given compare funtion:
# - majority() to get the majority mask for oxygen_rating
# - minority() to get the minority mask for co2_rating
# this mask can then be applied on inputs to find those that match the most
def rating(l, pos, mask, compare_function):
  if pos == bin_size:
    raise Exception('reached the end of the mask without finding a single element')
  # compute the number of 1s for each items of the list at position pos 
  ones = sum([bit(b, pos) for b in l])
  # 0 or 1, depending on which is the majority or minority
  majmin = compare_function(ones, l)
  # compute a new prefix with our majmin value at position pos
  mask |= majmin << (bin_size - pos - 1)
  # create a filtered list of items that match our majmin bit at pos
  filtered = [i for i in l if bit(i, pos) == majmin]
  # return early if only 1 item matches
  if len(filtered) == 1:
    return filtered[0]
  # recursively call mask to go to the next bits
  return rating(filtered, pos+1, mask, compare_function)

oxygen_rating = rating(input_bins, 0, 0, majority)
print(f'oxygen_rating = {oxygen_rating:>012b} = {oxygen_rating}')

co2_rating = rating(input_bins, 0, 0, minority)
print(f'co2_rating    = {co2_rating:>012b} = {co2_rating}')

print(oxygen_rating * co2_rating)

# oxygen_rating = 010100101111 = 1327
# co2_rating    = 110101100101 = 3429
# 4550283
