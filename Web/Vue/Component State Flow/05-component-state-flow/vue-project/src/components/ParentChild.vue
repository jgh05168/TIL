<template>
    <div>
        {{ myMsg }}
        {{ dynamicProps }}


        <ParentGrandChild :my-msg="myMsg" @updateName="updateName"/>

        <button @click="$emit('someEvent')">클릭</button>
        <button @click="buttonClick">클릭2</button>
        <button @click="emitArgs">추가 인자 전달</button>
    </div>
</template>

<script setup>
import ParentGrandChild from '@components/ParentGrandChild.vue'
// // 1. 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. 객체 선언 방식
defineProps({
    myMsg: String,      // 키: 타입
})

const props = defindProps({
    myMsg: String,
    dynamicProps: String,
})
console.log(props.myMsg)

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
    emit('someEvent')
}

const emitArgs = function() {
    emit('emitArgs', 1, 2, 3)
}

const updateName = function() {
    emit('updateName')
}
</script>

<style scoped>

</style>