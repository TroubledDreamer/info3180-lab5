

<template>
    <div>
        <h1>Add Movie Form View</h1>
        <MovieForm />
    </div>
</template>




<script>
import MovieForm from "@/components/MovieForm.vue";

export default {
  components: {
    MovieForm // Registering MovieForm component for use in this template
  }
}
</script>