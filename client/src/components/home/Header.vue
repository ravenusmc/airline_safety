<template>
  <div>
    <header/>
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


</style>
