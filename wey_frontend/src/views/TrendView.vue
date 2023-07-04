<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       
        

        <div class="main-center col-span-3 space-y-4">
            <h3 class="text-xl">
            #{{ $route.params.id }}
            </h3>
           
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
            }
        },
        watch: {
            "$route.params.id": {
                handler() {
                    this.getFeed()
                },
                immediate: true
            }
        },

        mounted() {
            this.getFeed()
        },

        methods: {
            getFeed(){
                axios
                .get(`/api/posts/?trend=${this.$route.params.id}`)
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
            
        }
    }

</script>