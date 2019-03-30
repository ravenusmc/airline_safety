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

    </section>
  </div>
</template>

<script>
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
      incident: 'An Incident',
      incidents: ['An Incident','fatal_accidents','fatalities'],
    }
  },
  methods: {
    submitChoice(evt) {
      evt.preventDefault();

    },
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
</style>
