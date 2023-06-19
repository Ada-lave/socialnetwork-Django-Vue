<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl"> Регистрация </h1>

                <p class="mb-6 text-gray-500">
                    мы рады что вы выбрали именно наш сайт, спасибо за вход
                </p>

                <p class="font-bold">
                    Уже есть аккаунт? <RouterLink v-bind:to="{'name':'login'}" href="#" class="underline">Нажмите сюда</RouterLink>
                </p>

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
                        <label>Пароль</label><br>
                        <input type="password" placeholder="Пароль" 
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg"
                        v-model="form.password1">
                    </div>

                    <div>
                        <label>Повторите пароль</label><br>
                        <input type="password" placeholder="Повторите ваш пароль" 
                        class="w-full
                        mt-2
                        px-6
                        py-4
                        border
                        border-gray-200 rounded-lg"
                        v-model="form.password2">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
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
                        rounded-lg"
                        type="submit">
                        Зарегистрироваться
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
export default {
    setup () {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },


    data() {
        return {
            form: {
                email:'',
                name: '',
                password1: '',
                password2: ''
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

            if (this.form.password1 === '')
            {
                this.errors.push('Вы забыли ввести пароль')
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push('Пароли не совпадают')
            }

            if (this.errors.length === 0){
                axios
                .post('/api/signup/',this.form)
                .then((response)=>{
                    console.log(response.data)
                    if (response.data.message === 'success') {
                        this.toastStore.showToast(5000, 'Вы успешно зарегистрированны','bg-emerald-500')
                        console.log('yes')
                        this.form.name = ''
                        this.form.email = ''
                        this.form.password1 = ''
                        this.form.password2 = ''
                    }
                    else {
                        this.toastStore.showToast(5000, 'Что то пошло не так', 'bg-red-300')
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