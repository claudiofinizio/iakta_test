
var map
function initialize() {
  var mapOptions = {
    // map options
  };
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);

var coordinates = [{latitude: 42, longitude: 42, title: "A Title"}]
var coordinates = [
	{% for row in points %}

		{latitude: {{  row.latitude }}, longitude: {{ row.longitude }}, title: "qwerty"},
	{% endfor %}
]

for(var i = 0; i < coordinates.length; i++){
  var loc = new google.maps.LatLng(coordinates[i].latitude, coordinates[i].longitude);
  var marker = new google.maps.Marker({
     position: loc,
     map: map,
     title: coordinates[i].title
  });
}