from torch import nn

class Discriminator(nn.Module):

    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            # Input layer
            nn.Linear(784, 1024),
            nn.ReLU(),
            nn.Dropout(0.3),
            # Hidden layer 1
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            # Hidden layer 2
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            # Output layer
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = x.view(x.size(0), 784)
        output = self.model(x)
        return output