<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       

        <div class="main-center col-span-3 space-y-4">
            
            <div class="p-4 bg-white border border-gray-200 rounded-lg"
            v-if="post.id">
                        
            <Feed v-bind:post="post"/>
            </div>


             <div class=" bg-white border border-gray-200 rounded-lg">

                <form v-on:submit.prevent="submitForm()" method="post">

                
                <div class="p-4">
                    <textarea class="p-4 w-full bg-gray-100 rounded-lg"
                     placeholder="Что вы думаете?"
                     v-model="body"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">

                    
                    <button
                    class=" inline-block py-4 px-3 bg-purple-600 text-white rounded-lg ml-auto"
                    type="submit">Комментировать</button>
                </div>

                </form>

                
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
        name: 'PostView',

        components: {
            PeopleYouMayKnow,
            Trends,
            Feed,
        },

        data(){
            return {
                post: {},
                body: ''
                
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
            submitForm(){
                console.log(this.body)


                axios
                .post(`/api/posts/${this.$route.params.id}/comment/`, {
                    'body' : this.body
                })
                .then(response => {
                    console.log(response)
                    
                    this.body = ''
                })
                .catch(error => {
                    console.log(error)
                })
            }

            
        }
    }

</script>