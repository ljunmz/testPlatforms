
var vm = new Vue({
    el: '#app',
    mounted: function () {
    },
    data() {
        return {
            activeIndex2: '10'
        }
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
    }
});
