# pytorch neural networks
from torch import nn, save, load
# optimizer
from torch.optim import Adam
# to load datsets
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# import dataset
train = datasets.MNIST(root = "data", download=True, train=True, transform=ToTensor())
dataset = DataLoader(dataset=train, batch_size=32)
# 10 classes, one for each digit 0 through 9


# image classifier neural network
class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels = 1, out_channels = 32, kernel_size = (3,3)),
            nn.ReLU(),
            nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = (3,3)),
            nn.ReLU(),            
            nn.Conv2d(in_channels = 64, out_channels = 64, kernel_size = (3,3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(in_features = 64*(28-6)*(28-6), 
                      out_features =  10)
        )    


    def forward(self, x):
        return self.model(x)

# instance of the neural network, loss, optimizer
clf = ImageClassifier().to('cpu')
opt = Adam(clf.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

# training function
if __name__ == "__main__":


    # local cpu training ~ 15 minutes
    print("\n\nBeginning the training process...")
    for epoch in range(10):
        for batch in dataset:
            X,y = batch
            X,y = X.to('cpu'), y.to('cpu')
            # make prediction
            yhat = clf(X)
            loss = loss_fn(yhat, y)

            # Apply backpro
            opt.zero_grad() # zero out gradient
            loss.backward() # calculate gradients
            opt.step()

        print(f"Epoch: {epoch} loss is {loss.item()}")

    with open('model_state.pt', 'wb') as f:
        save(clf.state_dict(), f)
