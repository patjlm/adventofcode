import sys

image = []
with open(sys.argv[1], 'r') as f:
    algo = [0 if c == '.' else 1 for c in f.readline().strip()]
    f.readline()
    for l in f:
        image.append([0 if c == '.' else 1 for c in l.strip()])

def print_image(image):
    for row in range(len(image)):
        print(''.join(['#' if c else '.' for c in image[row]]))

if algo[0] == '.':
    def infinity(_): return 0
else:
    def infinity(step): return 1 if step % 2 else 0

def expand(image, step=0):
    inf = infinity(step)
    cols = len(image[0])
    img = []
    img.append([inf]*(cols+2))
    for row in image:
        img.append([inf] + row + [inf])
    img.append([inf]*(cols+2))
    return img

def idx(img, row, col):
    s = ''
    for r in (row-1, row, row+1):
        for c in (col-1, col, col+1):
            s += str(img[r][c])
    return int(s, 2)

# finally figured out the universe is blinking due to the first char of the algothim being a #...
def blink(image):
    rows = len(image)
    cols = len(image[0])
    inf = int(image[0][0]==0)
    img = [[inf]*cols]
    for r in range(1, rows-1):
        img.append([inf] + image[r][1:cols-1] + [inf])
    img.append([inf]*cols)
    return img

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
    return blink(new)

image = expand(image)

for step in range(50):
    image = expand(image, step)
    image = process(image)

print_image(image)

s = 0
for r in range(len(image)):
    s += sum(image[r])
print(s)

# 17628
