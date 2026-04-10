# Modell speichern
torch.save(model.state_dict(), 'ae_model.pth')

# Modell laden
model = SimpleAE(input_dim=5, bottleneck_dim=2)
model.load_state_dict(torch.load('ae_model.pth'))
model.eval()