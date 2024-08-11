<template>
    <div class="selected-column">
        <h2>{{ column.name }}</h2>
        <div class="column-values">
            <div v-for="(value, index) in columnValues" :key="index">
                {{ value }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "SelectedColumn",
    props: {
        column: Object,
        columnValues: Array,
    },
};
</script>
