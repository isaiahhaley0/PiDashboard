const app = Vue.createApp({
    data() {
        return { memory: 5,
                temperature: 0,
                pct_used:"",
                uptime:0}
    },
    delimiters: ["[[","]]"],
    mounted(){
        this.getTemp();
        this.getMem();
        this.getPct();
        //window.setInterval(()=>{this.getUptime()},60000)
        this.getUptime();
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
     
        },
        getUptime(){
            fetch("/uptime").then(
                response=>response.json()
                ).then(
                       data=>(this.uptime=data["uptime"])
                        //see get temp
                );
     
        }
            
}
}).mount("#monitor")