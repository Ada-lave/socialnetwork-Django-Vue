<template>

                        <div class="mb-6 flex items-center justify-between">
                            
                                
                                <RouterLink class="flex items-center space-x-6" v-bind:to="{name:'profile', params: {'id':comment.created_by.id}}">
                                    <img v-bind:src="comment.created_by.getAvatar" class="w-[40px] rounded-full">
                                    <p><strong>{{ comment.created_by.name }}</strong></p>
                                </RouterLink>
                             

                            <p class="text-gray-600">{{ comment.createdAtFormater }} назад</p>
                        </div>

                      <p>{{ comment.body }}</p>
                         


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