<template>
  <div class='navbar_div'>

    <navbar>
      <ul>
        <li class="nav-item">
          <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/About">About</router-link>
        </li>
      </ul>
    </navbar>

  </div>
</template>

<script>
export default {
};
</script>

<style scoped>

ul {
  list-style-type: none;
  color: black;
}

a {
  color: black;
  font-size: 30px;
  text-decoration: none;
  line-height: 30px;
}

a:hover {
  color: white;
  text-decoration: none;
}

</style>
