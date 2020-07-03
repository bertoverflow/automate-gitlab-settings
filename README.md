# Automate Gitlab Settings

This project is used to configure Gitlab-Settings on a project level.
Since these settings have to be configured individually for every project,
we automate this process using the Gitlab-API.
We use https://github.com/python-gitlab/python-gitlab as an api-client.

## Setup

* Install docker
* Get a valid API_TOKEN and use it in the python-gitlab.cfg
  * https://docs.gitlab.com/ee/api/#authentication
  * https://python-gitlab.readthedocs.io/en/stable/api-usage.html#getting-started-with-the-api
* Build the image
```
docker build --build-arg GITLAB_TOKEN=<INSERT YOUT API TOKEN HERE> -t automate-gitlab-settings .
```

## Usage

```
docker run -it --rm automate-gitlab-settings
```

This will configure some project-level settings for all your owned projects at gitlab.com.
However, the used gitlab instance can be configured in app/pyton-gitlab.cfg

The settings that will be applied are listed in the respective python modules:
* app/general_settings.py
* app/merge_request_approvals.py
* app/protected_branches.py
* app/push_rules.py

The settings that are configured there, have to be adjusted to your needs of course.
There is no configuration file currently, just adjust the values in the python files.

Currently the script retrieves all projects, that:
* you own
* are not archived

You can adjust this programmatically in app/main.py.

### Search filter

To change the search filter (the list of projects that will be configured), you can set the environment variable `PROJECT_SEARCH_FILTER`.
With the search parameter you can easily restrict the project-list to a specific namespace, group. For example:
* only include a specific project: '/project-name'
* only include a specific group: 'group-name/'
* all projects: '' (empty string = no search filter)
```
docker run -it --rm -e PROJECT_SEARCH_FILTER='/my-project' automate-gitlab-settings
```

### Dry run

To see which projects your search filter will target, you can execute a dry run:
```
docker run -it --rm -e DRY_RUN=1 automate-gitlab-settings
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
Be sure to manually replace your GITLAB_TOKEN in the config-file.


## Use the CLI to test things

```
docker run -it --rm -v $PWD/app/python-gitlab.cfg:/python-gitlab.cfg -e GITLAB_CFG=/python-gitlab.cfg registry.gitlab.com/python-gitlab/python-gitlab:latest <command>
```

For example, to print the name of the logged in user (depending on the token)
```
docker run -it --rm -v $PWD/app/python-gitlab.cfg:/python-gitlab.cfg -e GITLAB_CFG=/python-gitlab.cfg registry.gitlab.com/python-gitlab/python-gitlab:latest current-user get
```
