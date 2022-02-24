numbers = list()

for x in range(0,200):
    numbers.append(int(input()))

answer=0

for x in numbers:
    for y in numbers:
        for z in numbers:
          if x+y+z == 2020:
              answer=x*y*z
              break
        if answer != 0:
            break
    if answer != 0:
        break

print(answer)