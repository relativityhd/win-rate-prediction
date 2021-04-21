<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200" />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Win Rate Predictor for League of Legends</h1>

        <p class="subheading font-weight-regular">
          You can find this project on
          <a href="https://github.com/relativityhd/win-rate-prediction" target="_blank">GitHub</a>!
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Please enter your stats:</h2>

        <v-row justify="center">
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="games"
              :rules="[rules.required, rules.number]"
              label="Games"
              hint="Number of Games played"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avgk"
              :rules="[rules.required, rules.number]"
              label="Avg. Kills"
              hint="Average Kills per Game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avgd"
              :rules="[rules.required, rules.number]"
              label="Avg. Deaths"
              hint="Average Creep Score per Minute per Game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avga"
              :rules="[rules.required, rules.number]"
              label="Avg. Assist"
              hint="Average Creep Score per Minute per Game"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="kda"
              :rules="[rules.required, rules.number]"
              label="KDA"
              hint="Kill Death Assist"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="csm"
              :rules="[rules.required, rules.number]"
              label="CS / min"
              hint="Average Creep Score per Minute per Game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="dpm"
              :rules="[rules.required, rules.number]"
              label="Dmg / min"
              hint="Damage per Minute per Game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="kp"
              :rules="[rules.required, rules.number, rules.percent]"
              label="Kill participation"
              hint="Average Kill Participation per Game"
              suffix="%"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="dmgp"
              :rules="[rules.required, rules.number, rules.percent]"
              label="Damage participation"
              hint="Average Damage Participation per Game"
              suffix="%"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avgwpm"
              :rules="[rules.required, rules.number]"
              label="Wards / min"
              hint="Wards per minute per Game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avgwcpm"
              :rules="[rules.required, rules.number]"
              label="Wards cleared / min"
              hint="Wards cleared per minute per game"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="avgvwpm"
              :rules="[rules.required, rules.number]"
              label="Vision wards / min"
              hint="Vision wards per minute per game"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="gdiff"
              :rules="[rules.required, rules.number]"
              label="Gold Diff@min15"
              hint="Average Gold Difference at 15 minutes"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="csdiff"
              :rules="[rules.required, rules.number]"
              label="CS Diff@min15"
              hint="Average Creep Score at 15 minutes"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="xpdiff"
              :rules="[rules.required, rules.number]"
              label="XP Diff@min15"
              hint="Average Experience Points Difference at 15 minutes"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="fb"
              :rules="[rules.required, rules.number, rules.percent]"
              label="Firstblood"
              hint="Firstblood Participation"
              suffix="%"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="fbv"
              :rules="[rules.required, rules.number, rules.percent]"
              label="Firstblood Victim"
              hint="Firstblood Victim"
              suffix="%"
            ></v-text-field>
          </v-col>
          <v-col class="mb-4" cols="3">
            <v-text-field
              v-model="solok"
              :rules="[rules.required, rules.number]"
              label="Solo Kills"
              hint="Total Kills without Teammate Participation"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col class="mb-5" cols="12">
            <v-btn color="primary" elevation="2" @click="predict">Predict</v-btn>
            <v-divider></v-divider>
            <h2 v-if="err" class="headline font-weight-bold mb-3">Couldn't predict stuff :(</h2>
            <h2 v-else class="headline font-weight-bold mb-3">Your win rate is: {{ winrate }}%</h2>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
const axios = require('axios').default

export default {
  name: 'Predictor',

  data: () => ({
    winrate: 5,
    err: false,
    games: undefined,
    kda: undefined,
    avgk: undefined,
    avgd: undefined,
    avga: undefined,
    csm: undefined,
    dpm: undefined,
    kp: undefined,
    dmgp: undefined,
    avgwpm: undefined,
    avgwcpm: undefined,
    avgvwpm: undefined,
    gdiff: undefined,
    csdiff: undefined,
    xpdiff: undefined,
    fb: undefined,
    fbv: undefined,
    solok: undefined,
    rules: {
      required: (value) => !!value || value === 0 || 'Required.',
      number: (value) => !isNaN(value) || 'Must be a number.',
      percent: (value) => (!isNaN(value) && 0 <= value && value <= 1) || 'Must between 0 and 1.'
    }
  }),

  methods: {
    predict() {
      axios
        .get('/api/predict', {
          params: {
            games: this.games,
            kda: this.kda,
            avgk: this.avgk,
            avgd: this.avgd,
            avga: this.avga,
            csm: this.csm,
            dpm: this.dpm,
            kp: this.kp,
            dmgp: this.dmgp,
            avgwpm: this.avgwpm,
            avgwcpm: this.avgwcpm,
            avgvwpm: this.avgvwpm,
            gdiff: this.gdiff,
            csdiff: this.csdiff,
            xpdiff: this.xpdiff,
            fb: this.fb,
            fbv: this.fbv,
            solok: this.solok
          }
        })
        .then((response) => {
          console.log(response)
          this.winrate = response.data['win rate']
          this.err = false
        })
        .catch(() => {
          console.log('not so good')
          this.err = true
        })
    }
  }
}
</script>
