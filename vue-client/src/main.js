import Vue from 'vue'
import App from './App.vue'
import router from './router';
import './common/plugins/bootstrap-vue'
import './common/plugins/vue-slick'
import * as VueGoogleMaps from 'vue2-google-maps'
Vue.config.productionTip = false


const API_KEY = process.env.API_KEY;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

Vue.use(VueGoogleMaps, {
  load: {
    
    key: API_KEY,
    libraries: 'places', // 필요한 라이브러리 선택
  },
});