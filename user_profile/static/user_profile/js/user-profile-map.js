// Intiate Map
function initMap() {
    axios.get('http://127.0.0.1:8000/api/current-user/')
        .then(function (response) {
            // handle success
            const lat = response.data.profile.latitude
            const lng = response.data.profile.longitude

            const options = {
                zoom:15,
                center: { lat: lat , lng: lng },
            }

            const map = new google.maps.Map(document.getElementById("map"), options);

            const marker = new google.maps.Marker({
                position:options.center,
                map:map,
            });

            const contentString = 
                `<div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4">
                                <img src="${response.data.profile.profile_picture}" style="width:100%">
                            </div>
                            <div class="col-8">
                                <h6 class="card-title">${response.data.first_name} ${response.data.last_name}</h6>

                                <div class="text-muted">
                                    <strong><small>${response.data.profile.profession}</small></strong>
                                </div>

                                <div class="my-1">
                                    <i class="fas fa-mobile-alt"></i> 
                                    <small>${response.data.profile.phone_number}</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`;

            const infowindow = new google.maps.InfoWindow({
                content: contentString,
                maxWidth:290
            });

            marker.addListener("click", () => {
                infowindow.open({
                    anchor: marker,
                    map,
                    shouldFocus: false,
                });
            });
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });

    // Place auto auto complete callback
    initAutocomplete()
}