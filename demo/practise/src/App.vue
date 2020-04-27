<template id='app'>  
</template>

<script>
Vue.component("hello-component",{
  template: '#hello',
  el:function(){
    return '#hello';

  },
})
new Vue({
  el: '#app'
})
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
