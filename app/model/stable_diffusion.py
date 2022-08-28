import logging
from os import getenv
from typing import List

from PIL import Image

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

# StableDiffusionパイプラインの準備
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16, use_auth_token=True)
pipe.to(device) if torch.cuda.is_available() else pipe.to("cpu")

def generate_image(prompts: List[str], init_image: Image = None, num_inference_steps: int = 50):
  with autocast("cuda"):
    images = pipe(prompts, init_image=init_image, num_inference_steps=num_inference_steps, guidance_scale=7.5)["sample"]
  return images

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    # grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid