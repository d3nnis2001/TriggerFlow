<script setup>
import { Handle, Position } from "@vue-flow/core";
import { ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps({
    data: {
        type: Object,
        required: true,
    },
});

const router = useRouter();
const emit = defineEmits(["updateNode"]);

const comment = ref("");

const changeRoute = () => {
    router.push("/editor");
};
</script>

<template>
    <div class="custom-node route-change-node" @dblclick="changeRoute">
        <Handle type="target" :position="Position.Top" />
        <h2 style="color: black">Editor</h2>
        <div class="comment-form">
            <div class="form-group">
                <label for="comment">Kommentar:</label>
                <textarea
                    id="comment"
                    v-model="comment"
                    rows="3"
                    placeholder="Kommentar eingeben"
                ></textarea>
            </div>
        </div>
        <Handle type="source" :position="Position.Bottom" />
    </div>
</template>

<style scoped>
.custom-node.route-change-node {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 250px;
    padding: 1rem;
    background: white;
    border: 1px solid black;
    border-radius: 4px;
    cursor: pointer;
}

.comment-form {
    width: 100%;
    margin-top: 1rem;
}

.form-group {
    margin-bottom: 0.5rem;
}

label {
    display: block;
    margin-bottom: 0.25rem;
    color: black;
}

textarea {
    width: 90%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    resize: vertical;
}
</style>
