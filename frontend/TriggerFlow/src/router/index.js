import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Editor from "../views/Editor.vue";
import ColumnPicker from "../views/ColumnList.vue";
import Login from "../views/Login.vue";
import Overview from "../views/Overview.vue";
import JobOverview from "../views/JobOverview.vue";

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
    {
      path: "/columns",
      name: "ColumnPicker",
      component: ColumnPicker,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/overview",
      name: "Overview",
      component: Overview,
    },
    {
      path: "/jobs",
      name: "JobOverview",
      component: JobOverview,
    },
  ],
});

export default router;
