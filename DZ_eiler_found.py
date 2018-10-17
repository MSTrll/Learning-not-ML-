
inp = input("Number of vertexes:  ")
v_am = int (inp)

inc = []
for i in range(0, v_am):
    inp_str = str(i+1) + " :  "
    inp = input(inp_str)
    inc = [(int (el)) - 1 for el in (inp.split())]

# TEMP TEMP TEMP TEMP(If you want to test it on examples below)

# v_am = 6
# inc = [[1, 2, 3, 4],
#        [0, 2],
#        [0, 1, 3, 4],
#        [0, 2],
#        [0, 2, 5],
#        [4]]

# v_am = 10
# inc = [[1],
#        [0, 2],
#        [1, 3, 6, 8],
#        [2, 4, 7, 9],
#        [3, 5],
#        [4],
#        [2, 7],
#        [3, 6],
#        [2, 9],
#        [3, 8]]

# v_am = 11
# inc1 = [[2, 5],
#         [1, 3, 8, 11],
#         [2, 4, 7, 10],
#         [3, 5, 6, 9],
#         [1, 4, 6, 9],
#         [4, 5],
#         [3, 8],
#         [2, 7],
#         [4, 5],
#         [3, 11],
#         [2, 10]]
# inc = [[el[i]-1 for i in range(0,len(el))] for el in inc1]

# TEMP TEMP TEMP TEMP

conn = []
all_conn = []
main_v = 0
move = 1


# DFS with collecting vertexes
def find_eiler_path(vert):

    global all_conn, conn, inc, main_v, move

    conn.append(vert)

    if (len(inc[vert]) == 0): move = 0
    if (move == 0):
        move += 1
        all_conn.append(conn)
        conn = []

    for i in inc[vert]:
        inc[vert].remove(i)
        inc[i].remove(vert)
        find_eiler_path(i)

    if (vert == main_v):
        for i in range(0,len(inc)):
            if (len(inc[i]) != 0):
                if(len(conn) != 0):
                    all_conn.append(conn)
                    conn = []
                find_eiler_path(i)


# choosing of the vertex algorithm'll begins from
vert = -1
iter = 0
for vt in inc:
    if (len(vt) % 2 == 1):
        vert = iter
        break
    iter += 1

if (vert == -1): vert = 0
main_v = vert

# start point
find_eiler_path(vert)

conn_temp = []
ct = []

# connecting of parts of the Eiler's path
# -At first there is the main(first) part of the path
# -Secondly(if some cycle will be found) the founded
# cycle inserts into the previous path(will be repeated as more as more parts'll be received)
if (len(all_conn) > 1):
    for path in range(0, len(all_conn)):
        if (len(conn_temp) == 0):
            conn_temp.extend(all_conn[path])
            continue
        ct = conn_temp
        p = all_conn[path]
        if(p[0] == p[-1]):
            all_conn[path].remove(p[0])
        conn_temp = ct[0:ct.index(p[-1]) + 1]
        conn_temp.extend(p)
        conn_temp.extend(ct[ct.index(p[-1]) + 1:])
else:
    conn_temp = all_conn[0]

# conn1 = [[el + 1 for el in all_conn[path]] for path in range(0, len(all_conn))]
conn_t = [el + 1 for el in conn_temp]
print(conn_t)
