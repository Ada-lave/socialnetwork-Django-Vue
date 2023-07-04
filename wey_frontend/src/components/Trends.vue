<template>
     <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <h3 class="mb-6 text-xl">Тренды</h3>

                <div class="space-y-4">
                    <div class="flex items-center justify-between"
                    v-for="trend in trends">
                        <div class="flex items-center space-x-2">
                            <p class="text-xs">
                                <strong>#{{ trend.hashtag }}</strong><br>
                                <span class="text-gray-500">{{ trend.occurences }} постов</span>
                            </p>
                        </div>
                        <RouterLink v-bind:to="{name:'trend', params:{id:trend.hashtag}}" class="py-2 px-3 bg-purple-900 text-white text-xs rounded-lg">Подробнее</RouterLink>
                        
                    </div>
                </div>
            </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import axios from 'axios'
export default {
    name: "trends",
    data() {
        return {
            trends: []
        };
    },
    mounted() {
        this.getTrends();
    },
    methods: {
        getTrends() {
            axios
                .get("/api/posts/trends/")
                .then(response => {
                console.log(response.data);
                this.trends = response.data;
            })
                .catch(error => {
                console.log(error);
            });
        }
    },
    components: { RouterLink }
}

</script>