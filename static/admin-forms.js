var Author_name;
var Blog_Title;
var Blog_Description;
var Blog_Content;
var Blog_Dates;
var Blog_Photo;

var helpText1;
var helpText2;
var helpText3;
var helpText4;
var helpText5;
var helpText6;
var helpText7;



function init() {
    var form = document.getElementById("form");
    Author_name = document.getElementById("Author_name");
    Blog_Title = document.getElementById("Blog_Title");
    Blog_Description = document.getElementById("Blog_Description");
    Blog_Content = document.getElementById("Blog_Content");
    Blog_Dates = document.getElementById("Blog_Dates");
    Blog_Photo = document.getElementById['Blog_Photo'];
   

    helpText1 = document.getElementById("helpText1");
    helpText2 = document.getElementById("helpText2");
    helpText3 = document.getElementById("helpText3");
    helpText4 = document.getElementById("helpText4");
    helpText5 = document.getElementById("helpText5");
    helpText6 = document.getElementById("helpText6");
    helpText7 = document.getElementById("helpText7");



    form.onsubmit = check;
    form.onreset = func2;
} // end function init

function check() {
    var pass = "";

    if (Author_name.value == "") {
        pass = "*The Author Name Cannot Be Blank. Please Fill This Field.<br/>";
        helpText1.innerHTML = pass;
        return false;
    }

    if (Blog_Title.value == "") {
        pass = "*The Title Cannot Be Blank. Please Fill This Field. <br/>";
        helpText2.innerHTML = pass;
        return false;
    }

    if (Blog_Description.value == "") {
        pass = "*Blog Description Cannot Be Blank. Please Fill This Field.<br/>";
        helpText3.innerHTML = pass;
        return false;
    }

    if (Blog_Content.value == "") {
        pass = "*Blog Content Cannot Be Blank. Please Fill This Field.<br/>";
        helpText4.innerHTML = pass;
        return false;
    }

    if (Blog_Dates.value == "") {
        pass = "*Blog Posted Date Cannot Be Blank. Please Fill This Field.<br/>";
        helpText10.innerHTML = pass;
        return false;
    }

    if (Blog_Photo.value == "") {
        pass = "*Blog Image Cannot Be Empty.<br/>";
        helpText5.innerHTML = pass;
        return false;
    }
 
}

function func2() {
    return confirm("Are you sure you want to clear?");
}

window.addEventListener("load", init, false);

