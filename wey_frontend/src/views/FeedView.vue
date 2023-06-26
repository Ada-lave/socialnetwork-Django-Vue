<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       

        <div class="main-center col-span-3 space-y-4">
            <div class=" bg-white border border-gray-200 rounded-lg">

                <form v-on:submit.prevent="submitForm()" method="post">

                
                <div class="p-4">
                    <textarea class="p-4 w-full bg-gray-100 rounded-lg"
                     placeholder="Пишите свои посты тут"
                     v-model="body"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">

                    <a class=" inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Добавить фото</a>
                    <button
                    class=" inline-block py-4 px-3 bg-purple-600 text-white rounded-lg"
                    type="submit">Выложить</button>
                </div>

                </form>

                
            </div>
            <div class="p-4 bg-white border border-gray-200 rounded-lg"
            v-for="post in posts"
            v-bind:key="post.id">
                        
            <Feed v-bind:post="post"/>
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">

            <PeopleYouMayKnow />
            <Trends/>
        </div>
        
    </div>
</template>


<script >
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import Feed from '../components/Feed.vue'



    export default {
        name: 'FeedView',

        components: {
            PeopleYouMayKnow,
            Trends,
            Feed,
        },

        data(){
            return {
                posts: [],
                body: ''
            }
        },

        mounted() {
            this.getFeed()
        },

        methods: {
            getFeed(){
                axios
                .get('/api/posts/')
                .then(response => {
                    console.log(response.data)
                    this.posts = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            },

            submitForm(){
                console.log(this.body)


                axios
                .post('/api/posts/createPost/', {
                    'body' : this.body
                })
                .then(response => {
                    console.log(response)
                    this.posts.unshift(response.data)
                    this.body = ''
                })
                .catch(error => {
                    console.log(error)
                })
            },
            submitForm2(){
                console.log(this.body)


                axios
                .post('/api/posts/m/', {
                    'body' : this.body
                })
                .then(response => {
                    console.log(response)
                    this.posts.unshift(response.data)
                    this.body = ''
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }

</script>