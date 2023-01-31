<template>
  <div class="menu-container">
    <div class="menu">
      <div v-for="(subMenu, index) in subMenuList" :key="index">
        <ul v-if="$route.path.includes(subMenu.urlName)">
          <li v-for="(menuInfo, index) in subMenu.menuList" :key="index">
            <nuxt-link :to="menuInfo.menuUrl">{{
              menuInfo.menuName
            }}</nuxt-link>
          </li>
        </ul>
      </div>
    </div>

    <div class="menu-label" @click="FoldingMenu">MENU</div>
  </div>
</template>


<style lang="scss" scoped>
.menu-container {
  min-height: 877px;
  position: relative;
  .menu {
    display: flex;
    flex-direction: column;
    width: 260px;
    border: 1px solid #e5e5e5;
    transition: 0.5s ease;
    opacity: 1;
    margin-top: -1px;
    height: 100%;
    ul {
      margin: 20px;
      li {
        margin: 20px 0px;
        a {
          color: #999;
          font-size: 18px;
          font-weight: bold;
          text-decoration: none;
          transition: color 0.3s ease;
          border-bottom: 0px solid #333;
        }
        a:hover {
          color: #3e3e3e;
          border-bottom: 4px solid#61774f;
        }
      }
    }
  }
  .menu-label {
    position: absolute;
    top: 20%;
    right: -15px;
    transform: translate(50%, -10px);
    background-color: #61774f;
    width: 30px;
    height: 60px;
    padding: 5px;
    color: white;
    text-align: center;
    writing-mode: vertical-rl;
    transition: 0.3s ease;
    border: none;
    cursor: pointer;
    z-index: 3;
  }
  .menu-label:hover {
    width: 60px;
  }
}
</style>

<script>
export default {
  data() {
    return {
      subMenuList: [
        {
          urlName: "js_css",
          menuList: [
            { menuName: "SLIDE-CAROUSEL", menuUrl: "js_css/slide_carousel" },
            { menuName: "DROP-DOWN", menuUrl: "js_css/drop_down" },
            { menuName: "TOAST-NOTIFICATION", menuUrl: "/" },
            { menuName: "TEXT-ANIMATION", menuUrl: "/" },
          ],
        },
        {
          urlName: "blog",
          menuList: [
            { menuName: "JAVASCRIPT", menuUrl: "/blog/javascript" },
            { menuName: "CSS", menuUrl: "/blog/css" },
            { menuName: "VUEJS", menuUrl: "/" },
          ],
        },
      ],
    };
  },
  mounted() {
    window.addEventListener("scroll", function () {
      const menuContainer = document.querySelector(".menu");
      let scrollPosY = window.scrollY;
      if (scrollPosY == 0) {
        menuContainer.style.width = "260px";
        menuContainer.style.opacity = "1";
      } else {
        const menuLabel = document.querySelector(".menu-lable");
        menuContainer.style.width = "0";
        menuContainer.style.opacity = "0";
      }
    });
  },
  methods: {
    FoldingMenu(e) {
      const menuContainer = document.querySelector(".menu");
      const labelClass = e.target.classList;
      if (labelClass.contains("folding")) {
        menuContainer.style.width = "260px";
        menuContainer.style.opacity = "1";
        labelClass.remove("folding");
      } else {
        const menuLabel = document.querySelector(".menu-lable");
        menuContainer.style.width = "0";
        menuContainer.style.opacity = "0";
        labelClass.add("folding");
      }
      console.log(e.target.classList);
    },
  },
};
</script>
