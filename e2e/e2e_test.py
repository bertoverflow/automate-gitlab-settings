import os
import sys

sys.path.append(os.path.abspath('../app/'))

import gitlab
import main

# token authentication from config file
gl = gitlab.Gitlab.from_config(config_files=["/tmp/python-gitlab.cfg"])
gl.auth()
assert isinstance(gl.user, gitlab.v4.objects.CurrentUser)

# create some test-projects
gl.projects.create({'name': 'testA'})
gl.projects.create({'name': 'testB'})

# execute our main-project
main.configure_projects()
