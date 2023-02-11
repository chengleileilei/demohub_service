# Usage

## Initialize Environment
```
conda create -n demohub.regnet python=3.7
conda activate demohub.regnet
conda install pytorch torchvision==0.11.0 torchaudio cudatoolkit=10.2 -c pytorch
```
**Note**: The conda environment only need to be initialized once.

## Activate Environment

```
conda activate demohub.regnet
```

## Run demo
```
python demo.py ${image_path}
```

## Example
```
python demo.py images/dog.jpg
```

should print and saved in images/dog.jpg.regnet.json
```
French bulldog 0.9992307424545288
Boston bull 0.0005822174716740847
toy terrier 4.839129906031303e-05
Chihuahua 4.475519017432816e-05
Cardigan 3.996558370999992e-05
```
