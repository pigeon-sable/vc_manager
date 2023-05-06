# DiscordBOT

## Description

A Discord Bot program that notifies you when you start a voice chat.

## Requirement

docker 20.10.17

Discord 0.0.273

## Usage

### 1. Clone this repository

```bash
git clone git@github.com:Kobayashi123/vc_manager.git
```

or

```bash
git clone https://github.com/Kobayashi123/vc_manager.git
```

### 2. Change the working directory

```bash
cd vc_manager
```

### 3. Rename .env_example to .env and enter your Discord Bot token

Do not enclose in single quotes("'").

```bash
cp .env_example .env
vim .env
    ACCESS_TOKEN=123456789abcdefg
```

### 4. Run the program

If you want to run it in a local environment, you can do so with the following command.

```bash
python src/vc_manager.py
```

Alternatively, a container can be used to run it. To execute, the following command is used.
The docker repository is at the following URL.
[https://hub.docker.com/repository/docker/mozsecurity/vc_manager/general](https://hub.docker.com/repository/docker/mozsecurity/vc_manager/general)

```bash
docker pull mozsecurity/vc_manager:latest
docker run -d --env-file .env mozsecurity/vc_manager:latest
```

## Licence

[Apache License, Version2.0](https://github.com/Gteruya/DiscordBOT/blob/main/LICENSE)

## Author

[Kobayashi123](https://github.com/Kobayashi123)
