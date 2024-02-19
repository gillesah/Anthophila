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
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}
.main {
	margin: 0 10vw 0 10vw;
}
</style>
