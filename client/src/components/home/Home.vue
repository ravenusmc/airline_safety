<template>
  <div>
    <main>

      <div>
        <navbar></navbar>
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
</style>
