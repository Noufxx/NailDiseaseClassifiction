// To show result box and hide the upload box
var button = document.getElementById('sub');
var xx = document.getElementById("fileInputField");
var div1 = document.getElementById('uploadbox');
var div2 = document.getElementById('resbox');
var div3 = document.getElementById('error');


button.addEventListener("click", submit)
function submit() {
    if (document.getElementsByName('file').value =='')
    {
    div1.style.display = 'none';
    div2.style.display = 'block';  
    div3.style.display = 'none';

    }
   else{
    div1.style.display = 'block'; 
    div2.style.display = 'none';
    div3.style.display = 'block'; 
    }
}