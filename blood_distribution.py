blood_unit = [int(i) for i in input().split(" ")]
blood_type = [int(i) for i in input().split(" ")]

def blood_distribution(type, distributed):
    blood_distributed = min(blood_type[type], blood_unit[distributed])
    blood_type[type] -= blood_distributed
    blood_unit[distributed] -= blood_distributed
    return blood_distributed

# use O-, O+, A-, A+, B-, B+ blood
count = blood_distribution(0, 0) + blood_distribution(1, 1) + blood_distribution(2, 2) + blood_distribution(3, 3) + blood_distribution(4, 4) + blood_distribution(5, 5)

# use remaining O+, A-, B- blood
if blood_type[3] - blood_unit[2] > blood_type[5] - blood_unit[4]:
    count += blood_distribution(3, 1) + blood_distribution(3, 2) + blood_distribution(5, 1) + blood_distribution(5, 4)
else:
    count += blood_distribution(5, 1) + blood_distribution(5, 4) + blood_distribution(3, 1) + blood_distribution(3, 2)

# AB- blood
for i in range(2, 7, 2):
    count += blood_distribution(6, i)

# AB+ blood
for i in range(1, 8):
    count += blood_distribution(7, i)

# remaining O-
count += min(sum(blood_type), blood_unit[0])
print(count)