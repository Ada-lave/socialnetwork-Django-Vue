import { defineStore } from 'pinia'
import axios from 'axios'

export  const useUserStore = defineStore({
    id: 'user',

    state: () =>({
        user: {
            isAunthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            console.log('initStore')
            if (localStorage.getItem('user.access')) {
                console.log('user has access')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAunthenticated = true
                
                this.refreshToken()

                console.log('Initialized user: ', this.user)
            }
        },

        setToken(data) {
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAunthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            console.log('RemoveToken')

            this.user.refresh = null
            this.user.access = null
            this.user.isAunthenticated = false
            this.user.id = false
            this.user.name = false
            this.user.email = false

            localStorage.setItem('user.access','')
            localStorage.setItem('user.refresh','')
            localStorage.setItem('user.name','')
            localStorage.setItem('user.id','')
            localStorage.setItem('user.email','')
        },

        setUserInfo(user) {
            console.log('setUserInfo ', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
            .then ((response) => {
                this.user.access = response.data.access

                localStorage.setItem('user.access',this.user.access)

                axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
            })

            .catch((error)  => {
                console.log(error)

                this.removeToken()
            })
        }
    }


})