/*
  손님이 분식점에서 라면을 시켰다 == 여러분들이 만든 서비스의 화면을 사용자가 요청
  라면 == 화면
  라면 재료 준비 == 화면을 보여주는데 필요한 데이터들
  다완성되면 서빙 == 다 준비되면 화면보여주기

  Promise 객체 사용법
  new Promise((resolve, reject) => {
    
    if (비동기작업 완료 조건){
      return resolve(value) // 비동기작업이 성공했을때 리턴하고 싶은 값이 있으면 value
    } else if (비동기작업 실패 조건) {
      return reject(value) // 비동기작업이 실패했을때 리턴하고 싶은 값이 있으면 value
    }

  })

  .then() 과 .catch() 는 Promise 객체에 사용하는 메소드
*/


console.log("라면을 끓인다. (각 과정이 준비되는데 1~3초 시간이 걸린다")
// 라면을 끓이는 순서 물 끓이고 ==> 스프랑, 면 ==> 계란

// 물은 끓는데 3초가 걸린다
const water = function (ramen) {
  // 라면은 배열
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("1. 물을 끓인다")
      ramen.push("물")
      return resolve(ramen)
      // return reject("물을 너무 많이 넣었다.")
    }, 3000)
  })
}

const soupAndNoodle = function(ramen) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("2. 스프와 면을 넣는다")
      ramen.push("스프")
      ramen.push("면")
      return resolve(ramen)
    }, 2000)
  })
}

const egg = function(ramen) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("3. 계란을 넣는다")
      ramen.push("계란")
      return resolve(ramen)
    }, 2000)
  })
}

const ramen = []

// axios()
//   .then((response) => {
//     console.log(response.data)
//   })


// await water()
// await soupAndNoodle()

water(ramen)
  .then((ramen) => {
    return soupAndNoodle(ramen)
  })
  .then((ramen) => {
    return egg(ramen)
  })
  .then((ramen) => {
    console.log("라면 완성!! : ", ramen)
  })
  .catch((err) => {
    console.log("라면을 끓이는 도중에 문제가 발생 : ", err)
  })
