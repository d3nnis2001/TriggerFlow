<template>
    <div class="search-filter">
        <input
            :value="searchQuery"
            @input="$emit('update:searchQuery', $event.target.value)"
            placeholder="Search jobs..."
        />
        <select
            :value="filterCriteria"
            @change="$emit('update:filterCriteria', $event.target.value)"
        >
            <option value="">All</option>
            <option value="recent">Recent</option>
            <option value="old">Old</option>
            <!-- Add more filter options as needed -->
        </select>
    </div>
</template>

<script>
export default {
    props: ["searchQuery", "filterCriteria"],
    emits: ["update:searchQuery", "update:filterCriteria", "filter"],
};
</script>

<style scoped>
.search-filter {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}
</style>
