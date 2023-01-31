<template>
  <div class="slide-container">
    <div class="title"><strong>기본-슬라이드</strong></div>
    <div class="slide-section">
      <img
        class="slideArrow prev"
        @click="SlidePrev"
        :src="imagePackage.prevArrow"
        alt=""
      />
      <img
        class="slideArrow next"
        @click="SlideNext"
        :src="imagePackage.nextArrow"
        alt=""
      />
      <div class="intervalSlide-group">
        <div class="intervalSlide bgColor-red"><p>Slide1</p></div>
        <div class="intervalSlide bgColor-blue"><p>Slide2</p></div>
        <div class="intervalSlide bgColor-yellow"><p>Slide3</p></div>
        <div class="intervalSlide bgColor-green"><p>Slide4</p></div>
      </div>
      <div class="indicator-group">
        <span
          v-for="index in 4"
          :key="index"
          :id="'intervalSlide-indicator' + (index - 1)"
          @click="indicating(index, 'intervalSlide', $event)"
          :class="index == 1 ? 'isSelected' : ''"
        ></span>
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

    ////////interval Slide////////
    .intervalSlide-group {
      display: flex;
      min-height: 400px;
      width: 1060px;
      transition: transform 0.5s ease;
      .intervalSlide {
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
</style>

<script>
export default {
  data() {
    return {
      intervalSlideCnt: 0,
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
    SlideNext(e) {
      const slideGroup = document.querySelector(".intervalSlide-group");
      const clientWith = e.target.parentNode.clientWidth;
      const slideCnt = document.querySelectorAll(".intervalSlide").length;
      this.intervalSlideCnt++;
      let targetNum = Math.abs(this.intervalSlideCnt) % slideCnt;
      const indicator = document.querySelector(
        `#intervalSlide-indicator${targetNum}`
      );
      this.indicatorInit("intervalSlide");
      indicator.classList.add("isSelected");
      slideGroup.style.transform = `translate(-${
        clientWith * (Math.abs(this.intervalSlideCnt) % slideCnt)
      }px,0)`;
      return false;
    },
    SlidePrev(e) {
      const slideGroup = document.querySelector(".intervalSlide-group");
      const slideCnt = document.querySelectorAll(".intervalSlide").length;
      const clientWith = e.target.parentNode.clientWidth;
      if (this.intervalSlideCnt <= 0) {
        this.intervalSlideCnt = slideCnt - 1;
      } else {
        this.intervalSlideCnt -= 1;
      }
      let targetNum = Math.abs(this.intervalSlideCnt) % slideCnt;
      const indicator = document.querySelector(
        `#intervalSlide-indicator${targetNum}`
      );
      this.indicatorInit("intervalSlide");
      indicator.classList.add("isSelected");
      slideGroup.style.transform = `translate(-${clientWith * targetNum}px,0)`;
      return false;
    },
    indicating(index, kind, e) {
      const slideGroup = document.querySelector(`.${kind}-group`);
      const clientWith = slideGroup.firstElementChild.clientWidth;
      const clientHeight = slideGroup.firstElementChild.clientHeight;

      this.intervalSlideCnt = index - 1;
      this.indicatorInit(kind);

      if (kind == "intervalSlide") {
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