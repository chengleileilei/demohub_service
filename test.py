from torchvision.models import resnet50
import torch
from torchstat import stat
from thop import profile
# model = resnet50()

model = torch.nn.Sequential(
    resnet50(), 
    torch.nn.Linear(1000, 2048),
    torch.nn.BatchNorm1d(2048),
    torch.nn.Linear(2048, 512),
    torch.nn.BatchNorm1d(512),
    torch.nn.Linear(512, 128),
    torch.nn.BatchNorm1d(128),
    torch.nn.Linear(128, 32),
    torch.nn.BatchNorm1d(32),
)

model = model.eval()

stat(model, (3, 256, 128))

# input = torch.randn(1, 3, 256, 128)
# print(model(input).shape)
# macs, params = profile(model, inputs=(input, ))

# print('FLOPs = ' + str(macs/1000**3) + 'G')
# print('Params = ' + str(params/1000**2) + 'M')