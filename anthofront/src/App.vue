<template>
	<!-- <img alt="Vue logo" src="./assets/logo.png"> -->
	<HeaderMenu> </HeaderMenu>
	<div class="main">
		<!-- <BeeyardApp></BeeyardApp> -->
		<router-view />
	</div>
</template>

<script>
import HeaderMenu from "./components/HeaderMenu.vue";
// import BeeyardApp from "./components/BeeyardApp.vue";

export default {
	name: "App",
	components: {
		HeaderMenu,
	},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");

#app {
	font-family: "Inter", sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}
.main {
	margin: 0 10vw 0 10vw;
}
</style>
