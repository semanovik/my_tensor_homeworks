for i in range(1, 1001):
    counter = 0
    for k in range(1, i+1):
        if i % k == 0:      # Делим i на всевозможные числа, которые ему предшествуют
            counter += 1
    if counter == 2:        # Если делителя только 2, означает, что число простое
        print(i)