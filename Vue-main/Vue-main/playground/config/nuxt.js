'use strict'

const { resolve } = require('path')

module.exports = {

  build: {
    /* 분석할때 쓰는거
    analyze: {
      analyzerMode: 'static',
      generateStatsFile: true,
      statsFilename: 'webpack-stats.json'
    }*/
  },
    modules: ['@nuxtjs/axios'],

  /*** Axios module configuration */
  axios: { // sk. this.$axios.get할때 적용됨 // See https://github.com/nuxt-community/axios-module#options
    baseURL: process.env.APP_URL, //baseURL: process.env.BASE_URL || process.env.APP_URL || 'sk-alert : no-base-url',
    browserBaseURL: process.env.APP_URL //browserBaseURL: process.env.BASE_URL || process.env.APP_URL || 'sk-alert : no-base-url',
    //credentials: true
  },

  //클라이언트와 서버서 공유할 환경 변수
  env: { // 이제 process.env.baseUrl 접근가능함. asyncData에서는 위 기본 axios세팅이 안먹히고 http로 시작해야해서
    baseUrl:process.env.APP_URL//baseURL: process.env.BASE_URL || process.env.APP_URL || 'sk-alert : no-base-url',
  }
  ,
  css: ['~assets/css/main.css'],

  head: {
    title: 'Adonuxt',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {
        charset: 'utf-8'
      },
      {
        name: 'viewport',
        content: 'width=device-width,initial-scale=1'
      },
      {
        'http-equiv': 'x-ua-compatible',
        content: 'ie=edge,chrome=1'
      },
      {
        hid: 'description',
        name: 'description',
        content: 'Adonuxt project'
      }
    ],
    link: [
      {
        rel: 'shortcut icon',
        type: 'image/x-icon',
        href: 'favicon.png'
      }
    ],
    noscript: [{ innerHtml: `
      <h1>Javascript Disabled</h1>
      <p>It appears that you do not have Javascript enabled. This application relies on Javascript for most of our features.<p>
      <p>Please enable Javascript and <a href=".">reload</a> in order to use this site.</p>
    `}]
  },

  loading: {
    color: '#744d82'
  },

  router: {
    base: '/',
    scrollBehaviour: () => ({
      x: 0,
      y: 0
    })
  },

  srcDir: resolve(__dirname, '..', 'resources'),
  telemetry:false,
}
