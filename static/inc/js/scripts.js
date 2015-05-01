if (!Modernizr.cssanimations) {
  $("#overlay").css("display", "none");
  $(".loading").css("overflow", "auto");
}

$(document).ready(function(){
	$("#video .container").fitVids();
});

$(function(){
  $.scrollIt();
});

// waypoints
$('.wp2').waypoint(function() {
	if ($(window).width() > 768) {
		$('.wp2-1').addClass('animated fadeInDownBig');
		$('.wp2-2').addClass('animated fadeInLeft');
		$('.wp2-3').addClass('animated fadeInDown');
		$('.wp2-4').addClass('animated fadeInRight');
		$('.wp2-5').addClass('animated fadeInUpBig');
		console.log("wp2 hit and large animate");
	} else {
		$('.wp2-1').addClass('animated fadeIn');
		$('.wp2-2').addClass('animated fadeIn');
		$('.wp2-3').addClass('animated fadeIn');
		$('.wp2-4').addClass('animated fadeIn');
		$('.wp2-5').addClass('animated fadeIn');
		console.log("wp2 hit and animated");
		console.log("wp2 hit and small animate");
	}
	this.destroy();
}, {
	offset: '75%'
});

var animationend = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';

$('.scrubber').on(animationend, function(event){
		if ($(event.target).is('.scrubber')) {
			console.log('scrubbing complete');
			$('body').removeClass('loading');
			$('#overlay').addClass('animated fadeOut');
		}
});

$('#overlay').on(animationend, function(event){
	if ($(event.target).is('#overlay')) {
		console.log('overlay complete');
		this.style.display="none";
	}
});

$(".navToggle").click(function() {
	$("header").toggleClass("nav-active");
});

$(".head-nav a").click(function(){
	
	if ($("header").hasClass('nav-active')) {
		$("header").removeClass("nav-active");
	}
		
});

$("#contact-form-submit").click(function() {
	$("#contact-form-message").addClass("animated shake form-field-error");
});

$("#contact-form-message").focus(function() {
	if ($(this).hasClass("form-field-error")) {
		$(this).removeClass("form-field-error");	
	}
});

//tabs
$('.tab1-input').click(function(){
	
	if($('.tab2-content').is(':visible')) {
		$('.tab2-input').removeClass('current');
		$('.tab1-input').addClass('current');
		$('.tab1-content').css('display', 'block');
		$('.tab2-content').css('display', 'none');
		$('#map-canvas2').addClass('tab-map-hide');
		$('#map-canvas').removeClass('tab-map-hide');
	}
	
});

$('.tab2-input').click(function(){
	
	if($('.tab1-content').is(':visible')) {
		$('.tab1-input').removeClass('current');
		$('.tab2-input').addClass('current');
		$('.tab2-content').css('display', 'block');
		$('.tab1-content').css('display', 'none');
		$('#map-canvas').addClass('tab-map-hide');
		$('#map-canvas2').removeClass('tab-map-hide');
	}
	
});

$('.tab2-input').on('click', function(){
     newLocation = new google.maps.LatLng(0,0);
     marker.setPosition( newLocation );
});