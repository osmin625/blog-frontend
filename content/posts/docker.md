---
title: 나를 위한 Docker 총정리
date: 2023-02-13T13:00:00+09:00
categories: [Tools, Ops]
tags: [Docker, Docker Compose]
type: post
---
| 눈송이 서버 | 가상화 |
| --- | --- |
| VM(Virtual Machine) | Container |
| Docker Image | Docker Container |

### **Background —** 왜 도커를 써야하나?

- **눈송이 서버들(Snowflake Servers)**
    
    모든 눈송이의 모양이 다르듯, 서버들도 모두 다르다.
    
    서버가 여러개인 경우, 서버 구성 시기에 따라 운영체제, 컴파일러, 설치된 패키지 등의 버전이 달라지게 된다.
    
    눈송이 서버를 방지하기 위해, 새로 서버를 구성할 때 다양한 방식으로 서버 운영 기록을 저장해 둔다.
    
- **가상화**
    
    특정 소프트웨어 환경을 만든 후, Local 서버나 Production 서버에서 그대로 활용하는 방법.
    
    어느 운영체제에서나 동일한 환경으로 프로그램 실행 가능
    
- **VM(Virtual Machine)**
    
    고전적인 가상화 방법
    
    OS 위의 OS → 과도한 리소스 활용
    
- **Container**
    
    VM을 다소 경량화하여, 빠르고 가벼운 가상화 지원
    

### **Docker**

**컨테이너 기술을 쉽게 사용할 수 있도록 나온 도구**

서버 운영 기록을 코드화한 것

**Dockerfile → Docker Image → Docker Container**

- **Dockerfile**
    
    Image를 만드는 설계도. 
    
    즉, 주형틀을 만드는 설계도.
    
- **Docker Image**
    
    Dockerfile을 기반으로 생성된 주형틀.
    
    객체 지향 언어에 비유하자면, Class에 해당한다.
    
    직접 제작할 수도 있고, Docker hub에서 다운받아 사용할 수도 있다.
    
- **Docker Container**
    
    Image로 생성해낸 초경량 컴퓨터.
    
    비유하자면, Instance에 해당한다.
    
    `Docker run`으로 Container를 찍어낼 수 있다.
    

자신만의 이미지를 생성한 후, 원격 저장소에 저장하면 어디서나 사용이 가능하다.

### Docker use case

![docker](/imgs/docker1.png)

## 기존 이미지 활용하기

1. `docker pull 이미지 이름:태그`   — 필요한 이미지 다운
    
    Dockerhub에서 공개된 모든 이미지를 다운받을 수 있다.
    
    Registry : Dockerhub, AWS ECR, GCP GCR
    
2. `docker images` — 다운받은 이미지 목록 확인
3. `docker run 이미지 이름:태그` — 이미지를 기반으로 **컨테이너 생성**
    
    컨테이너 생성 시 바로 실행된다.
    

---

위의 동작들은 자주 수행되지 않는다.

- `docker ps` — 실행중인 컨테이너 목록 확인
1. `**docker start [컨테이너 이름(ID)]` 컨테이너 실행하기.**
    - `docker exec -it “컨테이너” /bin/bash` — 컨테이너에 진입
        
        exec가 필요하다면 docker desktop을 활용하는 것이 훨씬 편하다.
        
2. `**docker stop 컨테이너 이름(ID)` — 실행 중인 컨테이너를 중지**
    - `docker rm 컨테이너 이름(ID)` — 중지된 컨테이너 삭제

---

## Docker 이미지 만들기 `docker build`

### **1. 폴더 하나를 만든 후, poetry 세팅과 torch 관련 패키지 설치**

`mkdir docker_prac && cd docker_prac`

`python -V # python 3.10.6`

`poetry init`

`poetry add torch torchvision`

### **2. `Dockerfile` 생성 및 작성하기**

Docker Image를 빌드하기 위한 정보가 담긴다.

```docker
FROM 이미지이름:태그

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN pip install pip=23.0.1 && \
		pip install poetry==1.2.1 && \
		poetry export -0 requirements.txt && \
		pip install -r requirements.txt

CMD ["python", "main.py"]
```

보통 처음부터 만드는 경우는 드물고, 기존 이미지를 변경하거나, 추가해서 사용한다.

