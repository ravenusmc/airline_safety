<template>
  <div>

    <header>
      <div class='header_div'>
        <h1 class='center'>Airline Safety</h1>
        <h4 class='center'>A Simple Study</h4>
      </div>
    </header>

  </div>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>

.center {
  text-align: center;
}

header {
  background-image: url('../../assets/img/united.gif');
  height: 400px;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  display: grid;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.header_div {
  background-color: rgba(255, 0, 0, 0.5);
  color: #fff;
  border-radius: 10px;
  padding: 20px;
}

</style>
