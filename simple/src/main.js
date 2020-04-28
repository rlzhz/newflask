import Vue from 'vue'
import VueRouter from 'vue-router'
import Base from './Base.vue'
import IndexPage from './components/index.vue'
import mock from './mock/mock'

Vue.use(VueRouter)
let router = new VueRouter({
    // 保存历史
    mode: 'history',
    routes: [{
        path: '/',
        component: IndexPage
    }]
})

new Vue({
    el: '#app',
    router,
    components: {
        Base,
        // HelloComponent
    },
    template: '<Base/>'

})