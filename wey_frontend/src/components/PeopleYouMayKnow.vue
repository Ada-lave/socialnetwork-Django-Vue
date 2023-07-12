<template>

    <div class="p-4 bg-white border border-gray-200 rounded-lg">

                <h3 class="mb-6 text-xl">Возможно знакомы?</h3>

                <div class="space-y-4">
                    <div class="flex items-center justify-between"
                    v-if="users.length"
                    v-for="user in users"
                    v-bind:key="user.id">

                        <div class="flex items-center space-x-2">
                        <img v-bind:src="user.getAvatar" class="w-[40px] rounded-full">

                        <p class="text-xs"> {{ user.name }} </p>

                        </div>

                        <RouterLink v-bind:to="{name:'profile', params: {id:user.id}}" class="py-2 px-3 bg-purple-900 text-white text-xs rounded-lg">Показать профиль</RouterLink>
                    </div>

                </div>
    </div>

</template>


<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'


export default{
    data() {
        return {
            users: []
        };
    },
    mounted() {
        this.friendSuggest();
    },
    methods: {
        friendSuggest() {
            axios
                .get("/api/friends/suggest/")
                .then(response => {
                this.users = response.data;
                console.log(this.users);
            })
                .catch(error => {
                console.log(error);
            });
        }
    },
    components: { RouterLink }
}

</script>