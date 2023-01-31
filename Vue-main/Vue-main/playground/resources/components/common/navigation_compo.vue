<template>
  <div class="nav-wrapper">
    <div class="nav-container">
      <div class="nav-title">
        <nuxt-link to="/"><h1>PLAYGROUND</h1></nuxt-link>
      </div>
      <div class="nav-menuList">
        <ul>
          <li><nuxt-link to="/js_css">JS&CSS</nuxt-link></li>
          <li><nuxt-link to="/blog">BLOG</nuxt-link></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.nav-wrapper {
  width: 100%;
  height: 60px;
  border: 1px solid #e5e5e5;
  .nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 1160px;
    height: 100%;
    margin: 0 auto;
    .nav-title {
      font-size: 24px;
      font-weight: bold;
      a {
        text-align: none;
        color: #333;
      }
    }
    .nav-menuList {
      ul {
        display: flex;
        justify-content: center;
        align-items: center;
        li {
          margin: 0 20px;
          a {
            color: #666;
            text-decoration: none;
          }
        }
      }
    }
  }
}
</style>

<script>
export default {};
</script>