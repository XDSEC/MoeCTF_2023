import torch.nn as nn
from torchvision.models import resnet18



class L2CS(nn.Module):
    def __init__(self):
        super(L2CS, self).__init__()
        self.backend = resnet18()
        self.backend = nn.Sequential(*list(self.backend.children())[:-1])

        self.avg_decoder = FC_block(512, 2048, [1024, 1024])
        
        self.fc_yaw_gaze = nn.Linear(2048, 90)
        self.fc_pitch_gaze = nn.Linear(2048, 90)


    def forward(self, x):
        x = self.backend(x)
        x = x.view(x.size(0), -1)
        x = self.avg_decoder(x)

        pre_yaw_gaze =  self.fc_yaw_gaze(x)
        pre_pitch_gaze = self.fc_pitch_gaze(x)
        return pre_yaw_gaze, pre_pitch_gaze



class FC_block(nn.Module):
    def __init__(self, input_size, output_size, mid_sizes=[]):
        # mid_sizes: list of int, the size for each hidden layer
        nn.Module.__init__(self)
        self.input_size = input_size
        self.output_size = output_size
        self.mid_sizes = mid_sizes

        self.fc = nn.ModuleList()
        if len(mid_sizes) == 0:
            self.fc.append(nn.Linear(input_size, output_size))
        else:
            self.fc.append(nn.Linear(input_size, mid_sizes[0]))
            for i in range(len(mid_sizes) - 1):
                self.fc.append(nn.Linear(mid_sizes[i], mid_sizes[i + 1]))
            self.fc.append(nn.Linear(mid_sizes[-1], output_size))


    def forward(self, x):
        for i in range(len(self.fc)):
            x = self.fc[i](x)
            if i != len(self.fc) - 1:
                x = nn.ReLU()(x)
        return x