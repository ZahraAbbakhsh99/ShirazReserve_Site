// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Select the error button
    const errorBtn = document.querySelector(".error-btn");
    // Select the error popup div
    const errorPopup = document.querySelector(".error-popup");

    // Add a click event listener to the error button
    errorBtn.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default anchor behavior

        // Hide the error popup
        errorPopup.style.display = "none";

        // Scroll to the #tracking section
        const trackingElement = document.querySelector("#tracking");
        if (trackingElement) {
            trackingElement.scrollIntoView({ behavior: "smooth" });
        }
    });
});
