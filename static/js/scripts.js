// Small UI enhancements for the site
(function(){
  'use strict'

  // Auto-dismiss bootstrap alerts after 5s
  document.addEventListener('DOMContentLoaded', function(){
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(a){
      setTimeout(function(){
        try{bootstrap.Alert.getOrCreateInstance(a).close()}catch(e){}
      }, 5000);
    });

    // Add active class to nav links that match current path
    try{
      var links = document.querySelectorAll('.nav-link');
      links.forEach(function(link){
        if(link.getAttribute('href') === window.location.pathname || window.location.pathname.startsWith(link.getAttribute('href'))){
          link.classList.add('active');
        }
      });
    }catch(e){}
  });
})();
