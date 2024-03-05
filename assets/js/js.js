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
        consolelog("Submit");
        newpswd=document.getElementById("password").value;
        error_container=document.getElementById("passwordCriteria");
        if (!newpswd.match(passwordRegex)){
            console.log(error_container);
            error_container.style.display='block';
            event.preventDefault()
        }
        else{
            console.log("passsed");
            error_container.style.display='block';
        }
      
    });


function fun(){
    console.log("1234567890")
}