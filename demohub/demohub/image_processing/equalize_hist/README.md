# Usage

## Initialize Environment
```
conda create -n demohub.equalize_hist python=3.7
conda activate demohub.equalize_hist
pip install opencv-python
```
**Note**: The conda environment only need to be initialized once.

## Activate Environment

```
conda activate demohub.equalize_hist
```

## Run demo
```
python demo.py ${image_path} --space ${space} # support rgb and hsv
```

## Example
```
python demo.py images/candle.jpg --space hsv
```

- input image 
![](images/candle.jpg)

- output_image
![](images/candle.jpg.eh.hsv.jpg)

