# Lineare Schicht
import torch.nn as nn
layer = nn.Linear(10, 5)
x = torch.randn(3, 10)
out = layer(x)
print(out.shape)  # torch.Size([3, 5])