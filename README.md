### docker gpu
- docker-compose 이용, 특정 GPU만 할당
    ```
    +-----------------------------------------------------------------+
    | Processes:                                                      |
    |  GPU   GI   CI    PID   Type   Process name          GPU Memory |
    |        ID   ID                                       Usage      |
    |=================================================================|
    |    0   N/A  N/A  1140      G   /usr/lib/xorg/Xorg          9MiB | // 0
    |    0   N/A  N/A  1377      G   /usr/bin/gnome-shell        6MiB | // 1
    +-----------------------------------------------------------------+
    ```

    - docker run -e NVIDIA_VISIBLE_DEVICES=1 imagename 명령어
    - docker-compose.yml
    ```
    version: '3'

    services:
    train:
        image: imagename
        environment:
            - NVIDIA_VISIBLE_DEVICES=1
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