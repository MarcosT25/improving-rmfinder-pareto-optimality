solutions = []

for w_cross in range (0, 1001, 200):
    for w_risk in range(0, 1001, 200):
        for w_atrib in range(0, 1001, 200):
            aux = 0
            if w_cross == 0:
                w_cross+=1
            if w_risk == 0:
                w_risk += 1
            if w_atrib == 0:
                w_atrib += 1
            this_solution = [w_cross, w_risk, w_atrib, w_atrib]
            if len(solutions) == 0:
                solutions.append(this_solution)
            is_different = True
            for solution in solutions:
                if (this_solution[0] / solution[0]) == (this_solution[1] / solution[1]) and (this_solution[0] / solution[0]) == (this_solution[2] / solution[2]) and (this_solution[0] / solution[0]) == (this_solution[3] / solution[3]):
                    is_different = False
                    break
            if is_different:
                solutions.append(this_solution)

with open("out.txt", "w") as file:
    for solution in solutions:
        file.write(f"FO_WEIGHT {solution[0]}, {solution[1]}, {solution[2]}, {solution[3]}\n")
    file.close()
print(f"Número de execuções do RMFinder: {len(solutions)}\nArquivo com os pesos: out.txt")
