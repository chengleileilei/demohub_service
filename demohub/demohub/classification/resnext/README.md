# Usage

## Initialize Env
```
conda create -n demohub.resnext python=3.7
conda activate demohub.resnext
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
```
**Note**: The conda env only need to be initialized once.

## Activate Env
```
conda activate demohub.resnext
```

## Run demo
```
python demo.py ${image_path}
```

## Example
```
python demo.py images/dog.jpg
```

should print and saved in images/dog.jpg.resnext.json
```
French bulldog 0.8786303400993347
Boston bull 0.11863873153924942
toy terrier 0.002016139216721058
Chihuahua 0.00043735586223192513
boxer 0.00011237680882913992
```
