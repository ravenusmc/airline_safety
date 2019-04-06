<template>
  <div>
    <main>

      <div>
        <Navbar/>
      </div>

      <div class='content_area'>
        <Header/>
        <sectionOne/>
        <GraphOne/>
        <!-- <GraphTwo/> -->
      </div>

    </main>
  </div>
</template>

<script>
import Header from '@/components/home/Header';
import sectionOne from '@/components/home/SectionOne';
import Navbar from '@/components/support/Navbar';
import GraphOne from '@/components/graphs/GraphOne';
import GraphTwo from '@/components/graphs/GraphTwo';

export default {
  name: 'Home',
  components: {
    Header,
    Navbar,
    sectionOne,
    GraphOne,
    GraphTwo,
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

.content_area {
  margin-bottom: 50px;
}

@media only all and (max-width: 968px){
  main {
    grid-template-columns: 1fr;
  }
}

</style>
