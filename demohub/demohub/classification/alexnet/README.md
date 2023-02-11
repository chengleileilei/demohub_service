# Usage

## Initialize Environment
```
conda create -n demohub.alexnet python=3.7
conda activate demohub.alexnet
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
```
**Note**: The conda environment only need to be initialized once.

## Activate Environment

```
conda activate demohub.alexnet
```

## Run demo
```
python demo.py ${image_path}
```

## Example
```
python demo.py images/dog.jpg
```

should print and saved in images/dog.jpg.alexnet.json
```
Boston bull 0.880911111831665
French bulldog 0.11439560353755951
boxer 0.0023653910029679537
toy terrier 0.0007555637857876718
Chihuahua 0.0006861794972792268
```
