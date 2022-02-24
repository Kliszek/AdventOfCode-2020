treemap = list()

for x in range(0,323):
    treemap.append(input())

def treesEncountered(slopeX, slopeY):    
    trees = 0
    offsetX = 0
    offsetY = 0

    while offsetY < len(treemap):
        if treemap[offsetY][offsetX] == '#':
            trees+=1
        offsetX+=slopeX
        offsetY+=slopeY
        offsetX%=len(treemap[0])
    return trees

result=1
result*=treesEncountered(1,1)
result*=treesEncountered(3,1)
result*=treesEncountered(5,1)
result*=treesEncountered(7,1)
result*=treesEncountered(1,2)

print(result)