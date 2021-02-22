$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function openNav() {
document.getElementById("mySidenav").style.width = "250px";
document.getElementById("main").style.marginLeft = "250px";
$("body > *:not(#mySidenav)").css('filter', 'blur(3px) grayscale(0.8)')
}

function closeNav() {
document.getElementById("mySidenav").style.width = "0";
document.getElementById("main").style.marginLeft = "0";
document.body.style.backgroundColor = "white";
$("body > *:not(#mySidenav)").css('filter', '')
}