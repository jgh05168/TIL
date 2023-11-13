<template>
    <div>
        <span @click="store.updateTodo(todoData.id)"
        :class="{'is-done': todoData.isDone}">
        {{ todoData.text }}
        </span>
        <button @click="store.deleteTodo(todoData.id)">delete</button>


    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

defineProps({
    todoData: Object,
})
</script>

<style scoped>
.is-done {
    text-decoration: line-through;
}
</style>