function subscribe() {
    const form = document.getElementById('subscribeForm');
    const formData = new FormData(form);

    fetch('Main', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            alert('Subscription successful!');
        } else {
            alert('Subscription failed. Please try again.');
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        alert('An error occurred. Please try again later.');
    });
  }

  // Attach the subscribe function to the button click event
  document.getElementById('subscribeButton').addEventListener('click', subscribe);

  // Function to get CSRF token from cookies
  function getCookie(name) {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.startsWith(name + '=')) {
              return decodeURIComponent(cookie.substring(name.length + 1)) || null;
          }
      }
      return null;
  }
