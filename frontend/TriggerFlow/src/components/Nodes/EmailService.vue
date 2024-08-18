<script setup>
import { Handle, Position } from "@vue-flow/core";
import { ref } from "vue";

const subject = ref("");
const recipient = ref("");
const body = ref("");
</script>

<template>
    <div class="custom-node email-service-node">
        <Handle type="target" :position="Position.Top" />
        <h2 style="color: black">Email Service</h2>
        <div class="email-form">
            <div class="form-group">
                <label for="recipient">An:</label>
                <input
                    id="recipient"
                    v-model="recipient"
                    type="email"
                    placeholder="Empfänger-Email"
                />
            </div>
            <div class="form-group">
                <label for="subject">Betreff:</label>
                <input
                    id="subject"
                    v-model="subject"
                    type="text"
                    placeholder="Betreff eingeben"
                />
            </div>
            <div class="form-group">
                <label for="body">Nachricht:</label>
                <textarea
                    id="body"
                    v-model="body"
                    rows="4"
                    placeholder="Nachrichtentext eingeben"
                ></textarea>
            </div>
        </div>
        <Handle type="source" :position="Position.Bottom" />
    </div>
</template>

<style scoped>
.custom-node.email-service-node {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 300px;
    padding: 1rem;
    background: white;
    border: 1px solid black;
    border-radius: 4px;
}

.email-form {
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

input,
textarea {
    width: 90%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

textarea {
    resize: vertical;
}
</style>
