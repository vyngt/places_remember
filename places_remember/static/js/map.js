let marker;

function place_marker(location, map) {
  if (marker) {
    marker.setPosition(location);
  } else {
    marker = new google.maps.Marker({
      position: location,
      map: map,
    });
  }
}

function set_location_input(location) {
  const lat = document.getElementById("in-lat");
  const lng = document.getElementById("in-lng");
  document.getElementById("in-lat").setAttribute("value", lat);
  if (lat && lng) {
    lat.setAttribute("value", location["lat"]);
    lng.setAttribute("value", location["lng"]);
  }
}

function initMap() {
  // The location of coords
  const coords = { lat: 11.746435259765041, lng: 106.70930183640134 };
  // The map, centered at coords
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: coords,
  });

  set_location_input(coords);
  place_marker(coords, map);

  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    const location = mapsMouseEvent.latLng.toJSON();
    set_location_input(location);
    place_marker(location, map);
  });
}

window.initMap = initMap;
