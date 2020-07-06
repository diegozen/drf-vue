<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">

      <b-form-group id="input-group-a" label="User" label-for="input-a">
        <b-form-select id="input-a" v-model="form.user" multiple>
          <option v-for="item in users" :key="item.id" :value="item.id">{{ item.nombre }}</option>
        </b-form-select>
      </b-form-group>

      <b-form-group id="input-group-b" label="End Date" label-for="input-b">
        <b-form-datepicker id="input-b" v-model="form.end_date" class="mb-2"></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-c" label="Note:" label-for="input-c">
        <b-form-textarea
          id="input-c"
          v-model="form.note"
          required
          placeholder="Enter something..."
          rows="3"
          max-rows="6"
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-d" label="Types:" label-for="input-d">
        <b-form-select
          id="input-d"
          v-model="form.tipo"
          :options="types"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-e">
          <b-form-checkbox v-model="form.task">Task</b-form-checkbox>
      </b-form-group>

      <b-form-group id="input-group-f">
          <b-form-tags input-id="tags-basic" v-model="form.tags" class="mb-2"></b-form-tags>
      </b-form-group>

      

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    <Cards
      :notes="notes"
    />
  </div>
</template>

<script>
import Cards from './components/Cards.vue'
  export default {
    name: 'App',
    components: {
      Cards,
    },
    data() {
      return {
        form: {
          note: '',
          tipo: "",
          task: false,
          end_date: null,
          user: [],
          tags: []
        },
        notes: [],
        types: [
          { text: 'Select One', value: null }, 
          {text: 'Tipo 1', value: "1"},
          {text: 'Tipo 2', value: "2"},
          {text: 'Tipo 3', value: "3"},
        ],
        users: [],
        show: true
      }
    },
    created () {
        fetch('http://127.0.0.1:8000/api/users/')
        .then(response => {
          console.log(response)
          return response.json()})
        .then(json => {
            this.users = json
            console.log(json)
        })
        fetch('http://127.0.0.1:8000/api/notes/')
        .then(response => {
          console.log(response)
          return response.json()})
        .then(json => {
            this.notes = json
            console.log(json)
        })
        
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        // alert(JSON.stringify(this.form))
        console.log(this.form)
        fetch('http://127.0.0.1:8000/api/notes/create', {method: 'post', headers:{'Content-Type': 'application/json'}, body: JSON.stringify(this.form)})
        .then(response => response.json())
        .then(json => {
            this.notes.push(json)
            console.log(json)
        })
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.note = ''
        this.form.task = false
        this.form.tipo = null
        this.form.end_date = null
        this.form.user = [],
        this.form.tags = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>