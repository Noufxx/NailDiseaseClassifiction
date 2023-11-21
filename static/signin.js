const form = document.getElementById('form');
const username = document.getElementById('username');
const pass = document.getElementById('pass');
var valid =true

form.addEventListener('submit', e => {
	
	result= checkInputs();
	if(result !=true){
		e.preventDefault();}
});

function checkInputs() {
	// trim to remove the whitespaces
	const usernameval = username.value.trim();
    const passval = pass.value.trim();

	if(usernameval === '') {
		setErrorFor(username, 'Username cannot be blank');
		valid=false;
	} else {
		setSuccessFor(username);
		valid=true;
	}


    if(passval === ''){
        setErrorFor(pass, 'Password cannot be blank');
		valid=false;
    } else{
        setSuccessFor(pass);
		valid=true;
    }

return valid
}
function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
function myPass1() {
    var x = document.getElementById("pass");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }