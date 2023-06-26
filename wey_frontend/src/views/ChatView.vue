<template>
    Chat
</template>

<script>
import axios from 'axios'
export default {
    name: 'chat',

    mounted() {
        this.getConversitions()
    },  

    methods: {
        getConversitions(){
            axios
            .get('/api/chat/')
            .then(response => {
                console.log(response.data)
            })
        }
    }
}
</script>