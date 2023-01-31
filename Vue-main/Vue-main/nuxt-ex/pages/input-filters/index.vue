<template>
  <div class="container">
      <div id="keyupEvent">
          <h4>filters 사용</h4>
          <p>숫자만 입력되게 + 3자리마다 콤마</p>
          <input type="text" v-model="input">
          <p>Value: {{input | comma}}</p>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            input:'',
        }
    },
    filters:{
        comma(v){
            return String(v).replace(/[^0-9]/g,'').replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
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
      width: 300px;
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
