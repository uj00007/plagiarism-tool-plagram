/**
 * Created by SHUBHAM on 9/2/2016.
 */
 function hidenav() {

      var x=document.getElementById("main").style.top;
    if (x==0) {
    document.getElementById("main-menu").style.backgroundColor = 'transparent';
        document.getElementById("main-menu").style.boxShadow = '0px 0px 0px 0px transparent';

              }

}

 function shownav() {
    document.getElementById("main-menu").style.backgroundColor = '#3F8ABF';
        document.getElementById("main-menu").style.boxShadow = ' 1px 2px 9px 2px #424242';


}









$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});


function change_l0(){
    document.getElementById("l0").style.backgroundColor='#397CAC';
    document.getElementById("l1").style.backgroundColor='#3F8ABF';
    document.getElementById("l2").style.backgroundColor='#3F8ABF';
    document.getElementById("l3").style.backgroundColor='#3F8ABF';

}

function change_l1(){
    document.getElementById("l1").style.backgroundColor='#397CAC';
     document.getElementById("l0").style.backgroundColor='#3F8ABF';
    document.getElementById("l2").style.backgroundColor='#3F8ABF';
    document.getElementById("l3").style.backgroundColor='#3F8ABF';
    document.getElementById("l1").style.scale=1.15;


}

function change_l2(){
    document.getElementById("l2").style.backgroundColor='#397CAC';
     document.getElementById("l1").style.backgroundColor='#3F8ABF';
    document.getElementById("l0").style.backgroundColor='#3F8ABF';
    document.getElementById("l3").style.backgroundColor='#3F8ABF';

}

function change_l3(){
    document.getElementById("l3").style.backgroundColor='#397CAC';
     document.getElementById("l1").style.backgroundColor='#3F8ABF';
    document.getElementById("l2").style.backgroundColor='#3F8ABF';
    document.getElementById("l0").style.backgroundColor='#3F8ABF';
}







