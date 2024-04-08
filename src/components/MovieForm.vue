
<template>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div>
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" />
        </div>
        <div>
            <label for="description">Description:</label>
            <textarea id="description" name="description"></textarea>
        </div>
        <div>
            <label for="poster">Poster:</label>
            <input type="file" id="poster" name="poster" />
        </div>
        <button type="submit">Submit</button>
    </form>
</template>

<script setup>
import { ref , onMounted } from 'vue';
let csrf_token = ref("");




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
    })
    .catch(function(error) {
        console.log(error);
    });
}








</script>
