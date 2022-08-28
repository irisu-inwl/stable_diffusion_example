# stable_diffusion_example

THIS REPO IS EXPERIMENTAL. 

DON'T YOU PUSH DOCKER IMAGE CREATED BY THIS REPO'S IMAGE BECAUSE THIS REPO'S DOCKER IMAGE IS INSECURED.

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