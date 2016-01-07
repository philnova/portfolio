$(document).ready( function() {
	console.log('Ready!');

	$PROJECTS_ELEM = $('#projects');

	var projects = {

		"projects" :
			[
			{
				"title" : 'Local Social News',
				"link" : 'http://localsocialnews.com',
				"description" : 'Aggregator for social media and news relevant to your city',
				"technologies" : 'JavaScript jQuery HTML/CSS',
				"image" : 'images/thumbnail_localsocialnews.png'
			},
			{
				"title" : "Phil's Phavorite Movies",
				"link" : 'http://google.com',
				"description" : 'A trailer site for my favorite films',
				"technologies" : 'JavaScript Python Bootstrap HTML/CSS',
				"image" : 'images/thumbnail_phavoritemovies.png'
			},
			{
				"title" : 'Resume',
				"link" : 'http://philnova.github.io',
				"description" : 'Resume site demonstrating DOM manipulation using jQuery',
				"technologies" : 'JavaScript jQuery HTML/CSS',
				"image" : 'images/thumbnail_resume.png'
			},
			{
				"title" : 'CRISpy',
				"link" : 'http://github.com/philnova/crispy',
				"description" : 'Python library for scanning the genome',
				"technologies" : 'Python',
				"image" : 'images/thumbnail_crispy.png'
			}]

	};

	projects.display = function() {
		for (idx in projects.projects) {
			//console.log(projects.projects[idx]);
			var link = projects.projects[idx].link;
			var image = projects.projects[idx].image;
			var description = projects.projects[idx].description;
			var technologies = projects.projects[idx].technologies;
			var project_element = HTMLportfolioBox.replace('%LINK%', link).replace('%IMAGE%', image).replace('%DESCRIPTION%', description);

			console.log(project_element);

			$PROJECTS_ELEM.append(project_element);
		}
	}

	projects.display();

});