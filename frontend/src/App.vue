<template>
  <v-app>
    <v-main>
      <Predictor />
    </v-main>
  </v-app>
</template>

<script>
import Predictor from './components/Predictor'

export default {
  name: 'App',

  components: {
    Predictor
  },

  data: () => ({
    //
  })
}
</script>
