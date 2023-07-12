<template>

                        <div class="mb-4 flex items-center justify-between p-4">
                            
                                
                                <RouterLink class="flex items-center space-x-6" v-bind:to="{name:'profile', params: {'id':comment.created_by.id}}">
                                    <img v-bind:src="comment.created_by.getAvatar" class="w-[40px] rounded-full">
                                    <p><strong>{{ comment.created_by.name }}</strong></p>
                                </RouterLink>
                             

                            <p class="text-gray-600">{{ comment.createdAtFormater }} назад</p>
                              
                        </div>
                        <p class="ml-4 mb-2">{{ comment.body }}</p>
                     
                         


</template>


<script>
import { RouterLink } from 'vue-router'

export default{
    props: {
        comment: Object
    },
    methods: {
        
    },
    components: { RouterLink }
}

</script>