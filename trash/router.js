// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import UserConnexion from "./components/auth/UserConnexion.vue";
import BeeyardAppConnected from "./components/connected/BeeyardAppConnected.vue";
import BeeyardApp from "./components/BeeyardApp"

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes: [
		{
			path: "/login",
			name: "Login",
			component: UserConnexion,
		},
		{
			path: "/mesruches",
			name: "MesRuches",
			component: BeeyardAppConnected,
		},
        {
			path: "/lesruches",
			name: "LesRuches",
			component: BeeyardApp,
		},
	],
});

export default router;
