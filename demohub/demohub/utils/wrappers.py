from typing import Tuple
from PIL import Image

import torch


def imread_norm_to_tensor_batch_device(
    image_path: str,
    size: int,
    mean: Tuple[float, float, float]=[0.485, 0.456, 0.406],
    std: [float, float, float]=[0.229, 0.224, 0.225],
    device: torch.device=torch.device("cpu")):
    input_image = Image.open(args.image_path)
    preprocess = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    input_batch = input_batch.to(device)
    return input_batch


def imagenet_probs2categories_dumpjson(
    porbs: torch.tensor,
    json_path: str,
    topk: int=5):
    with open(basedir + "./imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]

    topk_prob, topk_catid = torch.topk(probs, topk)

    results = {}
    for i in range(topk_prob.size(0)):
        results[categories[topk_catid[i]]] = topk_prob[i].item()

    with open(json_path, 'w+') as f:
        json.dump(results, f)