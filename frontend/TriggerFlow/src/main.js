import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";

import router from "./router";
import Tooltip from 'primevue/tooltip';
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';

// CSS imports
import "./assets/index.css";
import "element-plus/dist/index.css";

// Element Plus
import ElementPlus from "element-plus";

// PrimeVue
import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";
import Ripple from "primevue/ripple";
import StyleClass from 'primevue/styleclass';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ElementPlus);
app.directive('tooltip', Tooltip);
app.use(ConfirmationService);
app.use(ToastService);
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
