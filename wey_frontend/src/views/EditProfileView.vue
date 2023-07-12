<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl"> Изменение  </h1>

                

                
            </div>
        </div>

        <div class="main-right ">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Имя</label><br>
                        <input type="text" placeholder="ФИО" 
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg"
                        v-model="form.name">
                    </div>

                    <div>
                        <label>Почта</label><br>
                        <input type="email" placeholder="Ваша почта" 
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg"
                        v-model="form.email">
                    </div>

                    <div>
                        <label>Аватар</label><br>
                        <input type="file" ref="file"
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg change"
                        style="display: flex;"
                        >
                    </div>

                    

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">
                                {{ error }}
                            </p>
                        </div>
                    </template>

                    <div>
                        <button
                        class="py-4
                        px-8
                        bg-purple-600
                        text-white
                        rounded-lg"
                        type="submit">
                        Изменить
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {useToastStore} from '@/stores/toast'
import { useUserStore } from '@/stores/user'
export default {
    setup () {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore
        }
    },


    data() {
        return {
            form: {
                email:this.userStore.user.email,
                name: this.userStore.user.name,
            },
            errors: [],
        }
    },

    methods: {
        submitForm(){
            this.errors = []

            if (this.form.email ==='')
            {
                this.errors.push('Вы забыли ввести почту')
            }

            if (this.form.name ==='')
            {
                this.errors.push('Вы забыли ввести имя')
            }


            if (this.errors.length === 0){

                let formData = new FormData()
                formData.append('avatar', this.$refs.file.files[0])
                formData.append('name', this.form.name)
                formData.append('email', this.form.email)
                console.log(formData)


                axios
                .post('/api/profile/edit/',formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then((response)=>{
                    console.log(response.data)
                    if (response.data.message === 'info update') {
                        this.toastStore.showToast(5000, 'Сохранено','bg-emerald-500')
                        console.log('yes')
                        

                        this.userStore.setUserInfo({
                            id: this.userStore.user.id,
                            name: this.form.name,
                            email: this.form.email,
                            avatar: response.data.user.getAvatar,
                        })
                    }
                    else {
                        this.toastStore.showToast(5000, `${response.message}`, 'bg-red-300')
                    }
                })

                .catch(error => {
                    console.log(error)
                })
            }
        }
    }
}
</script>

