# Trainingsschleife für Autoencoder
import torch
import torch.nn as nn

model = SimpleAE(input_dim=5, bottleneck_dim=2)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.MSELoss()
data = torch.randn(100, 5)

for epoch in range(100):
    out = model(data)
    loss = criterion(out, data)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.4f}')