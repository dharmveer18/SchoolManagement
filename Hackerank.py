speed = [12, 112, 100, 13, 55]
reliability = [31, 4, 100, 55, 50]
maxMachines = 3

def maximumClusterQuality(speed, reliability, maxMachines):
    rel = sorted(reliability, reverse =True)
    total,product, res, full_res = 0, 1, 0, 0

    for i in range(maxMachines):
        total, res =0,0
        total= reliability[reliability.index(rel[i])]
        res = total* rel[i]
        if full_res < res:
            full_res = res
        res =0
        for j in range(i+1, maxMachines):
            total = reliability[reliability.index(rel[j])]
            res = total* min(rel[:j])
            if full_res < res:
                full_res = res
    return full_res

print(maximumClusterQuality(speed, reliability, maxMachines))