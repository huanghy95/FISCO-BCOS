<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>{{ datetime }}</h1>
  </div></template
>
<script>
export default {
  name: 'App',
  data () {
    return { datetime: 'ee' }
  },
  methods: {
    initData () {
      this.$ajax.get('/time', {}).then(res => {
        this.datetime = res.data.time
      })
    }
  },
  mounted () {
    this.initData()
  }
}
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
