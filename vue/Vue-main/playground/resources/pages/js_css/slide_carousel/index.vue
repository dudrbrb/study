<template>
  <div class="slide_wrapper">
    <DefaultSlideCompo />
    <VerticalSlideCompo />
  </div>
</template>

<style lang="scss" scoped>
.slide_wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  min-height: 500px;
}
</style>

<script>
import DefaultSlideCompo from "@/components/common/slide_carousel/defaultSlide_compo.vue";
import VerticalSlideCompo from "@/components/common/slide_carousel/verticalSlide_compo.vue";
export default {
  components: {
    DefaultSlideCompo,
    VerticalSlideCompo,
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {},
};
</script>