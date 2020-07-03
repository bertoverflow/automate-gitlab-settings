import gitlab

# Gitlab-UI: Settings -> Repository -> Protected Branches
# https://python-gitlab.readthedocs.io/en/stable/gl_objects/protected_branches.html
# https://docs.gitlab.com/ee/api/protected_branches.html
def configure_project_protected_branches(project):
  print("Configuring protected branches:", project.name)

  # Note: It is not possible to edit the protection settings, so we will delete
  # them and create them again

  # delete current master settings
  try:
    master_settings = project.protectedbranches.get('master')
    master_settings.delete()
  except gitlab.exceptions.GitlabGetError:
    print('No protection rules for master defined')

  # create new master settings
  # Possible access levels are:
  #  0  => No access (gitlab.NO_ACCESS -> currently not working, just use zero)
  # 30 => Developer access (gitlab.DEVELOPER_ACCESS)
  # 40 => Maintainer access (gitlab.MAINTAINER_ACCESS)
  # 60 => Admin access
  # Note that Maintainer access INCLUDES Developer access
  master_settings_new = project.protectedbranches.create({
    'name': 'master',
    'merge_access_level': gitlab.DEVELOPER_ACCESS,
    'push_access_level': 0
  })

  print("Saved protected branches:", project.name)

  return
