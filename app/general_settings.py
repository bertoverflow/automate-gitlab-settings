# Gitlab-UI: Settings -> General
# https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html
# https://docs.gitlab.com/ce/api/projects.html#edit-project
def configure_project_general_settings(project):
  print("Configuring general project settings:", project.name)

  # Set whether merge requests can only be merged with successful jobs
  # boolean
  project.only_allow_merge_if_pipeline_succeeds = True

  # Set whether or not merge requests can be merged with skipped jobs
  # boolean
  # Note: This is generally the recommended setting, but has to be changed for certain projects probably
  project.allow_merge_on_skipped_pipeline = False

  # Set whether merge requests can only be merged when all the discussions are resolved
  # boolean
  project.only_allow_merge_if_all_discussions_are_resolved = True

  # There are currently three options for merge_method to choose from:
  # merge: A merge commit is created for every merge, and merging is allowed as long as there are no conflicts.
  # rebase_merge: A merge commit is created for every merge, but merging is only allowed if fast-forward merge is possible. This way you could make sure that if this merge request would build, after merging to target branch it would also build.
  # ff: No merge commits are created and all merges are fast-forwarded, which means that merging is only allowed if the branch could be fast-forwarded
  project.merge_method = 'ff'

  # Enable Delete source branch option by default for all new merge requests
  # boolean
  project.remove_source_branch_after_merge = True

  # How many approvers should approve merge request by default
  # integer
  project.approvals_before_merge = 2

  project.save()

  print("Saved project:", project.name)

  return
