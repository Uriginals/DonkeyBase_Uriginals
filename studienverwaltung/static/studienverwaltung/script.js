$(document).ready(function() {
	    // Slide
	    $("#menu1 > li > a.expanded + ul").slideToggle("medium");
	    $("#menu1 > li > a").click(function() {
	        $(this).toggleClass("expanded").toggleClass("collapsed").parent().find('> ul').slideToggle("medium");})
            jQuery.
	 
	    // Accordion
	    $("#menu5 > li > a.expanded + ul").slideToggle("medium");
	    $("#menu5 > li > a").click(function() {
			$("#menu5 > li > a.expanded").not(this).toggleClass("expanded").toggleClass("collapsed").parent().find('> ul').					slideToggle("medium");
	        $(this).toggleClass("expanded").toggleClass("collapsed").parent().find('> ul').slideToggle("medium");
	    });
	});