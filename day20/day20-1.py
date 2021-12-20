import sys

input_image = []
with open(sys.argv[1], 'r') as f:
    algo = [0 if c == '.' else 1 for c in f.readline().strip()]
    f.readline()
    for l in f:
        input_image.append([0 if c == '.' else 1 for c in l.strip()])

# print(f'algo={algo}')

def print_image(image):
    for row in range(len(image)):
        print(''.join(['#' if c else '.' for c in image[row]]))

def expand(image):
    cols = len(image[0])
    img = []
    img.append([0]*(cols+2))
    for row in image:
        img.append([0] + row + [0])
    img.append([0]*(cols+2))
    return img

def idx(img, row, col):
    s = ''
    for r in (row-1, row, row+1):
        for c in (col-1, col, col+1):
            s += str(img[r][c])
    return int(s, 2)

def process(image):
    new = [image[0]]
    for row in range(1, len(image)-1):
        r = [0]
        new.append(r)
        for col in range(1, len(image[0])-1):
            id = idx(image, row, col)
            r.append(algo[id])
        r.append(0)
    new.append(image[0])
    return new

image = expand(input_image)
# dummy thing... make some room around
for _ in range(60):
    image = expand(image)
# print_image(image)

for step in range(2):
    print(f'step {step}')
    print('expand')
    image = expand(image)
    print_image(image)
    print('process')
    image = process(image)
    print_image(image)

s = 0
# and then ignore side artefacts!!! see part2 for proper solution
for r in range(3, len(image)-3):
    s += sum(image[r][3:-3])
print(s)

# 5682
