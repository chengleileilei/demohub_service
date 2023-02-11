import argparse
import timm

import torch

from demo.utils import imread_norm_to_tensor_batch_device


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, default="", help="")
    parser.add_arguement(
        "model", type=str, default="", options=timm.list_models(pretrained=True)
    )
    args = parser.parse_args()


def demo(
    image_path: str.
    model: str):
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    model = timm.create_model(model, pretrained=True, in_chans=1)
    model = model.eval()
    model = model.to(device)    

    image = imread_norm_to_tensor_batch_device(image_path, device=device)

    probs = model(image)

    imagenet_probs2categories_dumpjson(
        probs,
        f"{image_path}.{model}.json",
        topk=10)


if __name__ == "__main__":
    args = arg_parse()
    demo(image_path=args.image_path, model=args.model)
