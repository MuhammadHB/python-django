document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('facebook-comment-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const postId = document.getElementById('post-id').value;
        const commentMessage = document.getElementById('comment-message').value;

        // Make an API call to your server to post the comment to Facebook
        fetch('/post_facebook_comment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // For Django CSRF token
            },
            body: JSON.stringify({
                post_id: postId,
                message: commentMessage
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Comment posted successfully!');
            } else {
                alert('Failed to post comment.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
