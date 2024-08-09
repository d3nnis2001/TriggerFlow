<template>
    <div class="right-panels">
        <div class="panel docs">
            <h3>Docs / Functions</h3>
            <div class="scrollable-content">
                <div
                    v-for="func in docsFunctions"
                    :key="func.name"
                    class="function-item"
                >
                    <strong>{{ func.name }}</strong
                    >: {{ func.description }}
                </div>
            </div>
        </div>
        <div class="panel variables">
            <h3>Variables</h3>
            <div class="scrollable-content">
                <!-- Content for variables here -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "RightPanelComponent",
    props: {
        docsFunctions: Array,
    },
};
</script>

<style scoped>
.right-panels {
    width: 250px;
    display: flex;
    flex-direction: column;
}
.panel {
    flex: 1;
    border: 1px solid #ccc;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 10px;
}
.panel h3 {
    margin: 0;
    padding: 10px;
    background-color: #f7f7f7;
    color: black;
    border-bottom: 1px solid #ddd;
}
.scrollable-content {
    height: calc(100% - 40px);
    overflow-y: auto;
    padding: 10px;
}
.function-item {
    margin-bottom: 8px;
}
</style>
