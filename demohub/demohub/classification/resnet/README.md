# Usage

## Initialize Environment
```
conda create -n demohub.resnet python=3.7
conda activate demohub.resnet
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
```
**Note**: The conda environment only need to be initialized once.

## Activate Environment
```
conda activate demohub.resnet
```

## Run demo
```
python demo.py ${image_path}
```

## Example
```
python demo.py images/dog.jpg
```

should print and saved in images/dog.jpg.resnet.json
```
French bulldog 0.9953617453575134
Boston bull 0.0039363279938697815
toy terrier 0.00045485899318009615
Chihuahua 0.00013606551510747522
boxer 5.8253270253771916e-05
```
