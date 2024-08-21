<template>
  <div id="app">
    <h1>Input Summoner Info</h1>
    <input v-model="name" placeholder="Account Name" />
    <input v-model="tagline" placeholder="Tagline" />
    <input v-model="region" placeholder="Region" />
    
    <button @click="getSummonerInfo">Get Summoner Info</button>
    <div v-if="summonerInfo">
      <h2>Profile Picture</h2>
      <img :src = "summonerInfo.profilePicture" alt = "Summoner's Profile Picture" />
    </div>
    <div v-if="summonerInfo">
      <h2>Some Account Information</h2>
      <p><strong>Name:</strong>{{ summonerInfo.name }}</p>
      <p><strong>Level:</strong>{{ summonerInfo.level }}</p>
    </div>
    
  </div>
</template>

<script>

export default{
  data(){
    return{
      name: '',
      tagline: '',
      region: '',
      summonerInfo: null,
    }
  },
  methods: {
    async getSummonerInfo(){
        try{
          const response = await this.$axios.post('http://127.0.0.1:5000/summonerInfo', {
            name: this.name,
            tagline: this.tagline,
            region: this.region
          });

          this.summonerInfo = response.data;
        }
        catch (error){
          console.error('error:', error);
        }
    }
  }

  
}



// export default {
//   data() {
//     return {
//       name: '',
//       tagline: '',
//       region: '',
//       recency: '',
//       plotURL: null,
//     };
//   },
//   methods: {
//     async fetchplotURL() {
//       try {
//         const response = await this.$axios.post('http://127.0.0.1:5000/summoner', {
//           name: this.name,
//           tagline: this.tagline,
//           region: this.region,
//           recency: this.recency,
//         }, {
//           responseType: 'blob'
//         });

//         const blob = new Blob([response.data], { type: 'image/png' });
//         this.plotURL = URL.createObjectURL(blob);
//       } catch (error) {
//         console.error('error:', error);
//       }
//     },
//   },
// };
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
