<template>
    <div class="rec">
        <div style="display: flex; flex-direction: column">
            <p>Your Username</p>
            <el-input v-model="emailInput" style="width: 80%" placeholder="" />
            <div class="outerPassword">
                <p>Your Password</p>
                <div class="hide" @click="togglePasswordVisibility">
                    <img
                        :src="passwordVisibilityIcon"
                        alt="PasswordVisibility"
                    />
                    <p>{{ passwordVisibilityText }}</p>
                </div>
            </div>
            <el-input
                v-model="passInput"
                style="width: 80%"
                :type="passwordFieldType"
                placeholder=""
            />
        </div>
        <el-button type="primary" @click="handleLogin">Log in</el-button>
        <p v-if="error" class="error-message">{{ error }}</p>
    </div>
    <el-button type="primary">Request an Account</el-button>
</template>

<script>
import { ref, computed } from "vue";
import { ElButton, ElInput } from "element-plus";
import PasswordHideIcon from "../icons/PasswordHide.svg";
import PasswordShowIcon from "../icons/PasswordShow.svg";
import { checkLoginData } from "../../api/login";
import { useRouter } from "vue-router";

export default {
    components: {
        ElInput,
        ElButton,
    },
    setup() {
        const router = useRouter();
        const emailInput = ref("");
        const passInput = ref("");
        const showPassword = ref(false);
        const error = ref("");

        const passwordFieldType = computed(() =>
            showPassword.value ? "text" : "password",
        );
        const passwordVisibilityIcon = computed(() =>
            showPassword.value ? PasswordShowIcon : PasswordHideIcon,
        );
        const passwordVisibilityText = computed(() =>
            showPassword.value ? "Show" : "Hide",
        );

        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        };

        const handleLogin = async () => {
            try {
                const response = await checkLoginData(
                    emailInput.value,
                    passInput.value,
                );
                console.log(response);
                if (response.status == 200) {
                    router.push("/overview");
                } else {
                    throw new Error("Ungültige Anmeldedaten");
                }
            } catch (err) {
                error.value = err.message;
            }
        };

        return {
            emailInput,
            passInput,
            passwordFieldType,
            passwordVisibilityIcon,
            passwordVisibilityText,
            togglePasswordVisibility,
            handleLogin,
            error,
        };
    },
};
</script>

<style scoped>
.rec {
    background-color: #3f3f3f;
    border: 1px solid rgba(255, 255, 255, 0.25);
    width: 30vw;
    height: auto; /* Geändert von 20vh zu auto für flexiblere Höhe */
    border-radius: 16px;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
.hide {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    width: 80%;
    cursor: pointer;
}
.outerPassword {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 80%;
}
.error-message {
    color: red;
    margin-top: 10px;
}
</style>
