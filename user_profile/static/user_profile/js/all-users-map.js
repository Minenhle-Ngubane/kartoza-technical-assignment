// Intiate Map
function initMap() {

    axios.get('http://127.0.0.1:8000/api/users/')
        .then(function (response) {
            // handle success

            //  map options
            const options = {
                zoom:15,
                center: { lat: response.data[0].profile.latitude, lng: response.data[0].profile.longitude },
            }
            
            //  Create a new map
            const map = new google.maps.Map(document.getElementById("map"), options);

            //  Create a new viewpoint bound
            const bounds = new google.maps.LatLngBounds ();

            // Add marker for each user
            for (let i = 0; i < response.data.length; i++) { 
                // Increase the bounds to take this point
                bounds.extend({ lat: response.data[i].profile.latitude, lng: response.data[i].profile.longitude });
               
                // Add marker callback
                addMarker({
                    coords:{ lat: response.data[i].profile.latitude, lng: response.data[i].profile.longitude },
                    content: 
                        `<div class="card">
                            <div class="card-body">
                                <div class="row">
                                    <div class="col-4">
                                        <img src="${response.data[i].profile.profile_picture}" style="width:100%">
                                    </div>
                                    <div class="col-8">
                                        <h6 class="card-title">${response.data[i].first_name} ${response.data[i].last_name}</h6>

                                        <div class="text-muted">
                                            <strong><small>${response.data[i].profile.profession}</small></strong>
                                        </div>

                                        <div class="my-1">
                                            <i class="fas fa-mobile-alt"></i> 
                                            <small>${response.data[i].profile.phone_number}</small>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`          
                });

                
            };

            //  Fit these bounds to the map
            map.fitBounds(bounds);
        

            //  Add marker with infowindow function
            function addMarker(props) {
                const marker = new google.maps.Marker({
                    position:props.coords,
                    map:map,
                })

                const infowindow = new google.maps.InfoWindow({
                    content: props.content,
                    maxWidth:290
                });

                marker.addListener("click", () => {
                    infowindow.open({
                        anchor: marker,
                        map,
                        shouldFocus: false,
                    });
                });
            }
        
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}

