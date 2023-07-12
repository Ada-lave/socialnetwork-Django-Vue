<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">

            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                
                    <img v-bind:src="user.getAvatar" class="mb-6 rounded-full">
                

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink v-bind:to="{name:'friends', params: {'id':user.id}}">
                        <p class="text-xs text-gray-500">{{ user.friends_count }} друзей</p>
                    </RouterLink>
                    
                    <p class="text-xs text-gray-500">{{ user.posts_count }} постов</p>
                </div>

                <div class="mt-6 space-x-3">
                    <button
                     class="py-4 px-4 text-white bg-green-700 rounded-lg"
                     v-on:click="sendFriendshipRequest()"
                     v-if="userStore.user.id !== user.id && req">
                     Добавить в друзья
                    </button>
                    <button
                     class="py-4 px-8 text-white bg-red-700 rounded-lg"
                     v-on:click="logout()"
                     v-if="userStore.user.id == user.id">
                     Выйти
                    </button>
                    <RouterLink
                     class="py-4 px-8 text-white bg-green-700 rounded-lg"
                     v-if="userStore.user.id == user.id"
                     v-bind:to="{name:'editProfile'}">
                     Изменить
                    </RouterLink>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
            class=" bg-white border border-gray-200 rounded-lg"
            v-if="userStore.user.id === user.id"
            >

                <form v-on:submit.prevent="submitForm()" method="post">

                
                <div class="p-4">
                    <textarea class="p-4 w-full bg-gray-100 rounded-lg"
                     placeholder="Пишите свои посты тут"
                     v-model="body"></textarea>

                     <div id="preview">
                    <img v-if="url" v-bind:src="url" class="w-[100px] rounded-xl mt-2">  
                    </div>
                </div>

                

                <div class="p-4 border-t border-gray-100 flex justify-between">

                    <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                        <input type="file" ref="file" v-on:change="onChangeImage">
                        Добавить фото
                    </label>
                    
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
            const toastStore = useToastStore()

            return {
                userStore,
                toastStore,

            }
        },
        components: {
    PeopleYouMayKnow,
    Trends,
    Feed,
    RouterLink
},

        data(){
            return {
                posts: [],
                user: {},
                body: '',
                url:null,
                req: null,
            }
        },

        mounted() {
            this.getUserPosts()
        },

        watch: {
            "$route.params.id": {
                handler() {
                    this.getUserPosts()
                },
                immediate: true
            }
        },

        

        methods: {
            getUserPosts(){
                axios
                .get(`/api/posts/userAllPosts/${this.$route.params.id}`)
                .then(response => {
                    console.log(response.data)
                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.req = response.data.can_send_req
                })
                .catch(error => {
                    console.log(error)
                })
            },

            submitForm(){
                console.log(this.body)


                let form = new FormData()
                form.append('image',this.$refs.file.files[0])
                form.append('body',this.body)


                axios
                .post('/api/posts/createPost/',form,{
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response => {
                    console.log(response)
                    this.posts.unshift(response.data)
                    this.body = ''
                    this.$refs.file.files.value = null
                    this.url = null
                    this.user.posts_count+=1
                })
                .catch(error => {
                    console.log(error)
                })
            },

            sendFriendshipRequest() {
                axios
                .post(`/api/friends/${this.$route.params.id}/request/`,)
                .then(response => {
                    console.log(response.data.message)

                if (response.data.message=='user alredy in ship')
                {
                    this.toastStore.showToast(5000,'заявка уже отправлена', 'bg-red-500')
                }
                else if (response.data.message=='user add ship')
                {
                    this.toastStore.showToast(5000,'заявка  отправлена', 'bg-emerald-500')
                }
                })
                .catch(error => {
                    console.log(error)
                })
            },

            onChangeImage(e){
                const file = e.target.files[0]
                this.url = URL.createObjectURL(file)
            },
            logout(){
                this.userStore.removeToken()
                this.$router.push('/login')
            }
        }
    }

</script>

<style>
input[type="file"] {
    display: none;
}
</style>