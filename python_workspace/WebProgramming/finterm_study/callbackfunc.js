console.log("\n---------callback function---------")


function callThreeTimes(callback){
    for (let i=0;i<3;i++){
        callback(i)
    }
}

function print(i){
    console.log(`${i}번째 함수 호출`)
}
callThreeTimes(print)


callThreeTimes(function(i){
    console.log(`${i}번째 함수 호출`)
})

const arr =[1,2,3,4,5,6,7,8,9,10]

arr.forEach(function(value ,index,array){//array 생략 가능
    console.log(`${index}번째 요소: ${value}`)
})

let arrsqr = arr.map(function(value,index,array){// index, array 생략 가능
    return value*value
})

let even = arr.filter(function(value){
    return value%2 == 0
})

console.log(`짝수만:${even}`)


//(매개변수) =>{}

arr.filter((value)=>value%2 ==0).map((value)=>value*value).forEach((value)=>console.log(value))

//타이머 함수

// setTimeout(()=>{
//     console.log(`1초 후에 실행 됩니다.`)
// },1*1000)

let count = 1

let id = setInterval(()=>{
    // if(count === 10)
    //     clearInterval(id) // id를 통해 타이머를 종료한다.(return으로도 가능은 한듯?)
    console.log(`1초마다 실행 됩니다.${count}번째`)
    count++
 },1*1000)

 setTimeout(()=>{
     clearInterval(id)
     console.log("fin")
 },5*1000)