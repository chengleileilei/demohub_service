# Usage

## Initialize Environment
```
conda create -n demohub.efficientnet python=3.7
conda activate demohub.efficientnet
conda install pytorch torchvision==0.11.0 torchaudio cudatoolkit=10.2 -c pytorch
```
**Note**: The conda environment only need to be initialized once.

## Activate Environment
```
conda activate demohub.efficientnet
```

## Run demo
```
python demo.py ${image_path}
```

## Example
```
python demo.py images/dog.jpg
```

should print and saved in images/dog.jpg.efficientnet.json
```
French bulldog 0.504489541053772
Boston bull 0.43328842520713806
toy terrier 0.0019094339804723859
boxer 0.0011516936356201768
Staffordshire bullterrier 0.0007622102275490761
```
