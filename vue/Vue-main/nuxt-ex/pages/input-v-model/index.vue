<template>
  <div class="container">
      <div id="textInput">
          <h4>Text Input</h4>
          <input type="text" v-model="values.textInput">
          <p>Value: {{values.textInput}}</p>
      </div>

      <div id="numberInput">
          <h4>Number Input</h4>
          <input type="number" v-model="values.numberInput">
          <p>Value: {{values.numberInput}}</p>
      </div>

      <div id="rangeInput">
          <h4>Range Input</h4>
          <input type="range" min="1" max="100" value="1"  v-model="values.rangeInput">
          <p>Value: {{values.rangeInput}}</p>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            values: {
                textInput: '',
                numberInput: '',
                rangeInput: ''
            }
        }
    },
    mounted() {
    },

    methods:{
    },

    destroyed() {

    }
}
</script>

<style lang="scss">
.container{
    width: auto;
    margin-top: 100px;
    * {
        transition: all 0.1s;
    }
    > div{
      margin: 0 auto 40px;
      margin-bottom: 40px;
      position: relative;
      width: 200px;
      input{
        width: 100%;
        margin: 5px 0;
        height: 30px;
        outline: none;
        border: 1px solid #545454;
        opacity: 0.5;
      }
      input:focus{
        opacity: 1;

      }
    }
 
}
</style>
