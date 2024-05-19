import numpy as np

def calculate(list):
  calculations = {}
  #control to be 9 numbers only
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  array = np.array(list).reshape(3,3)
  calculations['mean'] = [array.mean(axis = 0).tolist(), array.mean(axis = 1).tolist(), array.mean().tolist()]
  calculations['variance'] = [array.var(axis = 0).tolist(), array.var(axis = 1).tolist(), array.var().tolist()]
  calculations['standard deviation'] = [array.std(axis = 0).tolist(), array.std(axis = 1).tolist(), array.std().tolist()]
  calculations['max'] = [array.max(axis = 0).tolist(), array.max(axis = 1).tolist(), array.max().tolist()]
  calculations['min'] = [array.min(axis = 0).tolist(), array.min(axis = 1).tolist(), array.min().tolist()]
  calculations['sum'] = [array.sum(axis = 0).tolist(), array.sum(axis = 1).tolist(), array.sum().tolist()]

  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))
