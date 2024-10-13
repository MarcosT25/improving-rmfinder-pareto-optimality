solves = []

for w_cross in range (0, 1001, 200):
    for w_risk in range(0, 1001, 200):
        for w_atrib in range(0, 1001, 200): 
            this_solve = [w_cross, w_risk, w_atrib, w_atrib]
            if w_cross + w_risk + w_atrib == 1000:
                if 0 in this_solve:
                    this_solve = [1 if x == 0 else x for x in this_solve]
                solves.append(this_solve)

with open("out-v2.txt", "w") as file:
    for solve in solves:
        file.write(f"FO_WEIGHT {solve[0]},{solve[1]},{solve[2]},{solve[3]}\n")
    file.close()
print(f"Número de execuções do RMFinder: {len(solves)}\nArquivo com os pesos: out-v2.txt")
