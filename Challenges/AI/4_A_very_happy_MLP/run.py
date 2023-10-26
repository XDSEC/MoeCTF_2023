import numpy as np
import torch
from model import Net



def chr2float(c):
    return ord(c) / 255. * 2. - 1



def float2chr(f):
    return f



def verify(flag_path):

    def verify_flag(flag_tensor):
        checkpoint = torch.load('_Checkpoint.pth')
        net = Net()
        net.load_state_dict(checkpoint['model'])
        base_input = checkpoint['input']
        output = net(base_input + flag_tensor)
        return torch.equal(torch.round(output.detach(), decimals=5), torch.tensor([2., 3., 3.]))

    def show_flag(flag_tensor):
        flag = ''
        for f in np.array(flag_tensor).ravel():
            flag += float2chr(f)
        print('moectf{' + flag + '}')
    
    try:
        flag_tensor = torch.load(flag_path).detach()
    except:
        print('Invalid flag path.')
        return
    if verify_flag(flag_tensor):
        print('You made this little MLP happy, here\'s his reward:')
        show_flag(flag_tensor)
    else:
        print('Sad :(')



if __name__ == '__main__':
    verify('_Flag.pth')