const form = document.getElementById('form');
const fname = document.getElementById('fname');
const lname = document.getElementById('lname');
const username = document.getElementById('username');
const dob = document.getElementById('dob');
const nat = document.getElementById('nat');
const pass1 = document.getElementById('pass1');
const pass2 = document.getElementById('pass2');
const email = document.getElementById('email');
var valid=false

form.addEventListener('submit', e => {
	result= checkInputs();
	if(result !=true){
		e.preventDefault();}
});

function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
    const fnameval = fname.value.trim();
    const lnameval = lname.value.trim();
    const dobval = dob.value;
    const natval = nat.value;
    const pass1val = pass1.value.trim();
    const pass2val = pass2.value.trim();
    const emailval = email.value.trim();

    var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*\_])(?=.{8,})");
    var usernameRegex = /^[a-z]{2,}\d*$/i;

	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
        valid=false;
	} else if(!usernameRegex.test(usernameValue)){
        setErrorFor(username, 'Username is at least 2 characters long and cannot start with a number ');
        valid=false;
    } else {
		setSuccessFor(username);
        valid=true;
	}

    if(fnameval === ''){
        setErrorFor(fname, 'First name cannot be blank');
        valid=false;
    } else{
        setSuccessFor(fname);
        valid=true;
    }

    if(lnameval === ''){
        setErrorFor(lname, 'Last name cannot be blank');
        valid=false;
    } else{
        setSuccessFor(lname);
        valid=true;
    }

    if(dobval === ''){
        setErrorFor(dob, 'Please select a date');
        valid=false;
    } else{
        setSuccessFor(dob);
        valid=true;
    }

    if(natval === ''){
        setErrorFor(nat, 'Please select a nationality');
        valid=false;
    } else{
        setSuccessFor(nat);
        valid=true;
    }

    if(pass1val === ''){
        setErrorFor(pass1, 'Password cannot be blank');
        valid=false;
    } else if(!strongRegex.test(pass1val)){
        setErrorFor(pass1, 'Please enter a valid password, click on the icon for instructions.');
        valid=false;
    }
    else{
        setSuccessFor(pass1);
        valid=true;
    }

    if(pass2val === ''){
        setErrorFor(pass2, 'Confirm password cannot be blank');
        valid=false;
    } else if(pass2val !== pass1val){
        setErrorFor(pass2, 'Password and Confirm password fields must match');
        valid=false;
    } else{
        setSuccessFor(pass2);
        valid=true;
    }

    if(emailval === ''){
        setErrorFor(email, 'Email address cannot be blank');
        valid=false;
    }else if (!isEmail(emailval)) {
		setErrorFor(email, 'Please enter a valid email address');
        valid=false;
    } else{
        setSuccessFor(email);
        valid=true;
    }

    return valid;
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
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function myPass1() {
    var x = document.getElementById("pass1");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }
  function myPass2() {
    var x = document.getElementById("pass2");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }
