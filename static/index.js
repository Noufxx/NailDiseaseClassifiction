
//JS for the drag and drop option
const draggerArea = document.getElementById('dragger');
const dragger = document.getElementById('dragger');
const inputField = document.getElementById('fileInputField');
const dragText = document.getElementById('drag-text');
const fileName = document.getElementById('fileName');
const browseFile = document.getElementById('browseFile');
const subbtn = document.getElementById('sub');

inputField.addEventListener('change', function(e) {
    file = this.files[0];
    fileHandler(file);
});

const fileHandler = (file) => {
    const validExt = ["image/jpeg", "image/jpg", "image/png"]
    if (validExt.includes(file.type)) {
        const fileReader = new FileReader();
        fileReader.onload = () => {
            subbtn.style.marginLeft="550px";
            dragger.style.background="white";
            dragger.style.border="none";
            const fileURL = fileReader.result;
            let imgTag = `<img src=${fileURL} style="margin-left:450px;" alt=""/>`
            draggerArea.innerHTML = imgTag;
            let paragraph = `<div class="fileName"><p>${file.name.split('.')[0]}</p><i class="fa-solid fa-trash-can" onclick={deleteHandler()}></i></div>`
            fileName.innerHTML = paragraph;
        }
        fileReader.readAsDataURL(file);
        draggerArea.classList.add('active')
    } else {
        draggerArea.classList.remove('active');
        dragText.textContent = "Drag and Drop File"
    }
};
            
// To show result box and hide the upload box

var button = document.getElementById('sub');
var xx = document.getElementById("fileInputField");
var div1 = document.getElementById('uploadbox');
var div2 = document.getElementById('resbox');
var div3 = document.getElementById('error');


button.addEventListener("click", submit)
function submit() {
   if (xx.files.length == 0)
   {
       //div1.style.display = 'block'; 
       //div2.style.display = 'none';
       //div3.style.display = 'block';
       
       Swal.fire({
               
           //title: 'Please choose an image to uplaod!',
           text: 'Please Choose an Image to Uplaod!',
           icon: 'error',
           confirmButtonText: 'Return to Page',
           confirmButtonColor: '#D10000'
           
         })
       return false;

   }
  else{
   //div1.style.display = 'none';
   //div2.style.display = 'block';  
   div3.style.display = 'none';

   }
}



   