import os
import gitlab
import general_settings
import merge_request_approvals
import protected_branches
import push_rules

def configure_projects():

  # check if we should do a dry run
  DRY_RUN_DEFAULT_VALUE = False
  dry_run = os.getenv("DRY_RUN")
  if dry_run == '1':
    dry_run = True
  elif dry_run == '0':
    dry_run = False
  else:
    dry_run = DRY_RUN_DEFAULT_VALUE

  # check if we were given a search filter for the projects via an Environment variable
  PROJECT_SEARCH_FILTER_DEFAULT_VALUE = ''
  project_search_filer = os.getenv('PROJECT_SEARCH_FILTER', PROJECT_SEARCH_FILTER_DEFAULT_VALUE)
  print("Using search filter: ", project_search_filer)

  gitlap_api_client = gitlab.Gitlab.from_config('gitlab', ['./python-gitlab.cfg'])

  # Gitlab version
  print("Gitlab Version: ", gitlap_api_client.version())

  # Current (logged-in) user
  gitlap_api_client.auth()
  print("Authenticated User: ", gitlap_api_client.user.name)

  # Get projects
  # https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html
  # The project 'name' is the visible name of the project in gitlab
  # The project 'path' is the internal representation (without spaces, the one that is used in the URLs etc.)
  # with the search parameter you can easily restrict the project-list to a specific namespace, group. For example:
  # - only include a specific project: search='/project-name'
  # - only include a specific group: search='group-name/'
  projects = gitlap_api_client.projects.list(
      archived=False, # no archived projects
      all=True, # no pagination, retrieve all results in one go
      owned=True, # only projects we own
      # membership=True, # only projects where we are a member
      order_by='name', # order by project name
      sort='asc',
      search=project_search_filer, # this is searched in the name AND in the path
      search_namespaces=True # include the namespace in the search
  )

  total_projects = len(projects)
  print("Total projects found: ", total_projects)

  for index, project in enumerate(projects, start=1):
    print()
    print("------------------------------------------------------")
    print(index, '/', total_projects, ":", project.name, "(", project.path_with_namespace, ")")
    print("------------------------------------------------------")

    if not dry_run:
      general_settings.configure_project_general_settings(project)
      merge_request_approvals.configure_project_merge_request_approval_settings(project)
      protected_branches.configure_project_protected_branches(project)
      push_rules.configure_project_push_rules(project)

if __name__ == '__main__':

  configure_projects()
