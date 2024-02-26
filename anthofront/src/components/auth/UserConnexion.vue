<template>
	<div>
		<form @submit.prevent="login">
			<input v-model="username" type="text" placeholder="Nom d'utilisateur" />
			<input v-model="password" type="password" placeholder="Mot de passe" />
			<button type="submit">Connexion</button>
		</form>
	</div>
</template>

<script>
export default {
	data() {
		return {
			username: "",
			password: "",
		};
	},
	methods: {
		login() {
			const credentials = {
				username: this.username,
				password: this.password,
			};

			fetch("https://api.anthophila.fr/auth/jwt/create", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(credentials),
			})
				.then((response) => response.json())
				.then((data) => {
					if (data.access) {
						localStorage.setItem("authToken", data.access);
						this.fetchUserInfo(); // Appellez fetchUserInfo après avoir obtenu le token
					} else {
						console.error("Échec de la connexion");
					}
				})
				.catch((error) => console.error("Erreur:", error));
		},
		fetchUserInfo() {
			const authToken = localStorage.getItem("authToken");
			if (!authToken) {
				console.error("Token d'authentification non trouvé.");
				return;
			}

			fetch("https://api.anthophila.fr/auth/users/me/", {
				// Assurez-vous que cette URL est correcte pour votre backend
				method: "GET",
				headers: {
					Authorization: `Bearer ${authToken}`,
					"Content-Type": "application/json",
				},
			})
				.then((response) => {
					if (!response.ok) {
						throw new Error("Échec de la récupération des informations de l'utilisateur");
					}
					return response.json();
				})
				.then((userInfo) => {
					localStorage.setItem("username", userInfo.username); // Stockez le nom d'utilisateur pour une utilisation future
					this.username = userInfo.username; // Mettez à jour le nom d'utilisateur dans l'état local
				})
				.catch((error) => {
					console.error("Erreur lors de la récupération des informations de l'utilisateur:", error);
				});
		},
		logout() {
			localStorage.removeItem("authToken");
			localStorage.removeItem("username");
			// Mise à jour de l'état pour refléter la déconnexion
			this.isAuthenticated = false;
			this.username = "";
		},
	},
};
</script>
