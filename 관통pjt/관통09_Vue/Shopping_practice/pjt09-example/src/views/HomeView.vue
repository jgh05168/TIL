<template>
    <div>
        <h1>홈</h1>
        <div v-if="productIsEmpty" class="product-list">
            <div v-for="product in products" :key="product.id" class="product-card">
                <img :src="product.image" alt="" class="product-card-image">
                <p><strong>{{ product.title }}</strong></p>
                <p>가격 : ${{ product.price }}</p>
                <button @click="goDetail(product)">상세페이지로 이동</button>
                <button @click="addCart(product)">장바구니에 추가</button>
            </div>
        </div>
        <div v-else>
            <strong>로딩 중이거나, 상품 정보가 없습니다.</strong>
        </div>
    </div>
</template>



<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
// Get all products & Get a single product
const products = ref([

])
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
    .then((response) => {
        // console.log(response.data)
        products.value = response.data
    })
    .catch((error) => {
        console.error(error)
    })

const productIsEmpty = computed(() => {
    return products.value.length
})


const goDetail = (product) => {
    router.push(`/${product.id}`)
}

const addCart = (product) => {
    // //setItem, getItem       :   하나의 데이터만 저장하기
    // // 문제점 : 덮어쓰기가 된다.
    // localStorage.setItem('cart', 'test')
    // const tmp = localStorage.getItem('cart')
    // console.log(tmp)
    // ```
    // 임시로 데이터를 저장할 공간

    // 브라우저의 스토리지

    // Local Storage
    // - 반영구적으로 브라우저에 저장할 수 있는 공간 
    //     -> 브라우저를 껐다 켜도 데이터가 유지됨
    // - 5MB 정도의 데이터를 저장할 수 있음
    //     -> 쿠키보다 많은 데이터를 저장할 수 있다.
    // - 보안이 조금 위험함
    // - value에는 문자열만 저장 가능

    // 따라서, 브라우저 쪽에 임시로 저장하고 싶은 데이터가 있는데 보안 수준이 낮다 ?
    // : 그 떄 사용.
    // ```
    // 여러 데이터 저장하기
    // 1. 현재 localStorage에 저장된 데이터 가져오기
    // 만약 없다면 비어있는 리스트로 초기화
    console.log(JSON.parse(localStorage.getItem('cart')))
    const existingCart = JSON.parse(localStorage.getItem('cart')) || []

    // 중복된 제품이 있는지 확인
    const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)

    if (!isDuplicate) {
        alert('장바구니에 추가')
        existingCart.push(product)
    }
    else {
        alert('장바구니에 있는 상품입니다.')
    }
    // 2. 중복이 아니라면 추가
    localStorage.setItem('cart', JSON.stringify(existingCart))

    router.push('/cart')
}

</script>

<!-- scoped 없애면 css 모두 적용 가능 -->
<style>         
.product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.product-card {
    border: 1px solid black;
    width: 300px;
}

.product-card-image {
    width: 200px;
    height: 250px;
    object-fit: fill;
}
</style>