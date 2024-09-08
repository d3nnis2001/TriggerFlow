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
import Ripple from "primevue/ripple";
import StyleClass from 'primevue/styleclass';

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

app.directive('styleclass', StyleClass);
app.directive('ripple', Ripple)
app.mount("#app");
