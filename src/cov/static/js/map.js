var lat1;
var lng1;


         function showLocation(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            //console.log(latitude);
            //console.log(longitude);
            var latlongvalue = position.coords.latitude + ","
            + position.coords.longitude;
            getCoords(latitude, longitude);
         }

         
         function getLocation(){
            if(navigator.geolocation){
               // timeout at 60000 milliseconds (60 seconds)
               navigator.geolocation.getCurrentPosition(showLocation);
              
            } 
            else{
               alert("Sorry, browser does not support geolocation!");
            }
         }
        function getCoords(lat, lng)
      {
           lat1 = lat;
           lng1 = lng;   
           console.log(lat1);
           console.log(lng1);  
      }


      function mapInit(){    
    var locations = [
      ['Bondi Beach', lat1, lng1, 4],
      ['Coogee Beach', -33.923036, 151.259052, 5],
      ['Cronulla Beach', -34.028249, 151.157507, 3],
      ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
      ['Maroubra Beach', -33.950198, 151.259302, 1]
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: new google.maps.LatLng(19.0760, 72.8777),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
  }
getLocation();
setTimeout(function(){ mapInit()}, 3000);



         //console.log(lat1);
         //console.log(lng1);  