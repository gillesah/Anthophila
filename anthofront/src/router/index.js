// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import UserConnexion from "..//components/auth/UserConnexion.vue";
import BeeyardAppConnected from "..//components/connected/BeeyardAppConnected.vue";
import CreateBeeyard from "..//components/connected/CreateBeeyard.vue";
import BeeyardApp from "..//components/BeeyardApp.vue";

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes: [
		{
			path: "/",
			name: "accueil",
			component: BeeyardApp,
		},
		{
			path: "/login",
			name: "Login",
			component: UserConnexion,
		},
		{
			path: "/lesruches",
			name: "Ruche",
			component: BeeyardApp,
		},
		{
			path: "/mesruches",
			name: "MesRuches",
			component: BeeyardAppConnected,
		},
		{
			path: "/create",
			name: "Créer un rucher",
			component: CreateBeeyard,
		},
	],
});

export default router;
