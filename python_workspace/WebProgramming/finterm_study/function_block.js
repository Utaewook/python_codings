console.log("\n---------function block---------")

// 다른곳에서 가져 온 js 코드

let pi = 3.14
console.log(`파이 값은 ${pi}입니다.`)

(function () {
    let pi = 3.141592
    console.log(`파이 값은 ${pi}입니다.`)  
})()

// 블록의 가장 위 쪽에 'use strict'라는 문자열
// 코드를 엄격하게 검사한다.