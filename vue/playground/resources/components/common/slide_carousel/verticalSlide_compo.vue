<template>
  <div class="slide-container">
    <div class="title"><strong>세로-슬라이드</strong></div>
    <div class="slide-section">
      <img
        class="slideArrow up"
        @click="SlideUp"
        :src="imagePackage.upArrow"
        alt=""
      />
      <img
        class="slideArrow down"
        @click="SlideDown"
        :src="imagePackage.downArrow"
        alt=""
      />
      <div class="verticalSlide-group">
        <div class="verticalSlide bgColor-red"><p>Slide1</p></div>
        <div class="verticalSlide bgColor-blue"><p>Slide2</p></div>
        <div class="verticalSlide bgColor-yellow"><p>Slide3</p></div>
        <div class="verticalSlide bgColor-green"><p>Slide4</p></div>
      </div>
      <div class="verticalIndicator-group">
        <span
          v-for="index in 4"
          :key="index"
          :id="'verticalSlide-indicator' + (index - 1)"
          @click="indicating(index, 'verticalSlide', $event)"
          :class="index == 1 ? 'isSelected' : ''"
        ></span>
      </div>
      <div class="slideCnt-container">
        <strong>{{ verticalSlidePos }}/4</strong>
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.slide-container {
  width: 1060px;
  height: 100%;
  min-height: 500px;
  margin: 0 auto;
  .slide-header {
    width: 100%;
    text-align: center;
    margin: 50px 0;
    strong {
      font-size: 32px;
    }
  }
  .slide-section {
    position: relative;
    width: 100%;
    height: 400px;
    overflow: hidden;
    margin-bottom: 80px;
    /////common/////
    .slideArrow {
      width: 40px;
      height: 40px;
      background: transparent;
      z-index: 3;
      filter: contrast(100%) invert(100%);
    }

    .up {
      position: absolute;
      top: 2%;
      left: 50%;
      transform: translate(-50%, -2%);
    }
    .down {
      position: absolute;
      bottom: 2%;
      left: 50%;
      transform: translate(-50%, -2%);
    }

    .prev {
      position: absolute;
      top: 50%;
      left: 2%;
      transform: translate(-2%, -50%);
    }
    .next {
      position: absolute;
      top: 50%;
      right: 2%;
      transform: translate(2%, -50%);
    }

    .indicator-group {
      display: flex;
      justify-content: space-around;
      position: absolute;
      width: 280px;
      right: 50%;
      bottom: 10%;
      transform: translate(50%, -10%);
      background-color: transparent;
      span {
        display: block;
        width: 50px;
        height: 15px;
        background-color: #fefefe;
        border-radius: 5px;
        transition: width 0.3s ease;
        cursor: pointer;
      }
      span:hover {
        background-color: #b2b2b2;
      }
      .isSelected {
        width: 60px;
        background-color: #b2b2b2;
      }
    }
    //////////////////////////

    /////////vertical slide////////
    .verticalSlide-group {
      display: flex;
      flex-direction: column;
      min-height: 400px;
      width: 1060px;
      transition: transform 0.5s ease;
      .verticalSlide {
        display: flex;
        justify-content: center;
        align-items: center;
        min-width: 1060px;
        height: 100%;
        min-height: 400px;
        font-size: 28px;
        font-weight: bold;
        p {
          color: #fefefe;
          font-size: 32px;
        }
      }
    }

    .verticalIndicator-group {
      display: flex;
      justify-content: center;
      flex-direction: column;
      position: absolute;
      height: 280px;
      width: 280px;
      left: 5%;
      top: 50%;
      transform: translate(5%, -50%);
      background-color: transparent;
      span {
        display: block;
        width: 10px;
        height: 100px;
        background-color: #fefefe;
        transition: width 0.3s ease;
        cursor: pointer;
      }
      span:hover {
        background-color: #b2b2b2;
      }
      .isSelected {
        height: 80px;
        background-color: #b2b2b2;
      }
    }
    .slideCnt-container {
      position: absolute;
      bottom: 5%;
      right: 5%;
      transform: translate(-5%, -5%);
      background-color: transparent;
      strong {
        font-size: 32px;
        font-weight: bold;
        color: #fefefe;
      }
    }
  }
  /////commom////////
  .bgColor-red {
    background-color: tomato !important;
  }
  .bgColor-blue {
    background-color: royalblue !important;
  }
  .bgColor-yellow {
    background-color: rgb(255, 230, 0) !important;
  }
  .bgColor-green {
    background-color: yellowgreen !important;
  }
  strong {
    display: block;
    font-size: 18px;
    margin: 20px 0;
  }
}
</style>

<script>
export default {
  data() {
    return {
      defaultSlideCnt: 0,
      verticalSlideCnt: 0,
      verticalSlidePos: 1,
      imagePackage: {
        nextArrow: require("@/assets/images/icon/next.png"),
        prevArrow: require("@/assets/images/icon/back.png"),
        downArrow: require("@/assets/images/icon/downArrow.png"),
        upArrow: require("@/assets/images/icon/upArrow.png"),
      },
    };
  },
  methods: {
    SlideDown(e) {
      const slideGroup = document.querySelector(".verticalSlide-group");
      const slideCnt = document.querySelectorAll(".verticalSlide").length;
      const clientHeight = e.target.parentNode.clientHeight;
      this.verticalSlideCnt++;
      let targetNum = Math.abs(this.verticalSlideCnt) % slideCnt;
      this.verticalSlidePos = targetNum + 1;
      const indicator = document.querySelector(
        `#verticalSlide-indicator${targetNum}`
      );
      this.indicatorInit("verticalSlide");
      indicator.classList.add("isSelected");
      slideGroup.style.transform = `translate(0,-${
        clientHeight * (Math.abs(this.verticalSlideCnt) % slideCnt)
      }px)`;
      return false;
    },
    SlideUp(e) {
      const slideGroup = document.querySelector(".verticalSlide-group");
      const slideCnt = document.querySelectorAll(".verticalSlide").length;
      const clientHeight = e.target.parentNode.clientHeight;
      if (this.verticalSlideCnt <= 0) {
        this.verticalSlideCnt = slideCnt - 1;
      } else {
        this.verticalSlideCnt -= 1;
      }
      let targetNum = Math.abs(this.verticalSlideCnt) % slideCnt;
      this.verticalSlidePos = targetNum + 1;
      const indicator = document.querySelector(
        `#verticalSlide-indicator${targetNum}`
      );
      this.indicatorInit("verticalSlide");
      indicator.classList.add("isSelected");
      slideGroup.style.transform = `translate(0,-${
        clientHeight * targetNum
      }px)`;
      return false;
    },
    indicating(index, kind, e) {
      const slideGroup = document.querySelector(`.${kind}-group`);
      const clientWith = slideGroup.firstElementChild.clientWidth;
      const clientHeight = slideGroup.firstElementChild.clientHeight;

      this.defaultSlideCnt = index - 1;
      this.indicatorInit(kind);

      if (kind == "defaultSlide") {
        slideGroup.style.transform = `translate(-${
          clientWith * (index - 1)
        }px,0)`;
      } else if (kind == "verticalSlide") {
        slideGroup.style.transform = `translate(0,-${
          clientHeight * (index - 1)
        }px)`;
      }

      e.target.classList.add("isSelected");
    },
    indicatorInit(kind) {
      const indicatorGroup = [
        ...document.querySelectorAll(`[id^="${kind}-indicator"]`),
      ];

      for (let i = 0; i < indicatorGroup.length; i++) {
        const element = indicatorGroup[i];
        element.classList.remove("isSelected");
      }
    },
  },
};
</script>