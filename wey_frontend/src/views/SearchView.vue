<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            
            <div class="bg-white  border border-gray-200 rounded-lg">
                <div class="p-4  space-x-4">
                    <form method="post" v-on:submit.prevent="submitForm()" class="flex">

                    <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Введите запрос">
                    <button class="inline-block py-4 px-6 bg-purple-500 text-white rounded-lg" type="submit">

                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
                        </svg>

                    </button>
                    
                    </form>
                </div>
            </div>

            <div class= "p-4 bg-white   border-gray-200 rounded-lg grid grid-cols-4 gap-4">

                
                <div class="p-4 text-center bg-gray-100 rounded-lg"
                v-for="user in users" v-bind:key="user">

                    <RouterLink v-bind:to="{name:'profile',params: {'id':user.id}}">

                        <img v-bind:src="user.getAvatar" class="mb-6 rounded-full">
                        <p><strong>{{ user.name }}</strong></p>

                    </RouterLink>
                    

                    

                    <div class="mt-6 flex space-x-8 justify-around">

                        <p class="text-xs text-gray-500"> {{ user.friends_count }} друзей </p>
                        <p class="text-xs text-gray-500"> {{ user.posts_count }} постов </p>

                    </div>
                </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg"
            v-for="post in posts"
            v-bind:key="post.id">
                        
            <Feed v-bind:post="post"/>
            </div>

                    
           
        </div>

        <div class="main-right col-span-1 space-y-4">

            <PeopleYouMayKnow />
            <Trends />

        </div>
    </div>
</template>

<script >
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import Feed from '../components/Feed.vue'

    export default {

        name: 'SearchView',
        components: {
        PeopleYouMayKnow,
        Trends,
        Feed,

},

        data() {
            return {
                users: [],
                query: '',
                posts: [],
            }
        },

        methods: {
            submitForm() {
                axios
                .post('/api/search/', {'query':this.query})
                .then(response => {
                    this.users = response.data.users
                    this.posts = response.data.posts
                    console.log(response.data.posts)
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }

</script>