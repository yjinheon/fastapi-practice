import {createStore} from 'vuex'

import notes from './modules/notes'
import users from './modules/users'

/*
Vuex : State Management

- store : State 를 관리하는 저장소
- data() : 

States
export const state = () => (...)

Getters
export const getters = {...}

Mutations
export const mutations = {...}

Actions
export const actions = {...}

 */



export default createStore({
    modules: {
        notes,
        users
    }
}