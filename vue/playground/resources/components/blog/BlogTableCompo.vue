<template>
  <div class="blogTable-wrapper">
    <div class="blogTable-header">blog-default-table</div>
    <div class="blogTable-body">

      <button @click="onClick">dddd</button>
      <table class="blog-table">
        <thead>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        </tbody>
        <tfoot>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<style lang="scss" scoped>

</style>

<script>
export default {
  mounted() {
  },
  methods: {
    async onClick() {
      console.log("ddd");

      let consultResultModel = await this.$axios.get(
        process.env.baseUrl + "/api/blog/getData",
      );
    }
  }
}

</script>
