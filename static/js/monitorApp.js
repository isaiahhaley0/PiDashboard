const app = Vue.createApp({
    data() {
        return { memory: 5}
    },
    delimiters: ["[[","]]"]
}).mount("#monitor")