<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       

        <div class="main-center col-span-3 space-y-4">
            
            <div class="p-4 bg-white border border-gray-200 rounded-lg"
            v-if="post.id">
                        
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
import { RouterLink } from 'vue-router'
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
                post: {},
                
            }
        },

        mounted() {
            this.getPost()
        },

        methods: {
            getPost(){
                axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    console.log(response.data.post)
                    this.post = response.data.post
                })
                .catch(error => {
                    console.log(error)
                })
            },

            
        }
    }

</script>