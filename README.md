# Automate Gitlab Settings

## Setup

* Install docker
* Build the image
```
docker build -t automate-gitlab-settings .
```

## Usage

```
docker run -it --rm automate-gitlab-settings
```

## Development

Start container
```
docker run -it --rm -v $PWD/app:/usr/src/app automate-gitlab-settings sh
```

You can then run the scripts inside the container, for example:
```
python main.py
```

However, since the app-directory is mounted, you can develop/edit the files on the host-machine.


### Use the CLI to test things

```
docker run -it --rm -v $PWD/app/python-gitlab.cfg:/python-gitlab.cfg -e GITLAB_CFG=/python-gitlab.cfg registry.gitlab.com/python-gitlab/python-gitlab:latest <command>
```

For example, to print the name of the logged in user (depending on the token)
```
docker run -it --rm -v $PWD/app/python-gitlab.cfg:/python-gitlab.cfg -e GITLAB_CFG=/python-gitlab.cfg registry.gitlab.com/python-gitlab/python-gitlab:latest current-user get
```

