# stable_diffusion_example

demo app streamlit+stable diffusion

THIS REPO IS EXPERIMENTAL. 

## Demo

https://twitter.com/irisuinwl/status/1563795746062643200

https://twitter.com/irisuinwl/status/1563799137102901248

## Preliminary: your huggingface token setting

### Local Poetry Setting

```
poetry install
```

### Create Huggingface Token

```
poetry run python3 -c 'from huggingface_hub import HfFolder; HfFolder.save_token("<TOKEN>")'
```

See: https://github.com/huggingface/transformers/issues/16813

## Build & Running

```
env DIR=$(pwd) docker compose -f ./app/docker-compose.yaml up
```
