import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Phil's Phabulous Portfolio</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <script>
    $(document).ready(function(){
        $('[data-toggle="popover"]').popover(); //initializes popover windows
        });
    </script>

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #project .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #project-video {
            width: 100%;
            height: 100%;
        }
        .project-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .project-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            max-height: 200px;
            position: relative;
        }
        .modal-body {
            height: 100%;
            max-height: 200px;
        }

        .modal-footer {
            text-align: center;
        }

        .scale-media iframe {
            border: none;
            height: 100%;
            max-height: 200px;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        footer {background-color: grey}

        .nav {
            border:1px solid #ccc;
            border-width:1px 0;
            list-style:none;
            margin:0;
            padding:0;
            text-align:center;
        }
        .nav li{
            display:inline;
        }
        .nav a{
            display:inline-block;
            padding:10px;
            text-color: white;
        }

        #modal-footer {
            text-align: center;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.project-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Project Modal -->
    
    {popout_tiles}
      
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Projects</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {project_tiles}
    </div>
      

<div class="footer">
    <ul class="nav">
      <li><a href="http://github.com/philnova">github</a></li>
      <li><a href="http://twitter.com/phil_nova">twitter</a></li>
      <li><a href="http://phil-nova.com/blog">blog</a></li>
      <li><a href="">linkedin</a>https://www.linkedin.com/in/phil-nova-73a76849</li>
      <li><a href="http://philnova.github.io">cv</a></li>
    </ul>
</div>

    </div>
  </div>


  

  </body>
</html>
'''


# A single movie entry html template
project_tile_content = '''
<div class="col-md-6 col-lg-4 project-tile text-center" data-toggle="modal" data-target="#{internal_link}">
    
    <img src="{image_url}" width="200" height="200">
    <h2>{project_title}</h2>
    
</div>

'''

popout_tile_content = '''
<div class="modal fade" role="dialog" id="{internal_link}">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
    </a>
    <h1>{project_title}</h1>
</div>
    <div class="modal-body">
        
    <p><strong>Description:</strong> {description} </p>
    <p><strong>Technologies Used:</strong> {technologies} </p>

    </div>
    <div class="modal-footer">
        <a href="{github}" class="btn btn-info" role="button">Source Code</a>
        <a href="{link}" class="btn btn-info" role="button">Website</a>
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
    </div>
</div>
</div>
    </div>
'''


def create_project_tiles_content(projects):
    # The HTML content for this section of the page
    content = ''
    for project in projects:

        # Append the tile for the project with its content filled in
        content += project_tile_content.format(
            project_title=project.title,
            image_url=project.image_url,
            technologies=project.technologies,
            description = project.description,
            link = project.link,
            internal_link = project.nickname #used as an internal link within the page
        )
    return content

def create_project_popout_content(projects):
    content = ''
    for project in projects:
        content += popout_tile_content.format(
            project_title = project.title,
            internal_link = project.nickname,
            description = project.description,
            technologies = project.technologies,
            link = project.link,
            github = project.github
            )
    return content


def open_projects_page(projects):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    final_content = main_page_content.format(
        popout_tiles=create_project_popout_content(projects),
        project_tiles=create_project_tiles_content(projects)
        )


    

    # Output the file
    output_file.write(main_page_head + final_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)