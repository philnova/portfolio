import project
import portfolio
import random


def parse_project_file(filename):
	project_array = []
	with open(filename) as fo:
		for idx, line in enumerate(fo):
			if idx: #ignore first line
				line_array = line.split("\t")
				title, description, link, github, image_url, technologies, nickname = line_array[0], line_array[1], line_array[2], line_array[3], line_array[4], line_array[5], line_array[6]
				current_project = project.Project(title, description, link, github, image_url, technologies, nickname)
				project_array.append(current_project)
	random.shuffle(project_array)
	return project_array

portfolio.open_projects_page(parse_project_file("projects_db.txt"))