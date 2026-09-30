import numpy as np

R,C = map(int, input("Sales table size: ").split())
values = np.array(list(map(int , input("Sales values: ").split())))
sale_values = np.array(values).reshape(R,C)

print("Branch totals:", np.sum(sale_values[:,1]))
print("Product totals:",np.sum(sale_values[:,0]) )
print("Best branch:", np.sum(sale_values))
print("Grand total:", np.sum(sale_values))