<template>
    <div class="rec">
        <div style="display: flex; flex-direction: column">
            <p>Your Username</p>
            <el-input v-model="emailInput" style="width: 80%" placeholder="" />
            <p>Your Password</p>
            <el-input v-model="passInput" style="width: 80%" placeholder="" />
        </div>
    </div>
</template>

<script>
import { ref } from "vue";
import { ElInput } from "element-plus";

export default {
    components: {
        ElInput,
    },
    setup() {
        const emailInput = ref("");
        const passInput = ref("");

        return {
            emailInput,
            passInput,
        };
    },
};
</script>

<style>
.rec {
    background-color: #3f3f3f;
    border: 1px solid rgba(255, 255, 255, 0.25);
    width: 30vw;
    height: 20vh;
    border-radius: 16px;
}
</style>
