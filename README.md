# portfolio
A responsive site to display my projects, built using Python and Bootstrap
Hosted at philnova.io

## Components
The site itself is fully contained within the file home.html. All JavaScript and CSS needed to power the site is inline; additional styles come from the Bootstrap framework (https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js)
The only additional content is the project thumbnail images, contained inside the images folder.

However, the site is built procedurally from a plain text file, projects_db.txt. The script project_fileparser.py reads in the projects, and uses the Project class in project.py to construct a Project object for each entry in the text file. Finally, project_fileparser.py calls to the script portfolio.py, which formats the Project objects into HTML. From each Project object a thumbnail is constructed on the main page, along with a modal window which pops over the page when the thumbnail is clicked.

### projects_db

In order to build the site, entries can be placed into projects_db.txt with the following columns:
TITLE	DESCRIPTION	LINK	GITHUB	IMAGE_URL	TECHNOLOGIES	NICKNAME
TITLE is a string, which will appear below the thumbnail image and at the top of the modal window
DESCRIPTION is a string describing the project which will appear in the modal window
LINK is a link to the project site
GITHUB is a link to the github repository for the project
IMAGE_URL is a link to the thumbnail image
TECHNOLOGIES is a string listing the technologies used to build the project, which will appear inside the modal window
NICKNAME is a string with a short name for the project, which is used as an internal link connecting the thumbnail to the modal window
The text file should be tab-delimited.

### Building the site

Once this file is complete, the site can be built by running project_fileparser.py from the command line. project_fileparser should be in the same directory as portfolio.py, project.py, and projects_db.txt. The HTML form, home.html, will be constructed and automatically opened in the browser.
