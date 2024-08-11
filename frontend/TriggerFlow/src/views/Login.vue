<template>
    <div class="outer-container">
        <Header></Header>
        <div class="side-content">
            <QuickLogin></QuickLogin>
            <LoginField></LoginField>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Footer from "../components/Login/Footer.vue";
import Header from "../components/Login/Header.vue";
import LoginField from "../components/Login/LoginField.vue";
import QuickLogin from "../components/Login/QuickLogin.vue";

export default {
    components: {
        Footer,
        Header,
        LoginField,
        QuickLogin,
    },
};
</script>
<style>
.outer-container {
    width: 100vw;
}
</style>
