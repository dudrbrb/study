<template>
  <div class="container">
      NUXT EXAMPLE
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
    * {
        transition: all 0.1s;
    }
}
</style>
