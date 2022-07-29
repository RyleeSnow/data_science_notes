## Try the "Hello-World"

```bash
$ sudo service docker start 
$ docker run hello-world
```

If the docker is working well, you shall see some outputs like "Hello from Docker! This message shows that your installation appears to be working correctly."

## Install docker

[reference: https://docs.docker.com/engine/install/ubuntu/]

- Remove the old version

```bash
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

- Set up the repository

```bash
$ sudo apt-get update

$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
  
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
 
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```

- Sometimes, you may need to use a specific version of docker-composer.

```bash
$ curl -L https://github.com/docker/compose/releases/download/1.26.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
```

# Install the image

Run the following comment

```bash
python environment.py -n 1 -p 22 -a build
```

You can use the following command to check if the docker image is correctly installed. (You shall see you image name and image_ID, record the ID)

```bash
docker images
```

# Create and Run a container

- Create a container based on the image

```bash
docker run -it -v /home/eliza:/home/eliza -v /usr/bin:/usr/bin 0a205763ff4d /bin/bash
docker run -it -v /home/eliza:/home/eliza --gpus all 0a205763ff4d /bin/bash
```

- After you enter the container for the first time, you will see your container_ID as "root@{container_ID}"
- If you want to use the conda environment, you need to do:

```bash
$ conda init bash

$ exit

$ docker start {container_ID}

$ docker attach {container_ID}

$ conda activate fair
```

- Anytime you want you check your containers

```bash
$ docker ps
$ docker ps -a
```

# Git

```
git config --global credential.helper store
git clone https://adlm.nielseniq.com/bitbucket/scm/rc/eliza.git
```

# Transfer files between the host and the container

- Get the container_long_ID

```bash
$ docker inspect -f '{{.Id}}' {container_ID}
```

- Transfer files

```bash
docker cp {your_host_file_path} {container_long_ID}:{the_container_file_path}
```

# Remote ssh

```bash
$ docker run -it -p 5001:22 -p 5000:8080 -v /home/storage/eliza:/home/eliza e11195ce59d6 /bin/bash
$ sudo apt-get install openssh-client
$ sudo apt-get install openssh-server

PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PermitRootLogin yes
```

docker run -it --gpus all -v /home/eliza:/home/eliza -v /experiment_folder:/experiment_folder 0a205763ff4d /bin/bash
mkdir -p /experiment_folder/text_classification/trec/original/splits

docker inspect -f '{{.Id}}' 1e8a335025f3
docker cp /home/nlp02/Desktop/trec_original_train.csv 1e8a335025f38eecee42fa3ff4ffa7ed8d1015ad1eceb114778ae0161397b4ed:/experiment_folder/text_classification/trec/original/splits/trec_original_train.csv
docker cp /home/nlp02/Desktop/trec_original_test.csv 1e8a335025f38eecee42fa3ff4ffa7ed8d1015ad1eceb114778ae0161397b4ed:/experiment_folder/text_classification/trec/original/splits/trec_original_test.csv
docker cp /home/nlp02/Desktop/trec_original_val.csv 1e8a335025f38eecee42fa3ff4ffa7ed8d1015ad1eceb114778ae0161397b4ed:/experiment_folder/text_classification/trec/original/splits/trec_original_val.csv

mkdir -p /experiment_folder/text_classification/BERT_test_cn/raw_data
trying again

e11195ce59d6

docker run -it -v /home/storage/eliza:/home/eliza e11195ce59d6 /bin/bash

sudo chmod -R 777 experiment_folder/


git fetch --all
git reset --hard origin/master
git pull