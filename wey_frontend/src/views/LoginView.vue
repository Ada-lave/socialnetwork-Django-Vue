<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl"> Вход </h1>

                <p class="mb-6 text-gray-500">
                    мы рады что вы выбрали именно наш сайт, спасибо за вход
                </p>

                <p class="font-bold">
                    Еще не зарегистрированны? <RouterLink v-bind:to="{'name':'signup'}" class="underline">Нажмите сюда</RouterLink> для создания аккаунта
                </p>

            </div>
        </div>

        <div class="main-right ">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm()">
                    

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
                        <label>Пароль</label><br>
                        <input type="password" placeholder="Пароль" 
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg"
                        v-model="form.password">
                    </div>

                    <template>

                        <div v-if="errors.length > 0" class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind.key="error">
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
                        rounded-lg">
                        Войти
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from "@/stores/user"
export default {
    setup(){
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form:{
                email: '',
                password: ''
            },
            errors: []
           
        }
    },

    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === "")
            {
                this.errors.push("Вы забыли ввести почту")
            }
            if (this.form.password === "")
            {
                this.errors.push("Вы забыли указать пароль")
            }

            if (this.errors.length === 0)
            {
                await axios
                .post('/api/login/', this.form)
                .then((response)=>{
                    this.userStore.setToken(response.data)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch(error => {
                    console.log(error)
                })

                await axios
                .get('/api/me/')
                .then(response => {
                    this.userStore.setUserInfo(response.data)

                    this.$router.push('/feed')
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }
}

</script>