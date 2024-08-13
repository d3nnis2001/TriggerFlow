<template>
    <div class="job-card">
        <img :src="job.image" :alt="job.name" class="job-image" />
        <div class="job-details">
            <h3>{{ job.name }}</h3>
            <p>{{ job.description }}</p>
            <p class="job-date">{{ formatDate(job.date) }}</p>
            <div class="job-actions">
                <button @click="$emit('load', job)">Load Job</button>
                <button @click="$emit('edit', job)">Edit</button>
                <button @click="$emit('delete', job)">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["job"],
    emits: ["load", "edit", "delete"],
    setup() {
        const formatDate = (date) => {
            return new Date(date).toLocaleDateString();
        };

        return { formatDate };
    },
};
</script>

<style scoped>
.job-card {
    display: flex;
    border: 1px solid #ddd;
    border-radius: 10px;
    width: 60vw;
    height: 150px;
    margin-bottom: 15px;
    padding: 15px;
}

.job-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    margin-right: 15px;
}

.job-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}
</style>
