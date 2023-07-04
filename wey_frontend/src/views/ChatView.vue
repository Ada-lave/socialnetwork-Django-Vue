<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">

                <div class="space-y-4">
                    

                     <div class="flex items-center justify-between"
                     v-for="c in conv" v-bind:key="conv.id">

                        <div class="flex items-center space-x-2">
                            
                        <template
                        v-for="user in c.users" 
                        v-bind:key="user.id">
                            <img v-if="user.id !== userStore.user.id" v-bind:src="user.getAvatar" class="w-[40px] rounded-full">
                            <p v-if="user.id !== userStore.user.id" class="text-xs font-bold"
                                v-on:click="getActiveConversition(c.id)"> {{ user.name }} </p>
                        </template>

                        <p class="text-gray-500 text-xs">{{ c.modifiedAtFormater }} назад</p>
                        

                        </div>

                        
                    </div>
                   

                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">

            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <template
                        v-for="messages in activeConv.messages"
                        v-bind:key="message.id">


                        <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                        v-if="messages.created_by.id === userStore.user.id">
                        <div>
                            <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm"> {{ messages.body }} </p>
                            </div>

                            <span class="text-xs text-gray-400 leading-none">{{ messages.createdAtFormater }} назад</span>
                        </div>

                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-200">

                            <img v-bind:src="messages.created_by.getAvatar" class="w-[40px] rounded-full">


                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-3 max-w-md mr-auto justify-start"
                    v-else>
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-200">

                            <img v-bind:src="messages.created_by.getAvatar" class="w-[40px] rounded-full">

                        </div>
                        <div>
                            <div class="bg-gray-200 p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm"> {{ messages.body }} </p>
                            </div>

                            <span class="text-xs text-gray-400 leading-none">{{ messages.createdAtFormater }} назад</span>
                        </div>

                        
                    </div>
                    </template>
                    

                    
                </div>

                
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
            <form v-on:submit.prevent="submitForm()">
               <div class="p-4">
                   <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder="" v-model="message"></textarea>
               </div>

               <div class="p-4 border-t border-gray-100 flex justify-between">


                   <button class="ml-auto py-4 px-3 bg-purple-600 text-white rounded-lg" type="submit">Отправить</button>
                
               </div>
            </form>
           </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'
export default {
    name: 'chat',

    setup() {
        const userStore = useUserStore()

        return{
            userStore
        }
    },
    data(){
        return {
            conv: [],
            activeConv: {},
            message: ''
        }
    },
    mounted() {
        this.getConversitions()
    },  

    methods: {
        getActiveConversition(id){
            this.activeConv = id
            this.getMessages()
        },
        getConversitions(){
            axios
            .get('/api/chat/')
            .then(response => {
                this.conv = response.data

                if (this.conv.length) {
                    this.activeConv = this.conv[0].id
                    console.log(this.activeConv)
                }
                

                this.getMessages()
            })
            .catch(error => {
                console.log(error)
            })
        },

        getMessages(){
            axios
            .get(`/api/chat/${this.activeConv}/`)
            .then(response => {
                this.activeConv = response.data
            })
            .catch(error => {
                console.log(error)
            })
        },

        submitForm(){
            axios
            .post(`/api/chat/${this.activeConv}/send/`,{body: this.message})
            .then(response => {
                this.activeConv.messages.push(response.data)
                this.message = ''
            })
        }
    }
}
</script>