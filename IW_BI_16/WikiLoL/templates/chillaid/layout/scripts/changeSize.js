new Vue({
    el: '#app',
    data: {
      likesTotales: 1
    },
    methods: {
      incrementLikes() {
        this.likesTotales++;
      }
    }
  });