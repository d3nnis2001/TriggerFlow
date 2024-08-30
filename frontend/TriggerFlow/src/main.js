import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import Tooltip from 'primevue/tooltip';

// CSS imports
import "./assets/index.css";
import "element-plus/dist/index.css";

// Element Plus
import ElementPlus from "element-plus";

// PrimeVue
import PrimeVue from "primevue/config";
import ToastService from "primevue/toastservice";
import Aura from "@primevue/themes/aura";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ElementPlus);
app.use(ToastService);
app.directive('tooltip', Tooltip);
app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      cssLayer: {
        name: "primevue",
        order: "tailwind-base, primevue, tailwind-utilities",
      },
    },
  },
});

app.mount("#app");
