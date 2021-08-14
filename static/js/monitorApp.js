const app = Vue.createApp({
    data() {
        return { memory: 5,
                temperature: 0,
                pct_used:""}
    },
    delimiters: ["[[","]]"],
    mounted(){
        this.getTemp();
        this.getMem();
        this.getPct();
    },
    methods:{
        getTemp(){
            fetch("/temperature").then(
                response=>response.json()
                ).then(
                       temperature=>(this.temperature=temperature["temperature"])
                        //probably the dumbest way of doing this
                );
     
        },
        getMem(){
            fetch("/memory").then(
                response=>response.json()
                ).then(
                       data=>(this.memory=data["used"])
                        //see get temp
                );
     
        },
        getPct(){
            fetch("/memory").then(
                response=>response.json()
                ).then(
                       data=>(this.pct_used=data["pct"])
                        //see get temp
                );
     
        }
            
}
}).mount("#monitor")