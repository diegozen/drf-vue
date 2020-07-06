<template>
  <div>
    <div v-for="note in notes" :key="note.id">
    <b-card-group>
      <b-card bg-variant="white" text-variant="dark" :title="note.end_date">
      <b-card-text>
        {{note.note}}
      </b-card-text>
    </b-card>
    </b-card-group>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Cards',
  props: {
    notes: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
