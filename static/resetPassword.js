/*
Done by: Maram Lutfi Alfaraj - ID: 2190001583
------
*/


//display or hide password rules
var rulsButton = document.querySelector(".rp-button-info");
var passDiveContainer = document.querySelector(".passwordrules-box");

rulsButton.addEventListener('mouseover', showPassRules);
rulsButton.addEventListener('mouseout', hidePassRules);

function showPassRules(){ //display when mose over
        passDiveContainer.style.display = 'block';
}
function hidePassRules(){ //hide when mouse out
    passDiveContainer.style.display= 'none';
}