<template>
  <div>
    <main>

      <div>
        <Navbar/>
      </div>

      <div>
        <Header/>
        <GraphOne/>
      </div>

    </main>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import Navbar from '@/components/support/Navbar';
import GraphOne from '@/components/graphs/GraphOne';

export default {
  name: 'Home',
  components: {
    Header,
    Navbar,
    GraphOne,
  }
}
</script>

<style scoped>
main {
  display: grid;
  grid-template-columns: 15% 85%;
  min-height: 100vh;
}

.navbar_div {
  height: 100%;
  background: #003268;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

</style>
