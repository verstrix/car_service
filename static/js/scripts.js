// Small UI enhancements for the site
(function(){
  'use strict'

  function setTheme(dark){
    var root = document.documentElement;
    if(dark){
      root.classList.add('dark');
      localStorage.setItem('theme','dark');
      document.getElementById('themeIcon').className = 'bi bi-moon-stars';
    } else {
      root.classList.remove('dark');
      localStorage.setItem('theme','light');
      document.getElementById('themeIcon').className = 'bi bi-sun';
    }
  }

  function initThemeToggle(){
    var saved = localStorage.getItem('theme');
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var startDark = (saved === 'dark') || (!saved && prefersDark);
    try{ setTheme(startDark); }catch(e){}

    var btn = document.getElementById('themeToggle');
    if(!btn) return;
    btn.addEventListener('click', function(){
      var isDark = document.documentElement.classList.contains('dark');
      setTheme(!isDark);
    });
  }

  function initAutoDismissAlerts(){
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(a){
      setTimeout(function(){
        try{bootstrap.Alert.getOrCreateInstance(a).close()}catch(e){}
      }, 5000);
    });
  }

  function initNavActive(){
    try{
      var links = document.querySelectorAll('.nav-link');
      links.forEach(function(link){
        var href = link.getAttribute('href'); if(!href) return;
        if(href === window.location.pathname || window.location.pathname.startsWith(href)){
          link.classList.add('active');
        }
      });
    }catch(e){}
  }

  function initSearch(){
    var input = document.getElementById('globalSearch');
    if(!input) return;
    input.addEventListener('input', function(){
      var q = input.value.trim().toLowerCase();

      // Filter table rows
      document.querySelectorAll('table').forEach(function(table){
        var tbody = table.tBodies[0]; if(!tbody) return;
        Array.from(tbody.rows).forEach(function(row){
          var text = row.textContent.replace(/\s+/g,' ').toLowerCase();
          row.style.display = q && text.indexOf(q) === -1 ? 'none' : '';
        });
      });

      // Filter card grids
      document.querySelectorAll('.grid-cards, .role-cards').forEach(function(grid){
        grid.querySelectorAll('.card, .role-card').forEach(function(card){
          var text = card.textContent.replace(/\s+/g,' ').toLowerCase();
          card.style.display = q && text.indexOf(q) === -1 ? 'none' : '';
        });
      });
    });
  }

  function animateEntrance(){
    // add fade-in-up to visible cards
    var items = document.querySelectorAll('.card, tbody tr, .role-card');
    items.forEach(function(it,i){
      it.classList.add('fade-in-up');
      setTimeout(function(){ it.classList.add('show'); }, 60 + i * 30);
    });
  }

  document.addEventListener('DOMContentLoaded', function(){
    initThemeToggle();
    initAutoDismissAlerts();
    initNavActive();
    initSearch();
    animateEntrance();

    // Tooltips
    try{ var t = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]')); t.map(function (el) { return new bootstrap.Tooltip(el); }); }catch(e){}
  });

})();
