<template>

<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       
           <div class="p-4 bg-white border border-gray-200 rounded-lg"
           v-for="notification in notifications"
           v-bind:key="notification.id">
                       
            {{ notification.body }}
            <template v-if="notification.type === 'postlike' || notification.type === 'postcomment'">
                <button 
                v-on:click="readNotification(notification)"
                class="underline">Перейти к записи</button>
            </template>
           </div>

</div>


</template>

<script>
import axios from 'axios'
export default {
    name: 'notifications',

    data() {
        return {
            notifications: []
        }
    },
    mounted() {
        this.notificationGet()
    },

    methods: {
        notificationGet() {
            axios
            .get('/api/notification/allUser/')
            .then(response => {
                console.log(response)
                this.notifications = response.data
            })
            .catch(error => {
                console.log(error)
            })
        },

        async readNotification(notification){
            
            await axios
            .post(`/api/notification/read/${notification.id}/`)
            .then(response => {
                if (notification.type === 'postlike' || notification.type==='postcomment'){
                    this.$router.push({name: 'postview', params: {id: notification.post}})
                }
                else {
                    this.$router.push({name:'friends', params: {id: notification.created_by}})
                }
                console.log(response.data.message)
            })
            .catch(error => {
                console.log(error)
            })
        },
    }
}

</script>