# EZ MLP

**Knowledge**

认识全连接层

**Exploit**

把脚本中矩阵乘法处的Bug修复即可获得flag

`line:4`维度匹配错误，交换位置：

```python
return np.matmul(weight, x) + bias
```

# ABC

**Knowledge**

矩阵运算，二维码

**Exploit**

在进行`A*B*C`后得到一个二维码，扫码获取flag

```python
from PIL import Image
import numpy as np

mat_A = np.load('A.npy')
mat_B = np.load('B.npy')
mat_C = np.load('C.npy')

mat_A, mat_B, mat_C = np.matrix(mat_A), np.matrix(mat_B), np.matrix(mat_C)

expResult = np.array(mat_A * mat_B * mat_C)

qr_len = 29
im=Image.new("RGB",(qr_len,qr_len))
for i in range(qr_len):
    for j in range(qr_len):
        if expResult[j][i] > 0:
            im.putpixel((j,i),(225,225,225))
im.save("exp_out.png")
```

# EZ Conv

**Knowledge**

认识卷积核

**Exploit**

把给出input通过conv获得二维码，扫码获得flag

```python
import numpy as np
from PIL import Image

inp = np.load('npys/inp.npy')
w = np.load('npys/w.npy')
b = np.load('npys/b.npy')

out = np.zeros((25, 5, 5))
for i in range(25):
    for j in range(5):
        for k in range(5):
            out[i, j, k] = np.sum(inp[0, j:j+5, k:k+5] * w[i]) + b[i]

out = np.array(out).reshape((25,25))

print(out)

qr_len = 25
im=Image.new("RGB",(qr_len,qr_len))
for i in range(qr_len):
    for j in range(qr_len):
        if out[j][i] > 0:
            im.putpixel((j,i),(225,225,225))
im.save("exp_out.png")
```

# A very happy MLP

**Knowledge**

全连接神经网络前向传播运算

**Exploit**

模型使用简单的全连接神经网络，输出维度为3

考察选手能否在给定`x`，`y`，`f()`的情况下解出`f(x+flag)=y`，其中`f()`为提供的模型，中间有已经被扩大范围了的`sigmoid()`作为激活函数

本题不需要训练，只需要写出`sigmoid()`以及`fc()`的反函数即可直接求得flag，梯度下降反而不能得到正确的flag，所以特意在description中强调了无需训练

```python
import torch
import numpy as np
from model import Net



def inv_fc(y, weight, bias):
    return torch.matmul(y - bias, torch.pinverse(weight).T)

def inv_sigmoid(y):
    return torch.log(y / (1 - y))

def float2chr(f):
    return chr(int(np.round((f + 1) / 2. * 255.)))

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



net = Net()

# Load model and base_input
checkpoint = torch.load('_Checkpoint.pth')
net.load_state_dict(checkpoint['model'])
base_input = checkpoint['input']

intended_out = torch.tensor([2., 3., 3.])
intended_fc3_inp = inv_fc(intended_out, net.fc3.weight, net.fc3.bias)

intended_fc2_out = inv_sigmoid((intended_fc3_inp + net.scale / 2) / net.scale)
intended_fc2_inp = inv_fc(intended_fc2_out, net.fc2.weight, net.fc2.bias)

intended_fc1_out = inv_sigmoid((intended_fc2_inp + net.scale / 2) / net.scale)
intended_fc1_inp = inv_fc(intended_fc1_out, net.fc1.weight, net.fc1.bias)

out = net(intended_fc1_inp)
assert torch.equal(torch.round(out.detach(), decimals=6), intended_out)

flag_tensor = intended_fc1_inp - base_input
torch.save(flag_tensor, '_ExpFlag.pth')

verify('_ExpFlag.pth')
```



# Classification

**Knowledge**

DNN的使用

**Exploit**

使用`Resnet`对图片序列进行分类，获得的label就是flag的ord

此处埋了一个坑，如果选手未调用`model.eval()`更改模型状态（as shown in `line:8`），则将因为batch norm层的问题无法得到正确的flag

```python
import torchvision
from torchvision import transforms
import torch
from PIL import Image
import numpy as np

model = torchvision.models.resnet50(pretrained=True)
model.eval()

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize,
])

preds = []
for i in range(60):
    img = Image.open('imgs/' + str(i) + '.png')
    pred = model(transform(img).unsqueeze(0)).detach()[0]
    pred = torch.argmax(pred).item()
    preds.append(pred)

flag = ''
salt = np.load('salt.npy')
for i in range(len(preds)):
    flag += chr((preds[i]-salt[i])%1000)
print(flag)
```

# Visual Hacker

**Knowledge**

认识Gaze Estimation模型，三维空间下的向量计算

**Exploit**

选手需要先了解模型的背景以及论文中提供的Github Repo，然后将所有Image Sequence通过Gaze Model获取Gaze角度，最后将这些视线角度通过某种三维空间中的映射方式获取flag的字符

