

$(document).ready(function() {
  $(".nav-link").click(function () {
      $(".nav-link").removeClass("active");
      // $(".tab").addClass("active"); // instead of this do the below 
      $(this).addClass("active");   
  });
  $('.dropdown').click(function(){
  $('.dropdown-menu').toggleClass('show');
});
  });

  