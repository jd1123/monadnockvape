var primaryColor = "#6C7A89";
var myLatlng = new google.maps.LatLng(42.935324, -72.277906);
var map,map2;

function initialize() {
	map = new google.maps.Map(document.getElementById('map-canvas'), {
		zoom: 17,
		scrollwheel: false,
		disableDefaultUI: true,
		zoomControl: true,
		zoomControlOptions: {
			style: google.maps.ZoomControlStyle.SMALL,
			position: google.maps.ControlPosition.LEFT_BOTTOM
		},
		center: myLatlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		styles: [
			{
				stylers: [
					{ hue: primaryColor },
					{ visibility: 'simplified' },
					{ gamma: 0.1 },
					{ saturation: -75 },
					{ weight: 0.5 }
				]
			},{
				elementType: "labels.text.fill",
					stylers: [
				      { color: "#ffffff" }
				    ]
			},{
				
				featureType: 'water',
				stylers: [
					{ color: primaryColor }
				]
				
				
			}, {
				featureType: 'poi.park',
				elementType: 'geometry',
				stylers: [
					{ visibility: 'simplified' },
					{ hue: '#77ff00' },
					{ gamma: 3.1 }
				]
				
				
			}
		]
	});
	
	//
	map2 = new google.maps.Map(document.getElementById('map-canvas2'), {
		zoom: 5,
		scrollwheel: false,
		disableDefaultUI: true,
		zoomControl: true,
		zoomControlOptions: {
			style: google.maps.ZoomControlStyle.SMALL,
			position: google.maps.ControlPosition.LEFT_BOTTOM
		},
		center: myLatlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
/*
		styles: [
			{
				stylers: [
					{ hue: primaryColor },
					{ visibility: 'simplified' },
					{ gamma: 0.1 },
					{ saturation: -75 },
					{ weight: 0.5 }
				]
			},{
				elementType: "labels.text.fill",
					stylers: [
				      { color: "#ffffff" }
				    ]
			},{
				
				featureType: 'water',
				stylers: [
					{ color: primaryColor }
				]
				
				
			}, {
				featureType: 'poi.park',
				elementType: 'geometry',
				stylers: [
					{ visibility: 'simplified' },
					{ hue: '#77ff00' },
					{ gamma: 3.1 }
				]
				
				
			}
		]
*/
	});
	//
	
	var markerIcon = {
		path: 'M0-165c-27.618 0-50 21.966-50 49.054C-50-88.849 0 0 0 0s50-88.849 50-115.946C50-143.034 27.605-165 0-165z',
		fillColor: '#59abe3',
		fillOpacity: 0.75,
		scale: .25,
		strokeColor: primaryColor,
		strokeWeight: 1
	};

	var contentString = '<div id="map-info-window">' + '<h1><a href="https://goo.gl/maps/xiSGp" target="_blank">Monadnock Vapor</a></h1><p>34 1/2 Washington St.</p><p>Keene, NH		03431</p><p><a href="https://goo.gl/maps/xiSGp" target="_blank">View on Google maps<a></p>' + '</div>';

	var infowindow = new google.maps.InfoWindow({//.gm-style-iw + div {display: none} to hide X (only if you disable other info windows!
		content: contentString
	});

	var marker = new google.maps.Marker({
		position: myLatlng,
		icon: markerIcon,
		map: map,
		title: 'Monadnock Vapor'
	});
  
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
	});
	infowindow.open(map,marker);//always show infowindow
  
  
}
// google.maps.event.addDomListener(window, 'resize', initialize); //jQuery function is smoother
google.maps.event.addDomListener(window, 'load', initialize);

$( window ).resize(function() { //resize / re-center map on window resize
	google.maps.event.trigger(map, 'resize')
	map.setCenter(myLatlng);
});
