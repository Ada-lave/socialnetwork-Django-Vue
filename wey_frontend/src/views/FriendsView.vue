<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">

            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img v-bind:src="user.getAvatar" class="mb-6 rounded-full">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink v-bind:to="{name:'friends',params: {id: user.id}}" class="text-xs text-gray-500">{{ user.friends_count }} friends</RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} постов </p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            
            <div class= "p-4 bg-white   border-gray-200 rounded-lg space-y-6"
                v-if="friendshipReq.length">

                
                <div class="p-4 text-center bg-gray-100 rounded-lg flex col-span-1"
                v-for="friendReq in friendshipReq" v-bind:key="friendReq">

                    <RouterLink v-bind:to="{name:'profile',params: {'id':friendReq.created_by.id}}" class="p-4 text-center  bg-gray-100 rounded-lg flex">

                        <img v-bind:src="friendReq.created_by.getAvatar" class="mb-6 rounded-full">
                        <p class="ml-2 my-auto text-sm"><strong>{{ friendReq.created_by.name }}</strong></p>

                    </RouterLink>

                    
                    <div class="ml-auto my-auto space-x-2">
                        <button 
                        class="px-3 py-2 text-sm bg-green-800 text-white rounded-lg"
                        v-on:click="handRequest('accepted', friendReq.created_by.id)">
                        Добавить</button>
                        <button
                         class="px-3 py-2 text-sm bg-red-800 text-white rounded-lg"
                         v-on:click="handRequest('rejected', friendReq.created_by.id)"
                         >Отклонить</button>
                    </div>
                    

                   
                </div>

                
            </div>

            <div class= "p-4 bg-white   border-gray-200 rounded-lg grid grid-cols-4 gap-4" v-if="friends.length">

                
                <div class="p-4 text-center bg-gray-100 rounded-lg"
                v-for="user in friends" v-bind:key="user">

                    <RouterLink v-bind:to="{name:'profile',params: {'id':user.id}}">

                        <img v-bind:src="user.getAvatar" class="mb-6 rounded-full">
                        <p><strong>{{ user.name }}</strong></p>

                    </RouterLink>
                    

                    

                    <div class="mt-6 flex space-x-8 justify-around">

                        <p class="text-xs text-gray-500"> 182 друзей </p>
                        <p class="text-xs text-gray-500"> 200 постов </p>

                    </div>
                </div>
            </div>
            
        </div>


        <div class="main-right col-span-1 space-y-4">

            <PeopleYouMayKnow />
            <Trends/>
        </div>
        
    </div>
</template>


<script >

import { RouterLink } from 'vue-router'
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import { useUserStore } from "@/stores/user"
import Feed from '../components/Feed.vue'
import {useToastStore} from '@/stores/toast'



    export default {
        name: 'SearchView',

        setup() {
            const userStore = useUserStore()
            const ToastStore = useToastStore()

            return {
                userStore,
                
            }
        },
        components: {
            PeopleYouMayKnow,
            Trends,
            Feed
        },

        data(){
            return {
                
                user: {},
                friendshipReq:[],
                friends: []
                
              
            }
        },

        mounted() {
            this.getFriends()
        },


        methods: {
            getFriends(){
                axios
                .get(`/api/profile/friends/${this.$route.params.id}/`)
                .then(response => {
                    console.log(response.data)
                    this.friends = response.data.friends
                    this.friendshipReq = response.data.requests
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log(error)
                })
            },

            handRequest(status, id) {
                console.log(status)

                axios
                .post(`/api/profile/friends/${id}/${status}/`)
                .then(response => {
                    console.log(response.data.message)
                })
            }

            

            
        }
    }

</script>