const button = document.getElementById('btn_delete');

button.onclick = function(el) {
    if (confirm("Do you want to delete the movie?")) {
        window.location.href = el.target.dataset.href;
    }
}

