<template>
  <div class='navbar_div'>

    <navbar>
      <ul>
        <li class="nav-item">
          <router-link class="font nav-link" to="/">HOME</router-link>
        </li>
        <li class="nav-item">
          <router-link class="font nav-link" to="/About">ABOUT</router-link>
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

.font {
  font-family: 'Roboto Mono', monospace;
}

ul {
  list-style-type: none;
  color: black;
}

a {
  color: #E3132C;
  font-size: 30px;
  text-decoration: none;
  line-height: 30px;
}

a:hover {
  color: #9B1631;
  text-decoration: none;
}

</style>