- Dockerfile Options
    - **FROM** : 베이스 이미지
        - 어느 이미지에서 시작할 지를 의미한다.
    - **COPY / ADD** : build 명령 중간에 호스트의 파일 또는 폴더를 이미지에 가져오는 것
        - ADD 명령문은 좀 더 파워풀한 COPY 명령문이라고 생각할 수 있다.
        - ADD 명령문은 일반 파일 뿐만 아니라 압축 파일이나 네트워크 상의 파일도 사용할 수 있다.
        - 이렇게 특수한 파일을 다루는 게 아니라면 COPY 명령문을 사용하는 것이 권장된다.
    - **WORKDIR** : 작업 디렉토리를 지정한다. 해당 디렉토리가 없으면 새로 생성한다.
        - 작업 디렉토리를 지정하면 그 이후 명령어는 해당 디렉토리를 기준으로 동작한다.
        - cd 명령어와 동일하다.
    - **RUN** : 새로운 레이어에서 명령어를 실행하고, 새로운 이미지를 생성한다.
        - RUN 명령을 실행할 때 마다 레이어가 생성되고 캐시된다.
        - 따라서 RUN 명령을 따로 실행하면 apt-get update는 다시 실행되지 않아서 최신 패키지를 설치할 수 없다.
        - 위 처럼 RUN 명령 하나에 apt-get update와 install을 함께 실행 해주자.
    - **CMD :** 컨테이너를 생성할 때 실행할 명령어
        - 보통 컨테이너 내부에서 항상 돌아가야하는 서버를 띄울 때 사용한다.
        - 컨테이너를 생성할 때만 실행된다. (docker run)
        - 컨테이너 생성 시, 추가적인 명령어에 따라 설정한 명령어를 수정할 수 있다.
        - CMD ["<커맨드>", "<파라미터1>", "<파라미터2>"]
        - CMD <커맨드> <파라미터1> <파라미터2>
    
    ---
    
    - **MAINTAINER** : 이미지를 생성한 개발자의 정보 (1.13.0 이후 사용 X)
    - **LABEL** : 이미지에 메타데이터를 추가 (key-value 형태)
    - **EXPOSE** : Dockerfile의 빌드로 생성된 이미지에서 열어줄 포트를 의미한다.
        - 호스트 머신과 컨테이너의 포트 매핑시에 사용된다.
        - 컨테이너 생성 시 -p 옵션의 컨테이너 포트 값으로 EXPOSE 값을 적어야 한다.
        - 이 이미지에서 해당 포트를 외부로 개방한다고 명시하는 것일 뿐, 
        사용자가 해당 포트로 접근이 가능한 것은 아니다.
    - **USER** : 이미지를 어떤 계정에서 실행 하는지 지정
        - 기본적으로 root에서 해준다.
    - **ENTRYPOINT :** 컨테이너를 시작할 때 실행할 명령어
        - 컨테이너를 시작할 때마다 실행된다. (docker start)
        - 컨테이너 시작 시, 추가적인 명령어 존재 여부와 상관 없이 무조건 실행된다.
        - ENTRYPOINT ["<커맨드>", "<파라미터1>", "<파라미터2>"]
        - ENTRYPOINT <커맨드> <파라미터1> <파라미터2>
    - **ENV** : 이미지에서 사용할 환경 변수 값을 지정한다.
        - path 등

### 3. `docker image build [OPTIONS] PATH | URL | -`

**예시) `docker build -t 02-docker:latest .`**

`.`은 현재 폴더에 Dockerfile이 있음을 의미한다.

태그는 미 지정 시 latest로 채워진다.

[도커 이미지 이름 컨벤션](https://climbtheladder.com/10-docker-image-naming-convention-best-practices/)

options

- `-t`: 이미지 명과 태그 명을 붙이는 옵션
    
    실제 사용에서 거의 필수적이다.
    
- `-f`: 기본 옵션인 Dockfile 대신 다른 파일 명을 사용할 경우 필요한 옵션
- Docker image 삭제 방법
    
    `docker images`로 imageID 확인
    
    `docker rmi [imageID]`
    
    - container에서 사용 중인 image의 경우 삭제가 불가능함.
    - 종료한 container가 사용 중인 image의 경우 `-f` 옵션으로 삭제 가능.

## Docker Container 만들기 `docker run`

### 4. `docker run [OPTIONS] IMAGE_NAME[:TAG|@DIGEST] [COMMAND] [ARG...]`

options

- `**-p [host port:container port]` host port를 container port로 포워딩시키기.**
    
    예시) `docker run -p 8080:8080 backserv`
    
    해당 옵션을 제공하지 않으면 container port로 접근할 수가 없다.
    
    꼭 같은 포트로 지정해줄 필요는 없다.
    
- **`-P(대문자)` 랜덤한 host port가 Dockfile에서 `EXPOSE` 구문으로 명시한 포트에 매핑된다.**
    
    호스트 OS에서 컨테이너를 실행할 때 매번 포트 룰을 정하는 것은 귀찮기 때문에, 랜덤한 포트를 EXPOSE한 포트에 매핑시킨다.
    
    도커를 다루는 GUI 프로그램에서 -p 옵션으로 제공할 수 있도록 힌트 역할을 하기도 한다.
    
