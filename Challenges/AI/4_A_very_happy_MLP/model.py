import torch



class Net(torch.nn.Module):
    def __init__(self):
        torch.nn.Module.__init__(self)
        self.fc1 = torch.nn.Linear(30, 20)
        self.fc2 = torch.nn.Linear(20, 10)
        self.fc3 = torch.nn.Linear(10, 3)
        self.scale = 40.0
    
    def forward(self, x):
        x = self.fc1(x)
        x = torch.sigmoid(x)
        # The following line of code enlarges the vector space
        x = x * self.scale - self.scale / 2
        x = self.fc2(x)
        x = torch.sigmoid(x)
        x = x * self.scale - self.scale / 2
        x = self.fc3(x)
        return x



# Hints:

#  > Learn all the functions in the model, what are their inputs and outputs, what are their formulas?

#  > Once you know the formulas, you can easily calculate the flag by code without training.