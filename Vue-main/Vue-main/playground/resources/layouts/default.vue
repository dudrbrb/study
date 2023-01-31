<template>
  <div class="wrapper">
    <Navigation />
    <div class="container">
      <SubMenu v-if="$route.path !== '/'" />
      <div class="nuxt-wrapper">
        <nuxt class="nuxt-container" />
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.wrapper {
  width: 100%;
  min-height: 100vh;
  .container {
    position: relative;
    width: 100%;
    min-height: 877px;
    display: flex;
    .nuxt-wrapper {
      display: flex;
      width: 100%;
      min-height: 877px;
      .nuxt-container {
        position: absolute;
        top: 0;
        left: 291px;
        width: 1160px;
      }
    }
  }
}
</style>

<script>
import Navigation from "~/components/common/navigation_compo.vue";
import SubMenu from "~/components/common/subMenu_compo.vue";
export default {
  data() {
    return {};
  },
  components: {
    Navigation,
    SubMenu,
  },

  methods: {},
};
</script>