- `**-d**`: 컨테이너를 백그라운드에서 실행한다.
- `-v [host dir:container dir]`: 호스트와 컨테이너 간의 디렉토리를 공유한다.
    
    컨테이너 내부의 파일을 Host와 공유하는 방법: `Volume Mount`
    
    만약 디렉토리를 공유하지 않는다면 컨테이너를 삭제할 때 컨테이너 내부 파일은 삭제된다.
    
    ex) docker run -it -p8888:8888 -v/some/host/folder/workspace
    jupyter/minimal -notebook
    
- `-it` 상호 입출력 옵션 및 tty 활성화
    
    tty를 활성화하면 default로 bash shell을 사용한다.
    
    해당 옵션을 제공하지 않으면 터미널에서의 ctrl+C 명령이 동작하지 않는다.
    
- `--name [CONTAINER_NAME]` container 이름을 직접 지정하고자 할 때 사용한다.
- `-rm` 명령이 종료되면 컨테이너를 내리는 옵션
    
    해당 옵션을 주지 않으면 컨테이너를 종료하더라도 exited된 상태로 ps에 남아있게 된다.
    
- `[COMMAND]` 이미지가 가진 시작 명령어(CMD로 추정)를 무시하고 `COMMAND`를 대신 실행한다.

### `docker commit`

### `docker save`

### Docker Container 시작

`docker start [container id]`

### Docker Container 종료

`docker ps`

`docker stop [container id]` : 동작을 완료하는 것을 기다린 후 종료

`docker kill [container id]` : 바로 종료

### Docker with VS Code

[Visual Studio Code에서 Docker 앱 시작](https://learn.microsoft.com/ko-kr/visualstudio/docker/tutorials/docker-tutorial?WT.mc_id=vscode_docker_aka_getstartedwithdocker)

1. Docker를 Linux 컨테이너 모드로 설정하기

**Settings > Builders > desktop-linux**

![docker](/imgs/docker0.png)

1. VS Code에서 새 터미널 열기

## Docker Compose 사용하기

### 1. docker-compose.yml 파일 작성하기

```docker
# compose 파일 버전
version: "1"
services:
  # 서비스 명
  backend:
    # 사용할 이미지
    image: backserv
    # 컨테이너 실행 시 재시작
    restart: always
    # 컨테이너명 설정
    container_name: blogback
    # 접근 포트 설정 (컨테이너 외부:컨테이너 내부)
    ports:
      - "8080:8080"
    # 환경 변수 설정
    # environment:

    # 볼륨 설정
    # volumes:

  postgresql:
    image: postgres
    # 컨테이너 실행 시 재시작
    restart: always
    container_name: blogdb
    ports:
      - "5432:5432"
    # 환경 변수 설정
    environment: 
      # PostgreSQL 계정 및 패스워드 설정 옵션
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - C:\Users\Ohseungmin\workspace\blog\pgdata:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    # 컨테이너 실행 시 재시작
    restart: always
    # 컨테이너명 설정
    container_name: pgadmin4
    ports:
      - "5050:80"
    # 환경 변수 설정
    environment:
      PGADMIN_DEFAULT_EMAIL: tmdals179@naver.com
      PGADMIN_DEFAULT_PASSWORD: password
    volumes:
      - C:\Users\Ohseungmin\workspace\blog\pgadmin:/var/lib/pgadmin
```

### 2. `docker-compose up -d` : 컨테이너 한 번에 생성하고 실행하기

### 3. `docker-compose stop -d` : 컨테이너 한 번에 종료하기

### 4. `docker-compose start -d` : 컨테이너 한 번에 실행하기

### 5. `docker-compose down` : 컨테이너 한 번에 종료하고 삭제하기

**이외**

[https://www.daleseo.com/docker-compose/](https://www.daleseo.com/docker-compose/)

[https://docs.docker.com/compose/reference/](https://docs.docker.com/compose/reference/)

[https://docs.docker.com/compose/](https://docs.docker.com/compose/)

## Docker Network

[https://jaehun2841.github.io/2018/12/01/2018-12-01-docker-5/#Container-모드-이것도-Bridge-모드의-일부](https://jaehun2841.github.io/2018/12/01/2018-12-01-docker-5/#Container-%EB%AA%A8%EB%93%9C-%EC%9D%B4%EA%B2%83%EB%8F%84-Bridge-%EB%AA%A8%EB%93%9C%EC%9D%98-%EC%9D%BC%EB%B6%80)

[https://www.daleseo.com/docker-networks/](https://www.daleseo.com/docker-networks/)

[https://velog.io/@jihwankim94/Docker-Host-와-Container-내부의-app들이-통신이-안되는-이유](https://velog.io/@jihwankim94/Docker-Host-%EC%99%80-Container-%EB%82%B4%EB%B6%80%EC%9D%98-app%EB%93%A4%EC%9D%B4-%ED%86%B5%EC%8B%A0%EC%9D%B4-%EC%95%88%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0)

### reference

[https://hynek.me/articles/docker-signals/](https://hynek.me/articles/docker-signals/)

[https://docs.docker.com/](https://docs.docker.com/)