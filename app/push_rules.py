# Gitlab-UI: Settings -> Repository -> Push Rules
# https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html#project-push-rules
# https://docs.gitlab.com/ce/api/projects.html#push-rules-starter
def configure_project_push_rules(project):
  print("Configuring push rules:", project.name)

  push_rules = project.pushrules.get()

  # Deny deleting a tag
  # boolean
  push_rules.deny_delete_tag = True

  # Restrict commits by author (email) to existing GitLab users
  # boolean
  push_rules.member_check = True

  # GitLab will reject any files that are likely to contain secrets
  # boolean
  push_rules.prevent_secrets = True

  # All commit messages must match this, e.g. Fixed \d+\..*
  # string
  push_rules.commit_message_regex = "^(NO-TICKET|ECOINFRA-\\d+|FAIT-\\d+)"

  # No commit message is allowed to match this, e.g. ssh\:\/\/
  # string
  push_rules.commit_message_negative_regex = ""

  # All branch names must match this, e.g. (feature|hotfix)\/*
  # string
  push_rules.branch_name_regex = "^(feature|hotfix)\\/(NO-TICKET|ECOINFRA-\\d+|FAIT-\\d+)"

  # All commit author emails must match this, e.g. @my-company.com$
  # string
  push_rules.author_email_regex = ""

  # All committed filenames must not match this, e.g. (jar|exe)$
  # string
  push_rules.file_name_regex = ""

  # Maximum file size (MB)
  # integer
  push_rules.max_file_size = 0

  push_rules.save()

  print("Saved push rules:", project.name)

  return
