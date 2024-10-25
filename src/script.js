document.addEventListener('DOMContentLoaded', () => {
    const success = (data) => {
        console.log(data)
    }
    fetch('http://localhost:8009/')
    .then(response => response.json())
    .catch(error => success(false))
    .then(data => success(data))
})