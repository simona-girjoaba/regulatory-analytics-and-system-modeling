import torch
M = torch.randn(3, 3, requires_grad=True)
z = M.sum()
z.backward()
print(M.grad)  # sollte eine 3x3 Matrix mit Einsen sein