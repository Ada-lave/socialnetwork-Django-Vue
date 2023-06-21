<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">

            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink v-bind:to="{name:'friends',params: {id: user.id}}" class="text-xs text-gray-500">200 friends</RouterLink>
                    <p class="text-xs text-gray-500">448 posts</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            
            <div class= "p-4 bg-white   border-gray-200 rounded-lg grid grid-cols-2 gap-4"
                v-if="friendshipReq.length">

                
                <div class="p-4 text-center bg-gray-100 rounded-lg"
                v-for="friendReq in friendshipReq" v-bind:key="friendReq">

                    <RouterLink v-bind:to="{name:'profile',params: {'id':friendReq.created_by.id}}">

                        <img src="https://i.pravatar.cc/100?img=70" class="mb-6 mx-auto rounded-full">
                        <p><strong>{{ friendReq.created_by.name }}</strong></p>

                    </RouterLink>
                    

                    

                    <div class="mt-6 flex space-x-8 justify-around">

                        <p class="text-xs text-gray-500"> 182 друзей </p>
                        <p class="text-xs text-gray-500"> 200 постов </p>

                    </div>
                </div>
            </div>
            
        </div>

        <div class="p-4 bg-white border border-gray-200 rounded-lg"
            v-for="post in posts"
            v-bind:key="post.id">
                        
            <Feed v-bind:post="post"/>
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



    export default {
        name: 'SearchView',

        setup() {
            const userStore = useUserStore()

            return {
                userStore
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

            

            
        }
    }

</script>