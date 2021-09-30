let autocomplete ;
function initAutocomplete() {
    // Create the autocomplete object, restricting the search to geographical
    // location types.
    autocomplete = new google.maps.places.Autocomplete(
        document.querySelector("#id_address"),
        {
            componentRestrictions: { country: ["za"]},
            fields: ["address_components", "geometry"],
            types: ["address"],

        }
    );

    // When the user selects an address from the dropdown, populate the address
    // fields in the form.
    // const address = document.querySelector("#id_address").value 
    // autocomplete.addListener('place_changed', fillInAddress());
}

// function fillInAddress(address) {

//     geocoder = new google.maps.Geocoder();
//     geocoder.geocode({'address' : address}, function(results, status){
//         if(status == google.maps.GeocoderStatus.OK){
//             var lat = results[0].geometry.location.lat();
//             var lng = results[0].geometry.location.lng();

//             document.querySelector("#id_latitude").value = lat;
//             document.querySelector("#id_longitude").value = lng;
//         }
//     });

//     // const place = autocomplete.getPlace();
//     // console.log(place.geometry.location)
//     // document.querySelector("#id_latitude").value = place.geometry.location;

//     // for (const component of place.geometry) {
//     //     const componentType = component.types[0];

//     //     switch (componentType) {
//     //         case "locality":
//     //             document.querySelector("#id_city").value = component.long_name;
//     //             break;

//     //         case "administrative_area_level_1":
//     //             document.querySelector("#id_province").value = component.long_name;
//     //             break;

//     //         case "postal_code":
//     //             document.querySelector("#id_postal_code").value = component.long_name;
//     //             break;

//     //         case "country":
//     //             document.querySelector("#id_country").value = component.long_name;
//     //             break;
//     //     }
//     // }
// }