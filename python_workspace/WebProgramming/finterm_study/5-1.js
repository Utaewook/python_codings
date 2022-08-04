console.log("\n---------------function---------------")

const array =[1,2,3,4,5,6,7];
const array2 = [8,9,10];
const fun = function(){ // 익명 함수
    console.log("First class Function");
    return 1;
}

function f() {
    return 1;
}

function sum(...args){
    s = 0
    for(const a of args){
        s += a
    }
    return s
}

console.log(sum(1,2,3,4,5,6))

function earnings(name, wage=9000,hours=40){
    console.log(`#${name}님의 급여 정보`)
    console.log(`- 시급:${wage}원`)
    console.log(`- 근무 시간:${hours}시간`)
    console.log(`- 급여:${wage*hours}원`)
}

earnings('태욱')
earnings('구름',10000,52)

function isLeapYear(year=new Date().getFullYear()){
    console.log(`매개변수 year:${year}`)
    return (year % 4 === 0) && (year%100 !== 0) || (year % 400 === 0)
}

console.log(`올해는 윤년일까? === ${isLeapYear()}`)

const array3 = [...array,...array2]; // 전개 연산자

console.log(sum(...array3));