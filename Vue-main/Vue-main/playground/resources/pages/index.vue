<template>
  <div class="content-wrapper">
    <div class="content-container">
      <div class="main-header">
        <h1 id="main-title">
          <span class="tilt-first">P</span>LAY-GROUN<span>D</span>
        </h1>
      </div>
      <div class="main-content">
        <div class="introduce">
          <div class="introduce-context">
            <div class="introduce-main">
              <strong>Introduce</strong>
              <p>
                이곳은 개발위한 놀이터, PLAY-GROUND입니다.<br />
                즐겁게 개발을 즐기기위한 공간으로 차곤차곤 컨텐츠를 쌓아갈
                예정입니다.
              </p>
            </div>
          </div>
          <div class="contentList-container">
            <div class="contentList">
              <div class="card-set">
                <div class="card-inner">
                  <div class="content-card">CSS</div>
                  <div class="behind">back</div>
                </div>
              </div>
              <div class="card-set">
                <div class="card-inner">
                  <div class="content-card">JAVASCRIPT</div>
                  <div class="behind">back</div>
                </div>
              </div>
              <div class="card-set">
                <div class="card-inner">
                  <div class="content-card">VUE JS</div>
                  <div class="behind">back</div>
                </div>
              </div>
              <div class="card-set">
                <div class="card-inner">
                  <div class="content-card">HTML</div>
                  <div class="behind">back</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.content-wrapper {
  width: 100%;
  height: 100%;
  .content-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    width: 100%;
    padding: 50px 0;
    .main-header {
      width: 100%;
      height: 100px;
      margin: 0 auto;
      font-size: 64px;
      font-weight: bold;
      text-align: center;
      line-height: 100px;
      letter-spacing: -1px;
      .tilt-first {
        display: inline-block;
        transform: rotateZ(-45deg);
        background-color: transparent;
        color: #61774f;
      }
    }
    .main-content {
      width: 1160px;
      .introduce {
        display: flex;
        justify-content: center;
        flex-direction: column;
        width: 100%;
        height: 100%;
        .introduce-context {
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: #f5f5f5;
          width: 1060px;
          height: 100%;
          margin: 50px auto;
          overflow: hidden;
          .introduce-main {
            width: 100%;
            background-color: #f5f5f5;
            padding: 40px;
            strong {
              font-size: 32px;
            }
            p {
              margin-top: 10px;
              line-height: 1.4;
              font-weight: bold;
              width: 65ch;
            }
          }
        }
      }
      .contentList-container {
        width: 1060px;
        height: 100%;
        margin: 0 auto;
        background-color: #e5e5e5;
        .contentList {
          display: flex;
          justify-content: space-between;
          align-items: center;
          .card-set {
            background-color: transparent;
            .card-inner {
              position: relative;
              transition: transform 0.4s ease-in-out;
              transform-style: preserve-3d;
              width: 250px;
              height: 250px;
              .content-card {
                position: absolute;
                top: 0;
                left: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                height: 100%;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0px 0px 10px #e5e5e5;
                backface-visibility: hidden;
                -webkit-backface-visibility: hidden;
                color: #61774f;
              }
              .behind {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #fefefe;
                font-size: 24px;
                font-weight: bold;
                background-color: #61774f;
                transform: rotateY(180deg);
                backface-visibility: hidden;
                -webkit-backface-visibility: hidden;
              }
            }
          }
          .card-set:hover .card-inner {
            transform: rotateY(180deg);
          }
        }
      }
    }
  }
}
</style>

<script>
export default {
  methods: {
    contact() {
      const contactBar = document.querySelector(".contact");
      const contactBarArrow = window.getComputedStyle(element, "::before");
      console.log(contactBar);
    },
  },
};
</script>