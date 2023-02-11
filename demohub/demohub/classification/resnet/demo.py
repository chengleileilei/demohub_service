import os.path as osp
import json
import argparse, ast
import torch
import torchvision
from torchvision import transforms
import os
basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":

    # prepare params
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, default='', help='')
    args = parser.parse_args()

    # prepare model
    model = torchvision.models.resnet152(pretrained=True)
    model.eval()

    # sample execution (requires torchvision)
    from PIL import Image
    input_image = Image.open(args.image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cpu')
        model.to('cpu')

    with torch.no_grad():
        output = model(input_batch)
    # Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
    # print(output[0])
    # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    # print(probabilities)

    # Read the categories
    with open(basedir + "/utils/imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    
    # Print and save
    results = {}
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())
        results[categories[top5_catid[i]]] = top5_prob[i].item()

    with open( args.image_path+'.alexnet.json', 'w+') as f:
        json.dump(results, f)
