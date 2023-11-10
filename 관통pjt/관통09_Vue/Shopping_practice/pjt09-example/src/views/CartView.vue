<template>
    <div>
        <h1>cart</h1>
        <div v-if="cartItems" class="product-list">
            <div v-for="product in cartItems" :key="product.id" class="product-card">
                <img :src="product.image" alt="" class="product-card-image">
                <p><strong>{{ product.title }}</strong></p>
                <p>가격 : ${{ product.price }}</p>
                <button @click="goDetail(product)">상세페이지로 이동</button>
                <button @click="removeCart(product)">장바구니에서 삭제</button>

            </div>
        </div>
        <div v-else>
            <p><strong>장바구니에 담긴 상품이 없습니다.</strong></p>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'


const router = useRouter()
const cartItems = ref('')

cartItems.value = JSON.parse(localStorage.getItem('cart')) || []


const goDetail = (product) => {
    router.push(`/${product.id}`)
}


const removeCart = (product) => {
    // localStorage에서 삭제
    // 현재 cartItems.value에서 삭제
    // 1. 현재 localStorage에 저장된 데이터 가져오기
    // const existingCart = JSON.parse(localStorage.getItem('cart'))

    // 2. 삭제할 아이템 index 검색
    const itemIndex = cartItems.value.findIndex((item) => item.id === product.id)

    // 3. 데이터 삭제
    cartItems.value.splice(itemIndex, 1)

    // 4. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('cart', JSON.stringify(existingCart))
    cartItems.value = existingCart

}
</script>

<style scoped>

</style>