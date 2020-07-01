import gitlab

gl = gitlab.Gitlab.from_config('gitlab', ['./python-gitlab.cfg'])

print(gl.version())

# List projects, where the user is a member
projects = gl.projects.list(membership=True)
print(projects)

