# part 1 was too long to rerun.. took this data from the output to reconstruct...

scanner_data = (
    (0, 2, ((-108, -76, 1254), (0, 2, 1), (1, -1, 1))),
    (0, 26, ((1161, -42, -84), (2, 0, 1), (-1, 1, -1))),
    (1, 7, ((-119, 22, 1278), (2, 1, 0), (1, 1, -1))),
    (1, 13, ((-21, 1186, -45), (1, 2, 0), (1, 1, 1))),
    (1, 17, ((-56, 59, -1296), (0, 2, 1), (-1, -1, -1))),
    (2, 0, ((108, -1254, -76), (0, 2, 1), (1, 1, -1))),
    (2, 8, ((-5, -74, -1263), (2, 1, 0), (-1, -1, -1))),
    (2, 10, ((1093, 7, -62), (1, 0, 2), (-1, 1, 1))),
    (2, 12, ((-1320, 104, 67), (1, 2, 0), (-1, -1, 1))),
    (2, 26, ((1237, 66, 1170), (1, 0, 2), (1, 1, -1))),
    (3, 6, ((1222, 7, 59), (2, 0, 1), (1, 1, 1))),
    (3, 11, ((55, 136, -1336), (0, 2, 1), (1, 1, -1))),
    (3, 20, ((-1212, -110, 97), (2, 1, 0), (1, -1, 1))),
    (4, 6, ((-26, 1167, -14), (0, 2, 1), (-1, -1, -1))),
    (4, 26, ((42, 17, -1286), (1, 2, 0), (1, 1, 1))),
    (5, 6, ((-1320, -22, 17), (0, 2, 1), (1, -1, 1))),
    (5, 22, ((-60, -1264, 62), (0, 2, 1), (1, 1, -1))),
    (5, 25, ((-26, -44, -1200), (2, 1, 0), (-1, -1, -1))),
    (5, 26, ((11, 1206, 8), (1, 2, 0), (-1, 1, -1))),
    (6, 3, ((-7, -59, -1222), (1, 2, 0), (1, 1, 1))),
    (6, 4, ((-26, -14, 1167), (0, 2, 1), (-1, -1, -1))),
    (6, 5, ((1320, -17, -22), (0, 2, 1), (1, 1, -1))),
    (6, 11, ((48, -1086, -1277), (1, 0, 2), (1, 1, -1))),
    (6, 22, ((1260, -1286, 79), (0, 1, 2), (1, -1, -1))),
    (6, 23, ((160, -13, 1110), (1, 0, 2), (1, -1, 1))),
    (6, 26, ((28, 1184, -1312), (2, 1, 0), (-1, -1, -1))),
    (7, 1, ((1278, -22, 119), (2, 1, 0), (-1, 1, 1))),
    (7, 13, ((-43, 1305, 1233), (1, 0, 2), (1, 1, -1))),
    (7, 16, ((76, -16, -1191), (2, 0, 1), (-1, -1, 1))),
    (7, 17, ((-1334, -60, -1274), (2, 0, 1), (1, -1, -1))),
    (7, 25, ((-115, -2, 1190), (1, 2, 0), (-1, -1, 1))),
    (8, 2, ((-1263, -74, -5), (2, 1, 0), (-1, -1, -1))),
    (8, 10, ((1167, -1256, -67), (1, 2, 0), (1, -1, -1))),
    (8, 12, ((-1246, 109, -1196), (1, 0, 2), (1, 1, -1))),
    (8, 15, ((-1140, 148, 48), (1, 2, 0), (1, 1, 1))),
    (8, 24, ((-1100, 9, -136), (2, 1, 0), (1, 1, -1))),
    (8, 26, ((1163, -1197, 1175), (1, 2, 0), (-1, -1, 1))),
    (9, 21, ((138, 21, -1198), (2, 0, 1), (-1, -1, 1))),
    (10, 2, ((-7, 1093, 62), (1, 0, 2), (1, -1, 1))),
    (10, 8, ((-67, -1167, -1256), (2, 0, 1), (-1, 1, -1))),
    (10, 18, ((42, -7, -1348), (2, 1, 0), (-1, -1, -1))),
    (11, 3, ((-55, -1336, -136), (0, 2, 1), (1, -1, 1))),
    (11, 6, ((1086, -48, -1277), (1, 0, 2), (1, 1, -1))),
    (11, 20, ((-1348, 1226, 42), (1, 2, 0), (1, 1, 1))),
    (11, 23, ((112, -1099, -167), (0, 1, 2), (1, -1, -1))),
    (12, 2, ((-67, -1320, 104), (2, 0, 1), (1, -1, -1))),
    (12, 8, ((-109, 1246, -1196), (1, 0, 2), (1, 1, -1))),
    (12, 15, ((106, -1048, -61), (0, 2, 1), (1, -1, 1))),
    (12, 19, ((43, 1159, 8), (2, 0, 1), (-1, -1, 1))),
    (12, 25, ((1181, -138, -142), (2, 0, 1), (-1, -1, 1))),
    (12, 26, ((-83, -1, 1066), (0, 2, 1), (-1, 1, 1))),
    (13, 1, ((45, 21, -1186), (2, 0, 1), (1, 1, 1))),
    (13, 7, ((-1305, 43, 1233), (1, 0, 2), (1, 1, -1))),
    (13, 16, ((-1157, 1289, -1148), (2, 1, 0), (1, -1, 1))),
    (13, 17, ((-101, 1245, -1317), (2, 1, 0), (-1, -1, -1))),
    (13, 19, ((-1296, 62, 35), (0, 2, 1), (-1, 1, 1))),
    (13, 25, ((-158, -1235, -115), (0, 2, 1), (-1, 1, 1))),
    (13, 26, ((-1180, 1338, 1093), (2, 0, 1), (1, 1, 1))),
    (14, 18, ((1153, -53, -103), (2, 1, 0), (-1, 1, 1))),
    (15, 8, ((-48, 1140, -148), (2, 0, 1), (1, 1, 1))),
    (15, 12, ((-106, 61, -1048), (0, 2, 1), (1, 1, -1))),
    (15, 17, ((-1304, 1211, 1070), (0, 2, 1), (1, -1, 1))),
    (15, 19, ((1091, 1265, 69), (1, 0, 2), (1, -1, 1))),
    (15, 24, ((-1248, 1149, -88), (1, 0, 2), (1, 1, -1))),
    (15, 26, ((23, -1049, 1127), (0, 1, 2), (-1, -1, 1))),
    (16, 7, ((-16, 1191, 76), (1, 2, 0), (-1, 1, -1))),
    (16, 13, ((1148, 1289, 1157), (2, 1, 0), (1, -1, 1))),
    (16, 21, ((-1122, -15, 38), (2, 0, 1), (1, -1, -1))),
    (16, 25, ((-1306, -78, 1174), (2, 0, 1), (-1, 1, -1))),
    (17, 1, ((-56, -1296, 59), (0, 2, 1), (-1, -1, -1))),
    (17, 7, ((-60, -1274, 1334), (1, 2, 0), (-1, -1, 1))),
    (17, 13, ((-1317, 1245, -101), (2, 1, 0), (-1, -1, -1))),
    (17, 15, ((1304, -1070, 1211), (0, 2, 1), (1, 1, -1))),
    (17, 19, ((21, -39, 1280), (2, 0, 1), (1, -1, -1))),
    (17, 25, ((1159, -1336, 1130), (2, 0, 1), (1, -1, -1))),
    (18, 10, ((-1348, -7, 42), (2, 1, 0), (-1, -1, -1))),
    (18, 14, ((103, 53, 1153), (2, 1, 0), (1, 1, -1))),
    (19, 12, ((1159, -8, 43), (1, 2, 0), (-1, 1, -1))),
    (19, 13, ((-1296, -35, -62), (0, 2, 1), (-1, 1, 1))),
    (19, 15, ((1265, -1091, -69), (1, 0, 2), (-1, 1, 1))),
    (19, 17, ((-39, 1280, -21), (1, 2, 0), (-1, -1, 1))),
    (19, 25, ((1138, -1297, -150), (0, 1, 2), (1, 1, 1))),
    (19, 26, ((-1242, 42, 1058), (1, 0, 2), (1, -1, 1))),
    (20, 3, ((-97, -110, 1212), (2, 1, 0), (1, -1, 1))),
    (20, 11, ((-42, 1348, -1226), (2, 0, 1), (1, 1, 1))),
    (21, 9, ((21, 1198, 138), (1, 2, 0), (-1, 1, -1))),
    (21, 16, ((-15, 38, 1122), (1, 2, 0), (-1, -1, 1))),
    (22, 5, ((60, 62, 1264), (0, 2, 1), (1, -1, 1))),
    (22, 6, ((-1260, -1286, 79), (0, 1, 2), (1, -1, -1))),
    (22, 23, ((-1126, 1247, 1189), (1, 0, 2), (-1, -1, -1))),
    (22, 25, ((-1290, -106, -1260), (1, 2, 0), (-1, 1, -1))),
    (23, 6, ((-13, -160, -1110), (1, 0, 2), (-1, 1, 1))),
    (23, 11, ((-112, -1099, -167), (0, 1, 2), (1, -1, -1))),
    (23, 22, ((1247, -1126, 1189), (1, 0, 2), (-1, -1, -1))),
    (23, 26, ((1138, 1344, -1299), (2, 0, 1), (-1, -1, 1))),
    (24, 8, ((-136, -9, 1100), (2, 1, 0), (-1, 1, 1))),
    (24, 15, ((-1149, 1248, -88), (1, 0, 2), (1, 1, -1))),
    (25, 5, ((-1200, -44, -26), (2, 1, 0), (-1, -1, -1))),
    (25, 7, ((-1190, -115, -2), (2, 0, 1), (1, -1, -1))),
    (25, 12, ((-138, 142, 1181), (1, 2, 0), (-1, 1, -1))),
    (25, 13, ((-158, 115, 1235), (0, 2, 1), (-1, 1, 1))),
    (25, 16, ((78, 1174, -1306), (1, 2, 0), (1, -1, -1))),
    (25, 17, ((-1336, 1130, -1159), (1, 2, 0), (-1, -1, 1))),
    (25, 19, ((-1138, 1297, 150), (0, 1, 2), (1, 1, 1))),
    (25, 22, ((-1260, -1290, 106), (2, 0, 1), (-1, -1, 1))),
    (25, 26, ((55, 1180, 1208), (1, 0, 2), (1, -1, 1))),
    (26, 0, ((42, -84, 1161), (1, 2, 0), (1, -1, -1))),
    (26, 2, ((-66, -1237, 1170), (1, 0, 2), (1, 1, -1))),
    (26, 4, ((1286, -42, -17), (2, 0, 1), (1, 1, 1))),
    (26, 5, ((8, 11, -1206), (2, 0, 1), (-1, -1, 1))),
    (26, 6, ((-1312, 1184, 28), (2, 1, 0), (-1, -1, -1))),
    (26, 8, ((-1175, 1163, -1197), (2, 0, 1), (1, -1, -1))),
    (26, 12, ((-83, -1066, 1), (0, 2, 1), (-1, 1, 1))),
    (26, 13, ((-1338, -1093, 1180), (1, 2, 0), (1, 1, 1))),
    (26, 15, ((23, -1049, -1127), (0, 1, 2), (-1, -1, 1))),
    (26, 19, ((42, 1242, -1058), (1, 0, 2), (-1, 1, 1))),
    (26, 23, ((1344, 1299, 1138), (1, 2, 0), (-1, 1, -1))),
    (26, 25, ((1180, -55, -1208), (1, 0, 2), (-1, 1, 1))),
)

class Scanner():
    def __init__(self, id) -> None:
        self.id = id
        self.pso = {}
        self.scanners = {}
    
    def advertise_scanner(self, id=None, coord=(0, 0, 0)):
        if id is None:
            id = self.id
        if id in self.scanners:
            return
        print(f'{self.id}.advertise_scanner({id}, {coord})')
        distance = abs(coord[0]) + abs(coord[1]) + abs(coord[2])
        self.scanners[id] = (distance, coord)
        for s, pso in self.pso.values():
            s.advertise_scanner(id, transform(coord, pso[0], pso[1], pso[2]))


def transform(coord, perm, sign, offset):
    return (coord[perm[0]]*sign[0]+offset[0],
            coord[perm[1]]*sign[1]+offset[1],
            coord[perm[2]]*sign[2]+offset[2])

scanners = [Scanner(i) for i in range(27)]

for scannerid, targetid, ops in scanner_data:
    offset, perm, sign = ops
    scanners[scannerid].pso[targetid] = (scanners[targetid], (perm, sign, offset))

for id, scanner in enumerate(scanners):
    scanner.advertise_scanner()

m = 0
for scanner in scanners:
    for d in [data[0] for data in scanner.scanners.values()]:
        m = max(m, d)

print(m)

# 10630
