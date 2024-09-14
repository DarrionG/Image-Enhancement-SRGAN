from torch import nn

class Generator:

    class Generator(nn.Module):

        def __init__(self):
            super().__init__()
            self.model = nn.Sequential(
                # Input layer
                nn.Linear(100, 256),
                nn.ReLU(),
                # Hidden layer 1
                nn.Linear(256, 512),
                nn.ReLU(),
                # Hidden layer 2
                nn.Linear(512, 1024),
                nn.ReLU(),
                # Output layer
                nn.Linear(1024, 784),
                nn.Tanh(),
            )

        def forward(self, x):
            output = self.model(x)
            output = output.view(x.size(0), 1, 28, 28)
            return output