# Autoencoder Grundstruktur
class SimpleAE(nn.Module):
    def __init__(self, input_dim=5, bottleneck_dim=2):
        super().__init__()
        self.encoder = nn.Linear(input_dim, bottleneck_dim)
        self.decoder = nn.Linear(bottleneck_dim, input_dim)
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded