<template>
	<header class="align-middle">
		<div class="row">
			<div class="col-md-3 col-sm-3 col-3">
				<div class="logo-container">
					<a href="/"><img src="../assets/logo.png" alt="" class="logo" /></a>
				</div>
			</div>
			<div class="vertical-flex col-md-6 col-sm-6 col-6 text-end align-middle">
				<div class="'bi ' + menu_icon" @click="toggleMenu">
					<i :class="menu_icon"></i>
				</div>
				<div :class="{ desktop_menu: true, mobile_menu: menuValue }">
					<ul>
						<li @click="closeMenu"><a href="/lesruches">Toutes les ruches</a></li>
						<li @click="closeMenu" v-if="isAuthenticated"><a href="/mesruches">Mes ruches</a></li>
						<li @click="closeMenu">Courses</li>
						<li @click="closeMenu">Contact</li>
					</ul>
				</div>
			</div>
			<div class="vertical-flex-center col-md-3 col-sm-3 col-3 text-center align-middle">
				<div class="">
					<i class="bi bi-person-fill"></i>
					<div v-if="isAuthenticated" class="user-info">Bonjour {{ username }}<br /><a href="" @click="logout">Déconnexion</a></div>
					<div v-else class="login-link">
						<a href="" data-bs-toggle="modal" data-bs-target="#connexion">se connecter</a>
						<div class="modal fade" id="connexion" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
							<div class="modal-dialog">
								<div class="modal-content">
									<div class="modal-header">
										<h5 class="modal-title" id="exampleModalLabel">Se connecter</h5>
										<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
									</div>
									<div class="modal-body">
										<form @submit.prevent="login">
											<input v-model="username" type="text" placeholder="Nom d'utilisateur" />
											<input v-model="password" type="password" placeholder="Mot de passe" />
											<button type="submit" data-bs-dismiss="modal">Connexion</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</header>
</template>

<script>
import "bootstrap-icons/font/bootstrap-icons.css";

export default {
	data() {
		return {
			menuValue: false,
			menu_icon: "bi-list",
			isAuthenticated: false,
			username: "",
		};
	},
	mounted() {
		const authToken = localStorage.getItem("authToken");
		const username = localStorage.getItem("username");
		if (authToken) {
			this.isAuthenticated = true;
			this.username = username;
		}
	},
	methods: {
		toggleMenu() {
			this.menuValue = !this.menuValue;
		},
		openMenu() {
			this.menuValue = true;
		},
		closeMenu() {
			this.menuValue = false;
		},
		logout() {
			localStorage.removeItem("authToken");
			localStorage.removeItem("username");
			this.isAuthenticated = false;
			this.username = null; // Mettez à jour pour utiliser null ou une chaîne vide
			// Optionnel: Redirigez l'utilisateur vers la page d'accueil ou de connexion
			this.$router.push("/login");
		},
		async login() {
			const credentials = { username: this.username, password: this.password };
			try {
				const response = await fetch("http://localhost:8008/auth/jwt/create", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(credentials),
				});

				const data = await response.json();
				if (data.access) {
					localStorage.setItem("authToken", data.access);
					this.fetchUserInfo();
					this.isAuthenticated = true;
				} else {
					console.error("Échec de la connexion");
				}
			} catch (error) {
				console.error("Erreur:", error);
			}
		},

		async fetchUserInfo() {
			const authToken = localStorage.getItem("authToken");
			if (!authToken) {
				console.error("Token d'authentification non trouvé.");
				return;
			}

			try {
				const response = await fetch("http://localhost:8008/auth/users/me/", {
					method: "GET",
					headers: {
						Authorization: `Bearer ${authToken}`,
						"Content-Type": "application/json",
					},
				});

				if (!response.ok) throw new Error("Échec de la récupération des informations de l'utilisateur");

				const userInfo = await response.json();
				localStorage.setItem("username", userInfo.username);
				this.username = userInfo.username; // Ceci devrait déclencher la mise à jour de l'UI
			} catch (error) {
				console.error("Erreur lors de la récupération des informations de l'utilisateur:", error);
			}
		},
	},
};
</script>

<style scoped>
header {
	padding: 0px;
	background: #dfb355;
	margin-bottom: 2em;
}
.logo {
	width: 10vw;
}
.logo:hover {
	cursor: pointer;
}

.desktop_menu {
	margin-top: 7vh;
}
.desktop_menu ul {
	padding: 0;
	margin: 0;
}
.desktop_menu ul li {
	list-style-type: none;
	color: #fff;
	display: inline-block;
	font-size: 1.5em;
	margin-left: 0.5em;
}
.desktop_menu ul li:hover {
	font-size: 1.6em;
	font-weight: bold;
	cursor: pointer;
	color: #333;
	transition: 0.4s ease-in-out;
	vertical-align: middle;
}
.bi-list {
	display: none;
}
.bi-person-fill {
	font-size: 2em;
	margin-bottom: 0 !important;
}
.login-link a {
	font-size: 1em;
}
.vertical-flex-center {
	display: flex;
	align-items: center;
	justify-content: center;
}
.vertical-flex {
	display: flex;
	align-items: center;
	justify-content: flex-end;
}

@media screen and (min-width: 128px) and (max-width: 900px) {
	.desktop_menu {
		position: fixed !important;
		transition: 0.4 ease-in-out;

		right: -280px;
		top: 34px;
		background: #dfb355;
		width: 280px;
		height: 100%;
	}
	.desktop_menu ul li {
		display: block;
		text-align: left;
		margin: 0;
		padding: 10px 0 10px 26px;
		border-bottom: 1px solid grey;
	}
	.bi-list {
		display: block !important;
		color: white;
		font-size: 3em;
		padding: 10px;
	}
	.mobile_menu {
		right: 0;
		transition: 0.4 ease-in-out;
	}
	.logo {
		width: 18vw;
	}
}
</style>