```python
# general_func.py

from transform import transform
from torch import nn
import torch
import numpy as np
from model import L2CS



softmax = None
idx_tensor = None



def InitVar(use_gpu=True):
    global softmax, idx_tensor
    softmax = nn.Softmax(dim=1)
    idx_tensor = [idx for idx in range(90)]
    idx_tensor = torch.FloatTensor(idx_tensor)
    if use_gpu:
        idx_tensor = idx_tensor.cuda()



def InitModel(checkpoint_path, use_gpu=True):
    model = L2CS()
    checkpoint = torch.load(checkpoint_path)
    model.load_state_dict(checkpoint)
    model.eval()
    if use_gpu:
        model = model.cuda()
    return model



def get_pitch_yaw(imgs, model, use_gpu=True):

    for i in range(len(imgs)):
        imgs[i] = transform(imgs[i])
    imgs = torch.stack(imgs, dim=0)
    if use_gpu:
        imgs = imgs.cuda()

    # Copied from https://github.com/Ahmednull/L2CS-Net/tree/main
    # ========================================================================
    # Gaze prediction
    gaze_pitch, gaze_yaw = model(imgs)
    pitch_predicted = softmax(gaze_pitch)
    yaw_predicted = softmax(gaze_yaw)

    # Get continuous predictions in degrees.
    pitch_predicted = torch.sum(pitch_predicted.data * idx_tensor, dim=1) * 4 - 180
    yaw_predicted = torch.sum(yaw_predicted.data * idx_tensor, dim=1) * 4 - 180

    pitch_predicted = pitch_predicted.cpu().detach().numpy() * np.pi / 180.0
    yaw_predicted = yaw_predicted.cpu().detach().numpy() * np.pi / 180.0
    # ========================================================================

    return pitch_predicted, yaw_predicted



def get_direction(pitch, yaw):
    # Get direction from pitch and yaw
    direction = np.array([
        np.cos(pitch) * np.sin(yaw),    # x: right
        np.sin(pitch),                  # y: up
        np.cos(pitch) * np.cos(yaw),    # z: forward
    ])
    return direction.T



def get_intersection(direction):
    # plane_distance: distance from camera to plane
    # plane_size: size of square plane
    plane_normal = np.array([0, 0, 1])
    ray_origin = np.array([0, 0, 0])
    
    # Get intersection of ray and plane
    intersection = []
    for i in range(len(direction)):
        t = 1.0 / np.dot(direction[i], plane_normal)
        inter_p = ray_origin + t * direction[i]
        intersection.append([-inter_p[0], inter_p[1]])

    return np.array(intersection)



def get_grid_point(intersection, resolution, plane_size):
    # plane_size: size of square plane
    points = []
    t0 = plane_size / 2
    t1 = plane_size / resolution
    for i in range(len(intersection)):
        x = np.round((intersection[i][0] + t0) / t1)
        y = np.round((intersection[i][1] + t0) / t1)
        # Check if x, y is in range
        if x < 0 or x >= resolution or y < 0 or y >= resolution:
            points.append(None)
        else:
            points.append((int(x), int(y)))
    return points
```

```python
# exp.py

from general_func import get_pitch_yaw, get_direction, get_intersection, InitModel, InitVar
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt



def ls(directory=None):
    if directory:
        try:
            file_list = os.listdir(directory)
        except FileNotFoundError:
            return f"Error: '{directory}' not found."
        except PermissionError:
            return f"Error: Permission denied for '{directory}'."
    else:
        try:
            file_list = os.listdir()
        except PermissionError:
            return "Error: Permission denied for current directory."

    return file_list


def mkdir(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except PermissionError:
        print(f"Error: Permission denied for creating '{directory_path}'.")
    except OSError as e:
        print(f"Error: {e.strerror} - '{directory_path}'")



if __name__ == '__main__':

    use_gpu = False
    batch_size = 16
    dir_rec_path = 'ExpTemp/direction_record/'

    InitVar(use_gpu=use_gpu)
    model = None
    # Get direction record
    mkdir(dir_rec_path)
    for i in range(10):

        if os.path.exists(dir_rec_path + str(i) + '.npy'):
            continue

        if model is None:
            model = InitModel('checkpoint.pkl', use_gpu=use_gpu)

        capture_dirs = ['Captures/' + str(i) + '/' + img_path for img_path in ls('Captures/' + str(i) + '/')]
        
        direction_record = []
        img_record = []
        for capture_dir in capture_dirs:
            img_record.append(Image.open(capture_dir))
            if len(img_record) < batch_size and capture_dir != capture_dirs[-1]:
                continue

            pitch, yaw = get_pitch_yaw(img_record, model, use_gpu=use_gpu)
            direction = list(get_direction(pitch, yaw))
            direction_record.extend(direction)

            img_record = []
        
        direction_record = np.array(direction_record)
        np.save(dir_rec_path + str(i) + '.npy', direction_record)

    # Draw intersection points
    mkdir('ExpTemp/fig/')
    for i in range(10):
        direction_record = list(np.load(dir_rec_path + str(i) + '.npy'))
        points = [get_intersection([direction])[0] for direction in direction_record]
        points = np.array(points)
        plt.scatter(points[:,1], -points[:,0], s=200.0)
        plt.savefig('ExpTemp/fig/' + str(i) + '.png')
        plt.clf()
```

