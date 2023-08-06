/*!
* Start Bootstrap - Freelancer v7.0.7 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

    // Gravatar support
    function getGravatarURL(email){
        const emailHash = md5(email.toLowerCase());
        return `https://www.gravatar.com/avatar/${emailHash}`; // construct the Gravatar URL
    }

    // Function to fetch and display timeline posts
    function fetchTimelinePosts() {
        fetch('/api/timeline_post')
          .then(response => response.json())
          .then(data => {
            const timelinePostsContainer = document.getElementById('timeline-posts-container');
            timelinePostsContainer.innerHTML = '';
  
            data.timeline_posts.forEach(post => {
              const postDiv = document.createElement('div');
              postDiv.classList.add('timeline-post');
              postDiv.innerHTML = `
                <h3>${post.name}</h3>
                <img src="${getGravatarURL(post.email)}" alt="Gravatar" />
                <p>${post.email}</p>
                <p>${post.content}</p>
                <hr>
              `;
              timelinePostsContainer.appendChild(postDiv);
            });
          })
          .catch(error => console.log(error));
      }
  
      // Function to handle form submission
      function handleFormSubmit(event) {
        event.preventDefault();
  
        const form = document.getElementById('timeline-post-form');
        const formData = new FormData(form);
  
        fetch('/api/timeline_post', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          form.reset();
          fetchTimelinePosts();
        })
        .catch(error => console.log(error));
      }
  
      // Add event listener to form submit event
      const form = document.getElementById('timeline-post-form');
      form.addEventListener('submit', handleFormSubmit);
  
      // Fetch and display initial timeline posts
      fetchTimelinePosts();


window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});
