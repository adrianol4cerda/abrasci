document.addEventListener("DOMContentLoaded", function () {
    checkAuthStatus();

    document
        .getElementById("loginForm")
        .addEventListener("submit", function (event) {
            event.preventDefault();
            var form = this;
            fetch(form.action, {
                method: "POST",
                body: new FormData(form),
            })
                .then((response) => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error("Failed to authenticate");
                    }
                })
                .then((data) => {
                    window.location.href = "/dashboard";
                })
                .catch((error) => console.error("Error:", error));
        });
});

function checkAuthStatus() {
    fetch("/users/me")
        .then((response) => {
            if (response.status === 200) {
                // User is authenticated, show protected content
                console.log("User is authenticated");
                // You can add logic here to display protected content
            } else {
                // User is not authenticated, redirect to login page
                console.log("User is not authenticated");
                // Don't redirect here, let the user attempt to log in
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            // Don't redirect on error, let the user attempt to log in
        });
}
