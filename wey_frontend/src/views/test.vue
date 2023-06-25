<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       

        <div class="main-center col-span-3 space-y-4">
            
            


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

        

       
        
    </div>
</template>


<script>
import { RouterLink } from 'vue-router'
import axios from 'axios'




    export default {
        name: 'PostView',

        components: {
            
        },

        data() {
        return {
            post: {
                id: null,
                comments: []
            },
            body: ''
        }
    },

        mounted() {
            this.getPost()
        },

        methods: {
            submitForm() {
            console.log('submitForm', this.body)

            axios
                .post(`/api/posts/m/`, {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.post.comments.push(response.data)
                    this.post.comments_count += 1
                    this.body = ''
                })
                .catch(error => {
                    console.log('error', error)
                })
        }

            
        }
    }

</script>