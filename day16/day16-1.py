with open('/Users/patmarti/dev/adventofcode/day16/input.txt', 'r') as f:
    line = f.read().strip()

l = len(line)*4
bits = format(int(line, 16), f'0>{l}b')

class Packet():
    def __init__(self, data, depth=0) -> None:
        self.data = data
        self.depth = depth
        self._prefix = " " * depth
        self._length = None

    def version(self):
        return int(self.data[:3], 2)

    def type_id(self):
        return int(self.data[3:6], 2)

    def length(self):
        return None

    def __repr__(self) -> str:
        return f'Packet(version={self.version()}, type_id={self.type_id()})'


def type_id(data):
    return int(data[3:6], 2)

def packet(data, depth=0):
    if type_id(data) == 4:
        return Literal(data, depth)
    return Operator(data, depth)


class Literal(Packet):
    def __init__(self, data, depth=0) -> None:
        super().__init__(data, depth=depth)
        # self._length = None
    
    def length(self):
        if not self._length:
            self.value()
        return self._length

    def sub_packets(self):
        return []
    
    def version_sum(self):
        return self.version()

    def value(self):
        i = 6
        res = ""
        while self.data[i] == '1':
            res += self.data[i+1:i+5]
            i += 5
        res += self.data[i+1:i+5]
        i += 5
        self._length = i
        return int(res, 2)

class Operator(Packet):
    def __init__(self, data, depth=0) -> None:
        super().__init__(data, depth=depth)
        self._packets = None
    
    def length_type_id(self):
        return int(self.data[6])
    
    def total_length(self):
        if self.length_type_id() == 0:
            return int(self.data[7:22], 2)
        return None

    def nb_packets(self):
        if self.length_type_id() == 1:
            return int(self.data[7:18], 2)
        return None

    def packets(self):
        if self._packets is not None:
            for p in self._packets:
                yield p
            return
        self._packets = []
        nb_packets = self.nb_packets()
        total_length = self.total_length()
        idx = 18 if nb_packets else 22
        packet_count = length = 0
        while not (packet_count == nb_packets or length == total_length):
            p = packet(self.data[idx+length:], self.depth+1)
            self._packets.append(p)
            packet_count += 1
            length += p.length()
            yield p
        self._length = idx+length

    def version_sum(self):
        v = self.version()
        for p in self.packets():
            v += p.version_sum()
        return v

    def length(self):
        if not self._length:
            list(self.packets())
        return self._length


master = Operator(bits)
print(master.version_sum())

# 993
