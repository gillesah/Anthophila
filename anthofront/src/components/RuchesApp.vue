<!-- Ruches.vue -->
<template>
	<div class="row">
		<div v-for="ruche in ruches" :key="ruche.id" class="col-md-2 col-sm-6">
			
			<div class="card mb-3">
				<div class="card-body">
					<h5 class="card-title">{{ ruche.name }}</h5>
					<p class="card-text">type d'abeille : {{ ruche.bee_type }} <br />Année de naissance de la reine : {{ ruche.queen_year }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	props: ["beeyardId"],
	data() {
		return {
			ruches: [],
		};
	},
	mounted() {
		this.fetchRuches();
	},
	methods: {
		fetchRuches() {
			fetch(`http://localhost:8008/API_PUBLIC/beehives/?beeyard=${this.beeyardId}`)
				.then((response) => response.json())
				.then((data) => {
					this.ruches = data.results;
				})
				.catch((error) => console.error("Error:", error));
		},
	},
};
</script>
