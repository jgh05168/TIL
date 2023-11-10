<template>
    <div>
        <h1>product</h1>
        <div v-if="product">
            <img :src="product.image" alt="" class="product-card-image">
            <p><strong>{{ product.title }}</strong></p>
            <p>가격 : ${{ product.price }}</p>
        </div>
        <div v-else>
            로딩중 ...
        </div>        
    </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref('')
const productId = route.params.productId
// console.log(productId)
const storeURL = `https://fakestoreapi.com/products/${productId}`
axios.get(storeURL)
    .then((response) => {
        // console.log(response.data)
        product.value = response.data
    })
    .catch((error) => {
        console.error(error)
    })
</script>



<style scoped>

</style>
