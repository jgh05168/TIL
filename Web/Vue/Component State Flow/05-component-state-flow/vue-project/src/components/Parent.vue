<template>
    <div>
        <ParentChild 
        @some-event="someCallback" 
        @emit-args="getNumbers" 
        @update-name="updateName"
        my-msg="message" :dynamic-props="name"
        />
    </div>
</template>

<script setup>
import ParentChild from './ParentChild.vue';
import {ref} from 'vue'

const name = ref('Alice')

const someCallback = function() {
    console.log('발신한 이벤트 수신')
}

const getNumbers = function(...args) {
    console.log(args)
    console.log(`${args} 수신`)
}

const updateName = function () {
    name.value = 'Bella'
}
</script>

<style scoped>

</style>