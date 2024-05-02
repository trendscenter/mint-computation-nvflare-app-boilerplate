# Hello World Tutorial

<iframe width="1280" height="720" src="https://www.youtube.com/embed/_wGZxmQclFA" title="Tutorial - Run the NVFLARE boilerplate repo for COINSTAC" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Build the dev image
```
docker build -t nvflare-pt -f Dockerfile-dev .
```

# Run the container
## Linux/Mac:
```
./dockerRun.sh
```
## Windows:
```
docker run --rm -it ^
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 ^
    --name flare ^
    -v %cd%:/workspace ^
    -w //workspace ^
    nvflare-pt:latest
```

# Run the simulator
```
nvflare simulator -c site1,site2 ./jobs/job
```

# View the results
Navigate to:
```
./test_results/simulate_job
```