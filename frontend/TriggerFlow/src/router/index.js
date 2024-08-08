import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Editor from "../views/Editor.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/home",
      name: "Home",
      component: Home,
    },
    {
      path: "/editor",
      name: "Editor",
      component: Editor,
    },
  ],
});

export default router;
