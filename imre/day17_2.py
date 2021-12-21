import re, math
file_content = open('input.txt', 'r').readline()
x1,x2,y1,y2 = [int(x) for x in re.findall(r'x=(\-?\d+)\.\.(\-?\d+), y=(\-?\d+)\.\.(\-?\d+)', file_content)[0]]
far_y = max(abs(y1), abs(y2))
far_x = max(abs(x1), abs(x2))
good_shots = set()


def shoot(vx:  int, vy: int):
    vx_orig, vy_orig = vx, vy
    x = y = ymax = 0
    cont = True
    hit = False
    while cont:
        x += vx
        y += vy
        ymax = max(ymax, y)
        vx += int(math.copysign(1, vx) * -1) if vx != 0 else 0
        vy += -1
        if x1 <= x <= x2 and y1 <= y <= y2:
            hit = True
            cont = False
            global good_shots
            good_shots.add(str(vx_orig) + '|' + str(vy_orig))
        if y < y1 :
            cont = False # It is a miss if y <
    return {'hit': hit, 'ymax': ymax, 'vx': vx_orig, 'vy': vy_orig}


# Idea is, we get a phase space of vx vy values, and we try all points in it. Get the one with the highest ymax,
# generate a new phase space and go on until there is no new hits.
def check_phasespace(ps, y_max):
    best_shot = {'ymax': y_max}
    theres_hit = False
    for i in range(min(ps['vx1'], ps['vx2']), max(ps['vx1'], ps['vx2']) + 1):
        for j in range(min(ps['vy1'], ps['vy2']), max(ps['vy1'], ps['vy2']) + 1):
            a = shoot(i, j)
            if a['hit'] and a['ymax'] > best_shot['ymax']:
                best_shot = a
                theres_hit = False
    return(best_shot, theres_hit)


scale = math.sqrt(far_x * far_x + far_y * far_y)
phase_space = {'vx1': int(math.copysign(1, x1)), # aim towards target
               'vx2': int(math.copysign(scale * 0.6, x1)),
               'vy1': int(math.copysign(1, y1)) + int(0.5 * scale), # shift phase space upwards
               'vy2': int(math.copysign(scale * 0.6, y1)) + int(0.5 * scale)}
theres_new_record = True
record = {'ymax': -1000}
while theres_new_record:
    y_max_before = record['ymax']
    record, theres_hit = check_phasespace(phase_space, y_max_before)
    theres_new_record = record['ymax'] > y_max_before and theres_hit
    # Let's put a cube on top of current record
    phase_space =  {'vx1': int(record['vx'] - 1.2 * scale),
                   'vx2': int(record['vx'] + 1.2 * scale),
                   'vy1': record['vy'],
                   'vy2': int(record['vy'] + 1.3 * scale)}
phase_space_boundaries = {'vx1': int(math.copysign(1, x1)),
                          'vx2': int(math.copysign(far_x, x1)),
                          'vy1': int(math.copysign(far_y, y1)),
                          'vy2': record['vy']}

check_phasespace(phase_space_boundaries, 1)
print(good_shots)
print(len(good_shots))
