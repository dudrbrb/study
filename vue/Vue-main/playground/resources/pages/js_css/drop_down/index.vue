<template>
  <div class="dropDown-wrapper">
    <div class="dropDown-container">
      <div class="dropDown-header">
        <strong>DROP-DOWN</strong>
      </div>
      <div class="title"><strong>기본-드롭다운</strong></div>
      <div class="dropDown-section">
        <div v-for="index in 4" class="default-dropDown" :key="index">
          <div class="defaultDropdown-head">
            <h2 @click="defaultDropDown">Drop-down{{ index }}</h2>
            <ul class="defaultDropdown-list">
              <li>list {{ index }}-1</li>
              <li>list {{ index }}-2</li>
              <li>list {{ index }}-3</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="title"><strong>마우스오버-드롭다운</strong></div>
      <div class="dropDown-section">
        <div v-for="index in 4" class="hover-dropDown" :key="index">
          <div class="hoverDropdown-head">
            <h2 @mouseover="hoverDropDown" @mouseleave="hoverDropDown">
              Drop-down{{ index }}
            </h2>
            <ul class="hoverDropdown-list">
              <li>list {{ index }}-1</li>
              <li>list {{ index }}-2</li>
              <li>list {{ index }}-3</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="title"><strong>마우스오버-드롭사이드</strong></div>
      <div class="dropDown-section">
        <div class="side-dropDown">
          <div class="sideDropdown-head">
            <h2
              v-for="index in 4"
              :key="index"
              @click="hoverDropside(index, $event)"
            >
              Drop-down{{ index }}
            </h2>
          </div>
          <div class="sideDropdown-body">
            <div class="sideDropdown-content"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.dropDown-wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  min-height: 500px;
  .dropDown-container {
    width: 1060px;
    height: 100%;
    min-height: 500px;
    margin: 0 auto;
    .dropDown-header {
      width: 100%;
      text-align: center;
      margin: 50px 0;
      strong {
        font-size: 32px;
      }
    }
    .title {
      strong {
        display: block;
        font-size: 18px;
        margin: 20px 0;
      }
    }
    .dropDown-section {
      width: 100%;
      height: 100%;
      margin-bottom: 50px;
      .default-dropDown {
        width: 100%;
        height: 100%;
        .defaultDropdown-head {
          h2 {
            display: block;
            width: 100%;
            height: 100%;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            border: 1px solid #e5e5e5;
            padding: 10px;
          }

          .defaultDropdown-list {
            height: 0px;
            overflow: hidden;
            transition: height 0.6s ease;
            margin: -1px 0;
            li {
              padding: 10px;
              font-weight: bold;
            }
          }
          .dropDown-active {
            background-color: #61774f;
            color: #fefefe;
          }
        }
      }
      .hover-dropDown {
        width: 100%;
        height: 100%;
        .hoverDropdown-head {
          h2 {
            display: block;
            width: 100%;
            height: 100%;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            border: 1px solid #e5e5e5;
            padding: 10px;
          }

          .hoverDropdown-list {
            height: 0px;
            overflow: hidden;
            transition: height 0.6s ease;
            margin: -1px 0;
            li {
              padding: 10px;
              font-weight: bold;
            }
          }
          .dropDown-active {
            background-color: #61774f;
            color: #fefefe;
          }
        }
      }
      .side-dropDown {
        display: flex;
        position: relative;
        align-items: center;
        width: 100%;
        .sideDropdown-head {
          width: 200px;
          h2 {
            display: block;
            width: 100%;
            height: 45px;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            border: 1px solid #e5e5e5;
            padding: 10px;
          }
        }
        .sideDropdown-body {
          width: 860px;
          height: 100%;
          .dropDown-active {
            background-color: #61774f;
            color: #fefefe;
          }
          .sideDropdown-content {
            transition: width 0.5s ease;
          }
        }
      }
    }
  }
}
</style>

<script>
export default {
  data() {
    return {
      dropSidePrev: "",
    };
  },
  methods: {
    defaultDropDown(e) {
      const dropDownList = e.target.nextElementSibling;
      let listHeight = dropDownList.style.height;
      if (listHeight == "" || listHeight == "0px") {
        dropDownList.style.height = "120px";
        dropDownList.style.border = "1px solid #e5e5e5";
        e.target.classList.add("dropDown-active");
      } else {
        dropDownList.style.height = "0";
        dropDownList.style.border = "0px solid #e5e5e5";
        e.target.classList.remove("dropDown-active");
        listHeight = "0";
      }
    },
    async hoverDropDown(e) {
      const dropDownList = e.target.nextElementSibling;
      if (e.type == "mouseover") {
        dropDownList.style.height = "120px";
        dropDownList.style.border = "1px solid #e5e5e5";
        e.target.classList.add("dropDown-active");
      } else {
        dropDownList.style.height = "0";
        dropDownList.style.border = "0px solid #e5e5e5";
        e.target.classList.remove("dropDown-active");
      }
    },
    async hoverDropside(index, e) {
      const container = document.querySelector(".sideDropdown-content");
      const prevList = document.querySelector(".sideDropdown-list");
      this.dropSidePrev = this.dropSidePrev == "" ? index : this.dropSidePrev;
      console.log(typeof index, typeof this.dropSidePrev);

      if (index == this.dropSidePrev) {
        if (container.style.width == "100%") {
          console.log("same");
          container.style.transition = "width .5s ease";
          container.style.width = "0px";
          container.style.backgroundColor = "#e5e5e5";
        } else {
          console.log("diff");
          container.style.transition = "width .5s ease";
          container.style.width = "100%";
          container.innerHTML = "";
          container.style.backgroundColor = "#e5e5e5";
          container.style.height = "180px";
        }
      } else {
        container.style.transition = "width .5s ease";
        container.style.width = "100%";
        container.innerHTML = "";
        container.style.backgroundColor = "#e5e5e5";
        container.style.height = "180px";
      }
      this.dropSidePrev = index;
    },
  },
};
</script>