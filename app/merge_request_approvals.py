# Gitlab-UI: Settings -> General -> Merge Request Approvals
# https://python-gitlab.readthedocs.io/en/stable/gl_objects/mr_approvals.html
# https://docs.gitlab.com/ee/api/merge_request_approvals.html#project-level-mr-approvals
def configure_project_merge_request_approval_settings(project):
  print("Configuring merge request approval settings:", project.name)

  # Please note: The number of needed approvers is a general project setting

  # these are the project-level merge approval settings
  merge_request_approval_settings = project.approvals.get()

  # Reset approvals on a new push
  # boolean
  merge_request_approval_settings.reset_approvals_on_push = True

  # Allow/Disallow overriding approvers per MR
  # boolean
  merge_request_approval_settings.disable_overriding_approvers_per_merge_request = True

  # Allow/Disallow authors from self approving merge requests; true means authors can self approve
  # boolean
  # Note: True is a much better setting for handling Pair-Programming
  merge_request_approval_settings.merge_requests_author_approval = True

  # Allow/Disallow committers from self approving merge requests
  # boolean
  # Note: False is a much better setting for handling Pair-Programming
  merge_request_approval_settings.merge_requests_disable_committers_approval = False

  merge_request_approval_settings.save()

  print("Saved merge request approval settings:", project.name)

  return
