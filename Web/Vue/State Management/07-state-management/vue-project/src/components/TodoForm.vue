<template>
    <div>
        <form @submit.prevent="createTodo()" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
const todoText = ref('')
const formElem = ref(null)

const createTodo = function () {
    store.addTodo(todoText.value)
    // todoText.value = ''
    formElem.value.reset()
}
</script>

<style scoped>

</style>