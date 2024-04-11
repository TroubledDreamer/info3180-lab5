<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies(){
    fetch("/api/v1/movies")
    .then(response => {
            if(response.ok){return response.json()}
            else{return Promise.reject('Something was wrong with fetch request!')}
        })
        .then(data => {
            console.log(data);
            movies.value = data["movies"]
        })
        .catch(error => {
            console.log(error);
        })
    }

    onMounted(() => {
        fetchMovies()
    });


</script>
<template>
    <div class="movies-container">
        <h1>Movies</h1>

        <div class="movies">
            <div v-for="movie in movies" class="movie">
                <div class="poster-container">
                    <img :src="movie.poster" :alt="movie.title" class="movie-poster">
                </div>
                <div class="movie-details">
                    <h2 class="movie-title">{{ movie.title }}</h2>
                    <p class="movie-description">{{ movie.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.movies-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
}

.movies {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.movie {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    width: calc(33.333% - 20px);
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: row;
    align-items: center;
}

.poster-container {
    width: 60%;
    padding: 15px;
}

.movie-poster {
    width: 100%;
    height: auto;
    border-radius: 4px;
}

.movie-details {
    padding: 5px;
    width: 70%;
    text-align: left;
}

.movie-title {
    margin-top: 0;
    font-size: 18px;
    color: #000;
}

.movie-description {
    font-size: 14px;
    color: #555;
}
</style>
