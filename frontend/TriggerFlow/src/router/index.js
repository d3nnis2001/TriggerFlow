import { createRouter, createWebHistory } from "vue-router";
import NodePage from "../views/NodePage.vue";
import Editor from "../views/Editor.vue";
import ColumnPicker from "../views/ColumnList.vue";
import Login from "../views/Login.vue";
import Overview from "../views/Overview.vue";
import JobOverview from "../views/JobOverview.vue";
import MappingPage from "../views/MappingPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "NodePage",
      component: NodePage,
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
    {
      path: "/mapping",
      name: "MappingPage",
      component: MappingPage,
    },
  ],
});

export default router;
