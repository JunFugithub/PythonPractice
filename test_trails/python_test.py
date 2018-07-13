"""
    Yang hui's Triangle
"""

def triangles():
    firow = [1]
    for i in range(10):
        yield firow
        firow = [1] + [firow[x] + firow[x+1] for x in range(len(firow)-1) ] + [1]

for i in triangles():
    print(i)