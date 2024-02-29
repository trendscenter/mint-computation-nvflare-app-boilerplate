docker run --rm -it --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name flare \
    -v /$(pwd):/workspace \
    -w //workspace \
    nvflare-pt:latest