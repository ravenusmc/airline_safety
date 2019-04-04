<template>
  <div>
    <section>

      <form @submit="submitChoice">
        <div class='form_div'>
          <h5>Airline:</h5>
          <select v-model="airline" name="airline">
            <option v-for="airline in airlines" :value="airline">{{airline}}</option>
          </select>
          <h5>Incident Type</h5>
          <select v-model="incident" name="incident">
            <option v-for="incident in incidents" :value="incident">{{incident}}</option>
          </select>
          <button type="submit">Submit</button>
        </div>
      </form>

      <section v-if='showGraphOne' id='graphOne'>
        <v-chart v-bind:chartData="adjustData"></v-chart>
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
      incident: 'incidents',
      incidents: ['incidents','fatal_accidents','fatalities'],
      height: 600,
      width: 600,
      xAxisLabels: ['incidents', 'fatal', 'fatalities'],
      vBarChartData: {},
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
        selector: "vChart",
        title: "Airline Accidents",
        width: 600,
        height: 500,
        //metric: ["total", "forecast"],
        dim: "month",
        data: this.graphOneData,
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
        incident: this.incident,
      };
      this.showGraphOne = true
      this.fetchGraphOneData(graphOneData);
    },
  },
  mounted() {

  },
}
</script>

<style scoped>
form {
  margin-top: 50px;
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

#graphOne {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
