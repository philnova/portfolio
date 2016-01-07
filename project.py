import webbrowser

class Project(object):

	def __init__(self, project_title, project_description, project_link, project_github, project_image_url, project_technologies, project_nickname):
		self.title = project_title
		self.description = project_description
		self.link = project_link
		self.image_url = project_image_url
		self.technologies = project_technologies
		self.nickname = project_nickname
		self.github = project_github
