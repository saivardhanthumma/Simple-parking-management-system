document.addEventListener('DOMContentLoaded', (event) => {
    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        let count = 0;

        const updateCount = () => {
            const increment = target / 200; // Adjust the speed of counting here
            count += increment;
            if(count < target) {
                counter.innerText = Math.ceil(count);
                setTimeout(updateCount, 1);
            } else {
                counter.innerText = target;
            }
        };

        updateCount();
    });
});

new DataTable('#example');

const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
const form = document.getElementById('FormId');

form.addEventListener('submit', function(event) {
    console.log("Submit");
    const newpswd = document.getElementById("NewPassword").value;
    const cnfpswd = document.getElementById("confirmPassword").value;
    const error_container = document.getElementById("passwordCriteria");
    const errormessage = document.getElementById("errormessage");
    
    if (!passwordRegex.test(newpswd)) {
        console.log(error_container);
        error_container.style.display = 'block';
        event.preventDefault(); // Prevent form submission
    }
    else if (newpswd !==cnfpswd){
        error_container.style.display = 'none';
        console.log("Passed12");
        errormessage.textContent="New password and confirm password do not match."
        event.preventDefault(); // Prevent form submission

    } else {
        console.log("Passed");
        error_container.style.display = 'none'; 
        errormessage.textContent=""// Hide error message if password criteria are met
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select all alerts
    const alerts = document.querySelectorAll('.auto-dismiss');
    // Set timeout for each alert
    alerts.forEach(function(alert) {
      setTimeout(function() {
        // Use Bootstrap's method to close the alert
        new bootstrap.Alert(alert).close();
      }, 5000); // Adjust time as needed in milliseconds
    });
  });

  function updateParkingInfo() {
    var vehicleTypeSelect = document.getElementById('VehicleTypeEntry');
    var selectedOption = vehicleTypeSelect.options[vehicleTypeSelect.selectedIndex];

    // Retrieve parking area and charge from the selected vehicle type's data attributes
    var parkingArea = selectedOption.getAttribute('data-parking-area');
    var parkingCharge = selectedOption.getAttribute('data-parking-charge');

    // Update the Parking Area Number and Parking Charge input fields
    document.getElementById('ParkingAreaNumberEntry').value = parkingArea;
    document.getElementById('ParkingChargeEntry').value = "$" + parkingCharge;
}
