console.log("\n---------객체---------")

// 배열은 요소에 접근할 때 인덱스를 사용하지만, 객체는 key를 사용한다. 파이썬의 dictionary와 유사

const product ={
    제품명: "건 망고",
    가격: "10000",
    원산지: "알래스카"
}


const pet = {
    name:"네모",
    eat:function(food){
        console.log(`${this.name}가 ${food.name} 먹고 싸는 것은?`)
        return food.type==='liquor'?"오쥼":"동"
    }
}


class Food {
    constructor(name="food",type="food"){
        this.name = name
        this.type = type
    }
    typeChange() {
        if(type==="food")
            type = "liquor"
        else
            type = 'food'
    }
}

let f = new Food("사료","food")
let juice = new Food("오렌지 주스","liquor")


console.log(pet.eat(f))
console.log(pet.eat(juice))

// 기본자료형 : 숫자(Number), 문자열(String), 부울(Boolean)은 객체가 아니다!
// 자바의 Wrapper 함수와 같이 new Number(), new String(), new Boolean() 같이 객체로 선언해서 사용가능!

const I = 123.456789
I.toFixed(2)//소수점 둘째 자리까지