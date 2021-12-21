### docker gpu
- docker-compose 이용, 특정 GPU만 할당
    ```
    - docker run -e NVIDIA_VISIBLE_DEVICES=1 imagename 명령어
    - docker-compose.yml
    version: '3'

    ```
    ```
    services:
    train:
        image: imagename
        environment:
            - NVIDIA_VISIBLE_DEVICES=1
        // or runtime: nvidia
        command:
            명령어
    ```


### nvidia-docker Command
- $ nvidia-docker login
- $ nvidia-docker build --tag <imagename>:<tagname>
- $ nvidia-docker run, build, commit, push, start, exec, attach..
- $ nvidia-docker history <imagename>:<tagname>
- $ nvidia-docker cp <host파일경로> <containername>:<docker파일경로>
- $ docker log [options] container

### nvidia environment
- nvidia driver
- os버전에 맞는 cuda설치, 이때 다른 버전의 cuda가 돌아가고 있으면 안된다.
- nvidia-docker, docker nvidia-container-tookit 설치
    - nvidia-docker 이용하지 않고, gpu 쓰는 방법
        - docker run --gpus all[0,1..]
        - docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all[0,1..]
- host의 cuda 버전과, 도커 이미지의 cuda버전 그리고 cuda버전에 맞는 tensorflow, pytorch 사용이 필수