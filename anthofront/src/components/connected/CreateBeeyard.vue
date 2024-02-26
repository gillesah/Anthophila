<template>
	<div>
		<h2>Créer un nouveau Rucher</h2>
		<form @submit.prevent="createBeeyard">
			<div>
				<input v-model="beeyardName" type="text" placeholder="Nom du beeyard" />
			</div>
			<button type="submit">Créer</button>
		</form>
		{{ messageBeeyard }}
	</div>
	<h2>Créer une nouvelle ruche</h2>
	<div>
		<form @submit.prevent="createBeehive">
			<input v-model="beehiveName" type="text" placeholder="Nom de la ruche" />
			<input v-model="queenYear" type="number" placeholder="Année de naissance de la reine" />
			<select v-model="selectedBeeyard">
				<option v-for="yard in beeyards" :key="yard.id" :value="yard.id">{{ yard.name }}</option>
			</select>
			<select v-model="selectedBeeType">
				<option v-for="type in beeTypes" :key="type" :value="type">{{ type }}</option>
			</select>
			<button type="submit">Créer</button>
		</form>
	</div>
</template>

<script>
export default {
	data() {
		return {
			beeyardName: "",
			messageBeeyard: "",
			beehiveName: "",
			queenYear: "",
			selectedBeeyard: "",
			selectedBeeType: "",
			beeyards: [],
			beeTypes: ["Abeille noire", "Abeille européenne", "Autre"], // Mettez à jour selon vos données
		};
	},
	mounted() {
		this.fetchBeeyards();
		const authToken = localStorage.getItem("authToken");
		const id = localStorage.getItem("id");

		const username = localStorage.getItem("username");
		if (authToken) {
			this.isAuthenticated = true;
			this.username = username;
			this.id = id;
		}
	},
	methods: {
		createBeeyard() {
			const authToken = localStorage.getItem("authToken");
			const beekeeperId = localStorage.getItem("id");

			if (!authToken) {
				console.error("Token d'authentification non trouvé. Veuillez vous connecter.");
				return;
			}

			const beeyardData = {
				name: this.beeyardName,
				beekeeper: beekeeperId,
			};

			fetch("https://api.anthophila.fr/API/beeyards/", {
				method: "POST",
				headers: {
					Authorization: `Bearer ${authToken}`,
					"Content-Type": "application/json",
				},
				body: JSON.stringify(beeyardData),
			})
				.then((response) => {
					if (!response.ok) {
						throw new Error("Échec de la création du beeyard");
					}
					return response.json();
				})
				.then((responseData) => {
					console.log("Beehive created successfully:", responseData);
				})
				.catch((error) => {
					console.error("Erreur lors de la création du beeyard:", error);
					this.messageBeeyard = `Désolé, le rucher n'a pas pu être créé`;
				});
		},
		createBeehive() {
			const authToken = localStorage.getItem("authToken");
			if (!authToken) {
				console.error("Token d'authentification non trouvé.");
				return;
			}
			const beehiveData = {
				name: this.beehiveName,
				queen_year: this.queenYear,
				bee_type: this.selectedBeeType,
				beeyard: this.selectedBeeyard,
			};

			fetch("https://api.anthophila.fr/API/beehives/", {
				method: "POST",
				headers: {
					Authorization: `Bearer ${authToken}`,
					"Content-Type": "application/json",
				},
				body: JSON.stringify(beehiveData),
			})
				.then((response) => {
					if (!response.ok) {
						throw new Error("Échec de la création de la ruche");
						//console.log(this.beehiveData);
						//console.log(response);
					}
					return response.json();
				})
				.then((data) => {
					console.log("Beehive created successfully:", data);
				})
				// Reset form or perform further actions
				.catch((error) => {
					console.error("Erreur lors de la création de la ruche:", error);
					console.log(beehiveData);

					this.messageBeeyard = `Désolé, la ruche n'a pas pu être créé $`;
				});
		},
		fetchBeeyards() {
			const authToken = localStorage.getItem("authToken");
			const id = localStorage.getItem("id");

			if (!authToken) {
				console.error("Token d'authentification non trouvé. Veuillez vous connecter.");
				return;
			}

			fetch(`https://api.anthophila.fr/API/beeyards/?beekeeper__id=${id}`, {
				headers: {
					Authorization: `Bearer ${authToken}`,
					"Content-Type": "application/json",
				},
			})
				.then((response) => {
					if (!response.ok) {
						throw new Error("Failed to fetch beeyards");
					}
					return response.json();
				})
				.then((data) => {
					this.beeyards = data.results; 
				})
				.catch((error) => console.error("Error:", error));
		},
	},
};
</script>
<style scoped></style>
