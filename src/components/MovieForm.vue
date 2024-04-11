
<script setup>
import { ref , onMounted } from 'vue';
let csrf_token = ref("");
let fetchResponseType = ref("")
let fetchResponse = ref("")
    



function getCsrfToken() {

    fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })

}


onMounted(() => {
    getCsrfToken();
})


function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    


    fetch("/api/v1/movies", {
        method: "POST",
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
        } 
    })

    .then(function(response) {
        return response.json();
    })

    .then(function(data) {
        console.log(data);
        fetchResponse.value = data
                    
        if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }

    })
    .catch(function(error) {
        console.log(error);
    });
}








</script>













<template>
    <form @submit.prevent="saveMovie" id="movieForm" class="movie-form">
        <div class="form-group">
            <label for="title" class="form-label">Title:</label>
            <input type="text" id="title" name="title" class="form-control" />
        </div>
        <div class="form-group">
            <label for="description" class="form-label">Description:</label>
            <textarea id="description" name="description" class="form-control"></textarea>
        </div>
        <div class="form-group">
            <label for="poster" class="form-label">Poster:</label>
            <input type="file" id="poster" name="poster" accept=".jpg,.png" class="form-control" />
        </div>
        <button class="submit-btn">Submit</button>
    </form>
</template>

<style scoped>
.movie-form {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

.form-group {
    margin-bottom: 15px;
}

.form-label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-control {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 14px;
}

.form-control[type="file"] {
    border: none;
}

textarea.form-control {
    height: 100px;
}

.submit-btn {
    background-color: #007bff;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

.submit-btn:hover {
    background-color: #0056b3;
}
</style>
