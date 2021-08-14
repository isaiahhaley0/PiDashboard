const app = Vue.createApp({
    data() {
        return { memory: 5,
                temperature: 0}
    },
    delimiters: ["[[","]]"],
    mounted(){
        this.getTemp();
    },
    methods:{
        getTemp(){
            fetch("/temperature").then(
                response=>response.json()
                ).then(
                       temperature=>(this.temperature=temperature["temperature"])
                        //probably the dumbest way of doing this
                );
     
        }
            
}
}).mount("#monitor")