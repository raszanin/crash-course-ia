import numpy as np

dataset = np.array([
  [1, 1, 1], 
  [-1, -1, 0]
])

pesos = [-0.5, 0.5, 0.5]

def predict(net_input, pesos):
  ativacao = pesos[0]
  for i in range(len(net_input)-1):
    ativacao += pesos[i + 1] * net_input[i]
  return 1.0 if ativacao >= 0.0 else 0.0

for row in dataset:
  prediction = predict(row, pesos)
  print("Esperado=%d, Previsto=%d" % (row[-1], prediction))

