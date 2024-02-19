<template>
	<div>
		<h2>Tous les ruchers quand connecté</h2>

		<div class="row beeyardchoice">
			<div v-for="beeyard in data" :key="beeyard.id" @click="selectBeeyard(beeyard.id)" class="col-md-3 col-sm-6">
				<div class="card mb-3" :class="{ 'selected-beeyard': beeyard.id === selectedBeeyardId }">
					<div class="card-body">
						<h5 class="card-title">{{ beeyard.name }}</h5>
						<p class="card-text">{{ beeyard.beekeeper_extended.username }}</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	<RuchesApp v-if="selectedBeeyardId" :key="selectedBeeyardId" :beeyardId="selectedBeeyardId" />
</template>
<script>
import RuchesApp from "../RuchesApp.vue";

export default {
	components: {
		RuchesApp,
	},
	data() {
		return {
			data: [],
			selectedBeeyardId: null,
		};
	},
	mounted() {
		this.fetchBeeyards();
	},
	methods: {
		fetchBeeyards() {
			fetch("http://localhost:8008/API_PUBLIC/beeyards/")
				.then((response) => response.json())
				.then((data) => {
					this.data = data.results;
				})
				.catch((error) => console.error("Error:", error));
		},
		selectBeeyard(id) {
			this.selectedBeeyardId = id;
		},
		fetchData() {
			const authToken = localStorage.getItem("authToken");
			if (!authToken) {
				console.error("Token d'authentification non trouvé. Veuillez vous connecter.");
				return;
			}

			fetch("http://localhost:8008/chemin/de/votre/api", {
				method: "GET", // ou autre méthode HTTP selon l'opération
				headers: {
					"Content-Type": "application/json",
					Authorization: `Bearer ${authToken}`,
				},
			})
				.then((response) => response.json())
				.then((data) => {
					// Traitez les données reçues de l'API
					console.log(data);
				})
				.catch((error) => console.error("Erreur:", error));
		},
	},
};
</script>
<style scoped>
.selected-beeyard {
	box-shadow: rgba(63, 63, 67, 0.4) 0px 17px 29px 0px !important;
}
.beeyardchoice {
	margin: 2em 0 2em 0;
}
.card {
	box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
	border: none !important;
	background-color: bisque;
}
.card:hover {
	transform: scale(1.05);
	transition: transform 0.3s ease;
}
</style>
