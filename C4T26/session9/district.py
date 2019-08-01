district = ['ST','BD','BTL','CG','DD','HBT']
area = [117.43,9.224,43.35,12.04,9.96,10.09]
population = [150300,247100,333300,266800,420900,318000]
density = []
max = 0
min = 100000000000
for i in range(6):
    if max < population[i]:
        max = population[i]
        maxp = i
    if min > population[i]:
        min = population[i]
        minp = i
    density.append(population[i]/area[i])
densum = sum(density)
mean = densum / len(density)
print(district[maxp])
print(district[minp])
print(mean)