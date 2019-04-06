<template>
  <div>

    <div>
      <h5 class='font center'>Section One: Examining Airline Incidents by Airline</h5>
    </div>

    <section>

      <form @submit="submitChoice">
        <div class='form_div'>
          <h5 class='font'>Airline:</h5>
          <select v-model="airline" name="airline">
            <option v-for="airline in airlines" :value="airline">{{airline}}</option>
          </select>
          <h5 class='font'>Year Group</h5>
          <select v-model="year" name="incident">
            <option v-for="year in years" :value="year">{{year}}</option>
          </select>
          <button class="waves-effect waves-light btn-small font" type="submit">Submit</button>
        </div>
      </form>

      <div class='hide_button_div'>
        <button @click="hideChart" class='waves-effect waves-light btn-small font'>Hide Chart</button>
      </div>

      <section v-if='showGraphOne' id='graphOne'>
        <v-chart :chartData="adjustData"></v-chart>
      </section>

    </section>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: 'GraphOne',
  data(){
    return {
      airline: "Aer Lingus",
      airlines: ['Aer Lingus', 'Aeroflot*', 'Aerolineas Argentinas', 'Aeromexico*',
      'Air Canada', 'Air France', 'Air India*', 'Air New Zealand*',
      'Alaska Airlines*', 'Alitalia', 'All Nippon Airways', 'American*',
      'Austrian Airlines', 'Avianca', 'British Airways*','Cathay Pacific*',
      'China Airlines', 'Condor', 'COPA', 'Delta / Northwest*','Egyptair', 'El Al',
      'Ethiopian Airlines', 'Finnair', 'Garuda Indonesia', 'Gulf Air',
      'Hawaiian Airlines', 'Iberia', 'Japan Airlines', 'Kenya Airways', 'KLM*',
      'Korean Air', 'LAN Airlines', 'Lufthansa*', 'Malaysia Airlines',
      'Pakistan International', 'Philippine Airlines', 'Qantas*',
      'Royal Air Maroc', 'SAS*', 'Saudi Arabian', 'Singapore Airlines',
      'South African', 'Southwest Airlines', 'Sri Lankan / AirLanka', 'SWISS*',
      'TACA', 'TAM', 'TAP - Air Portugal', 'Thai Airways', 'Turkish Airlines',
      'United / Continental*', 'US Airways / America West*', 'Vietnam Airlines',
      'Virgin Atlantic', 'Xiamen Airlines'],
      year: '85-99',
      years: ['85-99','00-14'],
      height: 600,
      width: 600,
      xAxisLabels: ['incidents', 'fatal', 'fatalities'],
      vBarChartData: [],
      showGraphOne: false,
    }
  },
  computed: {
    ...mapGetters([
      'graphOneData',
    ]),
    adjustData() {
      return this.vBarChartData = {
        chartType: "vBarChart",
        label: true,
        fill: 'blue',
        selector: "vChart",
        title: "Airline Accidents",
        subtitle: "Number of Incidents",
        width: 500,
        height: 500,
        metric: ["count"],
        dim: "name",
        data: this.graphOneData,
        legends: {
          enabled: true,
          height: 5,
          width: 50
        },
      }
    },
  },
  methods: {
    ...mapActions([
      'fetchGraphOneData',
    ]),
    submitChoice(evt) {
      evt.preventDefault();
      const graphOneData = {
        airline: this.airline,
        year: this.year,
      };
      this.showGraphOne = true
      this.fetchGraphOneData(graphOneData);
    },
    hideChart(){
      this.showGraphOne = false;
    },
  },
}
</script>

<style scoped>
form {
  margin-top: 50px;
}

.center {
  text-align: center;
}

.font {
  font-family: 'Roboto Mono', monospace;
}

.form_div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

select {
  margin: 10px;
}

.hide_button_div {
  text-align: center;
}

button {
  margin-left: 10px;
}

#graphOne {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
