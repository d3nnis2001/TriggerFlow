<template>
    <div class="outer-container-overview">
        <Header></Header>
        <h1>Services</h1>
        <div class="row-flex">
            <div class="rectangle" @click="changeRoute('jobs')">
                Job Übersicht
            </div>
            <div class="rectangle" @click="changeRoute('runningjobs')">
                Laufende Jobs
            </div>
            <div class="rectangle" @click="changeRoute('joboffer')">
                Job Angebot
            </div>
        </div>
        <div class="row-flex">
            <div class="rectangle" @click="changeRoute('dashboard')">
                Dashboard
            </div>
            <div class="rectangle" @click="changeRoute('archiv')">
                Job Archiv
            </div>
            <div class="rectangle" @click="changeRoute('fill')">
                Hier ist fill
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Header from "../components/Login/Header.vue";
import Footer from "../components/Login/Footer.vue";
import { useRouter } from "vue-router";

export default {
    components: {
        Footer,
        Header,
    },
    setup() {
        const router = useRouter();
        function changeRoute(route) {
            router.push(route);
        }

        return {
            changeRoute,
        };
    },
};
</script>
<style>
.outer-container-overview {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
}
.row-flex {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    width: 80vw;
}
.rectangle {
    background-color: rgba(255, 255, 255, 0);
    border-radius: 20px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    width: 250px;
    height: 250px;
    font-size: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.rectangle:hover {
    transform: scale(1.05);
    background-color: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.5);
}
</style>
