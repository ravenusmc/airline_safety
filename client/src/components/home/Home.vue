<template>
  <div>
    <main>

      <div>
        <Navbar/>
      </div>

      <div>
        <Header/>
      </div>

    </main>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import Navbar from '@/components/support/Navbar';

export default {
  name: 'Home',
  components: {
    Header,
    Navbar,
  }
}
</script>

<style scoped>
main {
  display: grid;
  grid-template-columns: 15% 85%;
}

.navbar_div {
  height: 100%;
  background: #28566c;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
